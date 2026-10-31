# ============================================================
#  MTF ENGINE — Multi-Timeframe analysis via candle aggregation
# ============================================================

from typing import List
import sys
sys.path.insert(0, '.')
from core.candle import Candle
from core.market_context import MarketContext, TrendState


class MTFEngine:
    """
    Simulates multi-timeframe analysis by aggregating candles.
    E.g. 5x 1m candles → 1x 5m candle.
    Checks higher-TF trend alignment and detects conflicts.
    """

    def analyse(self, candles: List[Candle], ctx: MarketContext) -> MarketContext:
        if len(candles) < 15:
            return ctx

        # Build higher-timeframe candles (5x aggregation)
        htf_candles = self._aggregate(candles, 5)
        if len(htf_candles) < 3:
            return ctx

        # Determine HTF trend
        ctx.htf_trend = self._quick_trend(htf_candles)

        # Check alignment
        ltf_bullish = ctx.trend_state in (TrendState.BULLISH, TrendState.STRONG_BULLISH)
        ltf_bearish = ctx.trend_state in (TrendState.BEARISH, TrendState.STRONG_BEARISH)
        htf_bullish = ctx.htf_trend in (TrendState.BULLISH, TrendState.STRONG_BULLISH)
        htf_bearish = ctx.htf_trend in (TrendState.BEARISH, TrendState.STRONG_BEARISH)

        ctx.mtf_aligned = (ltf_bullish and htf_bullish) or (ltf_bearish and htf_bearish)
        ctx.mtf_conflict = (ltf_bullish and htf_bearish) or (ltf_bearish and htf_bullish)

        # Reversal override: if last 3 candles show a strong shift,
        # the reversal IS the new direction — suppress MTF conflict
        if ctx.mtf_conflict and len(candles) >= 3:
            last3 = candles[-3:]
            bull_force = sum(c.body_ratio for c in last3 if c.is_bullish)
            bear_force = sum(c.body_ratio for c in last3 if c.is_bearish)
            # Strong recent reversal overrides old HTF
            if bull_force > 1.5 and ltf_bullish:
                ctx.mtf_conflict = False  # bullish reversal overrides
            elif bear_force > 1.5 and ltf_bearish:
                ctx.mtf_conflict = False  # bearish reversal overrides

        return ctx

    def _aggregate(self, candles: List[Candle], factor: int) -> List[Candle]:
        """Aggregate candles by factor (e.g. 5 → one higher-TF candle)."""
        result = []
        for i in range(0, len(candles) - factor + 1, factor):
            group = candles[i:i+factor]
            o = group[0].open
            c = group[-1].close
            h = max(g.high for g in group)
            l = min(g.low for g in group)
            result.append(Candle(o, c, h, l))
        return result

    def _quick_trend(self, candles: List[Candle]) -> TrendState:
        """Quick trend classification from a candle series."""
        if len(candles) < 3:
            return TrendState.SIDEWAYS
        bull = sum(1 for c in candles[-5:] if c.is_bullish)
        bear = sum(1 for c in candles[-5:] if c.is_bearish)
        avg_body = sum(c.body_ratio for c in candles[-3:]) / 3

        if bull >= 4 and avg_body > 0.4:
            return TrendState.STRONG_BULLISH
        elif bull >= 3:
            return TrendState.BULLISH
        elif bear >= 4 and avg_body > 0.4:
            return TrendState.STRONG_BEARISH
        elif bear >= 3:
            return TrendState.BEARISH
        return TrendState.SIDEWAYS
