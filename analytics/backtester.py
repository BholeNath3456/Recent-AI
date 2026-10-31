# ============================================================
#  BACKTESTER — Historical replay and accuracy analytics
# ============================================================

import json
import os
from typing import List, Dict, Optional
import sys
sys.path.insert(0, '.')
from core.candle import Candle
from core.signal_result import SignalResult, SignalGrade
from config import TRADE


class Backtester:
    """
    Replays stored candle sequences through the signal engine
    and computes accuracy metrics.
    """

    def __init__(self):
        self.results: List[dict] = []

    def run(self, candle_sequences: List[List[Candle]], engine_pipeline,
            lookahead: int = 3) -> dict:
        """
        Run backtest on candle sequences.
        engine_pipeline: callable(candles) -> SignalResult
        lookahead: candles to check for outcome
        """
        self.results = []

        for seq in candle_sequences:
            if len(seq) < 20 + lookahead:
                continue

            # Slide a window through the sequence
            for i in range(20, len(seq) - lookahead):
                window = seq[:i]
                future = seq[i:i+lookahead]

                try:
                    result = engine_pipeline(window)
                except Exception:
                    continue

                if not result.is_tradeable:
                    continue

                # Determine outcome: did price move in predicted direction?
                entry_price = window[-1].close
                if result.direction == "UP":
                    won = any(c.close > entry_price for c in future)
                elif result.direction == "DOWN":
                    won = any(c.close < entry_price for c in future)
                else:
                    continue

                self.results.append({
                    'direction': result.direction,
                    'confidence': result.confidence,
                    'grade': result.grade.value,
                    'reasons': result.reasons[:3],
                    'outcome': 'win' if won else 'loss',
                    'index': i,
                })

        return self.get_report()

    def get_report(self) -> dict:
        """Generate backtest report."""
        if not self.results:
            return {'total': 0, 'message': 'No tradeable signals found'}

        total = len(self.results)
        wins = sum(1 for r in self.results if r['outcome'] == 'win')

        # By grade
        by_grade = {}
        for r in self.results:
            g = r['grade']
            if g not in by_grade:
                by_grade[g] = {'wins': 0, 'total': 0}
            by_grade[g]['total'] += 1
            if r['outcome'] == 'win':
                by_grade[g]['wins'] += 1

        for g in by_grade:
            by_grade[g]['rate'] = round(
                by_grade[g]['wins'] / by_grade[g]['total'] * 100, 1
            )

        # By direction
        by_dir = {}
        for r in self.results:
            d = r['direction']
            if d not in by_dir:
                by_dir[d] = {'wins': 0, 'total': 0}
            by_dir[d]['total'] += 1
            if r['outcome'] == 'win':
                by_dir[d]['wins'] += 1

        # By confidence range
        by_conf = {'high': {'w': 0, 't': 0}, 'medium': {'w': 0, 't': 0}}
        for r in self.results:
            bucket = 'high' if r['confidence'] >= 80 else 'medium'
            by_conf[bucket]['t'] += 1
            if r['outcome'] == 'win':
                by_conf[bucket]['w'] += 1

        return {
            'total': total,
            'wins': wins,
            'losses': total - wins,
            'win_rate': round(wins / total * 100, 1),
            'by_grade': by_grade,
            'by_direction': by_dir,
            'by_confidence': by_conf,
        }

    def save_results(self, path: str = None):
        """Save backtest results to JSON."""
        path = path or TRADE.backtest_data_path.replace('.json', '_results.json')
        try:
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, 'w') as f:
                json.dump({'results': self.results, 'report': self.get_report()}, f, indent=2)
        except Exception:
            pass
