# ============================================================
#  VOLATILITY ENGINE — ATR, compression, noise filtering (v2)
#  Fixed: relative thresholds, choppiness detection
# ============================================================

from typing import List
import sys
sys.path.insert(0, '.')
from core.candle import Candle
from core.market_context import MarketContext, VolatilityRegime, MarketRegime
from config import ANALYSIS


class VolatilityEngine:
    """
    Volatility analysis: ATR, compression/expansion detection,
    choppiness classification, signal blocking conditions.

    v2 Changes:
    - should_block_signal() uses relative ATR threshold instead of absolute 0.1
    - Choppiness detection: direction changes OR low body (was AND — too strict)
    - Better regime classification
    """

    def __init__(self):
        self._atr_history: List[float] = []

    def reset(self):
        self._atr_history.clear()

    def analyse(self, candles: List[Candle], ctx: MarketContext) -> MarketContext:
        if len(candles) < ANALYSIS.volatility_lookback + 1:
            return ctx

        # ATR calculation
        atr = self._compute_atr(candles, ANALYSIS.atr_period)
        ctx.atr_value = atr

        # ATR ratio vs historical average
        self._atr_history.append(atr)
        if len(self._atr_history) > 50:
            self._atr_history.pop(0)
        avg_atr = sum(self._atr_history) / len(self._atr_history)
        ctx.atr_ratio = atr / max(avg_atr, 0.0001)

        # Volatility regime classification
        if ctx.atr_ratio < ANALYSIS.compression_threshold:
            ctx.volatility_regime = VolatilityRegime.COLLAPSED
            ctx.is_compressed = True
        elif ctx.atr_ratio < 0.7:
            ctx.volatility_regime = VolatilityRegime.COMPRESSING
            ctx.is_compressed = True
        elif ctx.atr_ratio > 1.5:
            ctx.volatility_regime = VolatilityRegime.EXPANDING
            ctx.is_compressed = False
        else:
            ctx.volatility_regime = VolatilityRegime.NORMAL
            ctx.is_compressed = False

        # Choppiness detection — FIXED: OR instead of AND
        ctx.is_choppy = self._detect_choppiness(candles)

        # Market regime
        ctx.market_regime = self._classify_regime(ctx)

        return ctx

    def should_block_signal(self, ctx: MarketContext) -> tuple:
        """Returns (should_block: bool, reasons: list)."""
        reasons = []
        if ctx.volatility_regime == VolatilityRegime.COLLAPSED:
            reasons.append("Volatility collapsed")
        if ctx.is_choppy:
            reasons.append("Market choppy")
        # FIXED: use relative threshold based on ATR history, not absolute 0.1
        # On a 0-100 pixel scale, ATR of 0.1 is unrealistic; use ratio instead
        if ctx.atr_ratio < 0.25:
            reasons.append("Candles too small (low ATR ratio)")
        return (len(reasons) > 0, reasons)

    def _compute_atr(self, candles: List[Candle], period: int) -> float:
        if len(candles) < period + 1:
            return sum(c.total_range for c in candles) / len(candles)
        trs = []
        for i in range(1, len(candles)):
            tr = max(
                candles[i].total_range,
                abs(candles[i].high - candles[i-1].close),
                abs(candles[i].low - candles[i-1].close)
            )
            trs.append(tr)
        if len(trs) < period:
            return sum(trs) / len(trs)
        atr = sum(trs[:period]) / period
        for i in range(period, len(trs)):
            atr = (atr * (period - 1) + trs[i]) / period
        return atr

    def _detect_choppiness(self, candles: List[Candle]) -> bool:
        """
        Detect choppy/ranging market.
        v2: uses OR logic — either many direction changes OR very weak bodies.
        Was AND logic (required both), which was too strict.
        """
        if len(candles) < 8:
            return False
        recent = candles[-8:]
        directions = [c.is_bullish for c in recent]
        changes = sum(1 for i in range(1, len(directions)) if directions[i] != directions[i-1])
        avg_body = sum(c.body_ratio for c in recent) / len(recent)

        # High alternation (direction change on most candles)
        high_alternation = changes >= 5

        # Very weak bodies (doji-like candles)
        very_weak = avg_body < 0.20

        # Either condition alone can indicate chop
        if high_alternation and very_weak:
            return True  # strong chop signal
        if changes >= 6:
            return True  # extreme alternation alone
        if very_weak and changes >= 4:
            return True  # weak bodies + moderate alternation

        return False

    def _classify_regime(self, ctx: MarketContext) -> MarketRegime:
        is_trending = ctx.trend_strength and abs(ctx.trend_strength) > 0.3
        is_volatile = ctx.volatility_regime == VolatilityRegime.EXPANDING

        if is_trending and not is_volatile:
            return MarketRegime.TRENDING
        elif is_volatile and is_trending:
            return MarketRegime.VOLATILE
        elif ctx.is_choppy or ctx.is_compressed:
            return MarketRegime.QUIET
        elif not is_trending:
            return MarketRegime.RANGING
        return MarketRegime.TRANSITIONAL
