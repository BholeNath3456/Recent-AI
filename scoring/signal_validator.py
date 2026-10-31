# ============================================================
#  SIGNAL VALIDATOR — Trade filter / rejection logic (v5)
#  v5: Confluence gate + tightened filters
#  - NEW: Confluence gate rejection (min 5/7 voters)
#  - Momentum threshold tightened to ±0.3
#  - Last candle force hard rejection (body_ratio 0.65)
#  - Recent candle dominance hard rejection
#  - Triple opposition hard rejection
#  - Net displacement check
#  - Tighter overextension chasing threshold
#  - Soft penalty increased to 10 per rejection
# ============================================================

from typing import List, Optional
import sys
sys.path.insert(0, '.')
from core.candle import Candle
from core.market_context import (
    MarketContext, TrendState, VolatilityRegime, StructureState
)
from core.signal_result import SignalResult, SignalGrade
from config import SCORING


class SignalValidator:
    """
    Validates signals and rejects trades when conditions are unfavourable.
    This is the final quality gate before a signal is displayed.

    v4 Changes:
    - Momentum conflict threshold tightened from ±0.5 to ±0.3
    - NEW: Last candle force hard rejection (strong candle opposes signal)
    - NEW: Recent candle dominance hard rejection (3+ of 4 candles oppose)
    - NEW: Triple opposition hard rejection (trend + momentum + structure all STRONGLY oppose)
    - NEW: Net displacement check (large move in opposite direction = reject)
    - Overextension chasing threshold lowered from 0.7 to 0.5
    - Hard penalty reduced from 15 to 10 for faster signal throughput
    """

    def __init__(self):
        self._last_signal_dir: Optional[str] = None
        self._last_signal_scan: int = 0
        self._consecutive_same_dir: int = 0
        self._scan_count: int = 0
        self._last_fingerprint: str = ""

    def validate(self, result: SignalResult, candles: List[Candle],
                 ctx: MarketContext, fake_breakout_prob: float,
                 fingerprint: str = "",
                 overextension_score: float = 0.0,
                 overextension_direction: str = None,
                 immediate_pressure: float = 0.0) -> SignalResult:
        """Apply all rejection filters. Modifies result in-place."""
        trend_weak = False
        self._scan_count += 1

        # Track whether candle data actually changed
        data_changed = fingerprint and fingerprint != self._last_fingerprint
        if fingerprint:
            self._last_fingerprint = fingerprint

        if result.direction is None:
            result.rejection_reasons.append("No directional bias")
            return result

        # ══════════════════════════════════════════════════════════════
        #  ELDER-RAY HARD REJECTIONS (highest priority — checked first)
        #  These rules are based on the oscillator and override everything.
        # ══════════════════════════════════════════════════════════════

        # Rule A: Elder-Ray Divergence Block
        # If Bulls Power is diverging bearishly (price up but bulls power down)
        # → it means the bulls are LOSING power at the top. Block UP signals.
        if ctx.elder_ray_valid and ctx.elder_ray_bulls_divergence:
            if result.direction == "UP":
                result.rejection_reasons.append(
                    "Elder-Ray: Bearish divergence (price rising but Bulls Power falling) — "
                    "UP signal blocked. Expect reversal DOWN.")
                result.grade = SignalGrade.NO_TRADE
                result.direction = None
                return result

        # Bullish divergence (price down but bears power rising toward zero)
        # → bears are LOSING power at the bottom. Block DOWN signals.
        if ctx.elder_ray_valid and ctx.elder_ray_bears_divergence:
            if result.direction == "DOWN":
                result.rejection_reasons.append(
                    "Elder-Ray: Bullish divergence (price falling but Bears Power rising) — "
                    "DOWN signal blocked. Expect reversal UP.")
                result.grade = SignalGrade.NO_TRADE
                result.direction = None
                return result

        # Rule B: Elder-Ray Exhaustion Block
        # Both oscillators shrinking toward zero = no momentum = no trade
        if ctx.elder_ray_valid and ctx.elder_ray_exhaustion:
            result.rejection_reasons.append(
                "Elder-Ray: Both Bulls & Bears Power exhausted (converging to zero) — "
                "no clear momentum. Wait for new signal.")
            result.grade = SignalGrade.NO_TRADE
            result.direction = None
            return result

        # Rule C: Elder-Ray Strong Direction Mismatch
        # If Elder-Ray clearly says one direction but signal says opposite → hard reject
        if ctx.elder_ray_valid and ctx.elder_ray_direction is not None:
            if (ctx.elder_ray_direction != result.direction and
                    abs(ctx.elder_ray_score) > 0.40):
                result.rejection_reasons.append(
                    f"Elder-Ray: Direction mismatch — oscillator says {ctx.elder_ray_direction} "
                    f"(score={ctx.elder_ray_score:+.2f}) but signal says {result.direction}. Blocked.")
                result.grade = SignalGrade.NO_TRADE
                result.direction = None
                return result


        # Rule D: STALE TREND + OVEREXTENSION + EXHAUSTION — Hard Block
        stale_trend_flag = any("Stale trend" in flag for flag in result.risk_flags)
        overextended_flag = any("Overextended" in flag for flag in result.risk_flags)
        
        # LOWERED to 0.60 (from 0.80) because OTC trends reverse extremely fast
        if stale_trend_flag and overextended_flag and overextension_score > 0.60:
            if overextension_direction == result.direction:
                # Require Elder-Ray exhaustion OR low confluence
                oscillator_exhausted = ctx.elder_ray_valid and ctx.elder_ray_exhaustion
                weak_confluence = result.confluence_count < 6  # requires 6/10 voters
                if oscillator_exhausted or weak_confluence:
                    result.rejection_reasons.append(
                        f"Stale & overextended {result.direction} ({overextension_score:.0%}) "
                        f"— trend exhaustion detected. Do NOT chase.")
                    result.grade = SignalGrade.NO_TRADE
                    result.direction = None
                    return result

        # ── Rule D2: STRICT EXHAUSTION CHASING BLOCK (1-Min Pullback Sniper) ──
        # Never chase a move that has already produced 2 or 3 same-colored candles.
        # In a 1-minute expiry, you MUST enter on a pullback or the very beginning of a move.
        if len(candles) >= 3 and result.direction is not None:
            c1, c2, c3 = candles[-1], candles[-2], candles[-3]
            
            # If the signal is UP, but the last candle is Green and recent candles are bullish
            if result.direction == "UP" and c1.is_bullish and (c2.is_bullish or c3.is_bullish):
                if c1.body_ratio > 0.35:
                    result.rejection_reasons.append("Exhaustion block: Move already in progress. Do not chase UP. Wait for a pullback.")
                    result.grade = SignalGrade.NO_TRADE
                    result.direction = None
                    return result
            
            # If the signal is DOWN, but the last candle is Red and recent candles are bearish
            if result.direction == "DOWN" and c1.is_bearish and (c2.is_bearish or c3.is_bearish):
                if c1.body_ratio > 0.35:
                    result.rejection_reasons.append("Exhaustion block: Move already in progress. Do not chase DOWN. Wait for a pullback.")
                    result.grade = SignalGrade.NO_TRADE
                    result.direction = None
                    return result


        # ── Rule F: STRICT MACRO-TREND ALIGNMENT (Hyper-Sniper Mode) ──
        # Do not allow any trades against the macro trend.
        if result.direction == "UP" and ctx.trend_state == TrendState.BEARISH:
            result.rejection_reasons.append("Macro-Trend Block: Cannot take UP signal in a BEARISH macro trend.")
            result.grade = SignalGrade.NO_TRADE
            result.direction = None
            return result
            
        if result.direction == "DOWN" and ctx.trend_state == TrendState.BULLISH:
            result.rejection_reasons.append("Macro-Trend Block: Cannot take DOWN signal in a BULLISH macro trend.")
            result.grade = SignalGrade.NO_TRADE
            result.direction = None
            return result


        # ── Rule E: IMMEDIATE REVERSAL BLOCK ──
        # This is the #1 cause of wrong signals: the historical trend says bearish
        # but the RECENT 3-5 candles are clearly reversing.
        # When the IMMEDIATE candle pressure strongly opposes the signal → HARD BLOCK.
        #
        # Example: Long bearish trend, then 5+ green candles going UP.
        # System says DOWN (from EMA/trend), but last candles are all green → WRONG.
        if result.direction is not None and len(candles) >= 3:
            last3 = candles[-3:]
            last5 = candles[-min(5, len(candles)):]

            # Count recent bullish vs bearish candles with body weight
            bull_power = sum(c.body_ratio for c in last5 if c.is_bullish)
            bear_power = sum(c.body_ratio for c in last5 if c.is_bearish)

            # All 3 last candles bullish AND immediate_pressure says bullish
            recent_all_bull = all(c.is_bullish for c in last3)
            recent_all_bear = all(c.is_bearish for c in last3)

            # BLOCK DOWN if recent candles are strongly bullish
            if result.direction == "DOWN":
                if recent_all_bull and immediate_pressure > 0.3:
                    result.rejection_reasons.append(
                        f"Reversal block: last 3 candles are ALL green + immediate pressure "
                        f"({immediate_pressure:+.2f}) opposes DOWN. Likely UP reversal.")
                    result.grade = SignalGrade.NO_TRADE
                    result.direction = None
                    return result
                if bull_power > bear_power * 2.5 and immediate_pressure > 0.5:
                    result.rejection_reasons.append(
                        f"Strong reversal: bull power ({bull_power:.2f}) >> bear power "
                        f"({bear_power:.2f}) with pressure {immediate_pressure:+.2f}. Block DOWN.")
                    result.grade = SignalGrade.NO_TRADE
                    result.direction = None
                    return result

            # BLOCK UP if recent candles are strongly bearish
            elif result.direction == "UP":
                if recent_all_bear and immediate_pressure < -0.3:
                    result.rejection_reasons.append(
                        f"Reversal block: last 3 candles are ALL red + immediate pressure "
                        f"({immediate_pressure:+.2f}) opposes UP. Likely DOWN reversal.")
                    result.grade = SignalGrade.NO_TRADE
                    result.direction = None
                    return result
                if bear_power > bull_power * 2.5 and immediate_pressure < -0.5:
                    result.rejection_reasons.append(
                        f"Strong reversal: bear power ({bear_power:.2f}) >> bull power "
                        f"({bull_power:.2f}) with pressure {immediate_pressure:+.2f}. Block UP.")
                    result.grade = SignalGrade.NO_TRADE
                    result.direction = None
                    return result

        # ── Rule F: OSCILLATOR REVERSAL BLOCK ──
        # When Elder-Ray oscillator shows clear reversal momentum:
        # Bulls Power growing (positive slope) while Bears Power weakening (rising toward 0)
        # AND signal is DOWN → the market is REVERSING, not continuing DOWN.
        if ctx.elder_ray_valid and result.direction is not None:
            bulls_rising = (hasattr(ctx, 'elder_ray_bulls_current') and
                           ctx.elder_ray_bulls_current > 0.05)  # Bulls power positive and building
            bears_weakening = (hasattr(ctx, 'elder_ray_bears_current') and
                               ctx.elder_ray_bears_current > -0.10)  # Bears near zero (weakening)

            if result.direction == "DOWN" and bulls_rising and bears_weakening:
                result.rejection_reasons.append(
                    f"Oscillator reversal: Bulls Power building ({ctx.elder_ray_bulls_current:+.2f}) "
                    f"+ Bears Power weakening ({ctx.elder_ray_bears_current:+.2f}). "
                    f"Market reversing UP — block DOWN signal.")
                result.grade = SignalGrade.NO_TRADE
                result.direction = None
                return result

            # Also block UP when bears building and bulls weakening
            bulls_weakening = (hasattr(ctx, 'elder_ray_bulls_current') and
                               ctx.elder_ray_bulls_current < 0.10)
            bears_strong = (hasattr(ctx, 'elder_ray_bears_current') and
                            ctx.elder_ray_bears_current < -0.05)
            if result.direction == "UP" and bears_strong and bulls_weakening:
                result.rejection_reasons.append(
                    f"Oscillator reversal: Bears Power strong ({ctx.elder_ray_bears_current:+.2f}) "
                    f"+ Bulls Power weak ({ctx.elder_ray_bulls_current:+.2f}). "
                    f"Market reversing DOWN — block UP signal.")
                result.grade = SignalGrade.NO_TRADE
                result.direction = None
                return result

        # ── Rule G: CLIMAX / IMPULSE CANDLE EXHAUSTION BLOCK ──
        # If the last candle is a huge impulse/climax candle (> 1.5x avg body of last 10 candles),
        # in 1-minute trading this represents EXHAUSTION & ABSORPTION.
        # The very next 1-minute candle will almost always mean-revert!
        if len(candles) >= 10 and result.direction is not None:
            avg_body = sum(c.body for c in candles[-10:-1]) / 9.0
            last_c = candles[-1]
            if last_c.body > avg_body * 1.5 and last_c.body_ratio > 0.55:
                if last_c.is_bearish and result.direction == "DOWN":
                    result.rejection_reasons.append(
                        f"Climax Exhaustion: Last candle is a huge impulse drop ({last_c.body:.1f} vs avg {avg_body:.1f}). "
                        f"Likely 1-min bounce UP — block DOWN.")
                    result.grade = SignalGrade.NO_TRADE
                    result.direction = None
                    return result
                elif last_c.is_bullish and result.direction == "UP":
                    result.rejection_reasons.append(
                        f"Climax Exhaustion: Last candle is a huge impulse pump ({last_c.body:.1f} vs avg {avg_body:.1f}). "
                        f"Likely 1-min pullback DOWN — block UP.")
                    result.grade = SignalGrade.NO_TRADE
                    result.direction = None
                    return result

        # ── 0. Confluence gate — penalty only, not hard block (allows learning)
        if result.confluence_count < SCORING.min_confluence_voters:
            # Soft penalty: lower confidence but don't hard-block
            result.rejection_reasons.append(
                f'confluence_low: {result.confluence_count}/10 voters ({SCORING.min_confluence_voters} needed)')
            result.confidence = max(0, result.confidence - 15)
            # Only hard-block if truly no agreement at all
            if result.confluence_count < 1:
                result.grade = SignalGrade.NO_TRADE
                result.direction = None
                return result

        hard_rejections = []
        soft_rejections = []

        # ── 1. Candle conflict (DISABLED for v5 as it triggers too often on screen capture)
        # if self._has_candle_conflict(candles, result.direction):
        #     soft_rejections.append("Candle conflict detected")

        # ── 2. Sideways market / Weak trend (only block if VERY sideways)
        if result.confluence_count < 3:
            if ctx.trend_state == TrendState.SIDEWAYS:
                if not ctx.liquidity_sweep_detected and not ctx.price_at_sr:
                    soft_rejections.append("Sideways market — no edge")

            trend_weak = abs(ctx.trend_strength) < SCORING.min_trend_strength
            if trend_weak:
                if not ctx.liquidity_sweep_detected and not ctx.price_at_sr:
                    soft_rejections.append("Trend too weak")

        # ── 5. Volatility collapse (hard)
        if ctx.volatility_regime == VolatilityRegime.COLLAPSED:
            hard_rejections.append("Volatility collapsed")

        # ── 6. Choppy market — made SOFT (was causing permanent no-trade)
        if ctx.is_choppy:
            soft_rejections.append("Market choppy — lower accuracy")

        # ── 7. Unclear structure
        structure_unclear = ctx.structure_state == StructureState.UNCLEAR
        if structure_unclear and not result.reasons:
            if trend_weak:
                soft_rejections.append("(Structure unclear — merged with trend)")
            else:
                soft_rejections.append("Market structure unclear")

        # ── 3. Fake breakout probability
        if fake_breakout_prob > SCORING.max_fake_breakout_prob:
            soft_rejections.append(f"High fakeout probability ({fake_breakout_prob:.0%})")

        # ── 8. MTF conflict — soft rejection (was causing permanent no-trade on MTF mismatch)
        if ctx.mtf_conflict:
            soft_rejections.append("Higher-timeframe conflict — caution")

        # ── 9. Consecutive exhaustion
        if ctx.is_exhausted:
            is_reversal_signal = any(
                "Exhaustion" in r or "Hammer" in r or "Shooting" in r or
                "Engulfing" in r or "Sweep" in r
                for r in result.reasons
            )
            if not is_reversal_signal:
                soft_rejections.append("Momentum exhausted — reversal likely")

        # ── 10. Trading against momentum — LOOSENED from ±0.3 to ±0.7
        # (±0.3 was too tight and blocked the vast majority of valid signals)
        if result.direction == "UP" and ctx.momentum_score < -0.7:
            hard_rejections.append("Signal against very strong bearish momentum")
        elif result.direction == "DOWN" and ctx.momentum_score > 0.7:
            hard_rejections.append("Signal against very strong bullish momentum")

        # ── 11. ANTI-CHASING: Only block overextension if confluence is WEAK
        # If 5+ voters all agree with the direction, the trend is genuine, not a chase.
        # Only hard-block overextension when confluence < 4 (weak agreement).
        if (overextension_score > 0.65 and
            overextension_direction is not None and
            result.direction == overextension_direction and
            result.confluence_count < 4):   # Allow strong-consensus trends to continue
            hard_rejections.append(
                f"Overextended {overextension_direction} ({overextension_score:.0%}) — weak confluence, pullback risk")
        elif (overextension_score > 0.90 and
              overextension_direction is not None and
              result.direction == overextension_direction):
            # Even with high confluence, flag extreme overextension as soft
            soft_rejections.append(
                f"Extremely overextended {overextension_direction} ({overextension_score:.0%}) — caution")

        # ── Momentum-based divergence: SOFT penalty only (rough heuristic)
        # Elder-Ray divergence (the accurate one) is handled above as hard rejection.
        # The momentum heuristic often gives false "bullish_div" in genuine strong trends.
        if result.direction == "UP" and any("bearish_div" in flag for flag in result.risk_flags):
            soft_rejections.append("Momentum bearish divergence — possible reversal")
        elif result.direction == "DOWN" and any("bullish_div" in flag for flag in result.risk_flags):
            soft_rejections.append("Momentum bullish divergence — possible reversal")

        # ── 12. Last Candle Indecision / Opposition (V5: Made Soft to prevent getting stuck)
        #    Never enter a 1-minute fixed trade if the immediate trigger candle (candles[-1])
        #    shows indecision (doji / body < 28%) or goes opposite to the signal!
        if len(candles) >= 1:
            last = candles[-1]
            if last.body_ratio < 0.28:
                soft_rejections.append(f"Last candle is indecision/doji (body {last.body_ratio:.0%}) — pullback risk")
            elif result.direction == "DOWN" and last.is_bullish:
                soft_rejections.append("Last candle is green/bullish — opposes DOWN signal")
            elif result.direction == "UP" and last.is_bearish:
                soft_rejections.append("Last candle is red/bearish — opposes UP signal")

        # ── 13. v4 NEW: Recent candle dominance (Made Soft)
        #    If 3+ of the last 4 candles are strongly directional opposing signal
        if len(candles) >= 4:
            last4 = candles[-4:]
            if result.direction == "UP":
                strong_bear = sum(1 for c in last4
                                  if c.is_bearish and c.body_ratio > 0.35)
                if strong_bear >= 3:
                    soft_rejections.append(
                        f"Recent candle dominance opposes UP ({strong_bear}/4 bearish)")
            elif result.direction == "DOWN":
                strong_bull = sum(1 for c in last4
                                  if c.is_bullish and c.body_ratio > 0.35)
                if strong_bull >= 3:
                    soft_rejections.append(
                        f"Recent candle dominance opposes DOWN ({strong_bull}/4 bullish)")

        # ── 14. Williams %R Soft Penalty
        if hasattr(ctx, 'williams_r_valid') and ctx.williams_r_valid:
            if result.direction == "DOWN" and ctx.williams_r <= -80:
                soft_rejections.append(f"Williams %R OVERSOLD ({ctx.williams_r:.0f}) — trend continuation risk")
            elif result.direction == "UP" and ctx.williams_r >= -20:
                soft_rejections.append(f"Williams %R OVERBOUGHT ({ctx.williams_r:.0f}) — trend continuation risk")

        # ── 14. v4 NEW: Triple opposition (Made Soft)
        #    If trend + momentum + structure ALL oppose the signal → soft reject
        trend_opposes = False
        momentum_opposes = False
        structure_opposes = False

        if result.direction == "UP":
            trend_opposes = ctx.trend_state in (
                TrendState.STRONG_BEARISH,)  # only STRONG, not mild
            momentum_opposes = ctx.momentum_score < -0.3  # tightened from -0.1
            structure_opposes = ctx.structure_state in (
                StructureState.BEARISH_STRUCTURE,
                StructureState.CHOCH_BEARISH,
                StructureState.BROKEN_BEARISH)
        elif result.direction == "DOWN":
            trend_opposes = ctx.trend_state in (
                TrendState.STRONG_BULLISH,)  # only STRONG, not mild
            momentum_opposes = ctx.momentum_score > 0.3  # tightened from 0.1
            structure_opposes = ctx.structure_state in (
                StructureState.BULLISH_STRUCTURE,
                StructureState.CHOCH_BULLISH,
                StructureState.BROKEN_BULLISH)

        if trend_opposes and momentum_opposes and structure_opposes:
            soft_rejections.append(
                f"Triple opposition: trend + momentum + structure against {result.direction}")

        # ── 15. v4 NEW: Net displacement check
        #    If net close-to-close displacement of last 5 candles exceeds
        #    1.5x ATR in one direction, reject signals in opposite direction
        if len(candles) >= 5 and ctx.atr_value > 0.001:
            net_disp = candles[-1].close - candles[-5].close
            disp_ratio = abs(net_disp) / ctx.atr_value
            if disp_ratio > 1.5:
                if result.direction == "UP" and net_disp < 0:
                    soft_rejections.append(
                        f"Net displacement against UP ({disp_ratio:.1f}x ATR bearish)")
                elif result.direction == "DOWN" and net_disp > 0:
                    soft_rejections.append(
                        f"Net displacement against DOWN ({disp_ratio:.1f}x ATR bullish)")

        # ── 16. v4 NEW: Immediate pressure opposition
        #    If the fast-reacting pressure strongly opposes signal direction
        if abs(immediate_pressure) > 0.5:
            if result.direction == "UP" and immediate_pressure < -0.5:
                hard_rejections.append("Immediate pressure strongly bearish")
            elif result.direction == "DOWN" and immediate_pressure > 0.5:
                hard_rejections.append("Immediate pressure strongly bullish")

        # ── 17. Confidence too low
        if result.confidence < SCORING.min_display_confidence:
            soft_rejections.append(f"Confidence too low ({result.confidence:.0f}%)")

        # ── 18. Signal cooldown — skip if candle data actually changed
        if not data_changed:
            scans_since_last = self._scan_count - self._last_signal_scan
            if (result.direction == self._last_signal_dir and
                scans_since_last < SCORING.signal_cooldown_scans):
                soft_rejections.append(f"Signal cooldown ({scans_since_last}/{SCORING.signal_cooldown_scans})")

        # ── 19. Anti-bias filter
        if result.direction == self._last_signal_dir:
            self._consecutive_same_dir += 1
        else:
            self._consecutive_same_dir = 0

        if self._consecutive_same_dir >= SCORING.max_consecutive_same_dir:
            if result.confidence < 85:
                soft_rejections.append(
                    f"Too many consecutive {result.direction} signals "
                    f"({self._consecutive_same_dir})")

        # ══════════════════════════════════════════
        #  APPLY REJECTIONS
        # ══════════════════════════════════════════
        effective_soft = [r for r in soft_rejections if not r.startswith("(")]

        all_rejections = hard_rejections + soft_rejections
        if all_rejections:
            result.rejection_reasons = all_rejections

        if hard_rejections:
            # TRUE HARD REJECTION: Cancel signal completely!
            result.grade = SignalGrade.NO_TRADE
            result.direction = None
            return result

        if soft_rejections:
            result.confidence = max(0, result.confidence - (5 * len(soft_rejections)))

        # Track for cooldown/anti-bias
        if result.confidence >= SCORING.min_display_confidence and result.direction is not None:
            self._last_signal_dir = result.direction
            self._last_signal_scan = self._scan_count

        return result

    def _has_candle_conflict(self, candles: List[Candle], direction: str) -> bool:
        """Check if recent candles conflict with signal direction."""
        if len(candles) < 3:
            return False
        last3 = candles[-3:]
        if direction == "UP":
            bearish_count = sum(1 for c in last3 if c.is_bearish and c.body_ratio > 0.3)
            return bearish_count >= 2
        else:
            bullish_count = sum(1 for c in last3 if c.is_bullish and c.body_ratio > 0.3)
            return bullish_count >= 2

    def reset(self):
        """Reset validator state (called on engine reset)."""
        self._last_signal_dir = None
        self._last_signal_scan = 0
        self._consecutive_same_dir = 0
        self._scan_count = 0
        self._last_fingerprint = ""
