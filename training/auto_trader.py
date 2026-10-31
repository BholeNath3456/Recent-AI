# ============================================================
#  AUTO TRADER  - Automated demo trading + ML training pipeline
#  Runs the signal engine, trades on Olymp Trade demo via browser,
#  records outcomes, and trains the ML model.
#
#  Usage: python -m training.auto_trader
# ============================================================

import sys
import os
import time
import json
import threading
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config import CAPTURE, ANALYSIS, SCORING, TRADE, ML
from core.signal_result import SignalResult, SignalGrade
from core.market_context import MarketContext

from capture.screen_capture import ScreenCapture
from capture.chart_detector import ChartDetector
from extraction.candle_extractor import CandleExtractor

from engines.market_structure import MarketStructureEngine
from engines.trend_engine import TrendEngine
from engines.momentum_engine import MomentumEngine
from engines.volatility_engine import VolatilityEngine
from engines.price_action import PriceActionEngine
from engines.pattern_engine import PatternEngine
from engines.mtf_engine import MTFEngine
from engines.liquidity_engine import LiquidityEngine

from scoring.confidence_engine import ConfidenceEngine
from scoring.signal_validator import SignalValidator
from scoring.trade_quality import TradeQualityGrader

from ml.ml_layer import MLLayer
from analytics.trade_journal import TradeJournal

from collections import deque

# Training state persistence
_TRAINING_STATE_PATH = "data/training_state.json"
_TRAINING_LOG_PATH = "data/training_log.json"


class AutoTrader:
    """
    Automated demo trading + ML training pipeline.

    This runs independently of the overlay UI. It:
    1. Captures the screen and runs the signal engine
    2. When a tradeable signal fires, records it
    3. Waits for the trade duration
    4. Captures the screen again and checks if the signal was correct
    5. Records the outcome and feeds it to ML training
    6. After enough samples, trains the ML model
    """

    def __init__(self):
        # Signal engine components
        self.screen_capture = ScreenCapture()
        self.chart_detector = ChartDetector()
        self.candle_extractor = CandleExtractor()

        self.market_structure = MarketStructureEngine()
        self.trend_engine = TrendEngine()
        self.momentum_engine = MomentumEngine()
        self.volatility_engine = VolatilityEngine()
        self.price_action = PriceActionEngine()
        self.pattern_engine = PatternEngine()
        self.mtf_engine = MTFEngine()
        self.liquidity_engine = LiquidityEngine()

        self.confidence_engine = ConfidenceEngine()
        self.signal_validator = SignalValidator()
        self.trade_quality = TradeQualityGrader()

        self.ml_layer = MLLayer()
        self.journal = TradeJournal()

        # State
        self.candle_history = deque(maxlen=ANALYSIS.candle_history)
        self._last_fingerprint = ""

        # Training stats
        self.total_trades = 0
        self.wins = 0
        self.losses = 0
        self.training_log = []
        self._consecutive_same_dir_count = 0

        # Load previous training state
        self._load_state()

    def run_pipeline(self, candles: list):
        """Run the full analysis pipeline."""
        if len(candles) < ANALYSIS.min_candles_for_analysis:
            return SignalResult(), MarketContext()

        ctx = MarketContext()
        ctx = self.market_structure.analyse(candles, ctx)
        ctx = self.trend_engine.analyse(candles, ctx)
        ctx = self.momentum_engine.analyse(candles, ctx)
        ctx = self.volatility_engine.analyse(candles, ctx)
        ctx = self.price_action.analyse(candles, ctx)
        ctx = self.mtf_engine.analyse(candles, ctx)
        ctx = self.liquidity_engine.analyse(candles, ctx)

        patterns = self.pattern_engine.detect_all(candles)
        ctx.active_patterns = [p.name for p in patterns]

        vol_block, vol_reasons = self.volatility_engine.should_block_signal(ctx)
        if vol_block and not ctx.liquidity_sweep_detected:
            result = SignalResult()
            result.rejection_reasons = vol_reasons
            result.grade = SignalGrade.NO_TRADE
            return result, ctx

        momentum_quality = self.momentum_engine.get_momentum_quality(candles)
        pullback_quality = self.trend_engine.get_pullback_quality(candles, ctx)
        fake_breakout_prob = self.liquidity_engine.get_fake_breakout_probability(candles, ctx)
        divergence = self.momentum_engine.get_divergence_hint(candles)

        # v4 NEW: Anti-chasing metrics
        overextension_score = self.momentum_engine.get_overextension_score(candles)
        overextension_direction = self.momentum_engine.get_overextension_direction(candles)
        trend_age_penalty = self.trend_engine.get_trend_age_penalty(candles, ctx)

        result = self.confidence_engine.calculate(
            candles, ctx, patterns,
            momentum_quality, pullback_quality,
            fake_breakout_prob, divergence,
            overextension_score, overextension_direction,
            trend_age_penalty
        )

        result = self.signal_validator.validate(
            result, candles, ctx, fake_breakout_prob,
            fingerprint=self._last_fingerprint,
            overextension_score=overextension_score,
            overextension_direction=overextension_direction
        )
        result = self.trade_quality.grade(result)
        result = self.ml_layer.adjust(result)
        if result.ml_adjustment != 0:
            result = self.trade_quality.grade(result)

        result.timeframe = TRADE.primary_timeframe
        return result, ctx

    def capture_and_analyze(self):
        """One scan cycle: capture -> detect -> extract -> analyze."""
        try:
            screen = self.screen_capture.grab()
            region = self.chart_detector.detect(screen)
            if region is None:
                # After 5 consecutive failures, recreate mss context
                self._no_chart_count = getattr(self, '_no_chart_count', 0) + 1
                if self._no_chart_count >= 5:
                    self.screen_capture.cleanup()
                    self.screen_capture = ScreenCapture()
                    self.chart_detector.reset()
                    self._no_chart_count = 0
                return None, None, "no_chart"
            self._no_chart_count = 0

            candles = self.candle_extractor.extract(screen, region)
            if not candles:
                return None, None, "no_candles"

            fp = self.candle_extractor.fingerprint
            if fp and fp == self._last_fingerprint:
                return None, None, "dedup"
            self._last_fingerprint = fp

            self.candle_history.clear()
            for c in candles:
                self.candle_history.append(c)

            candle_list = list(self.candle_history)
            result, ctx = self.run_pipeline(candle_list)
            return result, ctx, "ok"

        except Exception as e:
            return None, None, f"error: {str(e)[:60]}"

    def get_entry_price(self, candles):
        """Get the current price (last candle close) for outcome comparison."""
        if candles:
            return candles[-1].close
        return None

    def check_outcome(self, direction, entry_price):
        """
        Check trade outcome by comparing current price to entry price.
        Returns True (win), False (loss), or None (can't determine).
        """
        try:
            screen = self.screen_capture.grab()
            region = self.chart_detector.detect(screen)
            if region is None:
                return None

            candles = self.candle_extractor.extract(screen, region)
            if not candles:
                return None

            current_price = candles[-1].close

            if direction == "UP":
                return current_price > entry_price
            elif direction == "DOWN":
                return current_price < entry_price
            return None

        except Exception:
            return None

    def run_training_loop(self, max_trades=300, target_win_rate=0.60, overlay=None):
        """
        Main training loop. Runs until max_trades or target_win_rate reached.
        """
        print("=" * 60)
        print("  AUTO TRADER - ML Training Pipeline")
        print("=" * 60)
        print(f"  Target trades    : {max_trades}")
        print(f"  Target win rate  : {target_win_rate:.0%}")
        print(f"  Trade duration   : {TRADE.duration_minutes} min")
        print(f"  Existing samples : {len(self.ml_layer.training_data)}")
        print(f"  ML trained       : {self.ml_layer.is_trained}")
        print("=" * 60)
        print()

        scan_count = 0
        pending_trade = None  # {result, entry_price, entry_time}
        last_trade_time = 0      # timestamp of last completed trade
        last_trade_dir = None    # direction of last trade
        MIN_TRADE_INTERVAL = 90    # 90s = one full candle cycle between trades
        MIN_CONFIDENCE = 75.0     # higher threshold for training quality

        while self.total_trades < max_trades:
            scan_count += 1

            # If we have a pending trade, check if it's time to evaluate
            if pending_trade is not None:
                elapsed = time.time() - pending_trade['entry_time']
                wait_seconds = TRADE.duration_minutes * 60

                if elapsed >= wait_seconds:
                    # Trade period over - check outcome
                    outcome = self.check_outcome(
                        pending_trade['direction'],
                        pending_trade['entry_price']
                    )

                    if outcome is not None:
                        self._record_outcome(pending_trade, outcome)
                        last_trade_time = time.time()
                        last_trade_dir = pending_trade['direction']
                    else:
                        print(f"  [?] Could not determine outcome (no chart)")

                    pending_trade = None

                    # Check if we should retrain
                    if (len(self.ml_layer.training_data) >= ML.min_training_samples and
                        self.total_trades % ML.retrain_interval == 0):
                        print("\n  [ML] Retraining model...")
                        self.ml_layer.train()
                        print()

                    # Check if target reached
                    if self.total_trades >= 50:
                        current_rate = self.wins / self.total_trades
                        if current_rate >= target_win_rate:
                            print(f"\n  [OK] Target win rate reached! {current_rate:.1%} "
                                  f"({self.wins}/{self.total_trades})")
                            if self.total_trades >= ML.min_training_samples:
                                print("  [OK] Enough samples for ML training.")
                                self.ml_layer.train()
                                break

                else:
                    # Still waiting for trade to complete
                    remaining = wait_seconds - elapsed
                    if scan_count % 10 == 0:
                        print(f"  [..] Waiting for trade... {remaining:.0f}s remaining")
                    time.sleep(1)
                    continue

            # Enforce minimum cooldown between trades
            time_since_last = time.time() - last_trade_time
            if time_since_last < MIN_TRADE_INTERVAL and last_trade_time > 0:
                if scan_count % 30 == 0:
                    print(f"  [{self._time()}] Cooling down... "
                          f"{MIN_TRADE_INTERVAL - time_since_last:.0f}s remaining")
                time.sleep(CAPTURE.scan_interval)
                continue

            # No pending trade - scan for new signal
            result, ctx, status = self.capture_and_analyze()

            if status == "no_chart":
                if overlay:
                    overlay.root.after(0, overlay.set_no_chart)
                if scan_count % 20 == 0:
                    print(f"  [{self._time()}] No chart detected - open Olymp Trade")
                time.sleep(CAPTURE.scan_interval)
                continue

            if status in ("no_candles", "dedup"):
                time.sleep(CAPTURE.scan_interval)
                continue

            if status.startswith("error"):
                print(f"  [!] {status}")
                time.sleep(CAPTURE.scan_interval)
                continue

            if result is None:
                if overlay and status == "no_candles":
                    overlay.root.after(0, overlay.set_scanning)
                time.sleep(CAPTURE.scan_interval)
                continue

            if overlay:
                pending = pending_trade is not None
                if result.is_tradeable:
                    overlay.root.after(0, overlay.update_signal, result, ctx)
                overlay.root.after(0, overlay.update_training_stats, self.total_trades, self.wins, self.losses, len(self.ml_layer.training_data), pending)

            # Check if signal is tradeable with stricter criteria
            if result.is_tradeable and result.direction:
                # Gate 1: Minimum confidence for training trades
                if result.confidence < MIN_CONFIDENCE:
                    if scan_count % 30 == 0:
                        print(f"  [{self._time()}] Signal {result.direction} "
                              f"at {result.confidence:.0f}% - below {MIN_CONFIDENCE}% threshold")
                    time.sleep(CAPTURE.scan_interval)
                    continue

                # Gate 2: Don't take same direction 3+ times in a row
                if (result.direction == last_trade_dir and
                    self._consecutive_same_dir_count >= 3 and
                    result.confidence < 85):
                    if scan_count % 30 == 0:
                        print(f"  [{self._time()}] Skipping {result.direction} - "
                              f"already {self._consecutive_same_dir_count} consecutive")
                    time.sleep(CAPTURE.scan_interval)
                    continue

                entry_price = self.get_entry_price(list(self.candle_history))
                if entry_price is not None:
                    pending_trade = {
                        'result': result,
                        'direction': result.direction,
                        'confidence': result.confidence,
                        'grade': result.grade.value,
                        'entry_price': entry_price,
                        'entry_time': time.time(),
                        'entry_factors': result.entry_factors[:3],
                        'risk_flags': result.risk_flags[:2],
                        'factor_scores': dict(result.factor_scores),
                    }

                    # Track consecutive same direction
                    if result.direction == last_trade_dir:
                        self._consecutive_same_dir_count += 1
                    else:
                        self._consecutive_same_dir_count = 1

                    arrow = "^" if result.direction == "UP" else "v"
                    factors_str = ", ".join(result.entry_factors[:2])
                    print(f"  [{self._time()}] {arrow} {result.direction} signal "
                          f"({result.confidence:.0f}% {result.grade.value}) "
                          f"[{factors_str}] - waiting {TRADE.duration_minutes}m...")
            else:
                if scan_count % 30 == 0:
                    reason = ""
                    if result.rejection_reasons:
                        reason = f" ({result.rejection_reasons[0][:40]})"
                    print(f"  [{self._time()}] Scanning... no signal{reason}")
                
                if overlay and status != "dedup":
                    pending = pending_trade is not None
                    overlay.root.after(0, overlay.update_training_stats, self.total_trades, self.wins, self.losses, len(self.ml_layer.training_data), pending)

            time.sleep(CAPTURE.scan_interval)

        # Final summary
        self._print_summary()
        self._save_state()

    def _record_outcome(self, trade, won):
        """Record a trade outcome."""
        self.total_trades += 1
        if won:
            self.wins += 1
        else:
            self.losses += 1

        result_icon = "[WIN]" if won else "[LOSS]"
        rate = self.wins / self.total_trades * 100

        print(f"  [{self._time()}] {result_icon}  - "
              f"{trade['direction']} {trade['confidence']:.0f}% "
              f"| Record: {self.wins}W {self.losses}L ({rate:.0f}%)")

        # Feed to ML
        # Reconstruct a minimal SignalResult for ML training
        result = SignalResult()
        result.direction = trade['direction']
        result.confidence = trade['confidence']
        result.grade = SignalGrade(trade['grade'])
        result.factor_scores = trade['factor_scores']
        result.entry_factors = trade['entry_factors']
        result.risk_flags = trade['risk_flags']
        result.prob_up = trade.get('prob_up', 0.5)
        result.prob_down = trade.get('prob_down', 0.5)

        self.ml_layer.add_training_sample(result, won)

        # Log
        self.training_log.append({
            'time': self._time(),
            'direction': trade['direction'],
            'confidence': trade['confidence'],
            'grade': trade['grade'],
            'outcome': 'win' if won else 'loss',
            'total': self.total_trades,
            'win_rate': rate,
        })

        self._save_state()

    def _print_summary(self):
        """Print training summary."""
        print()
        print("=" * 60)
        print("  TRAINING SUMMARY")
        print("=" * 60)
        if self.total_trades > 0:
            rate = self.wins / self.total_trades * 100
            print(f"  Total trades : {self.total_trades}")
            print(f"  Wins         : {self.wins}")
            print(f"  Losses       : {self.losses}")
            print(f"  Win rate     : {rate:.1f}%")
            print(f"  ML samples   : {len(self.ml_layer.training_data)}")
            print(f"  ML trained   : {self.ml_layer.is_trained}")
            if self.ml_layer.is_trained:
                print(f"  ML CV score  : {self.ml_layer.cv_score:.1%}")
        else:
            print("  No trades completed.")
        print("=" * 60)

    def _save_state(self):
        """Persist training state."""
        try:
            os.makedirs(os.path.dirname(_TRAINING_STATE_PATH), exist_ok=True)
            state = {
                'total_trades': self.total_trades,
                'wins': self.wins,
                'losses': self.losses,
                'timestamp': time.time(),
            }
            with open(_TRAINING_STATE_PATH, 'w') as f:
                json.dump(state, f, indent=2)
            with open(_TRAINING_LOG_PATH, 'w') as f:
                json.dump(self.training_log[-500:], f, indent=2)
        except Exception:
            pass

    def _load_state(self):
        """Load previous training state."""
        try:
            if os.path.exists(_TRAINING_STATE_PATH):
                with open(_TRAINING_STATE_PATH, 'r') as f:
                    state = json.load(f)
                self.total_trades = state.get('total_trades', 0)
                self.wins = state.get('wins', 0)
                self.losses = state.get('losses', 0)
            if os.path.exists(_TRAINING_LOG_PATH):
                with open(_TRAINING_LOG_PATH, 'r') as f:
                    self.training_log = json.load(f)
        except Exception:
            pass

    def cleanup(self):
        """Release resources."""
        try:
            self.screen_capture.cleanup()
        except Exception:
            pass

    @staticmethod
    def _time():
        return datetime.now().strftime("%H:%M:%S")


def training_thread(trader, overlay):
    try:
        trader.run_training_loop(max_trades=300, target_win_rate=0.60, overlay=overlay)
    except KeyboardInterrupt:
        print("\n  Training interrupted by user.")
        trader._print_summary()
    finally:
        trader.cleanup()
        trader._save_state()

def main():
    print("\n  Starting Auto Trader with UI Overlay for ML training...")
    print("  Make sure Olymp Trade is open and visible.\n")
    
    from ui.overlay import SignalOverlay
    
    trader = AutoTrader()
    overlay = SignalOverlay()
    
    t = threading.Thread(target=training_thread, args=(trader, overlay), daemon=True)
    t.start()
    
    overlay.run()


if __name__ == "__main__":
    main()
