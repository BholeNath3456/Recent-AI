# ============================================================
#  TREND ENGINE — EMA-based trend analysis and scoring (v3)
#  Fixed: slope normalization uses price range, added close-over-close
#         trend detection, recent-direction sanity check
# ============================================================

from typing import List, Dict
import sys
sys.path.insert(0, '.')
from core.candle import Candle
from core.market_context import MarketContext, TrendState
from config import ANALYSIS


class TrendEngine:
    """
    Multi-EMA trend analysis engine.
    Computes EMA values, slopes, alignment, crossovers,
    and assigns a weighted trend state.

    v3 Changes:
    - Slope normalization uses price range instead of slow_ema value
      (fixes misleading slopes on pixel-normalized 0-100 scale)
    - Added close-over-close trend detection as a sanity check
    - Recent candle direction check prevents false strong-trend readings
    - Balanced scoring reduces UP bias
    """

    def __init__(self):
        pass

    def analyse(self, candles: List[Candle], ctx: MarketContext) -> MarketContext:
        """Run trend analysis and update MarketContext."""
        if len(candles) < max(ANALYSIS.ema_periods) + 2:
            # Not enough candles for full EMA — use candle-based fallback
            return self._fallback_trend(candles, ctx)

        closes = [c.close for c in candles]

        # Step 1: Calculate EMAs
        ema_values = {}
        ema_slopes = {}
        for period in ANALYSIS.ema_periods:
            ema_series = self._compute_ema(closes, period)
            current_ema = ema_series[-1]
            prev_ema = ema_series[-2] if len(ema_series) > 1 else current_ema

            ema_values[period] = current_ema
            ema_slopes[period] = current_ema - prev_ema

        ctx.ema_values = ema_values
        ctx.ema_slopes = ema_slopes

        # Step 2: EMA alignment
        periods_sorted = sorted(ANALYSIS.ema_periods)
        ema_ordered = [ema_values[p] for p in periods_sorted]

        if all(ema_ordered[i] > ema_ordered[i+1] for i in range(len(ema_ordered)-1)):
            ctx.ema_alignment = "bullish"   # Fast > Medium > Slow
        elif all(ema_ordered[i] < ema_ordered[i+1] for i in range(len(ema_ordered)-1)):
            ctx.ema_alignment = "bearish"   # Fast < Medium < Slow
        else:
            ctx.ema_alignment = "neutral"

        # Step 3: Trend state classification — FIXED
        fast_ema = ema_values[periods_sorted[0]]
        slow_ema = ema_values[periods_sorted[-1]]
        price = candles[-1].close

        # FIXED: Normalize slopes by price RANGE, not EMA value
        # On a 0-100 pixel scale, the visible range varies; using the
        # actual high-low range of recent candles gives meaningful normalization
        price_range = max(c.high for c in candles[-20:]) - min(c.low for c in candles[-20:])
        if price_range < 0.01:
            price_range = 1.0  # avoid division by zero

        # Slope-based scoring (normalized by price range)
        slope_score = 0.0
        for period in periods_sorted:
            normalised_slope = ema_slopes[period] / price_range
            slope_score += normalised_slope

        slope_score /= len(periods_sorted)
        # Scale to make meaningful: slopes of 1-2% of range = significant
        slope_score *= 10.0

        # Price position relative to EMAs
        above_count = sum(1 for p in periods_sorted if price > ema_values[p])
        below_count = sum(1 for p in periods_sorted if price < ema_values[p])

        # Combined trend strength
        alignment_score = 0.0
        if ctx.ema_alignment == "bullish":
            alignment_score = 1.0
        elif ctx.ema_alignment == "bearish":
            alignment_score = -1.0

        position_score = (above_count - below_count) / len(periods_sorted)

        # NEW: Close-over-close trend check
        # This is the most reliable trend indicator — are closes consistently
        # rising or falling? Immune to EMA normalization issues.
        coc_score = self._close_over_close_trend(candles)

        # NEW: Recent candle direction check (last 8 candles)
        recent_dir_score = self._recent_direction_score(candles)

        # Final trend strength: -1 (strong bearish) to +1 (strong bullish)
        # Rebalanced weights: more emphasis on close-over-close and recent direction
        raw_strength = (
            slope_score * 0.15 +          # reduced further (EMA lags reversals)
            alignment_score * 0.15 +      # reduced (lags)
            position_score * 0.10 +       # reduced
            coc_score * 0.25 +            # close-over-close
            recent_dir_score * 0.35       # INCREASED: most responsive to reversals
        )

        ctx.trend_strength = max(-1.0, min(1.0, raw_strength))

        # Classify trend state — lowered thresholds for pixel-based data
        if raw_strength > 0.45:
            ctx.trend_state = TrendState.STRONG_BULLISH
        elif raw_strength > 0.12:
            ctx.trend_state = TrendState.BULLISH
        elif raw_strength < -0.45:
            ctx.trend_state = TrendState.STRONG_BEARISH
        elif raw_strength < -0.12:
            ctx.trend_state = TrendState.BEARISH
        else:
            ctx.trend_state = TrendState.SIDEWAYS

        # Store previous EMAs for crossover detection
        self._prev_emas = dict(ema_values)

        return ctx

    def _fallback_trend(self, candles: List[Candle],
                        ctx: MarketContext) -> MarketContext:
        """
        Fallback trend detection using only candle data (no EMAs).
        Used when there aren't enough candles for full EMA analysis.
        Works with as few as 5 candles.
        """
        if len(candles) < 5:
            ctx.trend_state = TrendState.SIDEWAYS
            ctx.trend_strength = 0.0
            return ctx

        coc = self._close_over_close_trend(candles)
        rds = self._recent_direction_score(candles)

        # Weighted combination: recent direction is most responsive
        raw_strength = coc * 0.40 + rds * 0.60

        ctx.trend_strength = max(-1.0, min(1.0, raw_strength))

        # Classify trend state — same thresholds as full analysis
        if raw_strength > 0.45:
            ctx.trend_state = TrendState.STRONG_BULLISH
        elif raw_strength > 0.12:
            ctx.trend_state = TrendState.BULLISH
        elif raw_strength < -0.45:
            ctx.trend_state = TrendState.STRONG_BEARISH
        elif raw_strength < -0.12:
            ctx.trend_state = TrendState.BEARISH
        else:
            ctx.trend_state = TrendState.SIDEWAYS

        # Set EMA alignment from candle data
        if raw_strength > 0.25:
            ctx.ema_alignment = "bullish"
        elif raw_strength < -0.25:
            ctx.ema_alignment = "bearish"
        else:
            ctx.ema_alignment = "neutral"

        return ctx

    def _close_over_close_trend(self, candles: List[Candle]) -> float:
        """
        Close-over-close trend: are closes consistently rising or falling?
        Returns -1.0 (all declining) to +1.0 (all rising).
        Uses only last 5 candles for faster reversal detection.
        """
        n = min(5, len(candles))  # shortened from 10 for faster response
        if n < 3:
            return 0.0
        recent = candles[-n:]
        rises = 0
        falls = 0
        for i in range(1, len(recent)):
            if recent[i].close > recent[i-1].close:
                rises += 1
            elif recent[i].close < recent[i-1].close:
                falls += 1
        total = rises + falls
        if total == 0:
            return 0.0
        return (rises - falls) / total

    def _recent_direction_score(self, candles: List[Candle]) -> float:
        """
        Count bullish vs bearish candles in last 5 candles.
        Returns -1.0 (all bearish) to +1.0 (all bullish).
        Weighted by body strength, with EXTRA weight on last 2 candles
        to catch reversals faster.
        """
        n = min(5, len(candles))  # shortened from 8 for faster response
        if n < 3:
            return 0.0
        recent = candles[-n:]
        bull_weight = 0.0
        bear_weight = 0.0
        for i, c in enumerate(recent):
            # Last 2 candles get 2x weight for reversal sensitivity
            w = 2.0 if i >= n - 2 else 1.0
            if c.is_bullish:
                bull_weight += c.body_ratio * w
            elif c.is_bearish:
                bear_weight += c.body_ratio * w
        total = bull_weight + bear_weight
        if total < 0.01:
            return 0.0
        return (bull_weight - bear_weight) / total

    def get_trend_age_penalty(self, candles: List[Candle], ctx: MarketContext) -> float:
        """
        Measure how "stale" / aged the current trend move is.
        Returns 0.0 (fresh trend) to 1.0 (overaged, likely to reverse).

        This catches the scenario where the engine sees a strong trend that's
        been running for many candles and gives a continuation signal — which
        is actually chasing a move that's about to exhaust.
        """
        if len(candles) < 8:
            return 0.0

        # Count consecutive candles in the trend direction
        trend_dir = None
        if ctx.trend_state in (TrendState.BULLISH, TrendState.STRONG_BULLISH):
            trend_dir = "bull"
        elif ctx.trend_state in (TrendState.BEARISH, TrendState.STRONG_BEARISH):
            trend_dir = "bear"

        if trend_dir is None:
            return 0.0

        # Count how many of the last 10 candles agree with trend
        lookback = min(10, len(candles))
        recent = candles[-lookback:]
        agree_count = 0
        for c in recent:
            if (trend_dir == "bull" and c.is_bullish) or (trend_dir == "bear" and c.is_bearish):
                agree_count += 1

        # Also measure total displacement vs ATR
        atr = sum(c.total_range for c in candles[-min(14, len(candles)):]) / min(14, len(candles))
        if atr < 0.0001:
            return 0.0

        total_displacement = abs(candles[-1].close - candles[-lookback].close) / atr

        # Penalty based on age and displacement
        # High agreement (7+/10 candles) + large displacement (2+ ATR) = stale trend
        age_score = min(1.0, max(0.0, (agree_count - 4)) / 5.0)  # 0 at 4, 1.0 at 9
        disp_score = min(1.0, total_displacement / 3.0)  # 0 at 0 ATR, 1.0 at 3+ ATR

        penalty = age_score * 0.5 + disp_score * 0.5
        return min(1.0, penalty)

    def get_immediate_trend(self, candles: List[Candle]) -> float:
        """
        Ultra-fast trend signal from the last 3 candles only.
        Returns -1.0 (strong bearish) to +1.0 (strong bullish).
        Weighted by body size — a single large candle dominates.
        This catches sudden reversals before EMAs react.
        """
        if len(candles) < 2:
            return 0.0
        n = min(3, len(candles))
        recent = candles[-n:]
        bull_weight = 0.0
        bear_weight = 0.0
        for i, c in enumerate(recent):
            # Last candle gets 3x weight
            w = 3.0 if i == n - 1 else 1.0
            size_factor = c.body_ratio
            if c.is_bullish:
                bull_weight += size_factor * w
            elif c.is_bearish:
                bear_weight += size_factor * w
        total = bull_weight + bear_weight
        if total < 0.001:
            return 0.0
        return (bull_weight - bear_weight) / total

    def get_pullback_quality(self, candles: List[Candle], ctx: MarketContext) -> float:
        """
        Assess the quality of a trend pullback.
        Returns 0-1: 1.0 = clean pullback to EMA, 0.0 = no pullback or too deep.
        """
        if not ctx.ema_values or len(candles) < 5:
            return 0.0

        price = candles[-1].close
        fast_ema = ctx.ema_values.get(ANALYSIS.ema_periods[0], price)

        # Distance from fast EMA
        distance = abs(price - fast_ema) / max(abs(fast_ema), 0.01)

        # Good pullback = price touched EMA (small distance)
        if distance < 0.005:
            quality = 1.0
        elif distance < 0.02:
            quality = 0.7
        elif distance < 0.05:
            quality = 0.3
        else:
            quality = 0.0

        # Check that pullback didn't break structure
        if ctx.trend_state in (TrendState.BULLISH, TrendState.STRONG_BULLISH):
            # In uptrend, price should still be above slow EMA
            if ANALYSIS.ema_periods[-1] in ctx.ema_values:
                slow_ema = ctx.ema_values[ANALYSIS.ema_periods[-1]]
                if price < slow_ema:
                    quality *= 0.3  # Pullback too deep

        elif ctx.trend_state in (TrendState.BEARISH, TrendState.STRONG_BEARISH):
            if ANALYSIS.ema_periods[-1] in ctx.ema_values:
                slow_ema = ctx.ema_values[ANALYSIS.ema_periods[-1]]
                if price > slow_ema:
                    quality *= 0.3

        return quality

    def _compute_ema(self, data: List[float], period: int) -> List[float]:
        """Compute Exponential Moving Average."""
        if len(data) < period:
            return data[:]

        k = 2.0 / (period + 1)
        ema_values = [sum(data[:period]) / period]  # SMA seed

        for i in range(period, len(data)):
            ema_values.append(data[i] * k + ema_values[-1] * (1 - k))

        return ema_values
