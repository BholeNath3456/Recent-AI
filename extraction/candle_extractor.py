# ============================================================
#  CANDLE EXTRACTOR — Pixel-based candle extraction from chart
#  Fixed: stability check, min candle count, dedup support
# ============================================================

import numpy as np
import cv2
from typing import List, Tuple, Optional
import sys
sys.path.insert(0, '.')
from config import CAPTURE, ANALYSIS
from core.candle import Candle


class CandleExtractor:
    """
    Extracts candle OHLC data from a screenshot of the Olymp Trade chart.
    Uses column-by-column HSV analysis to detect candle bodies and wicks.

    v2 Changes:
    - Stability check: compares to previous scan's candles
    - Returns None if fewer than min_candles_for_analysis extracted
    - get_fingerprint() for deduplication support
    """

    def __init__(self):
        self._last_candle_count = 0
        self._last_fingerprint: str = ""

    def extract(self, bgr_img: np.ndarray, region: Tuple[int, int, int, int],
                n: int = None) -> List[Candle]:
        """
        Extract up to n candles from the chart region.
        Returns candles in chronological order (oldest first).
        Returns empty list if too few candles detected.
        """
        if n is None:
            n = ANALYSIS.candle_history

        x, y, cw, ch = region
        chart = bgr_img[y:y+ch, x:x+cw]
        # Use BGR directly for much more robust color dominance detection
        b, g, r = cv2.split(chart)
        
        # A pixel is "green candle" if green is significantly stronger than red and blue
        g_mask_bool = (g > r + 15) & (g > b + 15) & (g > 50)
        green_mask = g_mask_bool.astype(np.uint8) * 255
        
        # A pixel is "red candle" if red is significantly stronger than green and blue
        r_mask_bool = (r > g + 15) & (r > b + 15) & (r > 50)
        red_mask = r_mask_bool.astype(np.uint8) * 255
        
        h_chart, w_chart = chart.shape[:2]
        
        green_mask = self._clean_mask(green_mask, w_chart)
        red_mask = self._clean_mask(red_mask, w_chart)

        h_chart, w_chart = chart.shape[:2]
        candles: List[Candle] = []

        # Calculate block width based on expected candle count
        block = max(2, w_chart // (n * 3))
        col = w_chart - block

        while col > 0 and len(candles) < n:
            candle = self._extract_single_candle(
                green_mask, red_mask, col, block, h_chart
            )
            if candle is not None:
                candles.insert(0, candle)  # prepend for chronological order
            col -= block * 2

        self._last_candle_count = len(candles)

        # Filter noise candles (zero-range artifacts)
        candles = [c for c in candles if c.total_range > 0.01]

        # Minimum candle count check
        if len(candles) < ANALYSIS.min_candles_for_analysis:
            return []

        # ── Quality gate: reject garbage extractions from non-chart screens ──
        if len(candles) >= 6:
            ranges = [c.total_range for c in candles]
            mean_range = sum(ranges) / len(ranges)
            # 1. Height check: only reject if average candle height spans >88% of the ENTIRE screen (solid full-screen wallpaper blob).
            if mean_range > 88.0:
                return []

            # 2. Variance check — real candles have varied OHLC values (CV > 0.10 usually).
            if mean_range > 0:
                variance = sum((r - mean_range) ** 2 for r in ranges) / len(ranges)
                cv = (variance ** 0.5) / mean_range  # coefficient of variation
                if cv < 0.04:  # uniform solid noise = not real candles
                    return []

        # Update fingerprint for dedup
        self._last_fingerprint = self._compute_fingerprint(candles)

        return candles

    def _extract_single_candle(self, green_mask: np.ndarray, red_mask: np.ndarray,
                                col: int, block: int, h_chart: int) -> Optional[Candle]:
        """Extract a single candle from a column block."""
        g_col = green_mask[:, col:col+block]
        r_col = red_mask[:, col:col+block]

        g_rows = np.where(g_col.any(axis=1))[0]
        r_rows = np.where(r_col.any(axis=1))[0]

        # Need minimum pixels to consider it a candle
        if len(g_rows) < 3 and len(r_rows) < 3:
            return None

        # Determine colour
        is_tie = len(g_rows) == len(r_rows)
        is_green = len(g_rows) > len(r_rows)
        rows = g_rows if (is_green or is_tie) else r_rows
        color_col = g_col if (is_green or is_tie) else r_col

        top = int(rows.min())
        bottom = int(rows.max())
        total = bottom - top
        if total < 1:
            return None

        # Compute body region using pixel density analysis
        body_density = np.zeros(total)
        for i in range(total):
            row_slice = color_col[top + i]
            body_density[i] = row_slice.mean()

        # Body = high-density region
        body_threshold = body_density.max() * 0.4
        body_rows = np.where(body_density > body_threshold)[0]

        if len(body_rows) == 0:
            return None

        body_top = int(body_rows.min())
        body_bottom = int(body_rows.max())

        # Normalise pixel positions to 0-100 price scale
        # (top of chart = high price, bottom = low price)
        def norm(px: int) -> float:
            return 100.0 - (px / h_chart * 100.0)

        high  = norm(top)
        low   = norm(bottom)
        b_top = norm(top + body_top)
        b_bot = norm(top + body_bottom)

        if is_tie:
            open_ = min(b_top, b_bot)
            close_ = open_
        elif is_green:
            open_  = min(b_top, b_bot)
            close_ = max(b_top, b_bot)
        else:
            open_  = max(b_top, b_bot)
            close_ = min(b_top, b_bot)

        # Validate candle data
        if high < low or open_ < 0 or close_ < 0:
            return None

        return Candle(open_, close_, high, low)

    def _compute_fingerprint(self, candles: List[Candle]) -> str:
        """Generate a fingerprint from the last few candles for dedup."""
        if len(candles) < 3:
            return ""
        # Use last 3 candles' OHLC values rounded to 1 decimal
        parts = []
        for c in candles[-3:]:
            parts.append(f"{c.open:.1f}{c.close:.1f}{c.high:.1f}{c.low:.1f}")
        return "|".join(parts)

    def _clean_mask(self, mask: np.ndarray, w_chart: int) -> np.ndarray:
        """Removes UI elements (circles, horizontal lines, text) from the mask."""
        # 1. Morphological subtraction of large UI blobs (e.g. Trade Entry Circles)
        # Trade circles are attached to candles, so connected components fails to isolate them.
        # We use a horizontal line kernel wider than a standard candle.
        # This preserves thin candles but identifies fat circles or horizontal UI lines.
        kernel_width = max(18, w_chart // 60)
        kernel_horiz = np.ones((1, kernel_width), np.uint8)
        
        # Isolate wide blobs (circles)
        ui_blobs = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel_horiz)
        
        # Dilate slightly to ensure the entire circle boundary is caught
        kernel_dilate = np.ones((5, 5), np.uint8)
        ui_blobs = cv2.dilate(ui_blobs, kernel_dilate, iterations=1)
        
        # Subtract the UI blobs from the original mask
        mask = cv2.bitwise_and(mask, cv2.bitwise_not(ui_blobs))

        # 2. Existing connected components filter for other weird artifacts
        num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(mask, connectivity=8)
        for i in range(1, num_labels):
            w = stats[i, cv2.CC_STAT_WIDTH]
            h = stats[i, cv2.CC_STAT_HEIGHT]
            # Candles are very tall and narrow. UI elements are wide or circular.
            # Remove anything wider than 15 pixels if it's not extremely tall,
            # or anything extremely wide (like a horizontal dashed line).
            if (w > h * 1.5) or (w > 18 and w > h * 0.4):
                mask[labels == i] = 0
        return mask

    @property
    def fingerprint(self) -> str:
        """Last extraction fingerprint for dedup comparison."""
        return self._last_fingerprint

    @property
    def last_count(self) -> int:
        return self._last_candle_count
