import sys
sys.path.insert(0, '.')
from typing import List, Optional, Dict
from core.candle import Candle

class TechnicalIndicators:
    """Technical indicators computed from candle data: RSI, Stochastic, Bollinger Bands."""
    
    def compute_all(self, candles: List[Candle]) -> Dict:
        """Compute all indicators. Returns dict of indicator values."""
        result = {}
        if len(candles) >= 14:
            result['rsi'] = self._compute_rsi(candles, 14)
        if len(candles) >= 14:
            k, d = self._compute_stochastic(candles, 14, 3)
            result['stoch_k'] = k
            result['stoch_d'] = d
        if len(candles) >= 20:
            mid, upper, lower = self._compute_bollinger(candles, 20, 2.0)
            result['bb_mid'] = mid
            result['bb_upper'] = upper
            result['bb_lower'] = lower
        return result
    
    def _compute_rsi(self, candles: List[Candle], period: int = 14) -> float:
        """Compute RSI using Wilder's smoothing method."""
        closes = [c.close for c in candles]
        if len(closes) < period + 1:
            return 50.0  # neutral
        
        # Calculate price changes
        changes = [closes[i] - closes[i-1] for i in range(1, len(closes))]
        
        # Initial average gain/loss from first 'period' changes
        gains = [max(0, c) for c in changes[:period]]
        losses = [max(0, -c) for c in changes[:period]]
        avg_gain = sum(gains) / period
        avg_loss = sum(losses) / period
        
        # Wilder's smoothing for remaining changes
        for c in changes[period:]:
            gain = max(0, c)
            loss = max(0, -c)
            avg_gain = (avg_gain * (period - 1) + gain) / period
            avg_loss = (avg_loss * (period - 1) + loss) / period
        
        if avg_loss < 0.0001:
            return 100.0
        rs = avg_gain / avg_loss
        return 100.0 - (100.0 / (1.0 + rs))
    
    def _compute_stochastic(self, candles: List[Candle], k_period: int = 14, d_period: int = 3) -> tuple:
        """Compute Stochastic %K and %D."""
        if len(candles) < k_period:
            return 50.0, 50.0
        
        # Compute %K values for last d_period candles
        k_values = []
        for i in range(max(0, len(candles) - d_period), len(candles)):
            window = candles[max(0, i - k_period + 1):i + 1]
            highest = max(c.high for c in window)
            lowest = min(c.low for c in window)
            rng = highest - lowest
            if rng < 0.0001:
                k_values.append(50.0)
            else:
                k_values.append(((candles[i].close - lowest) / rng) * 100.0)
        
        k = k_values[-1] if k_values else 50.0
        d = sum(k_values) / len(k_values) if k_values else 50.0
        return k, d
    
    def _compute_bollinger(self, candles: List[Candle], period: int = 20, std_dev: float = 2.0) -> tuple:
        """Compute Bollinger Bands (mid, upper, lower)."""
        closes = [c.close for c in candles[-period:]]
        if len(closes) < period:
            mid = sum(closes) / len(closes)
            return mid, mid, mid
        
        mid = sum(closes) / period
        variance = sum((c - mid) ** 2 for c in closes) / period
        std = variance ** 0.5
        return mid, mid + std_dev * std, mid - std_dev * std
    
    def get_rsi_signal(self, rsi: float) -> tuple:
        """Returns (direction_bias, strength) based on RSI.
        Overbought (>70) = DOWN bias, Oversold (<30) = UP bias."""
        if rsi > 80:
            return 'DOWN', 0.9
        elif rsi > 70:
            return 'DOWN', 0.6
        elif rsi < 20:
            return 'UP', 0.9
        elif rsi < 30:
            return 'UP', 0.6
        return None, 0.0
    
    def get_stochastic_signal(self, k: float, d: float) -> tuple:
        """Returns (direction_bias, strength) based on Stochastic crossover."""
        if k > 80 and d > 80:
            return 'DOWN', 0.7
        elif k < 20 and d < 20:
            return 'UP', 0.7
        elif k > d and k < 30:  # bullish crossover in oversold
            return 'UP', 0.5
        elif k < d and k > 70:  # bearish crossover in overbought
            return 'DOWN', 0.5
        return None, 0.0
    
    def get_bollinger_signal(self, price: float, upper: float, lower: float, mid: float) -> tuple:
        """Returns (direction_bias, strength) based on Bollinger Band position."""
        band_width = upper - lower
        if band_width < 0.0001:
            return None, 0.0
        
        if price >= upper:
            return 'DOWN', min(1.0, (price - upper) / (band_width * 0.1) * 0.3 + 0.5)
        elif price <= lower:
            return 'UP', min(1.0, (lower - price) / (band_width * 0.1) * 0.3 + 0.5)
        elif abs(price - mid) < band_width * 0.05:  # at middle band
            return None, 0.1
        return None, 0.0

    def compute_elder_ray(self, candles: List[Candle], period: int = 13) -> dict:
        """
        Compute Elder-Ray Index (Bulls Power and Bears Power).
        Bulls Power = High - EMA(period)
        Bears Power = Low  - EMA(period)
        Returns dict with 'bulls_power', 'bears_power', 'bulls_slope', 'bears_slope'
        """
        if len(candles) < period + 1:
            return {}

        closes = [c.close for c in candles]
        highs  = [c.high  for c in candles]
        lows   = [c.low   for c in candles]

        # EMA calculation
        k = 2.0 / (period + 1)
        ema = sum(closes[:period]) / period
        ema_series = []
        for i, price in enumerate(closes[period:]):
            ema = price * k + ema * (1 - k)
            ema_series.append(ema)

        if not ema_series:
            return {}

        # ATR for normalization
        atr_vals = [candles[i].total_range for i in range(1, len(candles))]
        atr = sum(atr_vals[-14:]) / min(14, len(atr_vals)) if atr_vals else 1.0
        if atr < 0.0001:
            atr = 1.0

        n = len(ema_series)
        offset = len(candles) - period - n

        bulls_vals = []
        bears_vals = []
        for i, ema_val in enumerate(ema_series):
            ci = offset + period + i
            if 0 <= ci < len(candles):
                bp  = (highs[ci]  - ema_val) / atr
                brp = (lows[ci]   - ema_val) / atr
                bulls_vals.append(max(-1.0, min(1.0, bp)))
                bears_vals.append(max(-1.0, min(1.0, brp)))

        if not bulls_vals:
            return {}

        def slope(vals):
            if len(vals) < 3:
                return 0.0
            delta = vals[-1] - vals[-3]
            return max(-1.0, min(1.0, delta / 0.3))

        return {
            'bulls_power': bulls_vals[-1],
            'bears_power': bears_vals[-1],
            'bulls_series': bulls_vals,
            'bears_series': bears_vals,
            'bulls_slope': slope(bulls_vals),
            'bears_slope': slope(bears_vals),
        }

    def get_elder_ray_signal(self, er: dict) -> tuple:
        """
        Returns (direction_bias, strength) from Elder-Ray values.
        direction_bias: 'UP', 'DOWN', or None
        strength: 0.0 to 1.0
        """
        if not er:
            return None, 0.0
        bp  = er.get('bulls_power', 0.0)
        brp = er.get('bears_power', 0.0)
        bs  = er.get('bulls_slope', 0.0)
        brs = er.get('bears_slope', 0.0)

        # Classic Elder-Ray entry rule:
        # BUY:  Bears Power negative but RISING (toward zero) + Bulls Power positive
        # SELL: Bulls Power positive but FALLING (toward zero) + Bears Power negative
        if bp > 0.03 and brp < 0 and brs > 0.05:
            strength = min(1.0, bp * 2 + abs(brs))
            return 'UP', round(strength, 2)
        elif brp < -0.03 and bp > 0 and bs < -0.05:
            strength = min(1.0, abs(brp) * 2 + abs(bs))
            return 'DOWN', round(strength, 2)
        elif bp > 0.05 and bs > 0:
            return 'UP', round(min(0.6, bp * 2), 2)
        elif brp < -0.05 and brs < 0:
            return 'DOWN', round(min(0.6, abs(brp) * 2), 2)

        return None, 0.0

    # ──────────────────────────────────────────────────────────
    #  STOCHASTIC RSI
    #  Applies the Stochastic formula to RSI values.
    #  Far more sensitive than RSI or Stochastic alone.
    #  Best for short-term (1-min) Olymp Trade timing.
    # ──────────────────────────────────────────────────────────

    def _compute_rsi_series(self, candles: List[Candle], period: int = 14) -> List[float]:
        """Compute a full RSI series (one value per candle)."""
        closes = [c.close for c in candles]
        if len(closes) < period + 1:
            return [50.0] * len(closes)

        changes = [closes[i] - closes[i-1] for i in range(1, len(closes))]
        gains = [max(0, c) for c in changes[:period]]
        losses = [max(0, -c) for c in changes[:period]]
        avg_gain = sum(gains) / period
        avg_loss = sum(losses) / period

        rsi_values = [50.0] * (period + 1)   # first candles — neutral placeholder
        for ch in changes[period:]:
            gain = max(0, ch)
            loss = max(0, -ch)
            avg_gain = (avg_gain * (period - 1) + gain) / period
            avg_loss = (avg_loss * (period - 1) + loss) / period
            if avg_loss < 0.0001:
                rsi_values.append(100.0)
            else:
                rs = avg_gain / avg_loss
                rsi_values.append(100.0 - (100.0 / (1.0 + rs)))

        return rsi_values

    def compute_williams_r(self, candles: List[Candle], period: int = 14) -> dict:
        """
        Compute Williams %R (period).
        Formula: (Highest High - Close) / (Highest High - Lowest Low) * -100
        Returns dict with:
          'wpr': Williams %R value (-100 to 0)
          'zone': 'overbought', 'oversold', or 'neutral'
          'valid': bool
        """
        if len(candles) < period:
            return {'wpr': -50.0, 'zone': 'neutral', 'valid': False}

        window = candles[-period:]
        highest_high = max(c.high for c in window)
        lowest_low = min(c.low for c in window)
        current_close = window[-1].close

        rng = highest_high - lowest_low
        if rng < 0.00001:
            wpr = -50.0
        else:
            wpr = (highest_high - current_close) / rng * -100.0

        if wpr >= -20.0:
            zone = 'overbought'
        elif wpr <= -80.0:
            zone = 'oversold'
        else:
            zone = 'neutral'

        return {
            'wpr': wpr,
            'zone': zone,
            'valid': True
        }

    def get_williams_r_signal(self, wpr_data: dict) -> tuple:
        """
        Returns (direction_bias, strength, reason) from Williams %R.
        - Extreme Overbought (>= -20) -> DOWN bias
        - Extreme Oversold (<= -80) -> UP bias
        """
        if not wpr_data.get('valid', False):
            return None, 0.0, 'Williams %R not available'

        wpr = wpr_data['wpr']

        if wpr >= -20:
            return 'DOWN', 0.80, f'Williams %R overbought ({wpr:.0f}) — reversal risk DOWN'
        if wpr <= -80:
            return 'UP', 0.80, f'Williams %R oversold ({wpr:.0f}) — reversal risk UP'

        return None, 0.0, 'Williams %R neutral'
