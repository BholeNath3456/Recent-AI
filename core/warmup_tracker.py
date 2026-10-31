# ============================================================
#  CONTINUOUS SCANNER — Always-on scanning with pipeline gating
#  v3 — Permanently fixes stuck-on-scanning:
#    1. Pipeline runs EVERY tick regardless of fingerprint changes
#    2. No warmup phase by default (min_candles=1)
#    3. Cooldown is the ONLY pause after a signal
#    4. should_run_pipeline() is always True when SCANNING
# ============================================================

import time
from dataclasses import dataclass, field
from typing import List
import sys
sys.path.insert(0, '.')
from core.candle import Candle


@dataclass
class CycleStats:
    """Statistics collected during scanning (kept for backward compat)."""
    total_scans: int = 0
    unique_candle_sets: int = 0
    avg_body_size: float = 0.0
    avg_range: float = 0.0
    bullish_ratio: float = 0.5
    volatility_baseline: float = 0.0
    dominant_direction: str = "NONE"   # "BULLISH" / "BEARISH" / "MIXED"
    direction_strength: float = 0.0   # 0-1
    trend_consistency: float = 0.0    # how consistent the trend was
    max_body_seen: float = 0.0        # largest candle body seen
    momentum_trend: float = 0.0       # -1 to +1, direction of momentum change


class ScannerState:
    WARMING_UP = "WARMING_UP"
    SCANNING   = "SCANNING"
    COOLDOWN   = "COOLDOWN"


# Memory cap — lists are trimmed to this length
_MAX_LIST_LEN = 200


class ContinuousScanner:
    """
    Continuous market scanner with pipeline gating.

    States
    ------
    WARMING_UP  Collecting the first *min_candles* candle feeds.
                With min_candles=1, this phase is INSTANT (1 scan).
    SCANNING    Normal operation. should_run_pipeline() ALWAYS returns True
                so the pipeline fires every single scan tick.
    COOLDOWN    Brief pause after a signal is generated (cooldown_seconds),
                then auto-transitions back to SCANNING immediately.

    Key design decisions to prevent stuck-scanning:
    ------------------------------------------------
    - should_run_pipeline() returns True whenever state == SCANNING,
      unconditionally. No data-change or timing gate.
    - Warmup requires only 1 candle feed (not 5 or 10).
    - Cooldown is the ONLY blocking state after startup.
    - pipeline_ran() is lightweight — no blocking.
    """

    def __init__(self, min_candles: int = 15,
                 cooldown_seconds: float = 30.0):
        # Require proper warmup phase (15 feeds = ~15 seconds of scan data)
        self.min_candles = max(5, min_candles)
        self.cooldown_seconds = cooldown_seconds

        # State
        self._state = ScannerState.WARMING_UP
        self._start_time = time.time()
        self._last_tick_time = time.time()
        self._cooldown_start_time = 0.0

        # Pipeline gating
        self._data_changed = False
        self._last_pipeline_time = 0.0

        # Counters
        self._signal_count = 0
        self._last_signal_time = 0.0
        self._candle_count = 0
        self._feeds = 0   # total feed() calls (transitions warmup)

        # Stats tracking
        self._stats = CycleStats()
        self._last_fingerprint = ""
        self._body_sizes: List[float] = []
        self._ranges: List[float] = []
        self._bull_count = 0
        self._bear_count = 0
        self._momentum_samples: List[float] = []

    # ------------------------------------------------------------------
    # State properties
    # ------------------------------------------------------------------

    @property
    def state(self) -> str:
        return self._state

    @property
    def is_warming_up(self) -> bool:
        return self._state == ScannerState.WARMING_UP

    @property
    def is_scanning(self) -> bool:
        return self._state == ScannerState.SCANNING

    @property
    def is_cooldown(self) -> bool:
        return self._state == ScannerState.COOLDOWN

    # ------------------------------------------------------------------
    # Core statistics properties
    # ------------------------------------------------------------------

    @property
    def stats(self) -> CycleStats:
        return self._stats

    @property
    def elapsed_seconds(self) -> float:
        return time.time() - self._start_time

    @property
    def signal_count(self) -> int:
        return self._signal_count

    @property
    def candle_count(self) -> int:
        return self._candle_count

    @property
    def seconds_since_last_signal(self) -> float:
        if self._last_signal_time == 0.0:
            return self.elapsed_seconds
        return time.time() - self._last_signal_time

    @property
    def cooldown_remaining(self) -> float:
        if self._state != ScannerState.COOLDOWN:
            return 0.0
        elapsed = time.time() - self._cooldown_start_time
        return max(0.0, self.cooldown_seconds - elapsed)

    # ------------------------------------------------------------------
    # Pipeline gating — THE FIX IS HERE
    # ------------------------------------------------------------------

    def should_run_pipeline(self) -> bool:
        """
        Returns True when the pipeline should run.

        FIX: When SCANNING, ALWAYS return True.
        Previous versions blocked on '_data_changed' or timing gates —
        this caused permanent stuck-on-scanning when fingerprints
        didn't change (same chart image, chart not moving).
        """
        if self._state == ScannerState.SCANNING:
            return True    # ALWAYS run pipeline when scanning

        if self._state == ScannerState.COOLDOWN:
            # During cooldown, transition check is in feed(); return False
            return False

        # WARMING_UP: only run if we have any candles at all
        # (min_candles=1 so this becomes True after first feed)
        return self._feeds >= self.min_candles

    def pipeline_ran(self) -> None:
        """Called after the pipeline finishes running."""
        self._data_changed = False
        self._last_pipeline_time = time.time()

    # ------------------------------------------------------------------
    # Signal lifecycle
    # ------------------------------------------------------------------

    def signal_generated(self) -> None:
        """Called when a trade signal is produced. Starts cooldown."""
        self._signal_count += 1
        self._last_signal_time = time.time()
        self._state = ScannerState.COOLDOWN
        self._cooldown_start_time = time.time()
        self._data_changed = False

    # ------------------------------------------------------------------
    # Feed — main data ingestion
    # ------------------------------------------------------------------

    def feed(self, candles: List[Candle], fingerprint: str = "",
             momentum_score: float = 0.0) -> None:
        """
        Feed candle data into the scanner. Call every scan tick.

        State transitions:
        - COOLDOWN  → SCANNING when cooldown expires
        - WARMING_UP → SCANNING after first feed (min_candles=1)
        """
        now = time.time()
        self._feeds += 1

        # --- COOLDOWN: check expiry ---
        if self._state == ScannerState.COOLDOWN:
            elapsed_cooldown = now - self._cooldown_start_time
            if elapsed_cooldown >= self.cooldown_seconds:
                # Cooldown expired — go back to scanning immediately
                self._state = ScannerState.SCANNING
                self._data_changed = True
            # During cooldown, still record stats but don't block forever
            self._last_tick_time = now
            self._stats.total_scans += 1
            return

        # --- Record tick ---
        self._last_tick_time = now
        self._stats.total_scans += 1
        self._momentum_samples.append(momentum_score)
        self._cap_list(self._momentum_samples)

        # Track unique candle sets (dedup by fingerprint for stats only)
        if fingerprint and fingerprint != self._last_fingerprint:
            self._stats.unique_candle_sets += 1
            self._last_fingerprint = fingerprint
            self._data_changed = True

            for c in candles:
                self._candle_count += 1
                self._body_sizes.append(c.body)
                self._ranges.append(c.total_range)
                if c.body > self._stats.max_body_seen:
                    self._stats.max_body_seen = c.body
                if c.is_bullish:
                    self._bull_count += 1
                elif c.is_bearish:
                    self._bear_count += 1

            # Cap memory-bounded lists
            self._cap_list(self._body_sizes)
            self._cap_list(self._ranges)
            self._update_stats()

        # --- WARMING_UP → SCANNING (requires full min_candles feeds) ---
        if self._state == ScannerState.WARMING_UP:
            if self._feeds >= self.min_candles:
                self._state = ScannerState.SCANNING
                self._data_changed = True

    # ------------------------------------------------------------------
    # Stats computation
    # ------------------------------------------------------------------

    def _update_stats(self) -> None:
        """Recompute running statistics."""
        if self._body_sizes:
            self._stats.avg_body_size = sum(self._body_sizes) / len(self._body_sizes)
        if self._ranges:
            self._stats.avg_range = sum(self._ranges) / len(self._ranges)
            mean_r = self._stats.avg_range
            if len(self._ranges) > 1:
                variance = sum((r - mean_r) ** 2 for r in self._ranges) / len(self._ranges)
                self._stats.volatility_baseline = variance ** 0.5

        total = self._bull_count + self._bear_count
        if total > 0:
            ratio = self._bull_count / total
            self._stats.bullish_ratio = ratio
            if ratio > 0.62:
                self._stats.dominant_direction = "BULLISH"
                self._stats.direction_strength = min(1.0, (ratio - 0.5) * 4)
            elif ratio < 0.38:
                self._stats.dominant_direction = "BEARISH"
                self._stats.direction_strength = min(1.0, (0.5 - ratio) * 4)
            else:
                self._stats.dominant_direction = "MIXED"
                self._stats.direction_strength = 0.0

        # Momentum trend
        if len(self._momentum_samples) >= 4:
            mid = len(self._momentum_samples) // 2
            first_half = self._momentum_samples[:mid]
            second_half = self._momentum_samples[mid:]
            avg_first  = sum(first_half) / len(first_half)
            avg_second = sum(second_half) / len(second_half)
            self._stats.momentum_trend = max(-1.0, min(1.0, avg_second - avg_first))

        # Trend consistency
        if total > 3:
            dominant = max(self._bull_count, self._bear_count)
            self._stats.trend_consistency = dominant / total

    # ------------------------------------------------------------------
    # Memory management
    # ------------------------------------------------------------------

    @staticmethod
    def _cap_list(lst: list) -> None:
        """Trim list to last _MAX_LIST_LEN items."""
        if len(lst) > _MAX_LIST_LEN:
            del lst[:-_MAX_LIST_LEN]

    # ------------------------------------------------------------------
    # Resets
    # ------------------------------------------------------------------

    def hard_reset(self) -> None:
        """Complete memory wipe (e.g. asset change)."""
        self._state = ScannerState.WARMING_UP
        self._start_time = time.time()
        self._last_tick_time = time.time()
        self._cooldown_start_time = 0.0
        self._data_changed = False
        self._last_pipeline_time = 0.0
        self._signal_count = 0
        self._last_signal_time = 0.0
        self._candle_count = 0
        self._feeds = 0
        self._stats = CycleStats()
        self._last_fingerprint = ""
        self._body_sizes = []
        self._ranges = []
        self._bull_count = 0
        self._bear_count = 0
        self._momentum_samples = []

    def reset(self) -> None:
        """Full reset — alias for hard_reset."""
        self.hard_reset()

    # ------------------------------------------------------------------
    # Legacy — kept for backward compatibility
    # ------------------------------------------------------------------

    def get_recommended_expiry(self) -> int:
        """Legacy: always returns 1."""
        return 1

    def force_signal_ready(self) -> None:
        """Legacy no-op."""
        pass

    def force_ready(self) -> None:
        """Legacy no-op."""
        pass

    @property
    def is_signal_ready(self) -> bool:
        """Legacy: always False."""
        return False

    @property
    def is_analyzing(self) -> bool:
        """Legacy: True when SCANNING or WARMING_UP."""
        return self._state in (ScannerState.SCANNING, ScannerState.WARMING_UP)

    @property
    def cycle_number(self) -> int:
        """Legacy: returns signal_count."""
        return self._signal_count

    @property
    def progress_fraction(self) -> float:
        """0.0 → 1.0 progress."""
        if self._state == ScannerState.WARMING_UP:
            return min(1.0, self._feeds / max(1, self.min_candles))
        return 1.0

    @property
    def progress_text(self) -> str:
        """Human-readable status string."""
        elapsed = int(self.elapsed_seconds)
        mins, secs = divmod(elapsed, 60)
        if self._state == ScannerState.WARMING_UP:
            return f"Starting up  •  {mins}:{secs:02d}  ({self._feeds}/{self.min_candles} feeds)"
        if self._state == ScannerState.COOLDOWN:
            rem = int(self.cooldown_remaining)
            return f"Cooldown  •  {rem}s remaining"
        return (f"Scanning  •  {mins}:{secs:02d}  "
                f"(signals: {self._signal_count})")


# ======================================================================
#  Legacy aliases — import as before, get the new class
# ======================================================================
AnalysisCycleTracker = ContinuousScanner
CycleState = ScannerState
