# ============================================================
#  MARKET BEHAVIOR CLASSIFIER — Adaptive regime detection v2
#  Fixed: spike_retrace no longer misidentifies strong trends.
#  A "spike" must be large AND the retrace must be significant.
# ============================================================

from typing import List
from dataclasses import dataclass
from core.candle import Candle


@dataclass
class MarketBehavior:
    """Current market behavior classification."""
    regime: str  # 'trending', 'ranging', 'choppy', 'spike_retrace', 'momentum_burst', 'dead'
    confidence: float  # 0.0 to 1.0 — how confident are we in this classification
    candle_conviction: float  # 0.0 to 1.0 — are candles showing real directional conviction?
    fake_move_probability: float  # 0.0 to 1.0 — how likely the current move is a fake
    volatility_regime: str  # 'low', 'normal', 'high', 'extreme'
    dominant_pressure: float  # -1.0 (bearish) to +1.0 (bullish)
    consistency_score: float  # 0.0 to 1.0 — are candles behaving consistently?
    signal_reliability: float  # 0.0 to 1.0 — how reliable would a signal be right now?


class BehaviorClassifier:
    """
    Classifies current market behavior by analyzing raw candle data.
    Does NOT use indicators — only raw price action observation.
    """

    def classify(self, candles: List[Candle]) -> MarketBehavior:
        """Analyze last 10-20 candles to classify market behavior."""
        result = MarketBehavior(
            regime='dead',
            confidence=0.0,
            candle_conviction=0.0,
            fake_move_probability=0.5,
            volatility_regime='low',
            dominant_pressure=0.0,
            consistency_score=0.0,
            signal_reliability=0.0
        )

        if len(candles) < 5:
            return result

        n = min(20, len(candles))
        recent = candles[-n:]

        # ── 1. Candle Conviction Score ──
        # Are candles showing REAL directional conviction?
        # Big bodies = conviction. Long wicks = indecision.
        total_body = 0.0
        total_range = 0.0
        for c in recent:
            total_body += c.body
            total_range += c.high - c.low if c.high > c.low else 0.001
        avg_body_ratio = total_body / max(total_range, 0.001)
        result.candle_conviction = min(1.0, avg_body_ratio * 1.2)

        # ── 2. Direction Consistency ──
        # How consistently are candles moving in one direction?
        bull_count = sum(1 for c in recent if c.is_bullish)
        bear_count = sum(1 for c in recent if c.is_bearish)
        total = bull_count + bear_count
        if total > 0:
            dominant_ratio = max(bull_count, bear_count) / total
            result.consistency_score = (dominant_ratio - 0.5) * 2.0  # 0 when 50/50, 1.0 when 100%
            result.consistency_score = max(0.0, min(1.0, result.consistency_score))
        else:
            result.consistency_score = 0.0

        # ── 3. Dominant Pressure ──
        # Body-weighted directional pressure
        bull_force = sum(c.body * c.body_ratio for c in recent if c.is_bullish)
        bear_force = sum(c.body * c.body_ratio for c in recent if c.is_bearish)
        total_force = bull_force + bear_force
        if total_force > 0.001:
            result.dominant_pressure = (bull_force - bear_force) / total_force
        else:
            result.dominant_pressure = 0.0

        # ── 4. Volatility Regime ──
        ranges = [c.high - c.low for c in recent if c.high > c.low]
        if len(ranges) >= 3:
            avg_range = sum(ranges) / len(ranges)
            recent_range = sum(ranges[-3:]) / 3
            ratio = recent_range / max(avg_range, 0.0001)
            if ratio > 2.0:
                result.volatility_regime = 'extreme'
            elif ratio > 1.3:
                result.volatility_regime = 'high'
            elif ratio < 0.5:
                result.volatility_regime = 'low'
            else:
                result.volatility_regime = 'normal'

        # ── 5. FIXED Spike-and-Retrace Detection ──
        # OLD BUG: counted ANY direction flip as spike_retrace.
        # NEW FIX: Only count a genuine spike if:
        #   - The initial candle is LARGE (body_ratio > 0.65)
        #   - The retrace candle engulfs > 50% of the spike body
        # This prevents misidentifying strong trends as spike_retrace.
        avg_body = sum(c.body for c in recent) / max(len(recent), 1)
        spike_retrace_count = 0
        for i in range(1, len(recent)):
            prev = recent[i - 1]
            curr = recent[i]
            # Must be a LARGE spike (not just any candle flip)
            if prev.body_ratio > 0.65 and prev.body > avg_body * 1.5:
                if prev.is_bullish and curr.is_bearish:
                    # Retrace must recover > 50% of the spike
                    if curr.body > prev.body * 0.50:
                        spike_retrace_count += 1
                elif prev.is_bearish and curr.is_bullish:
                    if curr.body > prev.body * 0.50:
                        spike_retrace_count += 1

        # ── 6. Fake Move Detection ──
        # Multiple small candles in one direction often reverse
        last5 = recent[-min(5, len(recent)):]
        if len(last5) >= 3:
            avg_body_last5 = sum(c.body for c in last5) / len(last5)
            avg_range_last5 = sum(c.high - c.low for c in last5) / len(last5)
            small_ratio = avg_body_last5 / max(avg_range_last5, 0.001)

            if small_ratio < 0.4:  # Small bodies relative to range = indecision
                dir_count = sum(1 for c in last5 if c.is_bullish)
                if dir_count >= 4 or dir_count <= 1:  # All same direction but weak
                    result.fake_move_probability = 0.7
                else:
                    result.fake_move_probability = 0.3
            else:
                result.fake_move_probability = max(0.1, 0.5 - result.candle_conviction * 0.4)

        # ── 7. Regime Classification ──
        # Priority order: trending > momentum_burst > spike_retrace > choppy > ranging > dead
        # IMPORTANT: trending must be checked BEFORE spike_retrace to avoid misclassification
        if result.consistency_score > 0.55 and result.candle_conviction > 0.35:
            # Strong consistent directional movement = TRENDING (highest priority)
            result.regime = 'trending'
            result.confidence = result.consistency_score * result.candle_conviction
        elif result.volatility_regime in ('high', 'extreme') and result.consistency_score > 0.4:
            result.regime = 'momentum_burst'
            result.confidence = 0.5 + result.consistency_score * 0.3
        elif spike_retrace_count >= 2:
            # Only classify as spike_retrace if NOT consistently trending
            result.regime = 'spike_retrace'
            result.confidence = min(1.0, spike_retrace_count / 4)
        elif result.consistency_score < 0.25 and result.candle_conviction < 0.30:
            result.regime = 'choppy'
            result.confidence = 0.6
        elif result.volatility_regime == 'low' and result.consistency_score < 0.15:
            result.regime = 'dead'
            result.confidence = 0.7
        else:
            result.regime = 'ranging'
            result.confidence = 0.5

        # ── 8. Signal Reliability ──
        # How reliable would a signal be in this regime?
        reliability_map = {
            'trending': 0.80,
            'momentum_burst': 0.65,
            'ranging': 0.35,
            'choppy': 0.15,
            'spike_retrace': 0.20,
            'dead': 0.05,
        }
        base_reliability = reliability_map.get(result.regime, 0.35)

        # Adjust by conviction and consistency
        result.signal_reliability = base_reliability * (
            0.5 + result.candle_conviction * 0.3 + result.consistency_score * 0.2
        )

        # Penalize high fake move probability
        if result.fake_move_probability > 0.5:
            result.signal_reliability *= 0.7

        result.signal_reliability = min(1.0, result.signal_reliability)

        return result
