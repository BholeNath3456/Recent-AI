# ============================================================
#  MARKET STRUCTURE ENGINE — HH/HL/LH/LL, BOS, CHOCH, Swings
#  Fixed: persistent state, soft classification, BOS tracking
# ============================================================

from typing import List, Optional
import sys
sys.path.insert(0, '.')
from core.candle import Candle
from core.market_context import (
    MarketContext, StructureState, SwingPoint, SupportResistance
)
from config import ANALYSIS


class MarketStructureEngine:
    """
    Analyses price structure to determine:
    - Swing highs and lows
    - Higher-High / Higher-Low / Lower-High / Lower-Low sequences
    - Break of Structure (BOS) events
    - Change of Character (CHOCH) events
    - Support/resistance clustering

    v2 Changes:
    - Persistent structure state between scans (was resetting each time)
    - Soft classification for expanding/contracting (was all UNCLEAR)
    - Reduced swing lookback requirement when fewer candles available
    - Better BOS/CHOCH detection with directional tracking
    """

    def __init__(self):
        self._prev_structure: StructureState = StructureState.UNCLEAR
        self._swing_history: List[SwingPoint] = []
        self._structure_streak: int = 0  # how many scans with same structure

    def analyse(self, candles: List[Candle], ctx: MarketContext) -> MarketContext:
        """Run structure analysis and update MarketContext."""
        n = len(candles)
        # Adaptive lookback: use smaller lookback for fewer candles
        lb = min(ANALYSIS.swing_lookback, max(2, n // 5))

        if n < lb * 2 + 1:
            # Not enough candles — carry forward previous structure
            ctx.structure_state = self._prev_structure
            return ctx

        # Step 1: Detect swing points
        swings = self._detect_swing_points(candles, lb)
        ctx.swing_points = swings
        self._swing_history = swings

        # Step 2: Classify structure (HH/HL/LH/LL) — improved
        ctx.structure_state = self._classify_structure(swings, candles)

        # Step 3: Detect BOS / CHOCH
        self._detect_bos_choch(swings, ctx)

        # Step 4: Build support/resistance levels
        ctx.sr_levels = self._cluster_sr_levels(swings, candles)

        # Step 5: Find nearest S/R
        if candles and ctx.sr_levels:
            price = candles[-1].close
            supports = [s for s in ctx.sr_levels if s.is_support and s.price < price]
            resistances = [s for s in ctx.sr_levels if not s.is_support and s.price > price]
            ctx.nearest_support = max((s.price for s in supports), default=0.0)
            ctx.nearest_resistance = min((s.price for s in resistances), default=100.0)

            # Check if price is near S/R (within 8% of range)
            price_range = ctx.nearest_resistance - ctx.nearest_support
            if price_range > 0:
                dist_to_support = abs(price - ctx.nearest_support) / price_range
                dist_to_resistance = abs(price - ctx.nearest_resistance) / price_range
                ctx.price_at_sr = dist_to_support < 0.08 or dist_to_resistance < 0.08

        # Track structure persistence
        if ctx.structure_state == self._prev_structure:
            self._structure_streak += 1
        else:
            self._structure_streak = 0
        self._prev_structure = ctx.structure_state

        return ctx

    def _detect_swing_points(self, candles: List[Candle],
                              lb: int) -> List[SwingPoint]:
        """Detect confirmed swing highs and lows using lookback window."""
        swings: List[SwingPoint] = []
        n = len(candles)

        for i in range(lb, n - lb):
            # Swing High: higher than lb bars on each side
            is_swing_high = True
            for j in range(1, lb + 1):
                if i - j < 0 or i + j >= n:
                    is_swing_high = False
                    break
                if candles[i].high < candles[i - j].high or candles[i].high < candles[i + j].high:
                    is_swing_high = False
                    break

            if is_swing_high:
                avg_neighbour = sum(
                    candles[i + d].high for d in range(-lb, lb + 1) if d != 0
                ) / (2 * lb)
                strength = min(2.0, (candles[i].high - avg_neighbour) /
                               max(candles[i].total_range, 0.01))
                swings.append(SwingPoint(i, candles[i].high, True, max(0.1, abs(strength))))

            # Swing Low: lower than lb bars on each side
            is_swing_low = True
            for j in range(1, lb + 1):
                if i - j < 0 or i + j >= n:
                    is_swing_low = False
                    break
                if candles[i].low > candles[i - j].low or candles[i].low > candles[i + j].low:
                    is_swing_low = False
                    break

            if is_swing_low:
                avg_neighbour = sum(
                    candles[i + d].low for d in range(-lb, lb + 1) if d != 0
                ) / (2 * lb)
                strength = min(2.0, (avg_neighbour - candles[i].low) /
                               max(candles[i].total_range, 0.01))
                swings.append(SwingPoint(i, candles[i].low, False, max(0.1, abs(strength))))

        # Check last lb candles with forward-only (left-side only) confirmation
        for i in range(max(lb, n - lb), n):
            is_high = all(candles[i].high > candles[i-j].high for j in range(1, min(lb, i) + 1))
            is_low = all(candles[i].low < candles[i-j].low for j in range(1, min(lb, i) + 1))
            if is_high:
                strength = min(2.0, max(0.1, (candles[i].high - sum(candles[i-j].high for j in range(1, min(lb, i)+1)) / max(1, min(lb, i))) / max(candles[i].total_range, 0.01)))
                swings.append(SwingPoint(index=i, price=candles[i].high, is_high=True, strength=strength * 0.7))
            if is_low:
                strength = min(2.0, max(0.1, (sum(candles[i-j].low for j in range(1, min(lb, i)+1)) / max(1, min(lb, i)) - candles[i].low) / max(candles[i].total_range, 0.01)))
                swings.append(SwingPoint(index=i, price=candles[i].low, is_high=False, strength=strength * 0.7))

        swings.sort(key=lambda s: s.index)
        return swings

    def _classify_structure(self, swings: List[SwingPoint],
                            candles: List[Candle]) -> StructureState:
        """
        Classify market structure based on swing sequence.
        v2: Falls back to price-action analysis when not enough swings.
        """
        highs = [s for s in swings if s.is_high]
        lows = [s for s in swings if not s.is_high]

        # If we have enough swings, use classic HH/HL/LH/LL analysis
        if len(highs) >= 2 and len(lows) >= 2:
            h1, h2 = highs[-2], highs[-1]
            l1, l2 = lows[-2], lows[-1]

            hh = h2.price > h1.price  # Higher High
            hl = l2.price > l1.price  # Higher Low
            lh = h2.price < h1.price  # Lower High
            ll = l2.price < l1.price  # Lower Low

            if hh and hl:
                return StructureState.BULLISH_STRUCTURE
            elif lh and ll:
                return StructureState.BEARISH_STRUCTURE
            # NEW: soft classification for expanding/contracting
            elif hh and ll:
                # Expanding formation — lean toward the dominant side
                if h2.price - h1.price > l1.price - l2.price:
                    return StructureState.BULLISH_STRUCTURE  # more HH than LL
                else:
                    return StructureState.BEARISH_STRUCTURE
            elif lh and hl:
                # Contracting / triangle — use recent candle direction
                recent_bull = sum(1 for c in candles[-5:] if c.is_bullish)
                if recent_bull >= 3:
                    return StructureState.BULLISH_STRUCTURE
                elif recent_bull <= 2:
                    return StructureState.BEARISH_STRUCTURE

        # Fallback: use simple price action when no clear swings
        if len(candles) >= 8:
            recent = candles[-8:]
            bull = sum(1 for c in recent if c.is_bullish)
            if bull >= 6:
                return StructureState.BULLISH_STRUCTURE
            elif bull <= 2:
                return StructureState.BEARISH_STRUCTURE
            # Check if making higher closes
            closes = [c.close for c in recent]
            if all(closes[i] >= closes[i-1] for i in range(1, len(closes))):
                return StructureState.BULLISH_STRUCTURE
            elif all(closes[i] <= closes[i-1] for i in range(1, len(closes))):
                return StructureState.BEARISH_STRUCTURE

        return StructureState.UNCLEAR

    def _detect_bos_choch(self, swings: List[SwingPoint], ctx: MarketContext):
        """Detect Break of Structure and Change of Character events."""
        if len(swings) < 4:
            return

        highs = [s for s in swings if s.is_high]
        lows = [s for s in swings if not s.is_high]

        if len(highs) < 2 or len(lows) < 2:
            return

        prev_struct = self._prev_structure

        # BOS: structure continuation confirmed
        if (ctx.structure_state == StructureState.BULLISH_STRUCTURE and
            prev_struct in (StructureState.BULLISH_STRUCTURE,
                           StructureState.BROKEN_BULLISH)):
            ctx.last_bos = "bullish"
        elif (ctx.structure_state == StructureState.BEARISH_STRUCTURE and
              prev_struct in (StructureState.BEARISH_STRUCTURE,
                             StructureState.BROKEN_BEARISH)):
            ctx.last_bos = "bearish"

        # CHOCH: structure reversal detected
        if (prev_struct in (StructureState.BEARISH_STRUCTURE,
                           StructureState.BROKEN_BEARISH,
                           StructureState.CHOCH_BEARISH) and
            ctx.structure_state == StructureState.BULLISH_STRUCTURE):
            ctx.last_choch = "bullish"
            ctx.structure_state = StructureState.CHOCH_BULLISH
        elif (prev_struct in (StructureState.BULLISH_STRUCTURE,
                             StructureState.BROKEN_BULLISH,
                             StructureState.CHOCH_BULLISH) and
              ctx.structure_state == StructureState.BEARISH_STRUCTURE):
            ctx.last_choch = "bearish"
            ctx.structure_state = StructureState.CHOCH_BEARISH

    def _cluster_sr_levels(self, swings: List[SwingPoint],
                           candles: List[Candle]) -> List[SupportResistance]:
        """Cluster swing points into support/resistance levels."""
        if not swings or not candles:
            return []

        price_range = max(c.high for c in candles) - min(c.low for c in candles)
        if price_range < 0.01:
            return []

        tolerance = price_range * ANALYSIS.sr_cluster_tolerance / 100.0
        sr_levels: List[SupportResistance] = []

        for swing in swings:
            merged = False
            for sr in sr_levels:
                if abs(swing.price - sr.price) < tolerance:
                    sr.price = (sr.price * sr.touch_count + swing.price) / (sr.touch_count + 1)
                    sr.touch_count += 1
                    sr.strength = min(1.0, sr.touch_count / 5.0)
                    merged = True
                    break

            if not merged:
                current_price = candles[-1].close
                is_support = swing.price < current_price
                sr_levels.append(SupportResistance(
                    price=swing.price,
                    strength=swing.strength / 2.0,
                    is_support=is_support,
                    touch_count=1
                ))

        current_price = candles[-1].close
        for sr in sr_levels:
            sr.is_support = sr.price < current_price

        # Sort by proximity to current price
        if candles:
            current = candles[-1].close
            sr_levels.sort(key=lambda s: abs(s.price - current))

        return sr_levels[:10]

    def reset(self):
        """Reset state for fresh scanning."""
        self._prev_structure = StructureState.UNCLEAR
        self._swing_history = []
        self._structure_streak = 0
