import asyncio
import numpy as np
import cv2
import time
import difflib
from typing import Tuple
import re

try:
    from winsdk.windows.media.ocr import OcrEngine
    from winsdk.windows.graphics.imaging import BitmapPixelFormat, SoftwareBitmap
    from winsdk.windows.storage.streams import DataWriter
    HAS_WINSDK = True
except ImportError:
    HAS_WINSDK = False


class AssetMonitor:
    """
    Continuously monitors the top-left section of the screen (next to the '+' icon)
    to detect if the user has switched the active trading asset.
    """

    def __init__(self):
        self.engine = OcrEngine.try_create_from_user_profile_languages() if HAS_WINSDK else None
        self.current_asset = ""
        self._last_check_time = 0.0
        self._loop = None

    def check_asset(self, bgr_img: np.ndarray) -> Tuple[bool, str]:
        """
        Reads the asset name from the screen.
        Returns (has_changed, new_asset_name).
        To save CPU, we only run OCR every 1.0 second.
        """
        if not HAS_WINSDK or self.engine is None:
            return False, self.current_asset

        now = time.time()
        if now - self._last_check_time < 1.0:
            return False, self.current_asset

        self._last_check_time = now

        h_img, w_img = bgr_img.shape[:2]
        roi = bgr_img[0:150, 0:500]

        gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(gray, 160, 255, cv2.THRESH_BINARY)
        bgra = cv2.cvtColor(thresh, cv2.COLOR_GRAY2BGRA)
        
        try:
            if self._loop is None or self._loop.is_closed():
                self._loop = asyncio.new_event_loop()
            raw_lines = self._loop.run_until_complete(self._do_ocr_lines(bgra))
            
            # Filter empty lines and ignore tiny garbage strings
            lines = [l.strip() for l in raw_lines if len(l.strip()) > 3]
            
            if len(lines) > 0:
                new_asset = lines[0] # The first line is the asset name
                
                # Strip out common OCR noise, prices, or trailing percentages
                new_asset = re.sub(r'[0-9\.]+', '', new_asset).strip()
                new_asset = re.sub(r'\b[a-zA-Z]\b', '', new_asset).strip() # Remove single letters like 'v' or 'x'
                # Strip OTC badges and common OCR hallucination words
                new_asset = re.sub(r'\b(OTC|OTCI|OT|orc|Trad|Composite|Index)\b', '', new_asset, flags=re.IGNORECASE).strip()
                
                if "FT" in new_asset:
                    new_asset = new_asset.split("FT")[0].strip()
                if "%" in new_asset:
                    new_asset = new_asset.split("%")[0].strip()
                    
                if self.current_asset == "":
                    self.current_asset = new_asset
                    return False, new_asset
                
                # Fuzzy match: if it's 80%+ similar, it's just an OCR glitch, treat as identical
                similarity = difflib.SequenceMatcher(None, self.current_asset, new_asset).ratio()
                
                # Substring check: if one is a substantial part of the other ("USD/CAD" vs "USD/CAD OTC")
                is_substring = False
                if len(new_asset) >= 4 and len(self.current_asset) >= 4:
                    if new_asset in self.current_asset or self.current_asset in new_asset:
                        is_substring = True
                
                if similarity < 0.80 and not is_substring:
                    # Debounce: Ensure it's not a temporary glitch. Must be seen 3 times.
                    if not hasattr(self, '_candidate_asset'):
                        self._candidate_asset = new_asset
                        self._candidate_count = 1
                    else:
                        cand_sim = difflib.SequenceMatcher(None, self._candidate_asset, new_asset).ratio()
                        if cand_sim > 0.85:
                            self._candidate_count += 1
                        else:
                            self._candidate_asset = new_asset
                            self._candidate_count = 1
                        
                    # If we see the new asset 3 times in a row, confirm the change
                    if self._candidate_count >= 3:
                        self.current_asset = self._candidate_asset
                        self._candidate_count = 0
                        return True, self.current_asset
                else:
                    self._candidate_count = 0
                    
        except Exception as e:
            pass

        return False, self.current_asset

    async def _do_ocr(self, bgra_np: np.ndarray) -> str:
        h, w = bgra_np.shape[:2]
        bitmap = SoftwareBitmap(BitmapPixelFormat.BGRA8, w, h)
        writer = DataWriter()
        writer.write_bytes(bgra_np.flatten().tobytes())
        buf = writer.detach_buffer()
        bitmap.copy_from_buffer(buf)
        res = await self.engine.recognize_async(bitmap)
        return res.text
        
    async def _do_ocr_lines(self, bgra_np: np.ndarray) -> list:
        h, w = bgra_np.shape[:2]
        bitmap = SoftwareBitmap(BitmapPixelFormat.BGRA8, w, h)
        writer = DataWriter()
        writer.write_bytes(bgra_np.flatten().tobytes())
        buf = writer.detach_buffer()
        bitmap.copy_from_buffer(buf)
        res = await self.engine.recognize_async(bitmap)
        return [line.text for line in res.lines]

if __name__ == "__main__":
    # Test script
    monitor = AssetMonitor()
    print("Asset Monitor initialized:", monitor.engine is not None)
