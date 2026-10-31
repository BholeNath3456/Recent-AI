# ============================================================
#  CONFIDENCE ENGINE — Weighted probabilistic scoring (v4)
#  v4: Fixed false counter-trend signals
#  - Removed mean-reversion bonus (was creating false UP signals)
#  - Added immediate pressure as 4th direction voter
#  - Added absolute direction block for strong candles
#  - Counter-trend patterns penalized to 30% strength
#  - Replaced majority-rules with weighted directional gate
#  - Confidence partially directional
# ============================================================

from typing import List, Dict
import math
import sys
sys.path.insert(0, '.')
from core.candle import Candle
from core.market_context import MarketContext, TrendState, VolatilityRegime, StructureState
from core.signal_result import SignalResult
from engines.pattern_engine import PatternResult
from config import SCORING


class ConfidenceEngine:
    """
    Combines all analysis factors into a probabilistic signal.
    Outputs UP / DOWN / NO_TRADE probabilities.

    v4 Changes:
    - REMOVED mean-reversion bonus (was the #1 cause of false UP signals)
    - Added immediate_pressure (last 2-3 candle force) as a 4th direction voter
    - Absolute direction block: strong marubozu candles block opposite signals
    - Counter-trend pattern strength reduced to 30%
    - Weighted directional gate replaces binary majority-rules
    - Confidence scoring is partially direction-aware
    """

    def calculate(self, candles: List[Candle], ctx: MarketContext,
                  patterns: List[PatternResult],
                  momentum_quality: float,
                  pullback_quality: float,
                  fake_breakout_prob: float,
                  divergence: str,
                  overextension_score: float = 0.0,
                  overextension_direction: str = None,
                  trend_age_penalty: float = 0.0,
                  immediate_pressure: float = 0.0,
                  immediate_trend: float = 0.0,
                  elder_ray_score: float = 0.0) -> SignalResult:
        """Calculate weighted confidence scores."""
        result = SignalResult()
        if len(candles) < 5:
            result.prob_no_trade = 1.0
            return result

        last = candles[-1]
        scores: Dict[str, float] = {}

        # ── 0. ELDER-RAY (30% weight — highest priority, most accurate) ──
        # elder_ray_score is -1.0 (strong bear) to +1.0 (strong bull)
        # Passed from ctx.elder_ray_score which is set in main.py scan loop
        er_score = ctx.elder_ray_score if ctx.elder_ray_valid else elder_ray_score
        scores['elder_ray'] = abs(er_score)  # magnitude = quality

        # ── 1. Trend alignment (18% — reduced to make room for Elder-Ray)
        trend_up, trend_down = 0.0, 0.0
        if ctx.trend_state in (TrendState.STRONG_BULLISH, TrendState.BULLISH):
            trend_up = abs(ctx.trend_strength)
        elif ctx.trend_state in (TrendState.STRONG_BEARISH, TrendState.BEARISH):
            trend_down = abs(ctx.trend_strength)
        scores['trend_alignment'] = max(trend_up, trend_down)

        # ── 2. Momentum quality (12% — reduced)
        scores['momentum_quality'] = momentum_quality

        # ── 3. Candle strength (10%)
        candle_score = last.body_strength
        scores['candle_strength'] = candle_score

        # ── 4. Structure confirmation (15%)
        struct_score = 0.0
        if ctx.structure_state in (StructureState.BULLISH_STRUCTURE,
                                    StructureState.CHOCH_BULLISH,
                                    StructureState.BROKEN_BULLISH):
            struct_score = 0.8
        elif ctx.structure_state in (StructureState.BEARISH_STRUCTURE,
                                      StructureState.CHOCH_BEARISH,
                                      StructureState.BROKEN_BEARISH):
            struct_score = 0.8
        elif ctx.structure_state != StructureState.UNCLEAR:
            struct_score = 0.4
        scores['structure_confirmation'] = struct_score

        # ── 5. S/R reaction (10%)
        sr_score = 0.7 if ctx.price_at_sr else 0.0
        if ctx.price_at_sr and abs(last.wick_rejection_pressure) > 0.3:
            sr_score = 0.9
        scores['sr_reaction'] = sr_score
        if pullback_quality > 0.5:
            scores['sr_reaction'] = max(scores['sr_reaction'], pullback_quality * 0.8)

        # ── 6. Wick rejection (2%)
        raw_wick = abs(last.wick_rejection_pressure)
        wick_score = min(1.0, raw_wick * 0.8)
        scores['wick_rejection'] = wick_score

        # ── 7. Volatility quality (8%)
        vol_score = 0.0
        if ctx.volatility_regime == VolatilityRegime.NORMAL:
            vol_score = 0.8
        elif ctx.volatility_regime == VolatilityRegime.EXPANDING:
            vol_score = 0.6
        elif ctx.volatility_regime == VolatilityRegime.COMPRESSING:
            vol_score = 0.3
        scores['volatility_quality'] = vol_score

        # ── 8. Breakout confirmation (4%)
        breakout_score = 0.0
        for p in patterns:
            if p.pattern_type == "breakout":
                breakout_score = max(breakout_score, p.strength)
        for p in patterns:
            if "Momentum" in p.name or "Breakout" in p.name:
                breakout_score = max(breakout_score, p.strength * 0.8)
        scores['breakout_confirmation'] = breakout_score

        # ── 9. Exhaustion probability (3%)
        exhaust_score = 0.0
        if ctx.is_exhausted:
            exhaust_score = 0.7
        for p in patterns:
            if "Exhaustion" in p.name or "Fakeout" in p.name:
                exhaust_score = max(exhaust_score, p.strength)
        if len(candles) >= 4:
            last_reversal_prob = last.reversal_probability
            if last_reversal_prob > 0.6:
                exhaust_score = max(exhaust_score, last_reversal_prob * 0.7)
        scores['exhaustion_probability'] = exhaust_score

        # ── 10. Liquidity sweep (3%)
        sweep_score = 0.0
        if ctx.liquidity_sweep_detected:
            sweep_score = 0.8
        for p in patterns:
            if "Liquidity" in p.name or "Sweep" in p.name:
                sweep_score = max(sweep_score, p.strength)
        scores['liquidity_sweep'] = sweep_score

        # ── 11. Immediate pressure (2%) — NEW v4
        scores['immediate_pressure'] = abs(immediate_pressure)

        result.factor_scores = scores

        # ══════════════════════════════════════════
        #  COMPUTE WEIGHTED TOTAL
        # ══════════════════════════════════════════
        # Start with base weights and inject Elder-Ray
        adj_weights = dict(SCORING.weights)
        adj_weights['elder_ray'] = 0.15   # Reduced from 30% to 15% (less lag)
        # Proportionally reduce all other weights to accommodate Elder-Ray
        other_sum = sum(v for k, v in adj_weights.items() if k != 'elder_ray')
        scale = 0.85 / max(other_sum, 0.001)
        adj_weights = {k: (v * scale if k != 'elder_ray' else v)
                       for k, v in adj_weights.items()}

        # Volatility-adjusted weights
        if ctx.volatility_regime == VolatilityRegime.EXPANDING:
            adj_weights['momentum_quality'] = adj_weights.get('momentum_quality', 0.12) * 1.3
            adj_weights['candle_strength']  = adj_weights.get('candle_strength',  0.07) * 1.2
        elif ctx.volatility_regime == VolatilityRegime.COMPRESSING:
            adj_weights['breakout_confirmation'] = adj_weights.get('breakout_confirmation', 0.03) * 1.5
            adj_weights['sr_reaction']           = adj_weights.get('sr_reaction', 0.07) * 1.3
        # Re-normalize weights to sum to 1.0
        total_w = sum(adj_weights.values())
        adj_weights = {k: v / total_w for k, v in adj_weights.items()}

        weighted_total = sum(
            scores.get(k, 0.0) * w
            for k, w in adj_weights.items()
        )

        # ══════════════════════════════════════════
        #  ABSOLUTE DIRECTION BLOCK (v4 NEW)
        #  If the last candle is a strong directional candle,
        #  absolutely block any signal in the opposite direction.
        # ══════════════════════════════════════════
        absolute_block_up = False
        absolute_block_down = False

        if last.body_ratio > 0.80 and last.is_bearish:
            absolute_block_up = True  # strong red candle → no UP
        elif last.body_ratio > 0.80 and last.is_bullish:
            absolute_block_down = True  # strong green candle → no DOWN

        # Also block if last 2 candles are both strong same direction
        if len(candles) >= 2:
            prev = candles[-2]
            if (last.is_bearish and prev.is_bearish and
                last.body_ratio > 0.60 and prev.body_ratio > 0.60):
                absolute_block_up = True
            elif (last.is_bullish and prev.is_bullish and
                  last.body_ratio > 0.60 and prev.body_ratio > 0.60):
                absolute_block_down = True

        # ══════════════════════════════════════════
        #  DIRECTION SCORING (v5 — Elder-Ray leads)
        # ══════════════════════════════════════════
        up_signals = 0.0
        down_signals = 0.0

        # ── ELDER-RAY DIRECTION (reduced weight = 0.15) ──
        if er_score > 0.05:
            up_signals += er_score * 0.15
        elif er_score < -0.05:
            down_signals += abs(er_score) * 0.15

        # Elder-Ray divergence → strong penalty on diverging direction
        if ctx.elder_ray_bulls_divergence:   # bearish div → block UP
            down_signals += 0.20
        if ctx.elder_ray_bears_divergence:   # bullish div → block DOWN
            up_signals += 0.20

        # Elder-Ray zero-cross → strongest single signal
        if ctx.elder_ray_zero_cross_up:
            up_signals += 0.25
        if ctx.elder_ray_zero_cross_down:
            down_signals += 0.25

        # From trend (reduced weight)
        up_signals += trend_up * adj_weights.get('trend_alignment', 0.18)
        down_signals += trend_down * adj_weights.get('trend_alignment', 0.18)

        # From momentum (weighted by direction)
        if ctx.momentum_score > 0:
            up_signals += momentum_quality * SCORING.weights['momentum_quality']
        elif ctx.momentum_score < 0:
            down_signals += momentum_quality * SCORING.weights['momentum_quality']

        # From candle direction (weighted)
        if last.is_bullish:
            up_signals += candle_score * SCORING.weights['candle_strength']
        elif last.is_bearish:
            down_signals += candle_score * SCORING.weights['candle_strength']

        # From structure (directional)
        if ctx.structure_state in (StructureState.BULLISH_STRUCTURE,
                                    StructureState.CHOCH_BULLISH,
                                    StructureState.BROKEN_BULLISH):
            up_signals += struct_score * SCORING.weights['structure_confirmation']
        elif ctx.structure_state in (StructureState.BEARISH_STRUCTURE,
                                      StructureState.CHOCH_BEARISH,
                                      StructureState.BROKEN_BEARISH):
            down_signals += struct_score * SCORING.weights['structure_confirmation']

        # From wick rejection (directional)
        if last.wick_rejection_pressure > 0.1:
            up_signals += wick_score * SCORING.weights['wick_rejection']
        elif last.wick_rejection_pressure < -0.1:
            down_signals += wick_score * SCORING.weights['wick_rejection']

        # From patterns — v4: counter-trend patterns already penalized by pattern_engine
        pattern_up = 0.0
        pattern_down = 0.0
        for p in patterns:
            if p.direction == "UP":
                pattern_up += p.strength * 0.05
            else:
                pattern_down += p.strength * 0.05
        # Cap total pattern contribution (reduced from 0.12)
        max_pattern_contrib = 0.08
        up_signals += min(pattern_up, max_pattern_contrib)
        down_signals += min(pattern_down, max_pattern_contrib)

        # From divergence
        if divergence == "bullish_div":
            up_signals += 0.03
        elif divergence == "bearish_div":
            down_signals += 0.03

        # From liquidity sweep (directional)
        if ctx.liquidity_sweep_detected:
            if ctx.sweep_direction == "bullish":
                up_signals += 0.04
            elif ctx.sweep_direction == "bearish":
                down_signals += 0.04

        # From immediate pressure (INCREASED — must dominate for reversals)
        if immediate_pressure > 0.1:
            up_signals += abs(immediate_pressure) * 0.20  # was 0.08
        elif immediate_pressure < -0.1:
            down_signals += abs(immediate_pressure) * 0.20

        # From immediate trend (INCREASED)
        if immediate_trend > 0.1:
            up_signals += abs(immediate_trend) * 0.15  # was 0.06
        elif immediate_trend < -0.1:
            down_signals += abs(immediate_trend) * 0.15

        # ══════════════════════════════════════════
        #  WEIGHTED DIRECTIONAL GATE (v4 — replaces majority-rules)
        #  Uses weighted combination of 4 directional signals.
        #  If the gate opposes the computed direction, hard-block.
        # ══════════════════════════════════════════

        # Compute directional strength for each voter (-1 to +1 scale)
        # Trend direction
        trend_dir_val = 0.0
        if ctx.trend_state in (TrendState.STRONG_BULLISH, TrendState.BULLISH):
            trend_dir_val = abs(ctx.trend_strength)
        elif ctx.trend_state in (TrendState.STRONG_BEARISH, TrendState.BEARISH):
            trend_dir_val = -abs(ctx.trend_strength)

        # Momentum direction
        momentum_dir_val = ctx.momentum_score  # already -1 to +1

        # Recent candle direction (body-weighted)
        recent_bull = sum(c.body_ratio for c in candles[-5:] if c.is_bullish)
        recent_bear = sum(c.body_ratio for c in candles[-5:] if c.is_bearish)
        recent_total = recent_bull + recent_bear
        recent_dir_val = (recent_bull - recent_bear) / max(recent_total, 0.01)

        # Immediate pressure (last 2-3 candles, fast-reacting)
        imm_dir_val = immediate_pressure  # already -1 to +1

        # Elder-Ray direction for gate
        er_dir_val = er_score  # already -1 to +1

        # Weighted gate score: Elder-Ray leads, immediate pressure is 2nd
        gate_score = (
            er_dir_val     * 0.35 +      # Elder-Ray (NEW — most accurate)
            imm_dir_val    * 0.25 +      # last 2-3 candles (immediate)
            recent_dir_val * 0.20 +      # last 5 candles
            momentum_dir_val * 0.12 +    # momentum
            trend_dir_val  * 0.08        # EMA trend (slow, reduced)
        )

        # ══════════════════════════════════════════
        #  PROBABILITIES
        # ══════════════════════════════════════════
        total_dir = up_signals + down_signals + 0.0001
        raw_up = up_signals / total_dir
        raw_down = down_signals / total_dir

        # Direction clarity
        dir_clarity = abs(raw_up - raw_down)

        # NO_TRADE bias — reduced for signal throughput
        uncertainty = 1.0 - dir_clarity
        no_trade_prob = SCORING.no_trade_bias + uncertainty * 0.20  # was 0.35

        # Penalties
        if fake_breakout_prob > 0.5:
            no_trade_prob += fake_breakout_prob * 0.2
        if ctx.is_choppy:
            no_trade_prob += 0.05   # reduced from 0.15 (choppy is already a soft reject)
        if ctx.mtf_conflict:
            no_trade_prob += 0.08   # reduced from 0.20 (already a soft reject in validator)
        # Conflicting wick rejection vs direction
        if (raw_up > raw_down and last.wick_rejection_pressure < -0.4):
            no_trade_prob += 0.1
        elif (raw_down > raw_up and last.wick_rejection_pressure > 0.4):
            no_trade_prob += 0.1

        # ══════════════════════════════════════════
        #  ANTI-CHASING: Overextension penalty (v4 FIXED)
        #  NO mean-reversion bonus — only suppress chasing
        # ══════════════════════════════════════════
        computed_dir = "UP" if raw_up > raw_down else "DOWN"

        if overextension_score > 0.4 and overextension_direction is not None:
            # If signal wants to go in the SAME direction as the overextension = chasing
            # But reduce penalty if gate strongly agrees (genuine trend, not chasing)
            if computed_dir == overextension_direction:
                gate_agrees = ((computed_dir == "UP" and gate_score > 0.3) or
                               (computed_dir == "DOWN" and gate_score < -0.3))
                penalty_scale = 0.5 if gate_agrees else 1.0  # halve if gate agrees
                if overextension_score > 0.8:
                    no_trade_prob += 0.25 * penalty_scale
                elif overextension_score > 0.6:
                    no_trade_prob += 0.15 * penalty_scale
                else:
                    no_trade_prob += 0.08 * penalty_scale

        # Trend age penalty — capped
        if trend_age_penalty > 0.5:
            if computed_dir == overextension_direction:
                no_trade_prob += min(0.10, trend_age_penalty * 0.10)

        # v5: Weighted directional gate penalty — STRENGTHENED
        # If gate opposes computed direction, signal is very likely wrong
        if computed_dir == "UP" and gate_score < -0.15:
            no_trade_prob += 0.22
        elif computed_dir == "DOWN" and gate_score > 0.15:
            no_trade_prob += 0.22

        # If gate is strongly opposed, swap direction to trust the gate
        if computed_dir == "UP" and gate_score < -0.30:
            raw_up, raw_down = raw_down, raw_up
        elif computed_dir == "DOWN" and gate_score > 0.30:
            raw_up, raw_down = raw_down, raw_up

        # Mixed/no-consensus penalty (drastically reduced)
        if abs(gate_score) < 0.10:
            no_trade_prob += 0.05  # was 0.12

        # v4: Absolute direction block — REDUCED penalty (was 0.30, killing all signals)
        if absolute_block_up and raw_up > raw_down:
            no_trade_prob += 0.12  # was 0.30 — too high
        elif absolute_block_down and raw_down > raw_up:
            no_trade_prob += 0.12  # was 0.30 — too high

        no_trade_prob = min(0.75, no_trade_prob)  # Cap at 75% so dir prob can survive

        # Normalise
        scale = max(0.1, 1.0 - no_trade_prob)
        result.prob_up = max(0.0, raw_up * scale)
        result.prob_down = max(0.0, raw_down * scale)
        result.prob_no_trade = max(0.0, min(1.0, no_trade_prob))

        # Direction — v4: check absolute blocks
        if result.prob_up > result.prob_down and result.prob_up > result.prob_no_trade:
            if absolute_block_up:
                result.direction = None
            else:
                result.direction = "UP"
        elif result.prob_down > result.prob_up and result.prob_down > result.prob_no_trade:
            if absolute_block_down:
                result.direction = None
            else:
                result.direction = "DOWN"
        else:
            result.direction = None

        # v4: Final gate check — loosened threshold
        if result.direction is not None:
            if result.direction == "UP" and gate_score < -0.50:
                result.direction = None
            elif result.direction == "DOWN" and gate_score > 0.50:
                result.direction = None

        # ══════════════════════════════════════════
        #  CONFIDENCE — v5: reweighted for signal throughput
        # ══════════════════════════════════════════
        dir_prob = max(result.prob_up, result.prob_down)

        # Count directional factors that AGREE with signal — STRICT thresholds
        directional_agreement = 0.0
        agreement_count = 0  # Track how many core factors agree
        if result.direction == "UP":
            if trend_up > 0.3:
                directional_agreement += 0.25
                agreement_count += 1
            if ctx.momentum_score > 0.2:
                directional_agreement += 0.25
                agreement_count += 1
            if immediate_pressure > 0.2:
                directional_agreement += 0.25
                agreement_count += 1
            if last.is_bullish and last.body_ratio > 0.3:
                directional_agreement += 0.15
                agreement_count += 1
            if struct_score > 0.5 and ctx.structure_state in (
                StructureState.BULLISH_STRUCTURE, StructureState.CHOCH_BULLISH,
                StructureState.BROKEN_BULLISH):
                agreement_count += 1
        elif result.direction == "DOWN":
            if trend_down > 0.3:
                directional_agreement += 0.25
                agreement_count += 1
            if ctx.momentum_score < -0.2:
                directional_agreement += 0.25
                agreement_count += 1
            if immediate_pressure < -0.2:
                directional_agreement += 0.25
                agreement_count += 1
            if last.is_bearish and last.body_ratio > 0.3:
                directional_agreement += 0.15
                agreement_count += 1
            if struct_score > 0.5 and ctx.structure_state in (
                StructureState.BEARISH_STRUCTURE, StructureState.CHOCH_BEARISH,
                StructureState.BROKEN_BEARISH):
                agreement_count += 1

        # ADAPTIVE: Only kill if ZERO core factors agree (was <2, too strict)
        if result.direction is not None and agreement_count < 1:
            result.direction = None
            result.risk_flags.append(
                f"Low consensus ({agreement_count}/5 factors agree)")

        # ── IMMEDIATE PULLBACK BOOST (1-Min Sniper) ──
        # If the trend is UP, and the last candle was red (pullback), but now we have a signal UP,
        # this is exactly where we want to enter! Boost the signal.
        if len(candles) >= 2:
            prev = candles[-2]
            if trend_up > trend_down and last.is_bearish and prev.is_bullish:
                # UP trend, but pulling back right now. Boost UP signals slightly
                # if momentum is still generally bullish.
                if ctx.momentum_score > 0:
                    up_signals += 0.15
            elif trend_down > trend_up and last.is_bullish and prev.is_bearish:
                # DOWN trend, but pulling back right now. Boost DOWN signals.
                if ctx.momentum_score < 0:
                    down_signals += 0.15

        # Assign confidence based on dominant direction lowered to 0.35 (was 0.45 — too restrictive)
        # This means normal market conditions (net_score ~0.4) now give ~65% confidence
        net_score = weighted_total * 0.5 + (dir_prob * 0.3) + (directional_agreement / 5.0 * 0.2)
        sigmoid_conf = 100.0 / (1.0 + math.exp(-12.0 * (net_score - 0.35)))
        raw_confidence = sigmoid_conf
        result.confidence = max(0, min(95, raw_confidence))

        # Build reasons
        for p in patterns:
            result.reasons.append(f"{p.name} ({p.direction})")
        if ctx.trend_state != TrendState.SIDEWAYS:
            result.entry_factors.append(f"Trend: {ctx.trend_state.value}")
        if ctx.mtf_aligned:
            result.entry_factors.append("MTF aligned")
        if ctx.liquidity_sweep_detected:
            result.entry_factors.append(f"Liquidity sweep ({ctx.sweep_direction})")
        if momentum_quality > 0.6:
            result.entry_factors.append("Strong momentum")
        if pullback_quality > 0.5:
            result.entry_factors.append("Quality pullback")
        if struct_score > 0.5:
            result.entry_factors.append(f"Structure: {ctx.structure_state.value}")
        if breakout_score > 0.3:
            result.entry_factors.append("Breakout confirmed")
        if sr_score > 0.5:
            result.entry_factors.append("S/R reaction")
        # v4: Add gate consensus info
        if abs(gate_score) > 0.15:
            gate_dir = "Bullish" if gate_score > 0 else "Bearish"
            result.entry_factors.append(f"Consensus: {gate_dir} ({gate_score:+.2f})")
        # v4: Add immediate pressure info
        if abs(immediate_pressure) > 0.3:
            imm_dir = "Bullish" if immediate_pressure > 0 else "Bearish"
            result.entry_factors.append(f"Immediate: {imm_dir}")

        # Risk flags
        if fake_breakout_prob > 0.4:
            result.risk_flags.append(f"Fakeout risk {fake_breakout_prob:.0%}")
        if ctx.is_exhausted:
            result.risk_flags.append("Momentum exhaustion")
        if ctx.is_choppy:
            result.risk_flags.append("Choppy market")
        if ctx.mtf_conflict:
            result.risk_flags.append("MTF conflict")
        if divergence != "none":
            result.risk_flags.append(f"Divergence: {divergence}")
        if result.direction == "UP" and last.wick_rejection_pressure < -0.4:
            result.risk_flags.append("Wick rejects UP")
        elif result.direction == "DOWN" and last.wick_rejection_pressure > 0.4:
            result.risk_flags.append("Wick rejects DOWN")
        # v4: gate disagreement flag
        if result.direction == "UP" and gate_score < 0:
            result.risk_flags.append(f"Gate opposes UP ({gate_score:+.2f})")
        elif result.direction == "DOWN" and gate_score > 0:
            result.risk_flags.append(f"Gate opposes DOWN ({gate_score:+.2f})")
        # v4: overextension flag
        if overextension_score > 0.5:
            result.risk_flags.append(f"Overextended ({overextension_score:.0%})")
        if trend_age_penalty > 0.5:
            result.risk_flags.append(f"Stale trend ({trend_age_penalty:.0%})")
        # v4: absolute block flags
        if absolute_block_up:
            result.risk_flags.append("Strong bearish candle blocks UP")
        if absolute_block_down:
            result.risk_flags.append("Strong bullish candle blocks DOWN")

        return result

    def confluence_check(self, candles: List[Candle], ctx: MarketContext,
                         patterns: List[PatternResult],
                         immediate_pressure: float = 0.0,
                         immediate_trend: float = 0.0,
                         result: SignalResult = None,
                         elder_ray_score: float = 0.0) -> SignalResult:
        """
        8-Voter Confluence Gate (v5).
        Checks if 5+ of 8 independent analysis modules agree on direction.
        This is the PRIMARY quality filter — only signals with 5/8+ confluence
        are considered tradeable.

        Voters:
          1. Trend (EMA-based trend state)
          2. Momentum (momentum score)
          3. Structure (market structure state)
          4. Candle Pressure (last 2 candles' net direction)
          5. Pattern (candlestick pattern detection)
          6. S/R Position (price at support/resistance)
          7. Immediate Trend (last 3 candles direction)
          8. Momentum acceleration (technical proxy)
        """
        if result is None or result.direction is None:
            return result

        direction = result.direction
        voters = []

        # ── Voter 1: TREND ──
        if direction == "UP":
            if ctx.trend_state in (TrendState.BULLISH, TrendState.STRONG_BULLISH):
                voters.append("Trend: Bullish")
        elif direction == "DOWN":
            if ctx.trend_state in (TrendState.BEARISH, TrendState.STRONG_BEARISH):
                voters.append("Trend: Bearish")

        # ── Voter 2: MOMENTUM ──
        if direction == "UP" and ctx.momentum_score > 0.20:
            voters.append(f"Momentum: +{ctx.momentum_score:.2f}")
        elif direction == "DOWN" and ctx.momentum_score < -0.20:
            voters.append(f"Momentum: {ctx.momentum_score:.2f}")

        # ── Voter 3: STRUCTURE ──
        if direction == "UP" and ctx.structure_state in (
                StructureState.BULLISH_STRUCTURE, StructureState.BROKEN_BULLISH,
                StructureState.CHOCH_BULLISH):
            voters.append(f"Structure: {ctx.structure_state.value}")
        elif direction == "DOWN" and ctx.structure_state in (
                StructureState.BEARISH_STRUCTURE, StructureState.BROKEN_BEARISH,
                StructureState.CHOCH_BEARISH):
            voters.append(f"Structure: {ctx.structure_state.value}")

        # ── Voter 4: CANDLE PRESSURE (last 2 candles net) ──
        if len(candles) >= 2:
            c1, c2 = candles[-2], candles[-1]
            net_pressure = 0.0
            if c2.is_bullish:
                net_pressure += c2.body_ratio
            else:
                net_pressure -= c2.body_ratio
            if c1.is_bullish:
                net_pressure += c1.body_ratio * 0.5
            else:
                net_pressure -= c1.body_ratio * 0.5

            if direction == "UP" and net_pressure > 0.15:
                voters.append(f"Candle Pressure: Bullish ({net_pressure:+.2f})")
            elif direction == "DOWN" and net_pressure < -0.15:
                voters.append(f"Candle Pressure: Bearish ({net_pressure:+.2f})")

        # ── Voter 5: PATTERN / STRONG BREAKOUT ──
        matching_patterns = [p for p in patterns
                            if p.direction == direction and p.strength >= 0.40]
        if matching_patterns:
            best = max(matching_patterns, key=lambda p: p.strength)
            voters.append(f"Pattern: {best.name} ({best.strength:.0%})")
        elif len(candles) >= 1:
            last_c = candles[-1]
            if (direction == "UP" and last_c.is_bullish and last_c.body_ratio > 0.55) or \
               (direction == "DOWN" and last_c.is_bearish and last_c.body_ratio > 0.55):
                voters.append("Pattern: Strong Breakout Candle")

        # ── Voter 6: S/R POSITION / STRUCTURE BREAK ──
        if ctx.price_at_sr:
            if direction == "UP" and ctx.nearest_support is not None:
                voters.append("S/R: At Support")
            elif direction == "DOWN" and ctx.nearest_resistance is not None:
                voters.append("S/R: At Resistance")
        elif direction == "UP" and ctx.structure_state in (
                StructureState.BROKEN_BULLISH, StructureState.CHOCH_BULLISH):
            voters.append("S/R: Bullish Breakout")
        elif direction == "DOWN" and ctx.structure_state in (
                StructureState.BROKEN_BEARISH, StructureState.CHOCH_BEARISH):
            voters.append("S/R: Bearish Breakout")

        # ── Voter 7: IMMEDIATE TREND (last 3 candles) ──
        if direction == "UP" and immediate_trend > 0.15:
            voters.append(f"Immediate: Bullish ({immediate_trend:+.2f})")
        elif direction == "DOWN" and immediate_trend < -0.15:
            voters.append(f"Immediate: Bearish ({immediate_trend:+.2f})")

        # ── Voter 8: CANDLE MOMENTUM ACCELERATION ──
        if len(candles) >= 3:
            last3 = candles[-3:]
            bodies_increasing = all(last3[i].body >= last3[i-1].body * 0.8 for i in range(1, 3))
            same_direction = (all(c.is_bullish for c in last3) if direction == "UP"
                              else all(c.is_bearish for c in last3))
            if bodies_increasing and same_direction:
                voters.append("✓ Momentum acceleration")

        # ── Voter 9: ELDER-RAY DIRECTION (★ most powerful voter ★) ──
        er = ctx.elder_ray_score if ctx.elder_ray_valid else elder_ray_score
        if direction == "UP" and er > 0.10:
            voters.append(f"★ Elder-Ray: Bullish ({er:+.2f})")
        elif direction == "DOWN" and er < -0.10:
            voters.append(f"★ Elder-Ray: Bearish ({er:+.2f})")

        # ── Voter 10: ELDER-RAY ZERO-LINE CROSS (strongest entry signal) ──
        if direction == "UP" and ctx.elder_ray_zero_cross_up:
            voters.append("★★ Elder-Ray: Bears Zero-Cross UP")
        elif direction == "DOWN" and ctx.elder_ray_zero_cross_down:
            voters.append("★★ Elder-Ray: Bulls Zero-Cross DOWN")

        # ── Apply confluence to result ──
        result.confluence_count = len(voters)
        result.confluence_details = voters

        # Add confluence info to entry factors
        result.entry_factors.append(
            f"Confluence: {len(voters)}/10 voters agree")

        return result
