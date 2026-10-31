# ============================================================
#  MARKET CONTEXT — Aggregated state of current market conditions
# ============================================================

from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional, Tuple


class TrendState(Enum):
    STRONG_BULLISH = "Strong Bullish"
    BULLISH        = "Bullish"
    SIDEWAYS       = "Sideways"
    BEARISH        = "Bearish"
    STRONG_BEARISH = "Strong Bearish"


class VolatilityRegime(Enum):
    EXPANDING    = "Expanding"
    NORMAL       = "Normal"
    COMPRESSING  = "Compressing"
    COLLAPSED    = "Collapsed"


class MarketRegime(Enum):
    TRENDING     = "Trending"
    RANGING      = "Ranging"
    VOLATILE     = "Volatile"
    QUIET        = "Quiet"
    TRANSITIONAL = "Transitional"


class StructureState(Enum):
    BULLISH_STRUCTURE = "Bullish Structure"    # HH + HL
    BEARISH_STRUCTURE = "Bearish Structure"    # LH + LL
    BROKEN_BULLISH    = "BOS Bullish"          # break of bearish structure
    BROKEN_BEARISH    = "BOS Bearish"          # break of bullish structure
    CHOCH_BULLISH     = "CHOCH Bullish"        # change of character to bullish
    CHOCH_BEARISH     = "CHOCH Bearish"        # change of character to bearish
    UNCLEAR           = "Unclear"


@dataclass
class SwingPoint:
    """A confirmed swing high or swing low."""
    index: int
    price: float
    is_high: bool  # True = swing high, False = swing low
    strength: float = 1.0  # how many bars confirmed the swing


@dataclass
class SupportResistance:
    """A support or resistance level with strength."""
    price: float
    strength: float       # 0-1, based on number of touches and reactions
    is_support: bool
    touch_count: int = 1


@dataclass
class LiquidityZone:
    """Area where stop orders are likely clustered."""
    price_low: float
    price_high: float
    side: str  # 'above' or 'below'
    strength: float = 1.0


@dataclass
class MarketContext:
    """
    Aggregated market state computed each scan cycle.
    All engines write their results here; the confidence engine reads from it.
    """
    # Trend
    trend_state: TrendState = TrendState.SIDEWAYS
    trend_strength: float = 0.0        # 0-1
    ema_values: dict = field(default_factory=dict)   # {period: value}
    ema_slopes: dict = field(default_factory=dict)   # {period: slope}
    ema_alignment: str = "neutral"     # "bullish" / "bearish" / "neutral"

    # Market structure
    structure_state: StructureState = StructureState.UNCLEAR
    swing_points: List[SwingPoint] = field(default_factory=list)
    last_bos: Optional[str] = None     # "bullish" / "bearish"
    last_choch: Optional[str] = None

    # Volatility
    volatility_regime: VolatilityRegime = VolatilityRegime.NORMAL
    atr_value: float = 0.0
    atr_ratio: float = 1.0            # current ATR / average ATR
    is_compressed: bool = False
    is_choppy: bool = False

    # Momentum
    momentum_score: float = 0.0        # -1 (bearish) to +1 (bullish)
    momentum_acceleration: float = 0.0 # positive = accelerating
    is_exhausted: bool = False

    # Support / Resistance
    sr_levels: List[SupportResistance] = field(default_factory=list)
    nearest_support: float = 0.0
    nearest_resistance: float = 0.0
    price_at_sr: bool = False          # True if price is near S/R

    # Liquidity
    liquidity_zones: List[LiquidityZone] = field(default_factory=list)
    liquidity_sweep_detected: bool = False
    sweep_direction: Optional[str] = None  # "bullish" / "bearish"

    # Price action
    supply_zones: list = field(default_factory=list)
    demand_zones: list = field(default_factory=list)
    order_blocks: list = field(default_factory=list)

    # Regime
    market_regime: MarketRegime = MarketRegime.QUIET

    # Pattern
    active_patterns: list = field(default_factory=list)

    # MTF
    htf_trend: TrendState = TrendState.SIDEWAYS
    mtf_aligned: bool = False
    mtf_conflict: bool = False

    # ── Elder-Ray Oscillator (Bulls Power / Bears Power) ──
    # Populated by oscillator_extractor in the main scan loop
    elder_ray_direction: Optional[str] = None   # "UP", "DOWN", or None
    elder_ray_score: float = 0.0                # -1.0 (bear) to +1.0 (bull)
    elder_ray_bulls_current: float = 0.0        # latest Bulls Power value
    elder_ray_bears_current: float = 0.0        # latest Bears Power value
    elder_ray_bulls_divergence: bool = False     # bearish divergence (price up, bulls down)
    elder_ray_bears_divergence: bool = False     # bullish divergence (price down, bears up)
    elder_ray_zero_cross_up: bool = False        # Bears crossed above zero → buy
    elder_ray_zero_cross_down: bool = False      # Bulls crossed below zero → sell
    elder_ray_exhaustion: bool = False           # both powers shrinking → no trade
    elder_ray_valid: bool = False                # was oscillator data available?

    # ── Williams %R (computed from candle OHLC data — no screen needed) ──
    williams_r: float = -50.0          # Williams %R line (-100 to 0)
    williams_r_zone: str = 'neutral'   # 'overbought' | 'oversold' | 'neutral'
    williams_r_valid: bool = False     # enough candles to compute?

    def should_block_signal(self) -> bool:
        """Quick check if market conditions should block signals entirely."""
        return (
            self.volatility_regime == VolatilityRegime.COLLAPSED or
            self.is_choppy or
            self.mtf_conflict
        )

    @property
    def regime_label(self) -> str:
        return self.market_regime.value

    @property
    def trend_label(self) -> str:
        return self.trend_state.value
