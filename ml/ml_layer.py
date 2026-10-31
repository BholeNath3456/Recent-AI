# ============================================================
#  ML LAYER — scikit-learn probability adjustment (v3)
#  Added: directional features, cross-validation, data persistence,
#         confluence features (voter count + gate)
# ============================================================

import os
import sys
import json
import numpy as np
sys.path.insert(0, '.')
from core.signal_result import SignalResult
from config import ML

try:
    from sklearn.ensemble import GradientBoostingClassifier
    from sklearn.model_selection import cross_val_score
    import joblib
    HAS_SKLEARN = True
except ImportError:
    HAS_SKLEARN = False

# Path to persist training data
_TRAINING_DATA_PATH = "data/ml_training_data.json"


class MLLayer:
    """
    Machine learning probability layer.
    - Cold-start: uses heuristic weights until enough training data
    - After min_training_samples: trains GBT to classify good vs bad setups
    - Adjusts confidence scores from the confidence engine

    v2 Changes:
    - Added directional features (trend dir, momentum dir, candle dir balance)
    - Cross-validation scoring during training for accuracy estimate
    - Training data persisted to disk across restarts
    - GradientBoosting instead of RandomForest for better signal quality
    """

    def __init__(self):
        self.model = None
        self.is_trained = False
        self.training_data: list = []
        self.cv_score: float = 0.0  # cross-validation accuracy
        self._load_training_data()
        self._load_model()

    def adjust(self, result: SignalResult) -> SignalResult:
        """Apply ML adjustment to the signal result."""
        if not ML.enabled:
            return result

        features = self._extract_features(result)
        if features is None:
            return result

        if self.is_trained and self.model is not None:
            try:
                X = np.array([features])
                proba = self.model.predict_proba(X)[0]
                # proba[0] = bad setup, proba[1] = good setup
                good_prob = proba[1] if len(proba) > 1 else 0.5
                # Adjust confidence: blend ML opinion with engine score
                ml_adj = (good_prob - 0.5) * 20  # -10 to +10 adjustment
                result.confidence = max(0, min(95, result.confidence + ml_adj))
                result.ml_adjustment = ml_adj
            except Exception:
                pass  # Fall back to unadjusted
        else:
            # Cold-start heuristic: penalise low-quality factor combos
            result.ml_adjustment = self._heuristic_adjustment(result)
            result.confidence = max(0, min(95, result.confidence + result.ml_adjustment))

        return result

    def add_training_sample(self, result: SignalResult, outcome: bool):
        """Add a labeled sample (signal + win/loss outcome)."""
        features = self._extract_features(result)
        if features is None:
            return
        self.training_data.append({
            'features': features,
            'label': 1 if outcome else 0,
            'direction': result.direction,
            'confidence': result.confidence,
            'grade': result.grade.value,
        })
        self._save_training_data()

        # Auto-retrain when enough new data
        if (len(self.training_data) >= ML.min_training_samples and
            len(self.training_data) % ML.retrain_interval == 0):
            self.train()

    def train(self):
        """Train the ML model on accumulated data."""
        if not HAS_SKLEARN or len(self.training_data) < ML.min_training_samples:
            return

        X = np.array([d['features'] for d in self.training_data])
        y = np.array([d['label'] for d in self.training_data])

        # Use GradientBoosting for better signal quality
        self.model = GradientBoostingClassifier(
            n_estimators=100,
            max_depth=4,
            learning_rate=0.1,
            random_state=ML.random_state,
            subsample=0.8,
        )

        # Cross-validation to estimate real accuracy
        try:
            cv_scores = cross_val_score(self.model, X, y, cv=5, scoring='accuracy')
            self.cv_score = float(np.mean(cv_scores))
            print(f"[ML] Cross-validation accuracy: {self.cv_score:.1%} "
                  f"(±{np.std(cv_scores):.1%})")
        except Exception:
            self.cv_score = 0.0

        self.model.fit(X, y)
        self.is_trained = True
        self._save_model()
        print(f"[ML] Model trained on {len(self.training_data)} samples. "
              f"CV accuracy: {self.cv_score:.1%}")

    def get_status(self) -> dict:
        """Get ML layer status for display."""
        return {
            'is_trained': self.is_trained,
            'samples': len(self.training_data),
            'cv_score': self.cv_score,
            'min_required': ML.min_training_samples,
        }

    def _extract_features(self, result: SignalResult) -> list:
        """Extract feature vector from signal result (v3: +directional & confluence features, 16 total)."""
        scores = result.factor_scores
        if not scores:
            return None

        # Base features (same as v1)
        base = [
            scores.get('trend_alignment', 0),
            scores.get('momentum_quality', 0),
            scores.get('candle_strength', 0),
            scores.get('structure_confirmation', 0),
            scores.get('sr_reaction', 0),
            scores.get('wick_rejection', 0),
            scores.get('volatility_quality', 0),
            scores.get('breakout_confirmation', 0),
            scores.get('exhaustion_probability', 0),
            scores.get('liquidity_sweep', 0),
        ]

        # v2 NEW: Directional features
        # Direction encoding: UP=1, DOWN=-1, None=0
        dir_val = 1.0 if result.direction == "UP" else (-1.0 if result.direction == "DOWN" else 0.0)
        base.append(dir_val)

        # Probability spread (how confident is the direction)
        prob_spread = result.prob_up - result.prob_down
        base.append(prob_spread)

        # Number of entry factors and risk flags
        base.append(min(1.0, len(result.entry_factors) / 5.0))
        base.append(min(1.0, len(result.risk_flags) / 3.0))

        # v3 NEW: Confluence features
        confluence_count = getattr(result, 'confluence_count', 0)
        base.append(confluence_count / 7.0)  # normalised voter count (0.0–1.0)
        base.append(1.0 if confluence_count >= 5 else 0.0)  # binary confluence gate

        return base

    def _heuristic_adjustment(self, result: SignalResult) -> float:
        """Cold-start: direction-aware heuristic penalty/bonus."""
        scores = result.factor_scores
        direction = result.direction  # "UP" or "DOWN"
        adj = 0.0
        
        # Check directional agreement
        high_scores = sum(1 for v in scores.values() if v > 0.5)
        
        # Direction-aware check: trend should agree with signal
        dir_agree = 0
        if direction == "UP":
            if scores.get('trend_alignment', 0) > 0.5: dir_agree += 1
            if scores.get('momentum_quality', 0) > 0.5 and result.prob_up > result.prob_down: dir_agree += 1
        elif direction == "DOWN":
            if scores.get('trend_alignment', 0) > 0.5: dir_agree += 1  
            if scores.get('momentum_quality', 0) > 0.5 and result.prob_down > result.prob_up: dir_agree += 1
        
        if high_scores >= 5 and dir_agree >= 2:
            adj += 2.0
        elif high_scores >= 3 and dir_agree >= 2:
            adj += 1.0
        elif dir_agree < 1:
            adj -= 3.0
        
        risk_count = len(result.risk_flags)
        adj -= risk_count * 3.0
        
        return max(-10.0, min(8.0, adj))

    def _save_model(self):
        """Save trained model to disk."""
        if not HAS_SKLEARN or self.model is None:
            return
        try:
            os.makedirs(os.path.dirname(ML.model_path), exist_ok=True)
            joblib.dump(self.model, ML.model_path)
        except Exception:
            pass

    def _load_model(self):
        """Load previously trained model."""
        if not HAS_SKLEARN:
            return
        try:
            if os.path.exists(ML.model_path):
                self.model = joblib.load(ML.model_path)
                self.is_trained = True
        except Exception:
            self.model = None
            self.is_trained = False

    def _save_training_data(self):
        """Persist training data to disk."""
        try:
            os.makedirs(os.path.dirname(_TRAINING_DATA_PATH), exist_ok=True)
            with open(_TRAINING_DATA_PATH, 'w') as f:
                json.dump(self.training_data[-1000:], f)  # keep last 1000
        except Exception:
            pass

    def _load_training_data(self):
        """Load training data from disk."""
        try:
            if os.path.exists(_TRAINING_DATA_PATH):
                with open(_TRAINING_DATA_PATH, 'r') as f:
                    self.training_data = json.load(f)
        except Exception:
            self.training_data = []
