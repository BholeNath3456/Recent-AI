# ============================================================
#  LIQUIDITY ENGINE — Sweep detection, stop hunts, fake breakouts
# ============================================================

from typing import List, Optional
from core.candle import Candle
from core.market_context import MarketContext, LiquidityZone


class LiquidityEngine:
    """
    Detects liquidity pools, stop hunt patterns, and fake breakouts.
    """

    def analyse(self, candles: List[Candle], ctx: MarketContext) -> MarketContext:
        if len(candles) < 10:
            return ctx

        ctx.liquidity_zones = self._find_liquidity_zones(candles, ctx)
        sweep = self._detect_sweep(candles, ctx)
        if sweep:
            ctx.liquidity_sweep_detected = True
            ctx.sweep_direction = sweep

        return ctx

    def _find_liquidity_zones(self, candles: List[Candle],
                               ctx: MarketContext) -> List[LiquidityZone]:
        """Identify areas where stops are likely clustered."""
        zones = []
        # Stops cluster just beyond swing highs and lows
        for sp in ctx.swing_points:
            margin = candles[-1].total_range * 0.5
            if sp.is_high:
                zones.append(LiquidityZone(
                    sp.price, sp.price + margin, 'above', sp.strength
                ))
            else:
                zones.append(LiquidityZone(
                    sp.price - margin, sp.price, 'below', sp.strength
                ))
        return zones[-8:]

    def _detect_sweep(self, candles: List[Candle],
                      ctx: MarketContext) -> Optional[str]:
        """Detect if the most recent candle swept a liquidity zone."""
        if not ctx.liquidity_zones:
            return None
        last = candles[-1]
        prev = candles[-2] if len(candles) > 1 else last

        for zone in ctx.liquidity_zones:
            # Sweep above (took out highs) then reversed down
            if (zone.side == 'above' and
                last.high >= zone.price_low and
                last.close < zone.price_low and
                last.is_bearish):
                return "bearish"
            # Sweep below then reversed up
            if (zone.side == 'below' and
                last.low <= zone.price_high and
                last.close > zone.price_high and
                last.is_bullish):
                return "bullish"
        return None

    def get_fake_breakout_probability(self, candles: List[Candle],
                                       ctx: MarketContext) -> float:
        """Estimate probability that the current move is a fake breakout."""
        if len(candles) < 8:
            return 0.0
        last = candles[-1]
        prob = 0.0

        # Factor 1: Wick rejection after range break
        recent_high = max(c.high for c in candles[-8:-1])
        recent_low = min(c.low for c in candles[-8:-1])

        if last.high > recent_high and last.upper_wick_ratio > 0.4:
            prob += 0.4
        if last.low < recent_low and last.lower_wick_ratio > 0.4:
            prob += 0.4

        # Factor 2: Close back inside range
        if last.high > recent_high and last.close < recent_high:
            prob += 0.3
        if last.low < recent_low and last.close > recent_low:
            prob += 0.3

        # Factor 3: Low volume (small body)
        if last.body_ratio < 0.2:
            prob += 0.2

        return min(1.0, prob)
