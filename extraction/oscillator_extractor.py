# ============================================================
#  OSCILLATOR EXTRACTOR — Reads Bulls/Bears Power histograms
#  from Olymp Trade chart screenshot (Elder-Ray Index)
#
#  Elder-Ray Math:
#    Bulls Power = High - EMA(13)   → measures buyer strength
#    Bears Power = Low  - EMA(13)   → measures seller strength
#
#  Visual Reading:
#    Green bars ABOVE zero line → Bulls Power positive  (bullish)
#    Red bars   BELOW zero line → Bears Power negative  (bearish)
#
#  This module:
#    1. Detects the oscillator panel region on screen
#    2. Measures heights of green/red bars relative to zero line
#    3. Computes slopes, divergences, zero-line crosses
#    4. Returns OscillatorReading — used as primary direction voter
# ============================================================

import numpy as np
import cv2
from dataclasses import dataclass, field
from typing import List, Optional, Tuple
import sys
sys.path.insert(0, '.')


@dataclass
class OscillatorReading:
    """
    Parsed state of the Elder-Ray oscillator panel.
    All values are computed from the current screen capture.
    """
    # Raw bar values — list of N most recent readings
    # Positive = above zero line, Negative = below zero line, range approximately -1.0 to +1.0
    bulls_power: List[float] = field(default_factory=list)  # green bars
    bears_power: List[float] = field(default_factory=list)  # red bars (usually negative)

    # Current values (last bar)
    bulls_current: float = 0.0   # latest green bar height (normalized)
    bears_current: float = 0.0   # latest red bar height (normalized, negative = below zero)

    # Slopes: +1 = rising, -1 = falling, 0 = flat (last 3 bars trend)
    bulls_slope: float = 0.0
    bears_slope: float = 0.0

    # Zero-line crosses (very strong signals)
    zero_cross_up: bool = False    # Bears Power just crossed from negative to positive
    zero_cross_down: bool = False  # Bulls Power just crossed from positive to negative

    # Divergences (most reliable reversal signal)
    bulls_divergence: bool = False   # Price higher but Bulls Power lower → bearish div
    bears_divergence: bool = False   # Price lower  but Bears Power higher → bullish div

    # Regime
    both_shrinking: bool = False     # Both oscillators converging to zero → exhaustion
    trend_exhaustion: bool = False   # Strong move losing momentum

    # Signal strength boost/penalty for confidence engine
    # +1.0 = strong oscillator confirmation, -1.0 = strong oscillator rejection
    direction_score: float = 0.0

    # Whether we successfully extracted oscillator data
    is_valid: bool = False

    # Elder-Ray direction verdict
    elder_ray_direction: Optional[str] = None  # "UP", "DOWN", or None

    # Debug info
    panel_found: bool = False
    bar_count: int = 0


class OscillatorExtractor:
    """
    Extracts Bulls Power (green) and Bears Power (red) histogram values
    from the Elder-Ray oscillator panel displayed below the main candle chart.

    The oscillator panel is identified by:
    - Very dark background (nearly black)
    - Dense vertical bars that are either pure green or pure red
    - Located below the main candlestick chart area
    - Horizontal zero-line across the middle

    Extraction method:
    - Column-by-column scan from right (newest) to left (oldest)
    - For each column, measure height of green pixels vs red pixels
    - Locate the zero line as the horizontal boundary between green/red zones
    - Normalize bar heights to [-1.0, +1.0] range
    """

    def __init__(self):
        self.reset()

    def reset(self):
        self._last_bulls: List[float] = []
        self._last_bears: List[float] = []
        self._last_price_highs: List[float] = []
        self._last_price_lows: List[float] = []

    def extract(self, bgr_img: np.ndarray,
                chart_region: Tuple[int, int, int, int],
                oscillator_region: Optional[Tuple[int, int, int, int]] = None,
                candles=None) -> OscillatorReading:
        """
        Extract oscillator values from the screen.

        Args:
            bgr_img: Full screenshot in BGR format
            chart_region: (x, y, w, h) of the main candle chart
            oscillator_region: (x, y, w, h) of oscillator panel, or None to auto-detect
            candles: list of Candle objects (used for divergence detection and software fallback)

        Returns:
            OscillatorReading with all computed values
        """
        reading = OscillatorReading()

        # Try to get oscillator region
        osc_region = oscillator_region
        if osc_region is None:
            osc_region = self._detect_oscillator_panel(bgr_img, chart_region)

        if osc_region is None:
            # Fallback: compute Elder-Ray from candle data (software calculation)
            if candles and len(candles) >= 14:
                return self._software_elder_ray(candles)
            reading.is_valid = False
            return reading

        reading.panel_found = True

        # Extract bar heights from the oscillator panel
        bulls, bears = self._extract_bar_series(bgr_img, osc_region)

        if len(bulls) < 3 or len(bears) < 3:
            # Too few bars detected — fall back to software
            if candles and len(candles) >= 14:
                return self._software_elder_ray(candles)
            return reading

        reading.bar_count = max(len(bulls), len(bears))
        reading.bulls_power = bulls
        reading.bears_power = bears
        reading.bulls_current = bulls[-1] if bulls else 0.0
        reading.bears_current = bears[-1] if bears else 0.0

        # Compute slopes (trend of last 3 bars)
        reading.bulls_slope = self._compute_slope(bulls)
        reading.bears_slope = self._compute_slope(bears)

        # Detect zero-line crosses
        if len(self._last_bears) >= 2 and len(bears) >= 1:
            prev_bear = self._last_bears[-1] if self._last_bears else 0.0
            curr_bear = bears[-1]
            reading.zero_cross_up = (prev_bear < -0.05 and curr_bear > 0.02)

        if len(self._last_bulls) >= 2 and len(bulls) >= 1:
            prev_bull = self._last_bulls[-1] if self._last_bulls else 0.0
            curr_bull = bulls[-1]
            reading.zero_cross_down = (prev_bull > 0.05 and curr_bull < -0.02)

        # Detect divergences (requires price history)
        if candles and len(candles) >= 5:
            reading.bulls_divergence, reading.bears_divergence = \
                self._detect_divergence(bulls, bears, candles)

        # Detect exhaustion (both bars shrinking toward zero)
        if len(bulls) >= 3 and len(bears) >= 3:
            bulls_shrinking = abs(bulls[-1]) < abs(bulls[-3]) * 0.6
            bears_shrinking = abs(bears[-1]) < abs(bears[-3]) * 0.6
            reading.both_shrinking = bulls_shrinking and bears_shrinking

        # Compute composite direction score (-1.0 to +1.0)
        reading.direction_score = self._compute_direction_score(reading)
        if reading.direction_score > 0.15:
            reading.elder_ray_direction = "UP"
        elif reading.direction_score < -0.15:
            reading.elder_ray_direction = "DOWN"

        reading.is_valid = True

        # Cache for next scan
        self._last_bulls = list(bulls)
        self._last_bears = list(bears)
        if candles:
            self._last_price_highs = [c.high for c in candles[-10:]]
            self._last_price_lows  = [c.low  for c in candles[-10:]]

        return reading

    def _detect_oscillator_panel(self, bgr_img: np.ndarray,
                                  chart_region: Tuple[int, int, int, int]) \
            -> Optional[Tuple[int, int, int, int]]:
        """
        Auto-detect the oscillator panel below the chart region.
        The oscillator panel:
          - Has a very dark/black background
          - Contains dense green AND red vertical bars
          - Is typically in the bottom 20-35% of the total chart+oscillator area
        """
        cx, cy, cw, ch = chart_region
        img_h, img_w = bgr_img.shape[:2]

        # Search below the chart region (up to 50% of chart height below it)
        search_y_start = cy + ch
        search_y_end   = min(img_h, cy + ch + int(ch * 0.60))

        if search_y_end <= search_y_start:
            return None

        # Look for a region with both green and red bars on dark background
        region = bgr_img[search_y_start:search_y_end, cx:cx + cw]

        if region.size == 0:
            return None

        b, g, r = cv2.split(region)

        # Green pixels: green channel dominates
        green_mask = ((g > r + 20) & (g > b + 20) & (g > 40)).astype(np.uint8)
        # Red pixels: red channel dominates
        red_mask   = ((r > g + 20) & (r > b + 20) & (r > 40)).astype(np.uint8)

        green_count = green_mask.sum()
        red_count   = red_mask.sum()
        total_pixels = region.shape[0] * region.shape[1]

        # Valid oscillator panel: has both green AND red bars
        # Density check: 0.3% to 25% of pixels should be colored bars
        if total_pixels == 0:
            return None

        green_frac = green_count / total_pixels
        red_frac   = red_count   / total_pixels

        if green_frac < 0.003 or red_frac < 0.003:
            return None
        if green_frac > 0.35 or red_frac > 0.35:
            return None  # Probably the chart, not the oscillator

        # Find the vertical extent of colored bars
        colored = (green_mask | red_mask)
        rows_with_color = np.where(colored.any(axis=1))[0]

        if len(rows_with_color) < 5:
            return None

        panel_top    = int(rows_with_color.min())
        panel_bottom = int(rows_with_color.max())

        # Add small vertical padding
        pad = 4
        y1 = max(0, search_y_start + panel_top - pad)
        y2 = min(img_h, search_y_start + panel_bottom + pad)

        if (y2 - y1) < 20:
            return None

        return (cx, y1, cw, y2 - y1)

    def _extract_bar_series(self, bgr_img: np.ndarray,
                             osc_region: Tuple[int, int, int, int]) \
            -> Tuple[List[float], List[float]]:
        """
        Scan the oscillator panel column by column.
        Each column represents one time bar.
        Returns (bulls_values, bears_values) normalized to [-1.0, +1.0].
        """
        x, y, w, h = osc_region
        panel = bgr_img[y:y + h, x:x + w]

        if panel.size == 0 or h < 5:
            return [], []

        b_ch, g_ch, r_ch = cv2.split(panel)

        # Green and red masks using BGR dominance
        green_mask = ((g_ch > r_ch + 15) & (g_ch > b_ch + 15) & (g_ch > 35))
        red_mask   = ((r_ch > g_ch + 15) & (r_ch > b_ch + 15) & (r_ch > 35))

        # Find the zero line: the horizontal row with maximum transition between
        # green (above) and red (below) regions
        zero_row = self._find_zero_line(green_mask, red_mask, h)

        bulls_list: List[float] = []
        bears_list: List[float] = []

        # Scan columns from left to right (chronological order)
        # Use a stride of 2 pixels to reduce noise
        col = 0
        stride = max(1, w // 60)  # target ~50-60 bars

        while col < w:
            col_green = green_mask[:, col:col + stride]
            col_red   = red_mask[:, col:col + stride]

            g_rows = np.where(col_green.any(axis=1))[0]
            r_rows = np.where(col_red.any(axis=1))[0]

            # Bulls Power: green pixels ABOVE zero line → positive value
            if len(g_rows) >= 2:
                g_top = int(g_rows.min())
                g_bot = int(g_rows.max())
                # Height above zero line (normalized to panel half-height)
                bar_top = min(g_top, zero_row)
                bar_bot = min(g_bot, zero_row)
                height = bar_bot - bar_top
                norm = height / max(zero_row, 1)
                bulls_list.append(min(1.0, max(0.0, norm)))
            else:
                bulls_list.append(0.0)

            # Bears Power: red pixels BELOW zero line → negative value
            if len(r_rows) >= 2:
                r_top = int(r_rows.min())
                r_bot = int(r_rows.max())
                bar_top = max(r_top, zero_row)
                bar_bot = max(r_bot, zero_row)
                height = bar_bot - bar_top
                norm = height / max(h - zero_row, 1)
                bears_list.append(-min(1.0, max(0.0, norm)))
            else:
                bears_list.append(0.0)

            col += stride

        # Remove leading zeros (empty columns at edges)
        while len(bulls_list) > 1 and bulls_list[0] == 0.0 and bears_list[0] == 0.0:
            bulls_list.pop(0)
            bears_list.pop(0)

        return bulls_list, bears_list

    def _find_zero_line(self, green_mask: np.ndarray,
                        red_mask: np.ndarray, height: int) -> int:
        """
        Find the zero line row — the horizontal midpoint between
        green bars (above) and red bars (below).
        """
        # Sum colored pixels per row
        green_by_row = green_mask.sum(axis=1).astype(float)
        red_by_row   = red_mask.sum(axis=1).astype(float)

        # Find centroid of green (upper half) and red (lower half)
        total_green = green_by_row.sum()
        total_red   = red_by_row.sum()

        if total_green > 10 and total_red > 10:
            # Weighted centroid
            rows = np.arange(height, dtype=float)
            green_centroid = (green_by_row * rows).sum() / total_green
            red_centroid   = (red_by_row   * rows).sum() / total_red
            # Zero line is between the two centroids
            zero = int((green_centroid + red_centroid) / 2)
            return max(5, min(height - 5, zero))
        elif total_green > 10:
            # Only green visible → zero line near bottom of green bars
            rows = np.arange(height, dtype=float)
            green_centroid = (green_by_row * rows).sum() / total_green
            return int(min(height - 5, green_centroid + height * 0.25))
        elif total_red > 10:
            rows = np.arange(height, dtype=float)
            red_centroid = (red_by_row * rows).sum() / total_red
            return int(max(5, red_centroid - height * 0.25))
        else:
            return height // 2

    def _compute_slope(self, values: List[float]) -> float:
        """
        Slope of last 3 values. +1 = rising, -1 = falling, 0 = flat.
        """
        if len(values) < 3:
            return 0.0
        a, b, c = values[-3], values[-2], values[-1]
        delta = c - a
        if abs(delta) < 0.03:
            return 0.0
        return max(-1.0, min(1.0, delta / 0.5))

    def _detect_divergence(self, bulls: List[float], bears: List[float],
                            candles) -> Tuple[bool, bool]:
        """
        Detect Elder-Ray divergences vs price action.

        Bearish divergence (bulls_divergence=True):
          Price made a new HIGH in last N candles, but Bulls Power made a LOWER HIGH
          → Bulls are losing steam at the new price high → reversal down likely

        Bullish divergence (bears_divergence=True):
          Price made a new LOW, but Bears Power made a HIGHER LOW (less negative)
          → Bears are losing power at new price low → reversal up likely
        """
        bulls_div = False
        bears_div = False
        lookback = min(5, len(bulls) - 1, len(candles) - 1)

        if lookback < 2:
            return False, False

        # Price action in lookback window
        recent_highs = [c.high  for c in candles[-lookback:]]
        recent_lows  = [c.low   for c in candles[-lookback:]]
        prev_high    = max(recent_highs[:-1]) if len(recent_highs) > 1 else recent_highs[0]
        curr_high    = recent_highs[-1]
        prev_low     = min(recent_lows[:-1])  if len(recent_lows)  > 1 else recent_lows[0]
        curr_low     = recent_lows[-1]

        # Bulls Power in lookback window
        recent_bulls = bulls[-lookback:]
        prev_bull_max = max(recent_bulls[:-1]) if len(recent_bulls) > 1 else 0.0
        curr_bull     = recent_bulls[-1] if recent_bulls else 0.0

        # Bears Power in lookback window (bears are negative, so use min)
        recent_bears = bears[-lookback:]
        prev_bear_min = min(recent_bears[:-1]) if len(recent_bears) > 1 else 0.0
        curr_bear     = recent_bears[-1] if recent_bears else 0.0

        # Bearish divergence: price higher, bulls power lower
        if curr_high > prev_high * 1.001 and curr_bull < prev_bull_max * 0.80:
            if curr_bull < 0.20:  # bulls power must be weakening significantly
                bulls_div = True

        # Bullish divergence: price lower, bears power less negative (rising)
        if curr_low < prev_low * 0.999 and curr_bear > prev_bear_min * 0.80:
            if curr_bear > -0.20:  # bears power must be weakening significantly
                bears_div = True

        return bulls_div, bears_div

    def _compute_direction_score(self, r: OscillatorReading) -> float:
        """
        Compute composite Elder-Ray directional score.
        Returns -1.0 (strong bearish) to +1.0 (strong bullish).
        """
        score = 0.0

        # Exhaustion: if trend is exhausted or both shrinking -> Return 0.0 (no trade)
        if r.both_shrinking or r.trend_exhaustion:
            return 0.0

        # Zero-line cross is the strongest signal
        if r.zero_cross_up:
            score += 0.50
        if r.zero_cross_down:
            score -= 0.50

        # Divergences flip the expected direction
        if r.bears_divergence:
            score += 0.40   # Bullish divergence → expect UP
        if r.bulls_divergence:
            score -= 0.40   # Bearish divergence → expect DOWN

        # Current bulls power
        if r.bulls_current > 0.08 and r.bulls_slope > 0:
            score += 0.35   # Bulls strong and rising → UP
        elif r.bulls_current > 0.05 and r.bulls_slope < 0:
            score -= 0.25   # Bulls positive but FALLING → Buyers leaving → expect DOWN pullback
        elif r.bulls_current < -0.05:
            score -= 0.20   # Bulls below zero → Bearish

        # Current bears power
        if r.bears_current < -0.08 and r.bears_slope < 0:
            score -= 0.35   # Bears strong and falling → DOWN
        elif r.bears_current < -0.05 and r.bears_slope > 0:
            score += 0.25   # Bears negative but RISING → Sellers leaving → expect UP bounce
        elif r.bears_current > 0.05:
            score += 0.20   # Bears above zero → Bullish

        return max(-1.0, min(1.0, score))

    def _software_elder_ray(self, candles) -> OscillatorReading:
        """
        Compute Elder-Ray using candle OHLC data directly (software fallback).
        Uses EMA(13) as the baseline:
          Bulls Power = High - EMA(13)  (normalized by ATR)
          Bears Power = Low  - EMA(13)  (normalized by ATR)
        """
        reading = OscillatorReading()

        if len(candles) < 14:
            return reading

        closes = [c.close for c in candles]
        highs  = [c.high  for c in candles]
        lows   = [c.low   for c in candles]

        # Compute EMA(13)
        period = 13
        k = 2.0 / (period + 1)
        ema = sum(closes[:period]) / period
        ema_series = [ema]
        for price in closes[period:]:
            ema = price * k + ema * (1 - k)
            ema_series.append(ema)

        if not ema_series:
            return reading

        # ATR for normalization
        atr_vals = []
        for i in range(1, len(candles)):
            tr = max(candles[i].high - candles[i].low,
                     abs(candles[i].high - candles[i-1].close),
                     abs(candles[i].low  - candles[i-1].close))
            atr_vals.append(tr)
        atr = sum(atr_vals[-14:]) / min(14, len(atr_vals)) if atr_vals else 1.0
        if atr < 0.0001:
            atr = 1.0

        # Compute Bulls and Bears Power for last N candles
        n = min(20, len(ema_series))
        bulls_list = []
        bears_list = []
        for i in range(n):
            idx_ema = len(ema_series) - n + i
            idx_candle = len(candles) - n + i
            if idx_ema < 0 or idx_candle < 0:
                continue
            ema_val = ema_series[idx_ema]
            bp = (highs[idx_candle] - ema_val) / atr   # Bulls Power
            brp = (lows[idx_candle] - ema_val) / atr   # Bears Power
            bulls_list.append(max(-1.0, min(1.0, bp)))
            bears_list.append(max(-1.0, min(1.0, brp)))

        if not bulls_list or not bears_list:
            return reading

        reading.bulls_power = bulls_list
        reading.bears_power = bears_list
        reading.bulls_current = bulls_list[-1]
        reading.bears_current = bears_list[-1]
        reading.bulls_slope = self._compute_slope(bulls_list)
        reading.bears_slope = self._compute_slope(bears_list)

        # Zero-line crosses
        if len(bulls_list) >= 2:
            reading.zero_cross_down = (bulls_list[-2] > 0.05 and bulls_list[-1] < -0.02)
        if len(bears_list) >= 2:
            reading.zero_cross_up   = (bears_list[-2] < -0.05 and bears_list[-1] > 0.02)

        # Divergences
        reading.bulls_divergence, reading.bears_divergence = \
            self._detect_divergence(bulls_list, bears_list, candles)

        # ── Exhaustion detection (IMPROVED) ──
        if len(bulls_list) >= 3:
            # Both shrinking: both converging to zero
            reading.both_shrinking = (
                abs(bulls_list[-1]) < abs(bulls_list[-3]) * 0.5 and
                abs(bears_list[-1]) < abs(bears_list[-3]) * 0.5
            )

        # Single-side exhaustion: Bears Power shrinking toward zero in a downtrend
        # This is the key missed signal — bears LOSING power at bottom of trend
        if len(bears_list) >= 4:
            last4_bears = bears_list[-4:]
            # Bears power is negative (bearish). If it's rising toward zero (becoming
            # less negative), bears are losing strength — exhaustion.
            # Check: is bears_current LESS NEGATIVE than bears 3 bars ago?
            bears_shrinking = (
                abs(last4_bears[-1]) < abs(last4_bears[-4]) * 0.60 and   # shrinking toward 0
                last4_bears[-1] < -0.02 and                     # still negative (in downtrend)
                last4_bears[-1] > last4_bears[-3]               # consistently rising
            )
            if bears_shrinking:
                reading.trend_exhaustion = True   # Bears Power fading = DOWN exhaustion

        if len(bulls_list) >= 4:
            last4_bulls = bulls_list[-4:]
            # Bulls power shrinking toward zero in an uptrend = UP exhaustion
            bulls_top_exhaustion = (
                abs(last4_bulls[-1]) < abs(last4_bulls[-4]) * 0.60 and  # falling toward 0
                last4_bulls[-1] > 0.02 and                      # still positive
                last4_bulls[-1] < last4_bulls[-3]               # consistently falling
            )
            if bulls_top_exhaustion:
                reading.trend_exhaustion = True   # Bulls Power fading = UP exhaustion

        reading.direction_score = self._compute_direction_score(reading)
        if reading.direction_score > 0.15:
            reading.elder_ray_direction = "UP"
        elif reading.direction_score < -0.15:
            reading.elder_ray_direction = "DOWN"

        reading.is_valid = True
        reading.panel_found = False  # software, not screen
        reading.bar_count = len(bulls_list)

        # Cache
        self._last_bulls = list(bulls_list)
        self._last_bears = list(bears_list)

        return reading
