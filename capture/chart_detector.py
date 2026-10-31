# ============================================================
#  CHART DETECTOR — Finds Olymp Trade chart region on screen
#  v3: Added validate_region() to detect window-switch scenarios
# ============================================================

import numpy as np
import cv2
from typing import Optional, Tuple
import sys
sys.path.insert(0, '.')
from config import CAPTURE

# Minimum fraction of candle-colored pixels required in a valid chart region.
# Real charts have dense candle pixels; oscillator bars (Bears/Bulls Power) have very few.
# Raised from 0.0010 to 0.0050 (0.50%) to prevent IDE windows from passing detection.
_MIN_CANDLE_PIXEL_FRACTION = 0.0050  # 0.50% of region pixels


class ChartDetector:
    """
    Detects the candlestick chart area on the Olymp Trade platform
    using HSV colour density analysis.
    Caches the detected region and re-detects periodically.

    v3: validates cached region every scan to detect window switches.
    """

    def __init__(self):
        self._cached_region: Optional[Tuple[int, int, int, int]] = None
        self._scan_count: int = 0
        self._fail_count: int = 0

    def detect(self, bgr_img: np.ndarray, force: bool = False) -> Optional[Tuple[int, int, int, int]]:
        """
        Detect chart region. Returns (x, y, w, h) or None.
        Uses cached region unless force=True or cache expired,
        BUT always validates the cached region still contains chart content.
        """
        self._scan_count += 1

        # If we have a cache, validate it still shows a chart
        if self._cached_region is not None and not force:
            if not self._validate_region(bgr_img, self._cached_region):
                # User switched windows — cached region is stale
                self._cached_region = None
                self._fail_count += 1
                return None

            # Cache is valid AND not expired — use it
            if self._scan_count % CAPTURE.region_cache_scans != 0:
                return self._cached_region

        # Full re-detection
        region = self._find_chart(bgr_img)

        if region is not None:
            self._cached_region = region
            self._fail_count = 0
        else:
            self._fail_count += 1
            # After 3 consecutive failures, clear cache
            if self._fail_count > 3:
                self._cached_region = None

        return region

    def _validate_region(self, bgr_img: np.ndarray,
                         region: Tuple[int, int, int, int]) -> bool:
        """
        Quick validation: does the cached region still contain enough
        candle-colored (green + red) pixels to be a real chart?
        Returns False if the region looks like a non-chart window.
        """
        x, y, cw, ch = region
        h_img, w_img = bgr_img.shape[:2]

        # Bounds check (screen resolution might have changed)
        if x + cw > w_img or y + ch > h_img:
            return False

        roi = bgr_img[y:y+ch, x:x+cw]
        hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

        green_mask = cv2.inRange(hsv, CAPTURE.green_low, CAPTURE.green_high)
        red_mask = (cv2.inRange(hsv, CAPTURE.red_low1, CAPTURE.red_high1) |
                    cv2.inRange(hsv, CAPTURE.red_low2, CAPTURE.red_high2))

        candle_pixels = cv2.countNonZero(green_mask) + cv2.countNonZero(red_mask)
        total_pixels = cw * ch
        fraction = candle_pixels / max(1, total_pixels)

        # Real charts have candle pixels between 0.3% and 32% of total area.
        # > 32% red/green coverage means it's a colorful photo/wallpaper (e.g., sunset/mountains/clouds).
        if fraction < _MIN_CANDLE_PIXEL_FRACTION or fraction > 0.32:
            return False

        # Check background uniformity: real trading charts have a solid, uniform background color.
        # A desktop wallpaper/photo has massive variance, so no single color dominates > 45%.
        gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
        counts = np.bincount(gray.flatten())
        mode_val = counts.argmax()
        # Count pixels within a small +/- 2 intensity range of the most common background color
        uniform_pixels = np.sum(counts[max(0, mode_val-2):min(256, mode_val+3)])
        uniformity_fraction = uniform_pixels / max(1, total_pixels)
        
        if uniformity_fraction < 0.45:
            # If no single background color covers at least 45% of the window, it's a photo/wallpaper!
            return False

        return True

    def _find_chart(self, bgr_img: np.ndarray) -> Optional[Tuple[int, int, int, int]]:
        """Core detection: find largest cluster of red/green candle pixels."""
        h, w = bgr_img.shape[:2]
        hsv = cv2.cvtColor(bgr_img, cv2.COLOR_BGR2HSV)

        # Build combined candle mask (green + red)
        green_mask = cv2.inRange(hsv, CAPTURE.green_low, CAPTURE.green_high)
        red_mask = (cv2.inRange(hsv, CAPTURE.red_low1, CAPTURE.red_high1) |
                    cv2.inRange(hsv, CAPTURE.red_low2, CAPTURE.red_high2))
        candle_mask = cv2.bitwise_or(green_mask, red_mask)

        # CRITICAL FIX: Exclude Olymp Trade UI panels!
        # The left panel (Active Trades) takes ~30% of the screen.
        # The right panel (Up/Down buttons) takes ~20% of the screen.
        # If we don't mask these out, the giant red/green buttons are extracted as the most recent candles,
        # completely destroying momentum calculations and firing false signals.
        x_min_allowed = int(w * 0.30)
        x_max_allowed = int(w * 0.80)
        candle_mask[:, :x_min_allowed] = 0
        candle_mask[:, x_max_allowed:] = 0

        pts = cv2.findNonZero(candle_mask)
        if pts is None or len(pts) < 2000:
            return None

        x, y, cw, ch = cv2.boundingRect(pts)
        if cw < (w * 0.15) or ch < (h * 0.15):
            return None

        # Exclude top header (5%) and bottom trade buttons/footer (10%)
        y_max_allowed = int(h * 0.90)
        y_min_allowed = int(h * 0.05)
        
        y_end = min(y + ch, y_max_allowed)
        y = max(y, y_min_allowed)
        ch = max(100, y_end - y)

        # Add horizontal padding
        pad = 15
        x  = max(0, x - pad)
        cw = min(w - x, cw + 2 * pad)

        candidate_region = (x, y, cw, ch)
        if not self._validate_region(bgr_img, candidate_region):
            return None

        return candidate_region

    @property
    def is_chart_found(self) -> bool:
        return self._cached_region is not None

    @property
    def chart_region(self) -> Optional[Tuple[int, int, int, int]]:
        return self._cached_region

    def reset(self):
        """Force re-detection on next call."""
        self._cached_region = None
        self._scan_count = 0
        self._fail_count = 0
