# ============================================================
#  PRICE ACTION ENGINE — Supply/Demand, Order Blocks, Liquidity
# ============================================================

from typing import List, Optional
from core.candle import Candle
from core.market_context import MarketContext


class PriceActionEngine:
    """
    Institutional price action concepts:
    supply/demand zones, order blocks, liquidity grabs,
    smart money reversals, breakout retests.
    """

    def analyse(self, candles: List[Candle], ctx: MarketContext) -> MarketContext:
        if len(candles) < 10:
            return ctx

        ctx.supply_zones = self._find_supply_zones(candles)
        ctx.demand_zones = self._find_demand_zones(candles)
        ctx.order_blocks = self._find_order_blocks(candles)
        return ctx

    def _find_supply_zones(self, candles: List[Candle]) -> list:
        """Supply zone = area where strong selling originated."""
        zones = []
        for i in range(2, len(candles) - 1):
            c = candles[i]
            prev = candles[i-1]
            # Strong bearish candle after bullish = supply zone at the top
            if (c.is_bearish and c.body_ratio > 0.5 and
                prev.is_bullish and c.body > prev.body * 1.2):
                zones.append({
                    'high': prev.high,
                    'low': max(prev.open, prev.close),
                    'strength': c.body_ratio,
                    'index': i - 1
                })
        return zones[-5:]  # Keep last 5

    def _find_demand_zones(self, candles: List[Candle]) -> list:
        """Demand zone = area where strong buying originated."""
        zones = []
        for i in range(2, len(candles) - 1):
            c = candles[i]
            prev = candles[i-1]
            if (c.is_bullish and c.body_ratio > 0.5 and
                prev.is_bearish and c.body > prev.body * 1.2):
                zones.append({
                    'high': min(prev.open, prev.close),
                    'low': prev.low,
                    'strength': c.body_ratio,
                    'index': i - 1
                })
        return zones[-5:]

    def _find_order_blocks(self, candles: List[Candle]) -> list:
        """Order block = last opposing candle before a strong impulse move."""
        blocks = []
        for i in range(2, len(candles) - 1):
            curr = candles[i]
            prev = candles[i-1]
            # Bullish OB: bearish candle followed by strong bullish move
            if (prev.is_bearish and curr.is_bullish and
                curr.body > prev.body * 1.5 and curr.body_ratio > 0.5):
                blocks.append({
                    'type': 'bullish_ob',
                    'high': max(prev.open, prev.close),
                    'low': prev.low,
                    'index': i - 1
                })
            # Bearish OB
            elif (prev.is_bullish and curr.is_bearish and
                  curr.body > prev.body * 1.5 and curr.body_ratio > 0.5):
                blocks.append({
                    'type': 'bearish_ob',
                    'high': prev.high,
                    'low': min(prev.open, prev.close),
                    'index': i - 1
                })
        return blocks[-5:]

    def check_breakout_retest(self, candles: List[Candle], ctx: MarketContext) -> Optional[str]:
        """Check if price is retesting a broken S/R level."""
        if len(candles) < 5 or not ctx.sr_levels:
            return None
        price = candles[-1].close
        prev_price = candles[-2].close
        for sr in ctx.sr_levels:
            dist = abs(price - sr.price)
            rng = candles[-1].total_range * 3
            if dist < rng:
                if prev_price > sr.price and price <= sr.price + rng:
                    return "bullish_retest"
                elif prev_price < sr.price and price >= sr.price - rng:
                    return "bearish_retest"
        return None

    def detect_exhaustion_reversal(self, candles: List[Candle]) -> Optional[str]:
        """Detect exhaustion reversal (long run ending with reversal candle)."""
        if len(candles) < 6:
            return None
        streak = candles[-5:-1]
        last = candles[-1]
        if all(c.is_bullish for c in streak) and last.is_bearish and last.body_ratio > 0.4:
            if last.upper_wick_ratio > 0.3:
                return "bearish_exhaustion"
        if all(c.is_bearish for c in streak) and last.is_bullish and last.body_ratio > 0.4:
            if last.lower_wick_ratio > 0.3:
                return "bullish_exhaustion"
        return None

    def detect_momentum_ignition(self, candles: List[Candle]) -> Optional[str]:
        """Detect momentum ignition candle (sudden large candle after compression)."""
        if len(candles) < 6:
            return None
        compression = candles[-6:-1]
        last = candles[-1]
        avg_range = sum(c.total_range for c in compression) / 5.0
        if last.total_range > avg_range * 2.5 and last.body_ratio > 0.6:
            return "bullish_ignition" if last.is_bullish else "bearish_ignition"
        return None
