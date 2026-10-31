# ============================================================
#  CONFIGURATION — Advanced Quantitative Trading Signal Engine
#  All tunable constants in one place
# ============================================================

import numpy as np
from dataclasses import dataclass, field
from typing import List

# ─────────────────────────────────────────────
#  CAPTURE CONFIG
# ─────────────────────────────────────────────
@dataclass
class CaptureConfig:
    scan_interval: float = 1.0           # seconds between scans (full pipeline per scan)
    region_cache_scans: int = 10         # re-detect chart region every N scans
    monitor_index: int = 1               # primary monitor

    # HSV colour ranges for Olymp Trade DARK theme
    green_hsv_low:  tuple = (40,  80,  80)
    green_hsv_high: tuple = (85, 255, 255)
    red_hsv_low1:   tuple = (0,   80,  80)
    red_hsv_high1:  tuple = (10, 255, 255)
    red_hsv_low2:   tuple = (160, 80,  80)
    red_hsv_high2:  tuple = (180, 255, 255)

    @property
    def green_low(self):  return np.array(self.green_hsv_low)
    @property
    def green_high(self): return np.array(self.green_hsv_high)
    @property
    def red_low1(self):   return np.array(self.red_hsv_low1)
    @property
    def red_high1(self):  return np.array(self.red_hsv_high1)
    @property
    def red_low2(self):   return np.array(self.red_hsv_low2)
    @property
    def red_high2(self):  return np.array(self.red_hsv_high2)


# ─────────────────────────────────────────────
#  ANALYSIS CONFIG
# ─────────────────────────────────────────────
@dataclass
class AnalysisConfig:
    candle_history: int = 50            # increased from 30 for more analysis data
    ema_periods: List[int] = field(default_factory=lambda: [8, 13, 21])
    atr_period: int = 14
    swing_lookback: int = 5             # bars to confirm swing highs / lows
    structure_lookback: int = 15        # bars for market structure analysis
    momentum_lookback: int = 5
    volatility_lookback: int = 14
    compression_threshold: float = 0.4  # ATR ratio below which = compression
    noise_threshold: float = 0.15       # body-to-range ratio below = noise
    sideways_ema_slope: float = 0.002   # EMA slope below = sideways
    min_body_ratio: float = 0.25        # minimum body/range for a "real" candle
    exhaustion_streak: int = 4          # consecutive same-colour for exhaustion
    sr_cluster_tolerance: float = 0.5   # % range for S/R clustering
    min_candles_for_analysis: int = 8   # minimum candles needed for reliable analysis


# ─────────────────────────────────────────────
#  SCORING CONFIG
# ─────────────────────────────────────────────
@dataclass
class ScoringConfig:
    # Weighted factors for confidence calculation (must sum to 1.0)
    # Rebalanced: reduced wick_rejection (was always ~0.93), increased structure
    weights: dict = field(default_factory=lambda: {
        'trend_alignment':       0.25,
        'momentum_quality':      0.18,
        'candle_strength':       0.10,
        'structure_confirmation': 0.15,
        'sr_reaction':           0.10,
        'wick_rejection':        0.02,
        'volatility_quality':    0.08,
        'breakout_confirmation': 0.04,
        'exhaustion_probability': 0.03,
        'liquidity_sweep':       0.03,
        'immediate_pressure':    0.02,
    })

    # ── Signal Grading Thresholds ──
    grade_a_plus: float = 85.0          # Only the absolute best setups
    grade_a:      float = 75.0
    grade_b:      float = 65.0
    # Below grade_b = Weak; blocked by validator = No Trade

    # Minimum confidence to display any signal
    min_display_confidence: float = 75.0  # Hyper-sniper strict display limit

    # NO_TRADE bias — uncertainty penalty
    no_trade_bias: float = 0.18

    # Filter thresholds
    max_fake_breakout_prob: float = 0.50
    min_trend_strength: float = 0.35
    min_momentum_strength: float = 0.30
    max_candle_conflict: float = 0.40

    # Anti-spam / deduplication
    signal_cooldown_scans: int = 2
    max_consecutive_same_dir: int = 4

    # ── CONTINUOUS SCANNING — Confluence Gate ──
    min_confluence_voters: int = 8        # out of 10 voters must agree (Hyper-Sniper Mode)
    min_confidence_threshold: float = 75.0   # minimum confidence to fire
    signal_cooldown_seconds: float = 120.0   # 2 minutes between signals (Ultra-Strict Cooldown)
    min_candles_before_signal: int = 15      # require warmup to establish trend data


# ─────────────────────────────────────────────
#  UI CONFIG
# ─────────────────────────────────────────────
@dataclass
class UIConfig:
    width: int = 340
    height: int = 520
    bg_color: str = "#0a0a0f"
    panel_color: str = "#12121a"
    accent_cyan: str = "#00f0ff"
    accent_magenta: str = "#ff00ff"
    accent_green: str = "#00ff88"
    accent_red: str = "#ff1744"
    accent_gold: str = "#ffd700"
    accent_orange: str = "#ff8c00"
    text_primary: str = "#e0e0e0"
    text_secondary: str = "#888888"
    text_dim: str = "#555555"
    font_family: str = "Segoe UI"
    opacity: float = 0.93
    position_offset_x: int = 20   # from right edge
    position_offset_y: int = 30   # from top


# ─────────────────────────────────────────────
#  ML CONFIG
# ─────────────────────────────────────────────
@dataclass
class MLConfig:
    enabled: bool = True
    min_training_samples: int = 200
    retrain_interval: int = 50    # retrain after N new journal entries
    model_path: str = "data/ml_model.pkl"
    feature_count: int = 16
    random_state: int = 42


# ─────────────────────────────────────────────
#  TRADE CONFIG
# ─────────────────────────────────────────────
@dataclass
class TradeConfig:
    # Supported timeframes and their trade durations (duration matches TF)
    supported_timeframes: dict = field(default_factory=lambda: {
        "1m": 1, "2m": 2, "3m": 3, "5m": 5
    })
    primary_timeframe: str = "1m"       # default active timeframe
    journal_path: str = "data/journal.json"
    backtest_data_path: str = "data/backtest_candles.json"

    # Fixed trade duration (set via --duration CLI flag, default 1 minute)
    fixed_duration_minutes: int = 1

    @property
    def duration_minutes(self) -> int:
        """Trade duration — fixed by user selection."""
        return self.fixed_duration_minutes


# ─────────────────────────────────────────────
#  OSCILLATOR CONFIG (Elder-Ray Bulls/Bears Power)
# ─────────────────────────────────────────────
@dataclass
class OscillatorConfig:
    # Panel detection
    panel_search_fraction: float = 0.60   # search up to 60% below chart bottom
    min_bar_height_px: int = 3            # ignore bars shorter than N pixels (noise)
    min_color_density: float = 0.003      # min fraction of colored pixels for valid panel
    max_color_density: float = 0.35       # max fraction (above = it's the main chart)

    # Signal thresholds
    bulls_positive_threshold: float = 0.05   # bulls_current must exceed this to count UP
    bears_negative_threshold: float = -0.05  # bears_current must be below this to count DN
    divergence_lookback: int = 5             # candles to look back for divergence
    slope_threshold: float = 0.03           # min change to be considered "rising/falling"

    # Scoring weights in confidence engine
    elder_ray_weight: float = 0.30          # fraction of confidence score from Elder-Ray
    divergence_penalty: float = 0.40        # probability penalty when divergence detected
    zero_cross_boost: float = 0.50          # probability boost on zero-line cross

    # Hard rejection
    hard_reject_divergence: bool = True     # block signal on Elder-Ray divergence
    hard_reject_direction_mismatch: bool = True  # block if elder_ray dir != signal dir


# ─────────────────────────────────────────────
#  GLOBAL CONFIG INSTANCES
# ─────────────────────────────────────────────
CAPTURE    = CaptureConfig()
ANALYSIS   = AnalysisConfig()
SCORING    = ScoringConfig()
UI         = UIConfig()
ML         = MLConfig()
TRADE      = TradeConfig()
OSCILLATOR = OscillatorConfig()


# Legacy alias — some modules may still reference CYCLE
# Provides a minimal stub to prevent import errors during transition
class _CycleStub:
    min_cycle_seconds = 60.0
    max_cycle_seconds = 120.0
    min_unique_candles = 5
    cooldown_seconds = SCORING.signal_cooldown_seconds

CYCLE = _CycleStub()
