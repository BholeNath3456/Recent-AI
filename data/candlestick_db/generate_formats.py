#!/usr/bin/env python3
"""
Candlestick Pattern Database — Format Generator
================================================
Generates all 6 output formats from the master pattern database.

Outputs:
    1. CSV               → output/candlestick_patterns.csv
    2. JSON              → output/candlestick_patterns.json
    3. SQL               → output/candlestick_patterns.sql
    4. Python Dictionary → output/candlestick_patterns_dict.py
    5. Pandas DataFrame  → output/candlestick_patterns_dataframe.py
    6. AI Training       → output/candlestick_patterns_ai_training.py

Usage:
    cd d:/Signal/data/candlestick_db
    python generate_formats.py
"""

import csv
import json
import os
import sys
from datetime import datetime

# ═══════════════════════════════════════════════════════════════
#  LOAD PATTERN DATA FROM ALL MODULES
# ═══════════════════════════════════════════════════════════════

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from single_candle_patterns import PATTERNS as SINGLE_PATTERNS
from two_candle_patterns import PATTERNS as TWO_PATTERNS
from three_candle_patterns import PATTERNS as THREE_PATTERNS
from multi_candle_patterns import PATTERNS as MULTI_PATTERNS

ALL_PATTERNS = SINGLE_PATTERNS + TWO_PATTERNS + THREE_PATTERNS + MULTI_PATTERNS

# Assign sequential IDs
for _i, _p in enumerate(ALL_PATTERNS, 1):
    _p["id"] = _i

TOTAL = len(ALL_PATTERNS)

# ═══════════════════════════════════════════════════════════════
#  CONSTANTS
# ═══════════════════════════════════════════════════════════════

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")
os.makedirs(OUTPUT_DIR, exist_ok=True)

FIELDS = [
    "id", "pattern_name", "alternative_names", "japanese_name",
    "category", "sub_category", "sentiment", "expected_direction",
    "trend_required", "num_candles", "pattern_structure", "candle_by_candle",
    "market_psychology", "confirmation_required", "volume_confirmation",
    "volatility_conditions", "gap_requirement", "reliability",
    "success_rate_range", "failure_conditions", "entry_rules",
    "stop_loss_rules", "take_profit_rules", "risk_reward",
    "best_timeframes", "best_markets", "best_indicators",
    "common_mistakes", "ai_features", "ohlc_relationship",
    "label", "confidence_score", "probability_score"
]

LIST_FIELDS = {
    "alternative_names", "candle_by_candle", "failure_conditions",
    "best_timeframes", "best_markets", "best_indicators",
    "common_mistakes", "ai_features"
}


def _serialize_list(val):
    """Flatten list to pipe-separated string for CSV."""
    if isinstance(val, list):
        return " | ".join(str(v) for v in val)
    return str(val)


def _escape_sql(val):
    """Escape single quotes for SQL."""
    return str(val).replace("'", "''")


# ═══════════════════════════════════════════════════════════════
#  1. CSV FORMAT
# ═══════════════════════════════════════════════════════════════

def generate_csv():
    """Generate CSV file. Lists are pipe-separated within cells."""
    path = os.path.join(OUTPUT_DIR, "candlestick_patterns.csv")
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS, quoting=csv.QUOTE_ALL)
        writer.writeheader()
        for p in ALL_PATTERNS:
            row = {}
            for field in FIELDS:
                val = p.get(field, "")
                row[field] = _serialize_list(val) if field in LIST_FIELDS else val
            writer.writerow(row)
    print(f"  [1/6] CSV:              {path}")
    return path


# ═══════════════════════════════════════════════════════════════
#  2. JSON FORMAT
# ═══════════════════════════════════════════════════════════════

def generate_json():
    """Generate JSON with metadata and all patterns."""
    path = os.path.join(OUTPUT_DIR, "candlestick_patterns.json")
    output = {
        "metadata": {
            "title": "Complete Japanese Candlestick Pattern Database",
            "description": "Exhaustive database for AI/ML trading model training",
            "version": "1.0.0",
            "total_patterns": TOTAL,
            "fields_per_pattern": len(FIELDS),
            "generated_at": datetime.now().isoformat(),
            "categories": sorted(set(p["category"] for p in ALL_PATTERNS)),
            "sentiments": sorted(set(p["sentiment"] for p in ALL_PATTERNS)),
        },
        "patterns": ALL_PATTERNS
    }
    with open(path, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    print(f"  [2/6] JSON:             {path}")
    return path


# ═══════════════════════════════════════════════════════════════
#  3. SQL FORMAT
# ═══════════════════════════════════════════════════════════════

def generate_sql():
    """Generate SQL with CREATE TABLE + INSERT statements."""
    path = os.path.join(OUTPUT_DIR, "candlestick_patterns.sql")

    ddl = """-- ============================================================
-- Complete Japanese Candlestick Pattern Database
-- SQL Schema + Data for AI/ML Trading Model Training
-- ============================================================

DROP TABLE IF EXISTS candlestick_patterns;

CREATE TABLE candlestick_patterns (
    id                    INTEGER PRIMARY KEY,
    pattern_name          VARCHAR(100) NOT NULL,
    alternative_names     TEXT,
    japanese_name         VARCHAR(100),
    category              VARCHAR(50) NOT NULL,
    sub_category          VARCHAR(50) NOT NULL,
    sentiment             VARCHAR(20) NOT NULL,
    expected_direction    VARCHAR(30) NOT NULL,
    trend_required        VARCHAR(30) NOT NULL,
    num_candles           INTEGER NOT NULL,
    pattern_structure     TEXT,
    candle_by_candle      TEXT,
    market_psychology     TEXT,
    confirmation_required TEXT,
    volume_confirmation   TEXT,
    volatility_conditions TEXT,
    gap_requirement       VARCHAR(20),
    reliability           VARCHAR(10),
    success_rate_range    VARCHAR(20),
    failure_conditions    TEXT,
    entry_rules           TEXT,
    stop_loss_rules       TEXT,
    take_profit_rules     TEXT,
    risk_reward           VARCHAR(20),
    best_timeframes       TEXT,
    best_markets          TEXT,
    best_indicators       TEXT,
    common_mistakes       TEXT,
    ai_features           TEXT,
    ohlc_relationship     TEXT,
    label                 VARCHAR(20) NOT NULL,
    confidence_score      INTEGER,
    probability_score     INTEGER
);

-- Indexes for common queries
CREATE INDEX idx_cp_category ON candlestick_patterns(category);
CREATE INDEX idx_cp_sentiment ON candlestick_patterns(sentiment);
CREATE INDEX idx_cp_direction ON candlestick_patterns(expected_direction);
CREATE INDEX idx_cp_reliability ON candlestick_patterns(reliability);
CREATE INDEX idx_cp_num_candles ON candlestick_patterns(num_candles);
CREATE INDEX idx_cp_label ON candlestick_patterns(label);
CREATE INDEX idx_cp_confidence ON candlestick_patterns(confidence_score);

-- ============================================================
-- INSERT DATA
-- ============================================================
"""

    with open(path, "w", encoding="utf-8") as f:
        f.write(ddl + "\n")
        for p in ALL_PATTERNS:
            cols = ", ".join(FIELDS)
            vals = []
            for field in FIELDS:
                val = p.get(field, "")
                if isinstance(val, (int, float)):
                    vals.append(str(val))
                elif isinstance(val, list):
                    vals.append(f"'{_escape_sql(json.dumps(val))}'")
                else:
                    vals.append(f"'{_escape_sql(val)}'")
            f.write(f"INSERT INTO candlestick_patterns ({cols})\nVALUES ({', '.join(vals)});\n\n")

    print(f"  [3/6] SQL:              {path}")
    return path


# ═══════════════════════════════════════════════════════════════
#  4. PYTHON DICTIONARY FORMAT
# ═══════════════════════════════════════════════════════════════

def generate_python_dict():
    """Generate standalone Python file with CANDLESTICK_PATTERNS list."""
    path = os.path.join(OUTPUT_DIR, "candlestick_patterns_dict.py")
    with open(path, "w", encoding="utf-8") as f:
        f.write(f'"""\n')
        f.write(f'Complete Japanese Candlestick Pattern Database — Python Dictionary\n')
        f.write(f'Total Patterns: {TOTAL}\n')
        f.write(f'Fields per Pattern: {len(FIELDS)}\n')
        f.write(f'Generated: {datetime.now().isoformat()}\n')
        f.write(f'\n')
        f.write(f'Usage:\n')
        f.write(f'    from candlestick_patterns_dict import CANDLESTICK_PATTERNS\n')
        f.write(f'    for p in CANDLESTICK_PATTERNS:\n')
        f.write(f'        print(p["pattern_name"], p["expected_direction"])\n')
        f.write(f'"""\n\n')
        f.write("CANDLESTICK_PATTERNS = ")
        f.write(json.dumps(ALL_PATTERNS, indent=4, ensure_ascii=False))
        f.write("\n")
    print(f"  [4/6] Python Dict:      {path}")
    return path


# ═══════════════════════════════════════════════════════════════
#  5. PANDAS DATAFRAME FORMAT
# ═══════════════════════════════════════════════════════════════

def generate_pandas_dataframe():
    """Generate Python script that loads JSON and creates DataFrame."""
    path = os.path.join(OUTPUT_DIR, "candlestick_patterns_dataframe.py")

    header = f'''"""
Complete Japanese Candlestick Pattern Database — Pandas DataFrame
Total Patterns: {TOTAL}
Generated: {datetime.now().isoformat()}

Usage:
    from candlestick_patterns_dataframe import df, get_bullish, get_bearish
    bullish = get_bullish()
    high_conf = df[df["confidence_score"] >= 70]
"""

'''

    body = '''import json
import os
import pandas as pd

# ── Load data from JSON ──────────────────────────────────────

_JSON_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "candlestick_patterns.json")
with open(_JSON_PATH, "r", encoding="utf-8") as _f:
    _data = json.load(_f)

df = pd.DataFrame(_data["patterns"])


# ── Helper functions ──────────────────────────────────────────

def get_bullish():
    """Return all bullish patterns."""
    return df[df["sentiment"] == "Bullish"].copy()


def get_bearish():
    """Return all bearish patterns."""
    return df[df["sentiment"] == "Bearish"].copy()


def get_neutral():
    """Return all neutral/indecision patterns."""
    return df[df["sentiment"] == "Neutral"].copy()


def get_by_category(category: str):
    """Filter by candle count category (e.g., 'Single Candle')."""
    return df[df["category"] == category].copy()


def get_by_reliability(reliability: str):
    """Filter by reliability level ('High', 'Medium', 'Low')."""
    return df[df["reliability"] == reliability].copy()


def get_by_direction(direction: str):
    """Filter by expected direction ('UP', 'DOWN', etc.)."""
    return df[df["expected_direction"] == direction].copy()


def get_reversals():
    """Return all reversal patterns."""
    return df[df["sub_category"].str.contains("Reversal", na=False)].copy()


def get_continuations():
    """Return all continuation patterns."""
    return df[df["sub_category"].str.contains("Continuation", na=False)].copy()


def get_high_confidence(threshold=70):
    """Return patterns with confidence >= threshold."""
    return df[df["confidence_score"] >= threshold].copy()


def search_pattern(keyword: str):
    """Search patterns by name (case-insensitive)."""
    mask = df["pattern_name"].str.contains(keyword, case=False, na=False)
    return df[mask].copy()


def summary():
    """Print database summary statistics."""
    print(f"Total Patterns: {len(df)}")
    print(f"\\nBy Category:\\n{df['category'].value_counts().to_string()}")
    print(f"\\nBy Sentiment:\\n{df['sentiment'].value_counts().to_string()}")
    print(f"\\nBy Reliability:\\n{df['reliability'].value_counts().to_string()}")
    print(f"\\nBy Direction:\\n{df['expected_direction'].value_counts().to_string()}")
    print(f"\\nConfidence Score: mean={df['confidence_score'].mean():.1f}, "
          f"min={df['confidence_score'].min()}, max={df['confidence_score'].max()}")


if __name__ == "__main__":
    summary()
'''

    with open(path, "w", encoding="utf-8") as f:
        f.write(header + body)
    print(f"  [5/6] Pandas DataFrame: {path}")
    return path


# ═══════════════════════════════════════════════════════════════
#  6. AI TRAINING DATASET FORMAT
# ═══════════════════════════════════════════════════════════════

def generate_ai_training():
    """Generate Python script with numpy feature arrays for ML training."""
    path = os.path.join(OUTPUT_DIR, "candlestick_patterns_ai_training.py")

    # ── Encoding maps ─────────────────────────────────────────
    sentiment_map = {"Bullish": 1, "Bearish": -1, "Neutral": 0}
    direction_map = {
        "UP": 1.0, "DOWN": -1.0,
        "CONTINUATION_UP": 0.5, "CONTINUATION_DOWN": -0.5,
        "INDECISION": 0.0
    }
    reliability_map = {"High": 3, "Medium": 2, "Low": 1}
    trend_map = {"Downtrend": -1, "Uptrend": 1, "Any": 0, "None": 0}
    gap_map = {"None": 0, "Optional": 1, "Preferred": 2, "Required": 3}
    category_map = {
        "Single Candle": 1, "Two Candle": 2, "Three Candle": 3,
        "Four Candle": 4, "Five Candle": 5
    }

    # ── Compute feature vectors ───────────────────────────────
    features = []
    labels = []
    dir_labels = []
    names = []

    for p in ALL_PATTERNS:
        is_rev = 1 if "Reversal" in p.get("sub_category", "") else 0
        is_cont = 1 if "Continuation" in p.get("sub_category", "") else 0
        is_indec = 1 if p.get("sub_category", "") == "Indecision" else 0

        feat = [
            category_map.get(p["category"], 0),
            p["num_candles"],
            sentiment_map.get(p["sentiment"], 0),
            direction_map.get(p["expected_direction"], 0),
            trend_map.get(p["trend_required"], 0),
            reliability_map.get(p["reliability"], 0),
            gap_map.get(p["gap_requirement"], 0),
            round(p["confidence_score"] / 100.0, 2),
            round(p["probability_score"] / 100.0, 2),
            is_rev,
            is_cont,
            is_indec,
        ]
        features.append(feat)
        labels.append(sentiment_map.get(p["label"], 0))
        dir_labels.append(direction_map.get(p["expected_direction"], 0))
        names.append(p["pattern_name"])

    feat_names = [
        "num_category", "num_candles", "sentiment_encoded",
        "direction_encoded", "trend_required_encoded",
        "reliability_encoded", "gap_encoded",
        "confidence_normalized", "probability_normalized",
        "is_reversal", "is_continuation", "is_indecision"
    ]

    # ── Build output file ─────────────────────────────────────

    header = f'''"""
Complete Japanese Candlestick Pattern Database — AI Training Dataset
====================================================================
Total Patterns: {TOTAL}
Features: {len(feat_names)} per pattern
Generated: {datetime.now().isoformat()}

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

'''

    imports = 'import numpy as np\n\n'

    # Feature definitions
    feat_def = f'feature_names = {json.dumps(feat_names)}\n\n'
    feat_def += 'feature_descriptions = {\n'
    desc_map = {
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
    for k, v in desc_map.items():
        feat_def += f'    "{k}": "{v}",\n'
    feat_def += '}\n\n'

    # Data arrays
    data_section = f'X_train = np.array({json.dumps(features)})\n\n'
    data_section += f'y_train = np.array({json.dumps(labels)})\n\n'
    data_section += f'direction_labels = np.array({json.dumps(dir_labels)})\n\n'
    data_section += f'pattern_names = {json.dumps(names)}\n\n'

    # Directional subset + functions (no interpolation needed, use regular string)
    functions = '''# ── Directional subset (excludes neutral patterns) ───────────

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
    print(f"\\nDirectional subset: {len(X_directional)}")
    print(f"  UP (1):  {int(np.sum(y_binary == 1))}")
    print(f"  DOWN (0): {int(np.sum(y_binary == 0))}")
    print(f"\\nFeature names: {feature_names}")
'''

    with open(path, "w", encoding="utf-8") as f:
        f.write(header + imports + feat_def + data_section + functions)
    print(f"  [6/6] AI Training:      {path}")
    return path


# ═══════════════════════════════════════════════════════════════
#  VALIDATION
# ═══════════════════════════════════════════════════════════════

def validate_patterns():
    """Validate all patterns have required fields and valid values."""
    valid_sentiments = {"Bullish", "Bearish", "Neutral"}
    valid_directions = {"UP", "DOWN", "CONTINUATION_UP", "CONTINUATION_DOWN", "INDECISION"}
    valid_reliability = {"High", "Medium", "Low"}
    valid_categories = {"Single Candle", "Two Candle", "Three Candle", "Four Candle", "Five Candle"}
    valid_gaps = {"None", "Required", "Optional", "Preferred"}
    valid_trends = {"Downtrend", "Uptrend", "Any", "None"}

    errors = []
    for i, p in enumerate(ALL_PATTERNS):
        pid = p.get("pattern_name", f"Pattern #{i}")

        # Check all required fields exist
        for field in FIELDS:
            if field not in p:
                errors.append(f"{pid}: missing field '{field}'")

        # Validate enum values
        if p.get("sentiment") not in valid_sentiments:
            errors.append(f"{pid}: invalid sentiment '{p.get('sentiment')}'")
        if p.get("expected_direction") not in valid_directions:
            errors.append(f"{pid}: invalid direction '{p.get('expected_direction')}'")
        if p.get("reliability") not in valid_reliability:
            errors.append(f"{pid}: invalid reliability '{p.get('reliability')}'")
        if p.get("category") not in valid_categories:
            errors.append(f"{pid}: invalid category '{p.get('category')}'")
        if p.get("gap_requirement") not in valid_gaps:
            errors.append(f"{pid}: invalid gap_requirement '{p.get('gap_requirement')}'")
        if p.get("trend_required") not in valid_trends:
            errors.append(f"{pid}: invalid trend_required '{p.get('trend_required')}'")

        # Validate score ranges
        cs = p.get("confidence_score", -1)
        ps = p.get("probability_score", -1)
        if not (0 <= cs <= 100):
            errors.append(f"{pid}: confidence_score {cs} out of range 0-100")
        if not (0 <= ps <= 100):
            errors.append(f"{pid}: probability_score {ps} out of range 0-100")

        # Validate list fields are lists
        for lf in LIST_FIELDS:
            if lf in p and not isinstance(p[lf], list):
                errors.append(f"{pid}: '{lf}' should be a list, got {type(p[lf])}")

    if errors:
        print(f"\n  [!] VALIDATION ERRORS ({len(errors)}):")
        for e in errors:
            print(f"    - {e}")
        return False
    else:
        print(f"  [OK] All {TOTAL} patterns passed validation")
        return True


# ═══════════════════════════════════════════════════════════════
#  MAIN
# ═══════════════════════════════════════════════════════════════

def main():
    print()
    print("=" * 60)
    print("  CANDLESTICK PATTERN DATABASE - FORMAT GENERATOR")
    print("=" * 60)
    print(f"  Total patterns loaded: {TOTAL}")
    print(f"  Fields per pattern:    {len(FIELDS)}")
    print(f"  Output directory:      {OUTPUT_DIR}")
    print("=" * 60)
    print()

    # Validate first
    if not validate_patterns():
        print("\n  [!] Fix validation errors before generating outputs.\n")
        return

    print()

    # Generate all 6 formats
    generate_csv()
    generate_json()
    generate_sql()
    generate_python_dict()
    generate_pandas_dataframe()
    generate_ai_training()

    print()
    print("=" * 60)
    print(f"  [OK] ALL 6 FORMATS GENERATED SUCCESSFULLY ({TOTAL} patterns)")
    print("=" * 60)
    print()


if __name__ == "__main__":
    main()
