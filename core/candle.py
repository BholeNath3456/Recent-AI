# ============================================================
#  CANDLE — Enhanced candle data class with advanced analytics
# ============================================================

import math


class Candle:
    """
    Rich candle representation with derived analytics.
    All prices are normalised to a 0-100 pixel-based scale
    extracted from the Olymp Trade chart.
    """

    __slots__ = ('open', 'close', 'high', 'low')

    def __init__(self, open_: float, close: float, high: float, low: float):
        self.open  = open_
        self.close = close
        self.high  = high
        self.low   = low

    # ── Basic metrics ────────────────────────────

    @property
    def body(self) -> float:
        return abs(self.close - self.open)

    @property
    def upper_wick(self) -> float:
        return self.high - max(self.open, self.close)

    @property
    def lower_wick(self) -> float:
        return min(self.open, self.close) - self.low

    @property
    def total_range(self) -> float:
        return max(self.high - self.low, 0.0001)

    @property
    def midpoint(self) -> float:
        return (self.high + self.low) / 2.0

    @property
    def body_midpoint(self) -> float:
        return (self.open + self.close) / 2.0

    # ── Ratios ───────────────────────────────────

    @property
    def body_ratio(self) -> float:
        """Body size relative to total range. 1.0 = marubozu, 0.0 = doji."""
        return self.body / self.total_range

    @property
    def upper_wick_ratio(self) -> float:
        return self.upper_wick / self.total_range

    @property
    def lower_wick_ratio(self) -> float:
        return self.lower_wick / self.total_range

    @property
    def wick_ratio(self) -> float:
        """Total wick as fraction of range. High = indecision."""
        return (self.upper_wick + self.lower_wick) / self.total_range

    # ── Directional properties ───────────────────

    @property
    def is_bullish(self) -> bool:
        return self.close > self.open

    @property
    def is_bearish(self) -> bool:
        return self.close < self.open

    @property
    def is_doji(self) -> bool:
        return self.body_ratio < 0.10

    @property
    def is_marubozu(self) -> bool:
        """Strong directional candle with minimal wicks."""
        return self.body_ratio > 0.80

    @property
    def is_hammer(self) -> bool:
        """Long lower wick, small body near top."""
        return (self.lower_wick_ratio > 0.55 and
                self.body_ratio < 0.30 and
                self.upper_wick_ratio < 0.15)

    @property
    def is_shooting_star(self) -> bool:
        """Long upper wick, small body near bottom."""
        return (self.upper_wick_ratio > 0.55 and
                self.body_ratio < 0.30 and
                self.lower_wick_ratio < 0.15)

    # ── Advanced analytics ───────────────────────

    @property
    def body_strength(self) -> float:
        """
        0.0 = pure wick (no conviction)
        1.0 = pure body (maximum conviction)
        """
        return self.body_ratio

    @property
    def wick_rejection_pressure(self) -> float:
        """
        Directional wick pressure: positive = buying pressure (lower wick dominant),
        negative = selling pressure (upper wick dominant).
        Range: -1.0 to 1.0
        """
        total_wick = self.upper_wick + self.lower_wick
        if total_wick < 0.0001:
            return 0.0
        return (self.lower_wick - self.upper_wick) / total_wick

    @property
    def buyer_dominance(self) -> float:
        """
        Estimate of buyer control: 0.0 = sellers dominate, 1.0 = buyers dominate.
        Considers body direction, wick rejection, and body strength.
        """
        score = 0.5  # neutral
        if self.is_bullish:
            score += 0.25 * self.body_ratio
        else:
            score -= 0.25 * self.body_ratio
        # Lower wick = buying pressure
        score += 0.25 * (self.lower_wick_ratio - self.upper_wick_ratio)
        return max(0.0, min(1.0, score))

    @property
    def seller_dominance(self) -> float:
        return 1.0 - self.buyer_dominance

    @property
    def delta_pressure(self) -> float:
        """
        Estimated order flow delta: positive = net buying, negative = net selling.
        Range approximately -1.0 to 1.0
        """
        direction = 1.0 if self.is_bullish else (-1.0 if self.is_bearish else 0.0)
        body_component = direction * self.body_ratio * 0.6
        wick_component = self.wick_rejection_pressure * 0.4
        return body_component + wick_component

    @property
    def reversal_probability(self) -> float:
        """
        Probability this candle represents a reversal signal.
        Based on wick rejection, body weakness, and wick dominance.
        """
        wick_signal = max(self.upper_wick_ratio, self.lower_wick_ratio)
        body_weakness = 1.0 - self.body_ratio
        return min(1.0, wick_signal * 0.6 + body_weakness * 0.4)

    @property
    def continuation_probability(self) -> float:
        """Probability this candle supports continuation of current move."""
        return min(1.0, self.body_ratio * 0.7 + (1.0 - self.wick_ratio) * 0.3)

    @property
    def candle_imbalance(self) -> float:
        """
        Asymmetry between upper and lower portions.
        Positive = bullish imbalance, negative = bearish imbalance.
        """
        upper_portion = self.upper_wick + (self.body / 2 if self.is_bearish else 0)
        lower_portion = self.lower_wick + (self.body / 2 if self.is_bullish else 0)
        total = upper_portion + lower_portion
        if total < 0.0001:
            return 0.0
        return (lower_portion - upper_portion) / total

    def momentum_vs(self, other: 'Candle') -> float:
        """
        Momentum acceleration relative to another candle.
        > 1.0 means expanding, < 1.0 means contracting.
        """
        if other.body < 0.0001:
            return 2.0 if self.body > 0.0001 else 1.0
        return self.body / other.body

    def engulfs(self, other: 'Candle') -> bool:
        """Does this candle's body fully engulf the other's body?"""
        self_top  = max(self.open, self.close)
        self_bot  = min(self.open, self.close)
        other_top = max(other.open, other.close)
        other_bot = min(other.open, other.close)
        return self_top >= other_top and self_bot <= other_bot

    def __repr__(self):
        d = "▲" if self.is_bullish else "▼"
        return f"Candle({d} O={self.open:.1f} C={self.close:.1f} H={self.high:.1f} L={self.low:.1f} body={self.body_ratio:.0%})"
