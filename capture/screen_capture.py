# ============================================================
#  SCREEN CAPTURE — Optimized screen capture with region caching
# ============================================================

import numpy as np
import cv2
import mss
import time
from typing import Optional, Tuple
from collections import deque
import sys
sys.path.insert(0, '.')
from config import CAPTURE


class ScreenCapture:
    """
    High-performance screen capture engine.
    Uses mss for low-latency DirectX capture on Windows.
    NOTE: mss uses thread-local DirectX contexts, so the instance
    must be created in the same thread that calls grab().
    We lazy-init on first grab() to ensure this.
    """

    def __init__(self):
        self._sct = None          # lazy-init in calling thread
        self._monitor = None
        self._fps_times = deque(maxlen=30)

    def _ensure_init(self):
        """Create mss instance on first use (must happen in scanner thread)."""
        if self._sct is None:
            self._sct = mss.mss()
            self._monitor = self._sct.monitors[CAPTURE.monitor_index]

    def grab(self) -> np.ndarray:
        """Capture the full primary monitor and return BGR numpy array."""
        self._ensure_init()
        t0 = time.perf_counter()
        img = self._sct.grab(self._monitor)
        arr = np.array(img)
        bgr = cv2.cvtColor(arr, cv2.COLOR_BGRA2BGR)

        # FPS tracking (keep last 30 frames)
        self._fps_times.append(time.perf_counter() - t0)

        return bgr

    def grab_region(self, x: int, y: int, w: int, h: int) -> np.ndarray:
        """Capture a specific region for faster processing."""
        self._ensure_init()
        monitor = {"top": y, "left": x, "width": w, "height": h}
        img = self._sct.grab(monitor)
        arr = np.array(img)
        return cv2.cvtColor(arr, cv2.COLOR_BGRA2BGR)

    @property
    def avg_capture_ms(self) -> float:
        if not self._fps_times:
            return 0.0
        return (sum(self._fps_times) / len(self._fps_times)) * 1000

    @property
    def fps(self) -> float:
        avg = self.avg_capture_ms
        return 1000.0 / avg if avg > 0 else 0.0

    @property
    def screen_size(self) -> Tuple[int, int]:
        self._ensure_init()
        return self._monitor['width'], self._monitor['height']

    def cleanup(self):
        """Release mss resources."""
        try:
            if self._sct:
                self._sct.close()
        except Exception:
            pass
