# ============================================================
#  MOMENTUM ENGINE — Directional momentum and acceleration (v3)
#  Fixed: reduced recency weighting, trend consistency check,
#         balanced direction scoring
# ============================================================

from typing import List
import sys
sys.path.insert(0, '.')
from core.candle import Candle
from core.market_context import MarketContext
from config import ANALYSIS


class MomentumEngine:
    """
    Analyses momentum: rate of change, acceleration,
    exhaustion, divergence.

    v3 Changes:
    - Reduced recency weighting: (1 + 0.5*i/lb) instead of (i+1)/lb
      to prevent single recent candle from dominating
    - Directional scoring now symmetrical between bullish/bearish
    - Added body-weighted direction scoring for more reliable signals
    """

    def analyse(self, candles: List[Candle], ctx: MarketContext) -> MarketContext:
        if len(candles) < ANALYSIS.momentum_lookback + 1:
            return ctx
        lb = ANALYSIS.momentum_lookback
        recent = candles[-lb:]

        # FIXED: Reduced recency weighting to prevent single candle dominance
        # Old: (i+1)/lb — last candle gets weight 1.0, first gets 0.2
        # New: (1.0 + 1.0 * i/(lb-1)) — last candle gets weight 1.5, first gets 1.0
        bull_p = 0.0
        bear_p = 0.0
        for i, c in enumerate(recent):
            weight = 1.0 + 1.0 * (i / max(lb - 1, 1))
            if c.is_bullish:
                bull_p += weight * c.body_ratio
            elif c.is_bearish:
                bear_p += weight * c.body_ratio

        total = bull_p + bear_p
        ctx.momentum_score = (bull_p - bear_p) / total if total > 0 else 0.0

        if len(candles) >= lb * 2:
            older_avg = sum(c.body for c in candles[-(lb*2):-lb]) / lb
            recent_avg = sum(c.body for c in recent) / lb
            ctx.momentum_acceleration = (recent_avg - older_avg) / max(older_avg, 0.0001)
        ctx.is_exhausted = self._detect_exhaustion(candles)
        return ctx

    def get_momentum_quality(self, candles: List[Candle]) -> float:
        """
        Assess momentum quality. 0.0 = no momentum, 1.0 = perfect.

        v3: More balanced — doesn't over-reward single strong candle.
        Requires directional consistency across the window.
        """
        if len(candles) < 5:
            return 0.0
        r = candles[-5:]

        # Directional consistency
        bull = sum(1 for c in r if c.is_bullish)
        bear = sum(1 for c in r if c.is_bearish)
        consistency = max(bull, bear) / 5.0

        # Average body strength (penalize weak bodies more aggressively)
        avg_body = sum(c.body_ratio for c in r) / 5.0
        body_quality = avg_body ** 0.7

        # Increasing body sizes = accelerating momentum
        bodies = [c.body for c in r]
        if max(bodies) < 0.01:
            return 0.0  # all tiny candles = no momentum
        inc = sum(1 for i in range(1, 5) if bodies[i] >= bodies[i-1] * 0.9) / 4.0

        # Penalize if bodies are very small (noise candles)
        min_body_penalty = 1.0
        noise_count = sum(1 for c in r if c.body_ratio < ANALYSIS.noise_threshold)
        if noise_count >= 3:
            min_body_penalty = 0.3
        elif noise_count >= 2:
            min_body_penalty = 0.6

        # Penalize mixed direction candles more
        direction_penalty = 1.0
        if consistency < 0.6:
            direction_penalty = 0.5

        raw = consistency * 0.30 + body_quality * 0.35 + inc * 0.20 + min_body_penalty * 0.15
        return min(1.0, raw * direction_penalty)

    def get_overextension_score(self, candles: List[Candle]) -> float:
        """
        Measure how overextended the current move is.
        Returns 0.0 (normal) to 1.0 (severely overextended / chasing territory).

        This detects the exact scenario from the screenshot: price has already
        dropped massively and the engine should NOT chase it further down.

        Checks:
        1. Price displacement from 20-candle mean vs ATR
        2. Consecutive directional candle count
        3. Total body displacement in recent candles vs ATR
        """
        if len(candles) < 12:
            return 0.0

        # ATR approximation (average true range of last 14 candles)
        lookback = min(14, len(candles))
        atr = sum(c.total_range for c in candles[-lookback:]) / lookback
        if atr < 0.0001:
            return 0.0

        # 1. Price displacement from recent mean
        mean_lookback = min(20, len(candles))
        mean_price = sum(c.close for c in candles[-mean_lookback:]) / mean_lookback
        current_price = candles[-1].close
        displacement = abs(current_price - mean_price) / atr
        # Normalize: 0 at 0 ATR, 1.0 at 3+ ATR displacement
        displacement_score = min(1.0, displacement / 3.0)

        # 2. Consecutive directional candles
        consec = 0
        direction = None
        for c in reversed(candles[-12:]):
            if direction is None:
                direction = "bull" if c.is_bullish else "bear" if c.is_bearish else None
                if direction:
                    consec = 1
            elif (direction == "bull" and c.is_bullish) or (direction == "bear" and c.is_bearish):
                consec += 1
            else:
                break
        # Normalize: 0 at 0-2 candles, 1.0 at 7+ candles
        consec_score = min(1.0, max(0.0, (consec - 2)) / 5.0)

        # 3. Total directional body displacement in last 8 candles
        recent = candles[-min(8, len(candles)):]
        bull_body = sum(c.body for c in recent if c.is_bullish)
        bear_body = sum(c.body for c in recent if c.is_bearish)
        net_displacement = abs(bull_body - bear_body) / atr
        # Normalize: 0 at 0 ATR, 1.0 at 4+ ATR net displacement
        body_score = min(1.0, net_displacement / 4.0)

        # Combined score — displacement is most important
        score = displacement_score * 0.45 + consec_score * 0.25 + body_score * 0.30
        return min(1.0, score)

    def get_overextension_direction(self, candles: List[Candle]) -> str:
        """
        Which direction is the move overextended in?
        Returns "UP", "DOWN", or None.
        """
        if len(candles) < 5:
            return None
        mean_price = sum(c.close for c in candles[-20:]) / len(candles[-20:])
        current_price = candles[-1].close
        if current_price > mean_price:
            return "UP"
        elif current_price < mean_price:
            return "DOWN"
        return None

    def get_immediate_pressure(self, candles: List[Candle]) -> float:
        """
        Fast-reacting directional pressure from the last 2-3 candles.
        Returns -1.0 (extreme bearish) to +1.0 (extreme bullish).
        The LAST candle gets 3x weight to capture 'right now' direction.
        This is the fastest signal — catches big red/green candles immediately.
        """
        if len(candles) < 2:
            return 0.0
        n = min(3, len(candles))
        recent = candles[-n:]
        bull_force = 0.0
        bear_force = 0.0
        for i, c in enumerate(recent):
            # Last candle gets 3x weight, second-to-last 1.5x, rest 1x
            w = 3.0 if i == n - 1 else (1.5 if i == n - 2 else 1.0)
            if c.is_bullish:
                bull_force += c.body_ratio * w
            elif c.is_bearish:
                bear_force += c.body_ratio * w
        total = bull_force + bear_force
        if total < 0.001:
            return 0.0
        return (bull_force - bear_force) / total

    def _detect_exhaustion(self, candles: List[Candle]) -> bool:
        n = ANALYSIS.exhaustion_streak
        if len(candles) < n:
            return False
        streak = candles[-n:]
        if not (all(c.is_bullish for c in streak) or all(c.is_bearish for c in streak)):
            # Only detect distance-based exhaustion if price is at extreme (>0.48) AND body is shrinking
            if len(candles) >= 12:
                lookback = min(20, len(candles))
                highs = [c.high for c in candles[-lookback:]]
                lows = [c.low for c in candles[-lookback:]]
                mid = (max(highs) + min(lows)) / 2.0
                price_range = max(highs) - min(lows)
                if price_range > 0:
                    dist_from_mid = abs(candles[-1].close - mid) / price_range
                    avg_b = sum(c.body for c in candles[-5:]) / 5.0
                    if dist_from_mid > 0.48 and candles[-1].body < avg_b * 0.4:
                        return True
            return False
        bodies = [c.body for c in streak]
        # Shrinking bodies = exhaustion
        shrink = sum(1 for i in range(1, n) if bodies[i] < bodies[i-1])
        if shrink >= n - 1:
            return True
        # Spike candle after run = potential exhaustion
        avg = sum(bodies[:-1]) / max(n - 1, 1)
        return avg > 0 and bodies[-1] > avg * 2.5

    def get_divergence_hint(self, candles: List[Candle]) -> str:
        if len(candles) < 10:
            return "none"
        f, s = candles[-10:-5], candles[-5:]
        fh, sh = max(c.high for c in f), max(c.high for c in s)
        fl, sl = min(c.low for c in f), min(c.low for c in s)
        fm = sum(c.body if c.is_bullish else -c.body for c in f) / len(f)
        sm = sum(c.body if c.is_bullish else -c.body for c in s) / len(s)
        if sh > fh and sm < fm * 0.35:
            return "bearish_div"
        if sl < fl and sm > fm * 0.35:
            return "bullish_div"
        return "none"
