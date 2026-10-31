"""
Complete Japanese Candlestick Pattern Database — Pandas DataFrame
Total Patterns: 80
Generated: 2026-07-08T23:53:39.261155

Usage:
    from candlestick_patterns_dataframe import df, get_bullish, get_bearish
    bullish = get_bullish()
    high_conf = df[df["confidence_score"] >= 70]
"""

import json
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
    print(f"\nBy Category:\n{df['category'].value_counts().to_string()}")
    print(f"\nBy Sentiment:\n{df['sentiment'].value_counts().to_string()}")
    print(f"\nBy Reliability:\n{df['reliability'].value_counts().to_string()}")
    print(f"\nBy Direction:\n{df['expected_direction'].value_counts().to_string()}")
    print(f"\nConfidence Score: mean={df['confidence_score'].mean():.1f}, "
          f"min={df['confidence_score'].min()}, max={df['confidence_score'].max()}")


if __name__ == "__main__":
    summary()
