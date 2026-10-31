# ============================================================
#  MAIN — Advanced Quantitative Fixed-Time Trading Signal Engine
#  Entry point: python main.py --duration 1
#  v5: Continuous real-time scanner with 7-voter confluence gate
# ============================================================

import sys
import os
import shutil
import threading
import time
import argparse
from collections import deque

# Ensure project root is on path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from config import CAPTURE, ANALYSIS, SCORING, TRADE, UI, ML
from core.candle import Candle
from core.market_context import MarketContext
from core.signal_result import SignalResult, SignalGrade
from core.warmup_tracker import ContinuousScanner

from capture.screen_capture import ScreenCapture
from capture.chart_detector import ChartDetector
from extraction.candle_extractor import CandleExtractor
from extraction.oscillator_extractor import OscillatorExtractor

from engines.market_structure import MarketStructureEngine
from engines.trend_engine import TrendEngine
from engines.momentum_engine import MomentumEngine
from engines.volatility_engine import VolatilityEngine
from engines.price_action import PriceActionEngine
from engines.pattern_engine import PatternEngine
from engines.mtf_engine import MTFEngine
from engines.liquidity_engine import LiquidityEngine
from engines.behavior_classifier import BehaviorClassifier, MarketBehavior
from engines.indicators import TechnicalIndicators

from scoring.confidence_engine import ConfidenceEngine
from scoring.signal_validator import SignalValidator
from scoring.trade_quality import TradeQualityGrader

from ml.ml_layer import MLLayer
from analytics.trade_journal import TradeJournal
from ui.overlay import SignalOverlay


class SignalEngine:
    """
    Master engine — Continuous Real-Time Scanner with Confluence Gate.

    v5 Changes:
    - NO more 3-minute cycles. Pipeline runs on every new candle data.
    - 7-voter confluence gate: 5/7 modules must agree for tradeable signal.
    - Fixed trade duration (user-selected: 1/2/3/5 min via --duration).
    - 30-second cooldown after each signal.
    - Only A+ grade with 5/7+ confluence is tradeable.
    """

    def __init__(self):
        # Capture
        self.screen_capture = ScreenCapture()
        self.chart_detector = ChartDetector()
        self.candle_extractor = CandleExtractor()
        self.oscillator_extractor = OscillatorExtractor()
        
        # Continuous Asset Monitoring
        from capture.asset_monitor import AssetMonitor
        self.asset_monitor = AssetMonitor()

        # Analysis engines
        self.market_structure = MarketStructureEngine()
        self.trend_engine = TrendEngine()
        self.momentum_engine = MomentumEngine()
        self.volatility_engine = VolatilityEngine()
        self.price_action = PriceActionEngine()
        self.pattern_engine = PatternEngine()
        self.mtf_engine = MTFEngine()
        self.liquidity_engine = LiquidityEngine()
        self.behavior_classifier = BehaviorClassifier()
        self.indicators = TechnicalIndicators()

        # Scoring
        self.confidence_engine = ConfidenceEngine()
        self.signal_validator = SignalValidator()
        self.trade_quality = TradeQualityGrader()

        # ML
        self.ml_layer = MLLayer()

        # Analytics
        self.journal = TradeJournal()

        # State
        self.candle_history = deque(maxlen=ANALYSIS.candle_history)
        self.no_chart_count = 0
        self.scan_count = 0
        self.last_signal: SignalResult = SignalResult()
        self.last_context: MarketContext = MarketContext()
        self._reset_callback = None  # set by overlay
        self._last_behavior = None

        # Deduplication
        self._last_fingerprint: str = ""
        self._last_tradeable_dir: str = ""
        self._last_tradeable_scan: int = 0
        self._last_tradeable_time: float = time.time()  # Start cooldown timer immediately

        # Continuous scanner — min_candles set to SCORING.min_candles_before_signal (15 scans)
        self.scanner = ContinuousScanner(
            cooldown_seconds=SCORING.signal_cooldown_seconds,
            min_candles=SCORING.min_candles_before_signal
        )

        # Legacy alias for overlay compatibility
        self.cycle = self.scanner

        # Oscillator region cache (reset with full engine reset)
        self._oscillator_region = None

    def reset_all(self):
        """
        Full reset: clear caches, delete __pycache__, restart scanning fresh.
        Called from the overlay RESET button.
        """
        # 1. Clear candle history
        self.candle_history.clear()
        self.no_chart_count = 0
        self.scan_count = 0
        self.last_signal = SignalResult()
        self.last_context = MarketContext()
        self._last_tradeable_dir = ""
        self._last_tradeable_scan = 0
        self._last_tradeable_time = 0.0
        self._last_fingerprint = ""
        self._oscillator_region = None

        # 2. Reset scanner
        self.scanner.hard_reset()

        # 3. Reset chart detector cache (force re-detection)
        self.chart_detector.reset()
        self.oscillator_extractor.reset()

        # 4. Re-init screen capture (fresh mss context)
        self.screen_capture.cleanup()
        self.screen_capture = ScreenCapture()

        # 5. Reset engine internal state
        self.market_structure = MarketStructureEngine()
        self.trend_engine = TrendEngine()
        self.momentum_engine = MomentumEngine()
        self.volatility_engine = VolatilityEngine()
        self.price_action = PriceActionEngine()
        self.pattern_engine = PatternEngine()
        self.mtf_engine = MTFEngine()
        self.liquidity_engine = LiquidityEngine()
        self.behavior_classifier = BehaviorClassifier()
        self.indicators = TechnicalIndicators()

        # 6. Reset validator state (cooldown, anti-bias)
        self.signal_validator.reset()

        # 7. Delete all __pycache__ folders
        root_dir = os.path.dirname(os.path.abspath(__file__))
        for dirpath, dirnames, _ in os.walk(root_dir):
            for d in dirnames:
                if d == '__pycache__':
                    cache_path = os.path.join(dirpath, d)
                    try:
                        shutil.rmtree(cache_path)
                    except Exception:
                        pass

        print("[RESET] All caches cleared. Scanning fresh.")

    def run_pipeline(self, candles: list) -> tuple:
        """
        Run the full analysis pipeline on a list of candles.
        Returns (SignalResult, MarketContext).
        """
        if len(candles) < ANALYSIS.min_candles_for_analysis:
            return SignalResult(), MarketContext()

        ctx = MarketContext()
        
        # Inject Elder-Ray data from self._current_osc if available
        osc = getattr(self, "_current_osc", None)
        if osc and getattr(osc, "is_valid", False):
            ctx.elder_ray_valid            = True
            ctx.elder_ray_score            = osc.direction_score
            ctx.elder_ray_direction        = osc.elder_ray_direction
            ctx.elder_ray_bulls_current    = osc.bulls_current
            ctx.elder_ray_bears_current    = osc.bears_current
            ctx.elder_ray_bulls_divergence = osc.bulls_divergence
            ctx.elder_ray_bears_divergence = osc.bears_divergence
            ctx.elder_ray_zero_cross_up    = osc.zero_cross_up
            ctx.elder_ray_zero_cross_down  = osc.zero_cross_down
            ctx.elder_ray_exhaustion       = osc.both_shrinking or osc.trend_exhaustion

        # ── Step 1: Market Structure (HH/HL/BOS/CHOCH/S&R)
        ctx = self.market_structure.analyse(candles, ctx)

        # ── Step 2: Trend Analysis (EMA slopes, alignment)
        ctx = self.trend_engine.analyse(candles, ctx)

        # ── Step 3: Momentum Scoring
        ctx = self.momentum_engine.analyse(candles, ctx)

        # ── Step 4: Volatility Assessment
        ctx = self.volatility_engine.analyse(candles, ctx)

        # ── Step 5: Price Action (supply/demand, order blocks)
        ctx = self.price_action.analyse(candles, ctx)

        # ── Step 6: Multi-Timeframe Check
        ctx = self.mtf_engine.analyse(candles, ctx)

        # ── Step 7: Liquidity Sweep Detection
        ctx = self.liquidity_engine.analyse(candles, ctx)

        # ── Step 8: Pattern Detection — pass trend_state for context filtering
        patterns = self.pattern_engine.detect_all(candles, trend_state=ctx.trend_state)
        ctx.active_patterns = [p.name for p in patterns]

        # ── Step 8b: Williams %R (Pinpoint Reversals) ──
        wpr_data = self.indicators.compute_williams_r(candles, period=14)
        if wpr_data.get('valid'):
            ctx.williams_r       = wpr_data['wpr']
            ctx.williams_r_zone  = wpr_data['zone']
            ctx.williams_r_valid = True

        # ── Step 9: Pre-check — should we even generate a signal?
        vol_block, vol_reasons = self.volatility_engine.should_block_signal(ctx)
        if vol_block and not ctx.liquidity_sweep_detected:
            result = SignalResult()
            result.rejection_reasons = vol_reasons
            result.grade = SignalGrade.NO_TRADE
            return result, ctx

        # ── Step 10: Compute metrics for scoring
        momentum_quality = self.momentum_engine.get_momentum_quality(candles)
        pullback_quality = self.trend_engine.get_pullback_quality(candles, ctx)
        fake_breakout_prob = self.liquidity_engine.get_fake_breakout_probability(candles, ctx)
        divergence = self.momentum_engine.get_divergence_hint(candles)

        # Anti-chasing metrics
        overextension_score = self.momentum_engine.get_overextension_score(candles)
        overextension_direction = self.momentum_engine.get_overextension_direction(candles)
        trend_age_penalty = self.trend_engine.get_trend_age_penalty(candles, ctx)

        # Fast-reacting directional signals
        immediate_pressure = self.momentum_engine.get_immediate_pressure(candles)
        immediate_trend = self.trend_engine.get_immediate_trend(candles)

        # ── Step 9.5: Adaptive Behavior Classification ──
        behavior = self.behavior_classifier.classify(candles)
        self._last_behavior = behavior

        result = self.confidence_engine.calculate(
            candles, ctx, patterns,
            momentum_quality, pullback_quality,
            fake_breakout_prob, divergence,
            overextension_score, overextension_direction,
            trend_age_penalty,
            immediate_pressure=immediate_pressure,
            immediate_trend=immediate_trend,
            elder_ray_score=ctx.elder_ray_score
        )

        # ── CONFLUENCE GATE (v5 — 7-voter system) ──
        result = self.confidence_engine.confluence_check(
            candles, ctx, patterns,
            immediate_pressure=immediate_pressure,
            immediate_trend=immediate_trend,
            result=result,
            elder_ray_score=ctx.elder_ray_score
        )

        # ── ADAPTIVE BEHAVIOR GATE — Only hard-block truly dangerous regimes ──
        if behavior.signal_reliability < 0.10 or behavior.regime == 'dead':
            # Only 'dead' market fully blocks signals (reliability near 0)
            result.risk_flags.append(f"Dead market ({behavior.regime}: {behavior.signal_reliability:.0%})")
            if behavior.signal_reliability < 0.08:
                result.grade = SignalGrade.NO_TRADE
                result.direction = None
                return result, ctx
            result.confidence *= 0.85
        elif behavior.signal_reliability < 0.22:
            result.risk_flags.append(f"Low signal reliability ({behavior.regime}: {behavior.signal_reliability:.0%})")
            if result.confluence_count < 4:
                result.confidence *= 0.80
        elif behavior.regime == 'spike_retrace':
            # spike_retrace: reduce confidence but NEVER hard-block (trending can look like spike_retrace)
            result.risk_flags.append(f"Spike-retrace pattern ({behavior.signal_reliability:.0%})")
            result.confidence *= 0.90
        if behavior.fake_move_probability > 0.65 and result.direction is not None:
            result.risk_flags.append(f"Fake move likely ({behavior.fake_move_probability:.0%})")
            if result.confluence_count < 4:
                result.confidence -= 8.0
        if behavior.regime == 'choppy':
            result.risk_flags.append("Choppy market detected")
            if result.confluence_count < 4:
                result.confidence -= 8.0

        # ── Step 11: Signal Validation (rejection filters)
        result = self.signal_validator.validate(
            result, candles, ctx, fake_breakout_prob,
            fingerprint=self._last_fingerprint,
            overextension_score=overextension_score,
            overextension_direction=overextension_direction,
            immediate_pressure=immediate_pressure
        )

        # ── Step 12: Grade Assignment
        result = self.trade_quality.grade(result)

        # ── Step 13: ML Adjustment
        result = self.ml_layer.adjust(result)

        # Re-grade after ML adjustment
        if result.ml_adjustment != 0:
            result = self.trade_quality.grade(result)

        # Fixed trade duration (from config / CLI)
        result.timeframe = TRADE.primary_timeframe
        result.expiry_minutes = TRADE.fixed_duration_minutes

        return result, ctx

    def process_scan(self) -> tuple:
        """
        Perform one scan:
        capture -> detect -> extract -> check scanner -> run pipeline -> signal or skip.
        Returns (SignalResult, MarketContext, status_msg).
        """
        try:
            # Capture screen
            screen = self.screen_capture.grab()

            # Detect chart region
            region = self.chart_detector.detect(screen)
            if region is None:
                self.no_chart_count += 1
                return None, None, "no_chart"

            self.no_chart_count = 0
            
            # Asset Monitoring Reset Rule
            has_changed, asset_name = self.asset_monitor.check_asset(screen)
            if has_changed:
                print("\n==================================================")
                print(f"[ALERT] ASSET CHANGED -> {asset_name}")
                print("STOP -> CLEAR MEMORY -> RESET ANALYZER -> FRESH SCAN")
                print("==================================================\n")
                self.reset_all()
                return None, None, f"asset_reset:{asset_name}"

            # Extract candles
            candles = self.candle_extractor.extract(screen, region)
            if not candles:
                self.no_chart_count += 1
                return None, None, "no_chart"

            # ── Extract Elder-Ray Oscillator ──
            osc = self.oscillator_extractor.extract(
                screen,
                chart_region=region,
                oscillator_region=self._oscillator_region,
                candles=list(self.candle_history) if self.candle_history else candles
            )
            # Cache oscillator panel location if found on screen
            if osc.panel_found and self._oscillator_region is None:
                # Detect and cache the region for future scans
                pass  # region is detected internally

            # Update fingerprint and feed candles directly every second
            fp = self.candle_extractor.fingerprint
            self._last_fingerprint = fp

            # Merge with history — ADDITIVE, do NOT clear history every scan
            # (clearing + refilling caused fingerprint to always look "new")
            for c in candles:
                self.candle_history.append(c)   # deque(maxlen=50) auto-trims

            candle_list = list(self.candle_history)

            # Feed scanner with candle data
            ctx_quick = MarketContext()
            ctx_quick = self.momentum_engine.analyse(candle_list, ctx_quick)
            self.scanner.feed(candle_list, fingerprint=fp,
                            momentum_score=ctx_quick.momentum_score)

            # ── Pre-populate ctx with Elder-Ray data for pipeline ──
            # This is done BEFORE run_pipeline so confidence_engine can read it
            self._current_osc = osc  # store for pipeline access

            # ── CONTINUOUS SCANNER: Check if pipeline should run ──
            if not self.scanner.should_run_pipeline():
                self.scan_count += 1
                status = self.scanner.state.lower()
                return None, None, status

            # ── RUN FULL PIPELINE ──
            result, ctx = self.run_pipeline(candle_list)

            self.scanner.pipeline_ran()

            print(f"[DEBUG SCAN] grade={getattr(result.grade, 'value', result.grade)}, conf={result.confidence:.1f}, confl={result.confluence_count}, dir={result.direction}, rejections={result.rejection_reasons[:1]}")

            # ── Check if this is a TRADEABLE signal ──
            if result.is_tradeable and result.direction is not None:
                now_t = time.time()
                last_t = getattr(self, "_last_tradeable_time", 0.0)
                # Only fire and log a new trade if the strict 50-second cooldown has passed.
                # (Direction flips NO LONGER bypass the cooldown, preventing spam)
                if (now_t - last_t) >= SCORING.signal_cooldown_seconds:
                    self.journal.log_signal(result)
                    self._last_tradeable_dir = result.direction
                    self._last_tradeable_scan = self.scan_count
                    self._last_tradeable_time = now_t

                    self.scanner.signal_generated()

                    # ── Debug: trace signal decisions ──
                    print(f"\n{'='*55}")
                    print(f"  SIGNAL #{self.scanner.signal_count}  |  "
                          f"{result.expiry_minutes} MIN {result.direction}  |  "
                          f"Confidence: {result.confidence:.1f}%  |  "
                          f"Confluence: {result.confluence_count}/7")
                    print(f"{'='*55}")
                    if ctx:
                        print(f"  Trend:      {ctx.trend_state.value} ({ctx.trend_strength:.3f})")
                        print(f"  Momentum:   {ctx.momentum_score:.3f}")
                        print(f"  Structure:  {ctx.structure_state.value}")
                    if result.confluence_details:
                        print(f"  Voters:     {' | '.join(result.confluence_details[:4])}")
                        if len(result.confluence_details) > 4:
                            print(f"              {' | '.join(result.confluence_details[4:])}")
                    if result.entry_factors:
                        print(f"  Entries:    {', '.join(result.entry_factors[:4])}")
                    if result.risk_flags:
                        print(f"  Risks:      {', '.join(result.risk_flags[:3])}")
                    if self._last_behavior:
                        b = self._last_behavior
                        print(f"  Behavior:   {b.regime} (reliability: {b.signal_reliability:.0%})")
                    print(f"{'='*55}\n")

                    self.last_signal = result
                    self.last_context = ctx
                    self.scan_count += 1
                    return result, ctx, "signal"
                else:
                    # Same trade direction still holding inside the 55s window — treat as scanning
                    self.last_signal = result
                    self.last_context = ctx
                    self.scan_count += 1
                    return result, ctx, "scanning"

            # Not tradeable — still update last result for display
            self.last_signal = result
            self.last_context = ctx
            self.scan_count += 1
            return result, ctx, "scanning"

        except Exception as e:
            return None, None, f"error: {str(e)[:60]}"


def scanner_loop(engine: SignalEngine, overlay: SignalOverlay):
    """Background thread: continuously scan and update overlay."""
    while True:
        try:
            if not overlay.root.winfo_exists():
                break
        except Exception:
            break
        try:
            result, ctx, status = engine.process_scan()
            
            # Update the asset name label in the UI
            current_asset = getattr(engine, 'asset_monitor', None)
            if current_asset and current_asset.current_asset:
                overlay.root.after(0, overlay.asset_var.set, current_asset.current_asset)

            if status in ("scanning", "warming_up"):
                # Continuous scanning mode — show live status
                overlay.root.after(0, overlay.set_analyzing,
                                   engine.scanner.progress_fraction,
                                   engine.scanner.progress_text,
                                   result)
            elif status == "cooldown":
                overlay.root.after(0, overlay.set_cooldown)
            elif status and status.startswith("asset_reset:"):
                asset_name = status.split(":", 1)[1]
                overlay.root.after(0, overlay.set_reset_state, asset_name)
            elif status == "no_chart":
                if engine.no_chart_count > 3:
                    overlay.root.after(0, overlay.set_no_chart)
            elif status == "no_candles":
                overlay.root.after(0, overlay.set_scanning)
            elif status == "dedup":
                pass
            elif status and status.startswith("error"):
                overlay.root.after(0, overlay.reasons_var.set, status)
            elif status == "signal" and result is not None:
                # ── NEW TRADEABLE SIGNAL ──
                overlay.root.after(0, overlay.update_signal, result, ctx)
                stats = engine.journal.get_stats()
                overlay.root.after(0, overlay.update_stats, stats)
                overlay.root.after(0, overlay.update_scan_info,
                                   engine.scan_count,
                                   len(engine.candle_history),
                                   engine.scanner.signal_count)

        except Exception as e:
            try:
                overlay.root.after(0, overlay.reasons_var.set, f"Loop error: {str(e)[:40]}")
            except Exception:
                pass

        time.sleep(CAPTURE.scan_interval)


def main():
    if len(sys.argv) == 1:
        # Launch standalone GUI if run without arguments (e.g. double-click)
        try:
            from ui.launcher import LauncherGUI
            app = LauncherGUI()
            app.root.mainloop()
            return
        except ImportError:
            pass

    parser = argparse.ArgumentParser(description="Advanced Quantitative Trading Signal Engine v5")
    parser.add_argument("--timeframe", "-tf", default="1m",
                        choices=["1m", "2m", "3m", "5m"],
                        help="Primary timeframe (default: 1m)")
    parser.add_argument("--duration", "-d", type=int, default=1,
                        choices=[1, 2, 3, 5],
                        help="Fixed trade duration in minutes (default: 1)")
    parser.add_argument("--test-ui", action="store_true",
                        help="Launch overlay with dummy data for testing")
    parser.add_argument("--dry-run", action="store_true",
                        help="Run import checks only, no UI")
    args = parser.parse_args()

    # Apply settings
    TRADE.primary_timeframe = args.timeframe
    TRADE.fixed_duration_minutes = args.duration

    if args.dry_run:
        print("[DRY RUN] All imports successful. Engine ready.")
        engine = SignalEngine()
        print(f"  Scanner state: {engine.scanner.state}")
        print(f"  Duration: {TRADE.fixed_duration_minutes} min")
        print(f"  Confluence: {SCORING.min_confluence_voters}/7 required")
        print(f"  Confidence: >= {SCORING.min_confidence_threshold}%")
        return

    print("=" * 60)
    print("  QUANTITATIVE SIGNAL ENGINE v5 — CONTINUOUS SCANNER")
    print("=" * 60)
    print(f"  Chart TF       : {TRADE.primary_timeframe}")
    print(f"  Trade Duration : {TRADE.fixed_duration_minutes} MIN (fixed)")
    print(f"  Scan Interval  : {CAPTURE.scan_interval}s")
    print(f"  Confluence     : {SCORING.min_confluence_voters}/7 voters required")
    print(f"  Min Confidence : {SCORING.min_confidence_threshold}%")
    print(f"  Cooldown       : {SCORING.signal_cooldown_seconds}s after each signal")
    print(f"  ML Layer       : {'Enabled' if ML.enabled else 'Disabled'}")
    print(f"  Mode           : Continuous real-time scanning")
    print("=" * 60)
    print("  Overlay will appear on the right side. Drag to reposition.")
    print("  Close the overlay window to exit.")
    print("=" * 60)

    # Ensure data directory exists
    os.makedirs("data", exist_ok=True)

    # Initialize overlay
    overlay = SignalOverlay()
    overlay.update_timeframe(TRADE.primary_timeframe)

    if args.test_ui:
        # Test mode: show dummy signal
        dummy = SignalResult()
        dummy.direction = "UP"
        dummy.confidence = 87.5
        dummy.grade = SignalGrade.A_PLUS
        dummy.prob_up = 0.72
        dummy.prob_down = 0.13
        dummy.prob_no_trade = 0.15
        dummy.entry_factors = ["Trend: Strong Bullish", "MTF aligned",
                               "Strong momentum", "Structure: Bullish Structure",
                               "Confluence: 6/7 voters agree"]
        dummy.reasons = ["Bullish Engulfing", "Breakout Candle"]
        dummy.risk_flags = []
        dummy.confluence_count = 6
        dummy.confluence_details = ["Trend: Bullish", "Momentum: +0.65",
                                     "Structure: Bullish", "Candle Pressure: Bullish",
                                     "Pattern: Engulfing", "Immediate: Bullish"]
        dummy.expiry_minutes = TRADE.fixed_duration_minutes

        dummy_ctx = MarketContext()
        from core.market_context import TrendState, VolatilityRegime, MarketRegime
        dummy_ctx.trend_state = TrendState.STRONG_BULLISH
        dummy_ctx.trend_strength = 0.85
        dummy_ctx.market_regime = MarketRegime.TRENDING
        dummy_ctx.volatility_regime = VolatilityRegime.NORMAL
        dummy_ctx.momentum_score = 0.65
        dummy_ctx.active_patterns = ["Bullish Engulfing", "Breakout Candle"]

        overlay.root.after(500, overlay.update_signal, dummy, dummy_ctx)
        overlay.root.after(600, overlay.update_stats, {
            'today_total': 12, 'today_rate': 75.0,
            'streak': 4, 'streak_type': 'win'
        })
        overlay.root.after(700, overlay.update_scan_info, 42, 28, 6)
        overlay.run()
        return

    # Production mode
    engine = SignalEngine()

    # Wire reset button: overlay calls engine.reset_all + resets UI
    def on_reset():
        engine.reset_all()
        overlay.set_scanning()
        overlay.reasons_var.set("Cache cleared -- rescanning...")

    overlay.on_reset = on_reset

    # Wire timeframe button
    def on_tf_change(tf):
        TRADE.primary_timeframe = tf
        TRADE.fixed_duration_minutes = int(tf[0])
        engine.reset_all()
        overlay.update_timeframe(tf)
        overlay.set_scanning()
        overlay.reasons_var.set(f"Switched to {tf} timeframe. Rescanning...")

    overlay.on_tf_change = on_tf_change

    # Start scanner thread
    t = threading.Thread(target=scanner_loop, args=(engine, overlay), daemon=True)
    t.start()

    # Run overlay (blocks on main thread)
    overlay.run()

    # Cleanup
    engine.screen_capture.cleanup()
    print("\nEngine stopped. Session complete.")
    stats = engine.journal.get_stats()
    if stats.get('completed', 0) > 0:
        print(f"  Signals: {stats['total']} | Win Rate: {stats['win_rate']}%")


if __name__ == "__main__":
    main()
