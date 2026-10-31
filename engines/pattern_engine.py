# ============================================================
#  PATTERN ENGINE — 16 candlestick patterns with strength scoring
# ============================================================

from typing import List
from core.candle import Candle
from core.market_context import TrendState


class PatternResult:
    __slots__ = ('name', 'direction', 'strength', 'pattern_type')
    def __init__(self, name: str, direction: str, strength: float, pattern_type: str = "reversal"):
        self.name = name
        self.direction = direction  # "UP" or "DOWN"
        self.strength = strength     # 0.0 to 1.0
        self.pattern_type = pattern_type  # "reversal", "continuation", "breakout"
    def __repr__(self):
        return f"{self.name}({self.direction}, {self.strength:.0%})"


class PatternEngine:
    """Detects 16 priority candlestick patterns."""

    def detect_all(self, candles: List[Candle], trend_state: 'TrendState' = None) -> List[PatternResult]:
        if len(candles) < 3:
            return []
        patterns = []
        c = candles
        last, prev = c[-1], c[-2]
        prev2 = c[-3] if len(c) >= 3 else prev

        # Single-candle patterns
        patterns.extend(self._check_hammer(last))
        patterns.extend(self._check_shooting_star(last))
        patterns.extend(self._check_marubozu(last))
        patterns.extend(self._check_exhaustion_candle(last, c))
        patterns.extend(self._check_momentum_expansion(last, c))

        # Two-candle patterns
        patterns.extend(self._check_engulfing(last, prev))
        patterns.extend(self._check_tweezer(last, prev))
        patterns.extend(self._check_fakeout(last, prev, c))

        # Three-candle patterns
        if len(c) >= 3:
            patterns.extend(self._check_morning_evening_star(prev2, prev, last))
            patterns.extend(self._check_three_soldiers_crows(c))

        # Breakout / sweep candles
        patterns.extend(self._check_breakout_candle(last, c))
        patterns.extend(self._check_liquidity_sweep_candle(last, c))

        # ── Context filter: penalize counter-trend reversal patterns ──
        if trend_state is not None:
            is_strong_bull = trend_state in (TrendState.STRONG_BULLISH, TrendState.BULLISH)
            is_strong_bear = trend_state in (TrendState.STRONG_BEARISH, TrendState.BEARISH)
            filtered = []
            for p in patterns:
                if p.pattern_type == "reversal":
                    # Penalize reversal patterns that oppose the trend
                    if is_strong_bull and p.direction == "DOWN":
                        p.strength *= 0.30  # 70% penalty
                    elif is_strong_bear and p.direction == "UP":
                        p.strength *= 0.30  # 70% penalty
                    # Skip very weak patterns after penalty
                    if p.strength < 0.15:
                        continue
                filtered.append(p)
            patterns = filtered

        return patterns

    def _check_hammer(self, c: Candle) -> List[PatternResult]:
        if c.lower_wick_ratio > 0.55 and c.body_ratio < 0.30 and c.upper_wick_ratio < 0.15:
            s = min(1.0, c.lower_wick_ratio * 0.9)
            return [PatternResult("Hammer", "UP", s, "reversal")]
        return []

    def _check_shooting_star(self, c: Candle) -> List[PatternResult]:
        if c.upper_wick_ratio > 0.55 and c.body_ratio < 0.30 and c.lower_wick_ratio < 0.15:
            s = min(1.0, c.upper_wick_ratio * 0.9)
            return [PatternResult("Shooting Star", "DOWN", s, "reversal")]
        return []

    def _check_marubozu(self, c: Candle) -> List[PatternResult]:
        if c.body_ratio > 0.80:
            d = "UP" if c.is_bullish else "DOWN"
            return [PatternResult("Marubozu", d, c.body_ratio, "continuation")]
        return []

    def _check_engulfing(self, last: Candle, prev: Candle) -> List[PatternResult]:
        results = []
        if last.is_bullish and prev.is_bearish and last.engulfs(prev):
            s = min(1.0, last.body / max(prev.body, 0.01) * 0.5)
            results.append(PatternResult("Bullish Engulfing", "UP", s, "reversal"))
        if last.is_bearish and prev.is_bullish and last.engulfs(prev):
            s = min(1.0, last.body / max(prev.body, 0.01) * 0.5)
            results.append(PatternResult("Bearish Engulfing", "DOWN", s, "reversal"))
        return results

    def _check_tweezer(self, last: Candle, prev: Candle) -> List[PatternResult]:
        results = []
        tol = max(last.total_range, prev.total_range) * 0.1
        # Tweezer Bottom
        if (abs(last.low - prev.low) < tol and
            prev.is_bearish and last.is_bullish):
            results.append(PatternResult("Tweezer Bottom", "UP", 0.7, "reversal"))
        # Tweezer Top
        if (abs(last.high - prev.high) < tol and
            prev.is_bullish and last.is_bearish):
            results.append(PatternResult("Tweezer Top", "DOWN", 0.7, "reversal"))
        return results

    def _check_morning_evening_star(self, c1: Candle, c2: Candle, c3: Candle) -> List[PatternResult]:
        results = []
        # Morning Star: bearish, small body, bullish
        if (c1.is_bearish and c1.body_ratio > 0.3 and
            c2.body_ratio < 0.2 and
            c3.is_bullish and c3.body_ratio > 0.3):
            s = min(1.0, (c1.body_ratio + c3.body_ratio) / 2)
            results.append(PatternResult("Morning Star", "UP", s, "reversal"))
        # Evening Star
        if (c1.is_bullish and c1.body_ratio > 0.3 and
            c2.body_ratio < 0.2 and
            c3.is_bearish and c3.body_ratio > 0.3):
            s = min(1.0, (c1.body_ratio + c3.body_ratio) / 2)
            results.append(PatternResult("Evening Star", "DOWN", s, "reversal"))
        return results

    def _check_three_soldiers_crows(self, candles: List[Candle]) -> List[PatternResult]:
        if len(candles) < 3:
            return []
        last3 = candles[-3:]
        # Three White Soldiers
        if all(c.is_bullish and c.body_ratio > 0.4 for c in last3):
            if last3[1].close > last3[0].close and last3[2].close > last3[1].close:
                avg_s = sum(c.body_ratio for c in last3) / 3
                return [PatternResult("Three White Soldiers", "UP", avg_s, "continuation")]
        # Three Black Crows
        if all(c.is_bearish and c.body_ratio > 0.4 for c in last3):
            if last3[1].close < last3[0].close and last3[2].close < last3[1].close:
                avg_s = sum(c.body_ratio for c in last3) / 3
                return [PatternResult("Three Black Crows", "DOWN", avg_s, "continuation")]
        return []

    def _check_exhaustion_candle(self, last: Candle, candles: List[Candle]) -> List[PatternResult]:
        if len(candles) < 5:
            return []
        streak = candles[-5:-1]
        if all(c.is_bullish for c in streak) and last.is_bearish and last.upper_wick_ratio > 0.4:
            return [PatternResult("Exhaustion Candle", "DOWN", 0.50, "reversal")]
        if all(c.is_bearish for c in streak) and last.is_bullish and last.lower_wick_ratio > 0.4:
            return [PatternResult("Exhaustion Candle", "UP", 0.50, "reversal")]
        return []

    def _check_fakeout(self, last: Candle, prev: Candle, candles: List[Candle]) -> List[PatternResult]:
        if len(candles) < 8:
            return []
        recent_highs = [c.high for c in candles[-8:-1]]
        recent_lows = [c.low for c in candles[-8:-1]]
        rh = max(recent_highs)
        rl = min(recent_lows)
        # Fakeout above: prev broke above, last closed back inside
        if prev.high > rh and last.close < rh and last.is_bearish:
            return [PatternResult("Fakeout Candle", "DOWN", 0.55, "reversal")]
        if prev.low < rl and last.close > rl and last.is_bullish:
            return [PatternResult("Fakeout Candle", "UP", 0.55, "reversal")]
        return []

    def _check_breakout_candle(self, last: Candle, candles: List[Candle]) -> List[PatternResult]:
        if len(candles) < 8:
            return []
        prev_range = candles[-8:-1]
        rh = max(c.high for c in prev_range)
        rl = min(c.low for c in prev_range)
        avg_body = sum(c.body for c in prev_range) / len(prev_range)
        if last.close > rh and last.body > avg_body * 1.5 and last.body_ratio > 0.5:
            return [PatternResult("Breakout Candle", "UP", 0.85, "breakout")]
        if last.close < rl and last.body > avg_body * 1.5 and last.body_ratio > 0.5:
            return [PatternResult("Breakout Candle", "DOWN", 0.85, "breakout")]
        return []

    def _check_momentum_expansion(self, last: Candle, candles: List[Candle]) -> List[PatternResult]:
        if len(candles) < 6:
            return []
        avg_range = sum(c.total_range for c in candles[-6:-1]) / 5
        if last.total_range > avg_range * 2.0 and last.body_ratio > 0.6:
            d = "UP" if last.is_bullish else "DOWN"
            return [PatternResult("Momentum Expansion", d, 0.8, "continuation")]
        return []

    def _check_liquidity_sweep_candle(self, last: Candle, candles: List[Candle]) -> List[PatternResult]:
        if len(candles) < 10:
            return []
        prev_lows = [c.low for c in candles[-10:-1]]
        prev_highs = [c.high for c in candles[-10:-1]]
        # Sweep lows then close bullish
        if last.low < min(prev_lows) and last.is_bullish and last.lower_wick_ratio > 0.4:
            return [PatternResult("Liquidity Sweep", "UP", 0.60, "reversal")]
        if last.high > max(prev_highs) and last.is_bearish and last.upper_wick_ratio > 0.4:
            return [PatternResult("Liquidity Sweep", "DOWN", 0.60, "reversal")]
        return []
