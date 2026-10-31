# ============================================================
#  TRADE JOURNAL — Trade logging and statistics
# ============================================================

import os
import json
import time
from typing import List, Dict, Optional
import sys
sys.path.insert(0, '.')
from core.signal_result import SignalResult
from config import TRADE


class TradeJournal:
    """
    JSON-based trade journal. Logs signals and tracks outcomes.
    Provides win-rate statistics by grade, pattern, trend state, etc.
    """

    def __init__(self):
        self.entries: List[dict] = []
        self._load()

    def log_signal(self, result: SignalResult, timeframe: str = None):
        """Log a signal to the journal."""
        entry = result.to_dict()
        entry['timeframe'] = timeframe or TRADE.primary_timeframe
        entry['outcome'] = None       # filled in later
        entry['outcome_time'] = None
        self.entries.append(entry)
        self._save()

    def record_outcome(self, index: int, won: bool):
        """Record win/loss for a journal entry."""
        if 0 <= index < len(self.entries):
            self.entries[index]['outcome'] = 'win' if won else 'loss'
            self.entries[index]['outcome_time'] = time.time()
            self._save()

    def get_stats(self) -> dict:
        """Calculate comprehensive statistics."""
        completed = [e for e in self.entries if e.get('outcome')]
        if not completed:
            return {'total': 0, 'win_rate': 0, 'completed': 0}

        wins = sum(1 for e in completed if e['outcome'] == 'win')
        total = len(completed)

        # By grade
        by_grade = {}
        for e in completed:
            g = e.get('grade', 'Unknown')
            if g not in by_grade:
                by_grade[g] = {'wins': 0, 'total': 0}
            by_grade[g]['total'] += 1
            if e['outcome'] == 'win':
                by_grade[g]['wins'] += 1

        for g in by_grade:
            by_grade[g]['rate'] = (by_grade[g]['wins'] / by_grade[g]['total'] * 100
                                   if by_grade[g]['total'] > 0 else 0)

        # By direction
        by_dir = {}
        for e in completed:
            d = e.get('direction', 'None')
            if d not in by_dir:
                by_dir[d] = {'wins': 0, 'total': 0}
            by_dir[d]['total'] += 1
            if e['outcome'] == 'win':
                by_dir[d]['wins'] += 1

        # Today's stats
        today_start = time.time() - 86400
        today = [e for e in completed if e.get('timestamp', 0) > today_start]
        today_wins = sum(1 for e in today if e['outcome'] == 'win')

        # Current streak
        streak = 0
        streak_type = None
        for e in reversed(completed):
            if streak_type is None:
                streak_type = e['outcome']
                streak = 1
            elif e['outcome'] == streak_type:
                streak += 1
            else:
                break

        return {
            'total': len(self.entries),
            'completed': total,
            'wins': wins,
            'losses': total - wins,
            'win_rate': round(wins / total * 100, 1) if total > 0 else 0,
            'by_grade': by_grade,
            'by_direction': by_dir,
            'today_total': len(today),
            'today_wins': today_wins,
            'today_rate': round(today_wins / len(today) * 100, 1) if today else 0,
            'streak': streak,
            'streak_type': streak_type or 'none',
        }

    def _save(self):
        try:
            os.makedirs(os.path.dirname(TRADE.journal_path), exist_ok=True)
            with open(TRADE.journal_path, 'w') as f:
                json.dump(self.entries[-500:], f, indent=2)  # keep last 500
        except Exception:
            pass

    def _load(self):
        try:
            if os.path.exists(TRADE.journal_path):
                with open(TRADE.journal_path, 'r') as f:
                    self.entries = json.load(f)
        except Exception:
            self.entries = []
