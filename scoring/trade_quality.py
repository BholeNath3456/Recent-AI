# ============================================================
#  TRADE QUALITY — Signal grading system (A+ / A / B / Weak)
#  v3: Confluence-gated, maximum strictness
# ============================================================

import sys
sys.path.insert(0, '.')
from core.signal_result import SignalResult, SignalGrade
from config import SCORING


class TradeQualityGrader:
    """
    Grades signals based on confidence, confluence, and confirmation factors.
    Only A+ grade with 5/7+ confluence is tradeable.

    v3 Changes:
    - A+ requires confluence_count >= 5 (out of 7 voters)
    - All soft rejections now kill the signal (maximum strictness)
    - Only A+ is tradeable (A/B are display-only)
    """

    # Keywords that indicate a HARD rejection (signal should be killed)
    HARD_KEYWORDS = [
        "collapsed", "choppy", "Against higher", "Against strong",
        "fakeout probability", "conflict",
        "opposes", "against", "displacement",
        "confluence_insufficient"   # new: confluence gate failure
    ]

    def grade(self, result: SignalResult) -> SignalResult:
        """Assign a grade to the signal result."""

        # Separate hard vs soft rejections
        hard_rejections = [
            r for r in result.rejection_reasons
            if any(kw in r for kw in self.HARD_KEYWORDS)
        ]
        soft_rejections = [
            r for r in result.rejection_reasons
            if not any(kw in r for kw in self.HARD_KEYWORDS)
        ]

        # Hard rejections -> immediate NO_TRADE
        if hard_rejections:
            result.grade = SignalGrade.NO_TRADE
            return result

        conf = result.confidence
        factors = len(result.entry_factors)
        risks = len(result.risk_flags)
        soft_rej_count = len(soft_rejections)
        confluence = result.confluence_count

        # A+ Setup: high confidence, multiple confirmations, confluence gate
        if (conf >= SCORING.grade_a_plus and
            factors >= 4 and
            risks == 0 and
            soft_rej_count == 0 and
            confluence >= SCORING.min_confluence_voters):
            result.grade = SignalGrade.A_PLUS

        # A Setup: good confidence, decent confirmations (display-only)
        elif (conf >= SCORING.grade_a and
              factors >= 2 and
              soft_rej_count <= 1):
            result.grade = SignalGrade.A

        # B Setup: moderate confidence (display-only, dimmer style)
        elif conf >= SCORING.grade_b and factors >= 1:
            result.grade = SignalGrade.B

        # Weak
        elif conf >= 45:
            result.grade = SignalGrade.WEAK

        else:
            result.grade = SignalGrade.NO_TRADE

        # Maximum strictness: ANY soft rejection downgrades A+/A to B
        # REMOVED: Soft rejections already reduce confidence score. Double-penalizing blocks too many good trades.
        # if soft_rej_count >= 1 and result.grade in (SignalGrade.A_PLUS, SignalGrade.A):
        #     result.grade = SignalGrade.B

        return result
