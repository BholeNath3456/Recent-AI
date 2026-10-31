"""
Complete Japanese Candlestick Pattern Database — AI Training Dataset
====================================================================
Total Patterns: 80
Features: 12 per pattern
Generated: 2026-07-08T23:53:39.261155

Feature Engineering:
  - Categorical variables → numerical encoding
  - Scores normalized to 0.0-1.0
  - Binary flags for pattern type (reversal/continuation/indecision)
  - Labels: Bullish=1, Neutral=0, Bearish=-1

Usage:
    from candlestick_patterns_ai_training import (
        X_train, y_train, feature_names, pattern_names,
        X_directional, y_binary,
        PATTERN_LOOKUP, get_pattern_vector, get_similar_patterns
    )
    from sklearn.ensemble import GradientBoostingClassifier
    clf = GradientBoostingClassifier(n_estimators=100, max_depth=4)
    clf.fit(X_train, y_train)
"""

import numpy as np

feature_names = ["num_category", "num_candles", "sentiment_encoded", "direction_encoded", "trend_required_encoded", "reliability_encoded", "gap_encoded", "confidence_normalized", "probability_normalized", "is_reversal", "is_continuation", "is_indecision"]

feature_descriptions = {
    "num_category": "Pattern category (1=Single, 2=Two, 3=Three, 4=Four, 5=Five candle)",
    "num_candles": "Number of candles in the pattern",
    "sentiment_encoded": "Sentiment (1=Bullish, 0=Neutral, -1=Bearish)",
    "direction_encoded": "Expected direction (1=UP, 0.5=CONT_UP, 0=INDECISION, -0.5=CONT_DOWN, -1=DOWN)",
    "trend_required_encoded": "Required prior trend (1=Uptrend, 0=Any/None, -1=Downtrend)",
    "reliability_encoded": "Reliability (3=High, 2=Medium, 1=Low)",
    "gap_encoded": "Gap requirement (0=None, 1=Optional, 2=Preferred, 3=Required)",
    "confidence_normalized": "Confidence score (0.0-1.0)",
    "probability_normalized": "Probability score (0.0-1.0)",
    "is_reversal": "Is reversal pattern (1=yes, 0=no)",
    "is_continuation": "Is continuation pattern (1=yes, 0=no)",
    "is_indecision": "Is indecision pattern (1=yes, 0=no)",
}

X_train = np.array([[1, 1, 1, 1.0, -1, 2, 0, 0.6, 0.6, 1, 0, 0], [1, 1, 1, 1.0, -1, 1, 0, 0.45, 0.55, 1, 0, 0], [1, 1, -1, -1.0, 1, 2, 1, 0.55, 0.55, 1, 0, 0], [1, 1, -1, -1.0, 1, 2, 2, 0.6, 0.6, 1, 0, 0], [1, 1, 0, 0.0, 0, 1, 0, 0.35, 0.5, 0, 0, 1], [1, 1, 1, 1.0, -1, 2, 0, 0.6, 0.6, 1, 0, 0], [1, 1, -1, -1.0, 1, 2, 0, 0.6, 0.6, 1, 0, 0], [1, 1, 0, 0.0, 0, 1, 0, 0.3, 0.5, 0, 0, 1], [1, 1, 0, 0.0, 0, 1, 0, 0.1, 0.5, 0, 0, 1], [1, 1, 0, 0.0, 0, 1, 0, 0.3, 0.5, 0, 0, 1], [1, 1, 0, 0.0, 0, 1, 0, 0.3, 0.5, 0, 0, 1], [1, 1, 1, 0.5, 0, 3, 0, 0.75, 0.65, 0, 1, 0], [1, 1, -1, -0.5, 0, 3, 0, 0.75, 0.65, 0, 1, 0], [1, 1, 0, 0.0, 0, 1, 0, 0.3, 0.5, 0, 0, 1], [1, 1, 1, 1.0, -1, 2, 2, 0.55, 0.6, 1, 0, 0], [1, 1, -1, -1.0, 1, 2, 2, 0.55, 0.6, 1, 0, 0], [2, 2, 1, 1.0, -1, 3, 2, 0.75, 0.68, 1, 0, 0], [2, 2, -1, -1.0, 1, 3, 2, 0.75, 0.68, 1, 0, 0], [2, 2, 1, 1.0, -1, 2, 0, 0.55, 0.55, 1, 0, 0], [2, 2, -1, -1.0, 1, 2, 0, 0.55, 0.55, 1, 0, 0], [2, 2, 1, 1.0, -1, 2, 0, 0.6, 0.58, 1, 0, 0], [2, 2, -1, -1.0, 1, 2, 0, 0.6, 0.58, 1, 0, 0], [2, 2, 1, 1.0, -1, 2, 2, 0.62, 0.6, 1, 0, 0], [2, 2, -1, -1.0, 1, 2, 2, 0.62, 0.6, 1, 0, 0], [2, 2, -1, -1.0, 1, 2, 0, 0.55, 0.55, 1, 0, 0], [2, 2, 1, 1.0, -1, 2, 0, 0.55, 0.55, 1, 0, 0], [2, 2, -1, -1.0, 1, 1, 0, 0.4, 0.48, 1, 0, 0], [2, 2, 1, 1.0, -1, 1, 0, 0.4, 0.48, 1, 0, 0], [2, 2, 1, 1.0, -1, 1, 0, 0.42, 0.5, 1, 0, 0], [2, 2, 1, 1.0, -1, 1, 2, 0.42, 0.5, 1, 0, 0], [2, 2, -1, -1.0, 1, 1, 2, 0.42, 0.5, 1, 0, 0], [2, 2, 1, 0.5, 1, 2, 0, 0.55, 0.58, 0, 1, 0], [2, 2, -1, -0.5, -1, 2, 0, 0.55, 0.58, 0, 1, 0], [2, 2, 1, 1.0, -1, 2, 2, 0.52, 0.55, 1, 0, 0], [2, 2, -1, -1.0, 1, 2, 2, 0.52, 0.55, 1, 0, 0], [2, 2, 1, 1.0, 0, 3, 3, 0.8, 0.72, 1, 0, 0], [2, 2, -1, -1.0, 0, 3, 3, 0.8, 0.72, 1, 0, 0], [2, 2, -1, -0.5, -1, 2, 2, 0.55, 0.58, 0, 1, 0], [2, 2, -1, -0.5, -1, 2, 2, 0.5, 0.55, 0, 1, 0], [2, 2, -1, -0.5, -1, 1, 2, 0.45, 0.52, 0, 1, 0], [3, 3, -1, -1.0, 1, 2, 3, 0.55, 0.58, 1, 0, 0], [2, 2, 1, 0.5, 1, 2, 3, 0.6, 0.6, 0, 1, 0], [2, 2, -1, -0.5, -1, 2, 3, 0.6, 0.6, 0, 1, 0], [3, 3, 1, 1.0, -1, 3, 2, 0.78, 0.72, 1, 0, 0], [3, 3, -1, -1.0, 1, 3, 2, 0.78, 0.72, 1, 0, 0], [3, 3, 1, 1.0, -1, 3, 2, 0.8, 0.75, 1, 0, 0], [3, 3, -1, -1.0, 1, 3, 2, 0.8, 0.75, 1, 0, 0], [3, 3, 1, 1.0, -1, 3, 3, 0.85, 0.78, 1, 0, 0], [3, 3, -1, -1.0, 1, 3, 3, 0.85, 0.78, 1, 0, 0], [3, 3, 1, 1.0, -1, 3, 0, 0.75, 0.7, 1, 0, 0], [3, 3, -1, -1.0, 1, 3, 0, 0.75, 0.7, 1, 0, 0], [3, 3, 1, 1.0, -1, 3, 0, 0.7, 0.65, 1, 0, 0], [3, 3, -1, -1.0, 1, 3, 0, 0.7, 0.65, 1, 0, 0], [3, 3, 1, 1.0, -1, 3, 0, 0.72, 0.68, 1, 0, 0], [3, 3, -1, -1.0, 1, 3, 0, 0.72, 0.68, 1, 0, 0], [3, 3, 1, 1.0, -1, 3, 3, 0.75, 0.7, 1, 0, 0], [3, 3, -1, -1.0, 1, 3, 3, 0.75, 0.7, 1, 0, 0], [3, 3, 1, 1.0, -1, 2, 0, 0.55, 0.58, 1, 0, 0], [3, 3, 1, 1.0, -1, 1, 0, 0.45, 0.5, 1, 0, 0], [3, 3, -1, -1.0, 1, 2, 3, 0.58, 0.6, 1, 0, 0], [3, 3, -1, -1.0, 1, 3, 0, 0.75, 0.72, 1, 0, 0], [3, 3, -1, -1.0, 1, 1, 1, 0.45, 0.5, 1, 0, 0], [3, 3, -1, -1.0, 1, 2, 0, 0.55, 0.55, 1, 0, 0], [3, 3, 1, 1.0, -1, 1, 0, 0.42, 0.48, 1, 0, 0], [4, 4, 1, 1.0, -1, 2, 3, 0.55, 0.58, 1, 0, 0], [3, 3, 1, 0.5, 1, 2, 3, 0.52, 0.55, 0, 1, 0], [3, 3, -1, -0.5, -1, 2, 3, 0.5, 0.55, 0, 1, 0], [3, 3, 1, 0.5, 1, 2, 3, 0.58, 0.6, 0, 1, 0], [3, 3, -1, -0.5, -1, 2, 3, 0.58, 0.6, 0, 1, 0], [3, 3, 1, 0.5, 1, 1, 3, 0.48, 0.52, 0, 1, 0], [3, 3, -1, -0.5, -1, 1, 3, 0.48, 0.52, 0, 1, 0], [5, 5, 1, 0.5, 1, 3, 0, 0.78, 0.72, 0, 1, 0], [5, 5, -1, -0.5, -1, 3, 0, 0.77, 0.71, 0, 1, 0], [5, 5, 1, 1.0, -1, 2, 3, 0.62, 0.6, 1, 0, 0], [5, 5, -1, -1.0, 1, 2, 3, 0.6, 0.58, 1, 0, 0], [5, 5, 1, 0.5, 1, 3, 3, 0.8, 0.74, 0, 1, 0], [4, 4, 1, 1.0, -1, 2, 0, 0.65, 0.63, 1, 0, 0], [4, 4, -1, -1.0, 1, 2, 0, 0.63, 0.61, 1, 0, 0], [5, 5, 1, 1.0, -1, 2, 2, 0.63, 0.62, 1, 0, 0], [5, 5, -1, -1.0, 1, 2, 2, 0.61, 0.6, 1, 0, 0]])

y_train = np.array([1, 1, -1, -1, 0, 1, -1, 0, 0, 0, 0, 1, -1, 0, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, -1, 1, -1, 1, 1, 1, -1, 1, -1, 1, -1, 1, -1, -1, -1, -1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, 1, -1, -1, -1, -1, 1, 1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, 1, -1, 1, -1])

direction_labels = np.array([1.0, 1.0, -1.0, -1.0, 0.0, 1.0, -1.0, 0.0, 0.0, 0.0, 0.0, 0.5, -0.5, 0.0, 1.0, -1.0, 1.0, -1.0, 1.0, -1.0, 1.0, -1.0, 1.0, -1.0, -1.0, 1.0, -1.0, 1.0, 1.0, 1.0, -1.0, 0.5, -0.5, 1.0, -1.0, 1.0, -1.0, -0.5, -0.5, -0.5, -1.0, 0.5, -0.5, 1.0, -1.0, 1.0, -1.0, 1.0, -1.0, 1.0, -1.0, 1.0, -1.0, 1.0, -1.0, 1.0, -1.0, 1.0, 1.0, -1.0, -1.0, -1.0, -1.0, 1.0, 1.0, 0.5, -0.5, 0.5, -0.5, 0.5, -0.5, 0.5, -0.5, 1.0, -1.0, 0.5, 1.0, -1.0, 1.0, -1.0])

pattern_names = ["Hammer", "Inverted Hammer", "Hanging Man", "Shooting Star", "Doji", "Dragonfly Doji", "Gravestone Doji", "Long-Legged Doji", "Four Price Doji", "Bullish Spinning Top", "Bearish Spinning Top", "Bullish Marubozu", "Bearish Marubozu", "High Wave Candle", "Bullish Belt Hold", "Bearish Belt Hold", "Bullish Engulfing", "Bearish Engulfing", "Bullish Harami", "Bearish Harami", "Bullish Harami Cross", "Bearish Harami Cross", "Piercing Pattern", "Dark Cloud Cover", "Tweezer Top", "Tweezer Bottom", "Matching High", "Matching Low", "Homing Pigeon", "Bullish Meeting Lines", "Bearish Meeting Lines", "Bullish Separating Lines", "Bearish Separating Lines", "Bullish Counterattack", "Bearish Counterattack", "Bullish Kicking", "Bearish Kicking", "On Neck Line", "In Neck Line", "Thrusting Pattern", "Two Crows", "Rising Window", "Falling Window", "Morning Star", "Evening Star", "Morning Doji Star", "Evening Doji Star", "Bullish Abandoned Baby", "Bearish Abandoned Baby", "Three White Soldiers", "Three Black Crows", "Three Inside Up", "Three Inside Down", "Three Outside Up", "Three Outside Down", "Bullish Tri-Star", "Bearish Tri-Star", "Three Stars in the South", "Unique Three River Bottom", "Upside Gap Two Crows", "Identical Three Crows", "Deliberation", "Advance Block", "Stick Sandwich", "Concealing Baby Swallow", "Bullish Side-by-Side White Lines", "Bearish Side-by-Side White Lines", "Upside Tasuki Gap", "Downside Tasuki Gap", "Upside Gap Three Methods", "Downside Gap Three Methods", "Rising Three Methods", "Falling Three Methods", "Bullish Breakaway", "Bearish Breakaway", "Mat Hold", "Bullish Three Line Strike", "Bearish Three Line Strike", "Ladder Bottom", "Ladder Top"]

# ── Directional subset (excludes neutral patterns) ───────────

_bull_mask = y_train == 1
_bear_mask = y_train == -1
_dir_mask = _bull_mask | _bear_mask

X_directional = X_train[_dir_mask]
y_directional = y_train[_dir_mask]
y_binary = (_bull_mask[_dir_mask]).astype(int)  # 1=Bullish/UP, 0=Bearish/DOWN


# ── Pattern lookup ────────────────────────────────────────────

PATTERN_LOOKUP = {name: vec.tolist() for name, vec in zip(pattern_names, X_train)}


def get_pattern_vector(name: str) -> np.ndarray:
    """Get feature vector for a named pattern."""
    if name in PATTERN_LOOKUP:
        return np.array(PATTERN_LOOKUP[name])
    raise KeyError(f"Pattern '{name}' not found in database")


def get_similar_patterns(vector: np.ndarray, top_k: int = 5) -> list:
    """Find most similar patterns by cosine similarity."""
    from numpy.linalg import norm
    sims = []
    for i, row in enumerate(X_train):
        n1, n2 = norm(vector), norm(row)
        cos_sim = np.dot(vector, row) / (n1 * n2 + 1e-8) if n1 > 0 and n2 > 0 else 0.0
        sims.append((pattern_names[i], float(cos_sim)))
    sims.sort(key=lambda x: x[1], reverse=True)
    return sims[:top_k]


# ── Summary ───────────────────────────────────────────────────

if __name__ == "__main__":
    print("AI Training Dataset Summary")
    print("=" * 40)
    print(f"Total patterns:     {len(X_train)}")
    print(f"Features/pattern:   {X_train.shape[1]}")
    print(f"Bullish patterns:   {int(np.sum(y_train == 1))}")
    print(f"Bearish patterns:   {int(np.sum(y_train == -1))}")
    print(f"Neutral patterns:   {int(np.sum(y_train == 0))}")
    print(f"\nDirectional subset: {len(X_directional)}")
    print(f"  UP (1):  {int(np.sum(y_binary == 1))}")
    print(f"  DOWN (0): {int(np.sum(y_binary == 0))}")
    print(f"\nFeature names: {feature_names}")
