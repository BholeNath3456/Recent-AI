# ============================================================
#  SIGNAL RESULT — Output of the signal engine
#  v3: Added confluence fields, fixed trade duration
# ============================================================

from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional
import time


class SignalGrade(Enum):
    A_PLUS  = "A+"
    A       = "A"
    B       = "B"
    WEAK    = "Weak"
    NO_TRADE = "No Trade"


@dataclass
class SignalResult:
    """Complete signal output from the engine pipeline."""

    # Direction
    direction: Optional[str] = None    # "UP" / "DOWN" / None

    # Probabilities (sum to ~1.0)
    prob_up: float = 0.0
    prob_down: float = 0.0
    prob_no_trade: float = 1.0

    # Confidence (0-100)
    confidence: float = 0.0

    # Grade
    grade: SignalGrade = SignalGrade.NO_TRADE

    # Reasons
    reasons: List[str] = field(default_factory=list)

    # Entry factors (what confirmed the signal)
    entry_factors: List[str] = field(default_factory=list)

    # Risk flags (what could go wrong)
    risk_flags: List[str] = field(default_factory=list)

    # Rejection reasons (why signal was blocked, if applicable)
    rejection_reasons: List[str] = field(default_factory=list)

    # Factor scores (for ML training)
    factor_scores: dict = field(default_factory=dict)

    # Metadata
    timestamp: float = field(default_factory=time.time)
    timeframe: str = "1m"

    # ML adjustment
    ml_adjustment: float = 0.0  # how much ML shifted confidence

    # Trade expiry — fixed by user selection (1, 2, 3, or 5 minutes)
    expiry_minutes: int = 1

    # ── Confluence fields (v3) ──
    confluence_count: int = 0           # how many of 8 voters agree (0-8)
    confluence_details: List[str] = field(default_factory=list)  # which voters agreed

    @property
    def is_tradeable(self) -> bool:
        """Signals with sufficient confluence are tradeable."""
        from config import SCORING
        return (self.grade in (SignalGrade.A_PLUS, SignalGrade.A, SignalGrade.B) and
                self.confluence_count >= SCORING.min_confluence_voters)

    @property
    def is_displayable(self) -> bool:
        """True for A+, A, and B grades (B shown with dimmer style)."""
        return self.grade in (SignalGrade.A_PLUS, SignalGrade.A, SignalGrade.B)

    @property
    def display_direction(self) -> str:
        """Signal format: '1 MIN UP' / '2 MIN DOWN' etc."""
        if not self.is_tradeable:
            return "WAIT"
        if not self.direction:
            return "WAIT"
        return f"{self.expiry_minutes} MIN {self.direction}"

    @property
    def arrow(self) -> str:
        if self.direction == "UP":
            return "▲"
        elif self.direction == "DOWN":
            return "▼"
        return "●"

    @property
    def confluence_label(self) -> str:
        """Human-readable confluence: '5/8', '6/8', '7/8', '8/8'"""
        return f"{self.confluence_count}/8"

    def to_dict(self) -> dict:
        """Serialize for journal / backtesting."""
        return {
            'timestamp':     self.timestamp,
            'direction':     self.direction,
            'confidence':    round(self.confidence, 1),
            'grade':         self.grade.value,
            'prob_up':       round(self.prob_up, 3),
            'prob_down':     round(self.prob_down, 3),
            'prob_no_trade': round(self.prob_no_trade, 3),
            'reasons':       self.reasons,
            'entry_factors': self.entry_factors,
            'risk_flags':    self.risk_flags,
            'rejection_reasons': self.rejection_reasons,
            'factor_scores': {k: round(v, 3) for k, v in self.factor_scores.items()},
            'ml_adjustment': round(self.ml_adjustment, 3),
            'timeframe':     self.timeframe,
            'expiry_minutes': self.expiry_minutes,
            'confluence_count': self.confluence_count,
            'confluence_details': self.confluence_details,
        }
