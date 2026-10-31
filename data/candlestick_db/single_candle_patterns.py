"""
Single Candle Candlestick Pattern Database
==========================================

A comprehensive database of 16 single-candle candlestick patterns for use in
quantitative trading AI systems. Each pattern is defined as a dictionary with
31 standardized fields covering identification, structure, psychology, trading
rules, and machine-learning features.

Patterns included:
    1.  Hammer
    2.  Inverted Hammer
    3.  Hanging Man
    4.  Shooting Star
    5.  Doji
    6.  Dragonfly Doji
    7.  Gravestone Doji
    8.  Long-Legged Doji
    9.  Four Price Doji
    10. Bullish Spinning Top
    11. Bearish Spinning Top
    12. Bullish Marubozu
    13. Bearish Marubozu
    14. High Wave Candle
    15. Bullish Belt Hold
    16. Bearish Belt Hold

DISCLAIMER: Success rates and confidence scores are conservative estimates
based on general technical-analysis literature. No pattern predicts future
price action with certainty. Always combine with other analysis methods
and proper risk management.
"""

# =============================================================================
# SINGLE CANDLE PATTERNS — 16 entries, 31 keys each
# =============================================================================

PATTERNS = [
    # -----------------------------------------------------------------
    # 1. Hammer
    # -----------------------------------------------------------------
    {
        "id": 0,
        "pattern_name": "Hammer",
        "alternative_names": ["Takuri", "Hammer Line"],
        "japanese_name": "Takuri",
        "category": "Single Candle",
        "sub_category": "Bullish Reversal",
        "sentiment": "Bullish",
        "expected_direction": "UP",
        "trend_required": "Downtrend",
        "num_candles": 1,
        "pattern_structure": "Small real body near the top with a long lower shadow at least 2x the body and little or no upper shadow",
        "candle_by_candle": [
            "Candle 1: Small real body (bullish or bearish) near session high. "
            "Long lower shadow >= 2x body length. Little or no upper shadow."
        ],
        "market_psychology": (
            "In a downtrend, sellers push price sharply lower intraday but "
            "strong buying emerges near the lows, pushing price back up to "
            "close near the open. This rejection of lower prices signals "
            "sellers losing control and potential reversal."
        ),
        "confirmation_required": (
            "Bullish confirmation candle closing above the hammer's high "
            "significantly increases reliability."
        ),
        "volume_confirmation": (
            "Higher than average volume on the hammer strengthens the signal. "
            "Volume spike during the lower wick formation indicates "
            "institutional buying."
        ),
        "volatility_conditions": (
            "Most effective in normal to moderately elevated volatility. "
            "Less reliable in extreme volatility or very low volatility."
        ),
        "gap_requirement": "None",
        "reliability": "Medium",
        "success_rate_range": "55-65%",
        "failure_conditions": [
            "No bullish confirmation follows",
            "Appears in sideways market rather than downtrend",
            "Lower shadow less than 2x the body",
            "Very low volume",
            "Strong resistance immediately above",
        ],
        "entry_rules": (
            "Enter long on close of confirmation candle (closes above hammer "
            "high). Aggressive: enter at hammer close."
        ),
        "stop_loss_rules": (
            "Below the hammer low. Conservative: 1-2 ATR below hammer low."
        ),
        "take_profit_rules": (
            "Target nearest resistance or previous swing high. "
            "Or use 1:2 to 1:3 RR ratio."
        ),
        "risk_reward": "1:2",
        "best_timeframes": ["Daily", "4H", "Weekly"],
        "best_markets": ["Stocks", "Forex", "Crypto", "Futures", "Commodities"],
        "best_indicators": [
            "RSI (oversold)",
            "MACD (divergence)",
            "Volume",
            "Support/Resistance",
            "Moving Averages",
        ],
        "common_mistakes": [
            "Trading without confirmation",
            "Identifying in non-trending markets",
            "Ignoring prior trend context",
            "Confusing with Hanging Man (uptrend version)",
        ],
        "ai_features": [
            "body_ratio < 0.30",
            "lower_wick_ratio > 0.55",
            "upper_wick_ratio < 0.15",
            "prior_trend = downtrend",
            "lower_shadow / body >= 2.0",
        ],
        "ohlc_relationship": (
            "lower_wick = min(O,C) - L > 2 * |C-O|; "
            "upper_wick = H - max(O,C) < 0.15 * (H-L); "
            "body_ratio < 0.30"
        ),
        "label": "Bullish",
        "confidence_score": 60,
        "probability_score": 60,
    },

    # -----------------------------------------------------------------
    # 2. Inverted Hammer
    # -----------------------------------------------------------------
    {
        "id": 1,
        "pattern_name": "Inverted Hammer",
        "alternative_names": ["Inverted Hammer Line", "Reverse Hammer"],
        "japanese_name": "Tohba",
        "category": "Single Candle",
        "sub_category": "Bullish Reversal",
        "sentiment": "Bullish",
        "expected_direction": "UP",
        "trend_required": "Downtrend",
        "num_candles": 1,
        "pattern_structure": (
            "Small real body near the bottom of the candle with a long upper "
            "shadow at least 2x the body length and little or no lower shadow."
        ),
        "candle_by_candle": [
            "Candle 1: Small real body (bullish or bearish) near session low. "
            "Long upper shadow >= 2x body length. Little or no lower shadow."
        ],
        "market_psychology": (
            "During a downtrend, buyers attempt to push prices significantly "
            "higher intraday, but sellers still manage to pull the close back "
            "down near the open. However, the buying attempt itself suggests "
            "that bullish sentiment is building and a reversal may follow once "
            "buyers gain confidence."
        ),
        "confirmation_required": (
            "Strong bullish confirmation is essential—next candle should close "
            "above the inverted hammer's high. Without confirmation, this "
            "pattern is unreliable."
        ),
        "volume_confirmation": (
            "Above-average volume on the inverted hammer adds credibility. "
            "Rising volume on the confirmation candle further validates the "
            "reversal signal."
        ),
        "volatility_conditions": (
            "Works best in moderate volatility environments. In extremely "
            "volatile markets, the long upper shadow may be noise rather than "
            "a meaningful buying attempt."
        ),
        "gap_requirement": "None",
        "reliability": "Low",
        "success_rate_range": "50-60%",
        "failure_conditions": [
            "No bullish confirmation candle follows",
            "Appears in a range-bound market",
            "Upper shadow less than 2x the body",
            "Heavy overhead resistance within the upper shadow range",
            "Declining volume on the pattern and confirmation",
        ],
        "entry_rules": (
            "Enter long after bullish confirmation candle closes above the "
            "inverted hammer's high. Aggressive entry at the open of the next "
            "candle is higher risk."
        ),
        "stop_loss_rules": (
            "Below the inverted hammer's low. Conservative: 1-2 ATR below the "
            "pattern low."
        ),
        "take_profit_rules": (
            "Target previous swing high or nearest resistance level. "
            "Use 1:2 to 1:3 risk-reward ratio."
        ),
        "risk_reward": "1:2",
        "best_timeframes": ["Daily", "4H", "Weekly"],
        "best_markets": ["Stocks", "Forex", "Futures", "Commodities"],
        "best_indicators": [
            "RSI (oversold)",
            "Stochastic (oversold)",
            "Volume",
            "Support levels",
            "Bollinger Bands (lower band touch)",
        ],
        "common_mistakes": [
            "Trading without confirmation—this is the most common error",
            "Confusing with Shooting Star (which appears in uptrends)",
            "Ignoring the prior downtrend requirement",
            "Over-relying on the pattern without confluence",
        ],
        "ai_features": [
            "body_ratio < 0.30",
            "upper_wick_ratio > 0.55",
            "lower_wick_ratio < 0.15",
            "prior_trend = downtrend",
            "upper_shadow / body >= 2.0",
        ],
        "ohlc_relationship": (
            "upper_wick = H - max(O,C) > 2 * |C-O|; "
            "lower_wick = min(O,C) - L < 0.15 * (H-L); "
            "body_ratio < 0.30"
        ),
        "label": "Bullish",
        "confidence_score": 45,
        "probability_score": 55,
    },

    # -----------------------------------------------------------------
    # 3. Hanging Man
    # -----------------------------------------------------------------
    {
        "id": 2,
        "pattern_name": "Hanging Man",
        "alternative_names": ["Hanging Man Line"],
        "japanese_name": "Kubitsuri",
        "category": "Single Candle",
        "sub_category": "Bearish Reversal",
        "sentiment": "Bearish",
        "expected_direction": "DOWN",
        "trend_required": "Uptrend",
        "num_candles": 1,
        "pattern_structure": (
            "Small real body near the top of the candle with a long lower "
            "shadow at least 2x the body length and little or no upper shadow. "
            "Identical shape to Hammer but appears in an uptrend."
        ),
        "candle_by_candle": [
            "Candle 1: Small real body (bullish or bearish) near session high. "
            "Long lower shadow >= 2x body length. Little or no upper shadow. "
            "Appears after a sustained uptrend."
        ],
        "market_psychology": (
            "After a rally, price drops sharply intraday—revealing that "
            "sellers are becoming more aggressive. Although buyers manage to "
            "push price back up near the open, the deep intraday selloff is "
            "an early warning that the uptrend may be exhausting. The pattern "
            "suggests distribution is beginning."
        ),
        "confirmation_required": (
            "Bearish confirmation candle closing below the hanging man's body "
            "(ideally below its low) is strongly recommended before acting."
        ),
        "volume_confirmation": (
            "Above-average volume strengthens the signal by indicating "
            "meaningful selling pressure. A bearish-body hanging man on high "
            "volume is more reliable than a bullish-body one."
        ),
        "volatility_conditions": (
            "Effective in normal volatility. In very high volatility, the "
            "long lower shadow may simply reflect market noise. Best when "
            "preceded by a clean, sustained uptrend."
        ),
        "gap_requirement": "Optional",
        "reliability": "Medium",
        "success_rate_range": "50-60%",
        "failure_conditions": [
            "No bearish confirmation follows",
            "Appears in a sideways or weak uptrend",
            "Lower shadow shorter than 2x the body",
            "Strong support just below the pattern",
            "Volume is declining rather than expanding",
        ],
        "entry_rules": (
            "Enter short on close of bearish confirmation candle (closes below "
            "hanging man's low). Aggressive: enter at hanging man close if "
            "body is bearish."
        ),
        "stop_loss_rules": (
            "Above the hanging man's high. Conservative: 1-2 ATR above the "
            "pattern high."
        ),
        "take_profit_rules": (
            "Target nearest support level or prior swing low. "
            "Use 1:2 to 1:3 risk-reward ratio."
        ),
        "risk_reward": "1:2",
        "best_timeframes": ["Daily", "4H", "Weekly"],
        "best_markets": ["Stocks", "Forex", "Crypto", "Futures", "Commodities"],
        "best_indicators": [
            "RSI (overbought)",
            "MACD (bearish crossover)",
            "Volume",
            "Resistance/Supply zones",
            "Moving Averages",
        ],
        "common_mistakes": [
            "Confusing with Hammer (which requires a downtrend)",
            "Trading without bearish confirmation",
            "Ignoring the strength and duration of the prior uptrend",
            "Placing stop too tight—the high of the hanging man can be retested",
        ],
        "ai_features": [
            "body_ratio < 0.30",
            "lower_wick_ratio > 0.55",
            "upper_wick_ratio < 0.15",
            "prior_trend = uptrend",
            "lower_shadow / body >= 2.0",
        ],
        "ohlc_relationship": (
            "lower_wick = min(O,C) - L > 2 * |C-O|; "
            "upper_wick = H - max(O,C) < 0.15 * (H-L); "
            "body_ratio < 0.30; prior_trend = uptrend"
        ),
        "label": "Bearish",
        "confidence_score": 55,
        "probability_score": 55,
    },

    # -----------------------------------------------------------------
    # 4. Shooting Star
    # -----------------------------------------------------------------
    {
        "id": 3,
        "pattern_name": "Shooting Star",
        "alternative_names": ["Shooting Star Line"],
        "japanese_name": "Nagare Boshi",
        "category": "Single Candle",
        "sub_category": "Bearish Reversal",
        "sentiment": "Bearish",
        "expected_direction": "DOWN",
        "trend_required": "Uptrend",
        "num_candles": 1,
        "pattern_structure": (
            "Small real body near the bottom of the candle with a long upper "
            "shadow at least 2x the body length and little or no lower shadow. "
            "Identical shape to Inverted Hammer but appears in an uptrend."
        ),
        "candle_by_candle": [
            "Candle 1: Small real body (bullish or bearish) near session low. "
            "Long upper shadow >= 2x body length. Little or no lower shadow. "
            "Appears after a sustained uptrend."
        ],
        "market_psychology": (
            "During an uptrend, buyers push price to new intraday highs but "
            "sellers aggressively drive price back down to close near the "
            "open. The failed rally attempt demonstrates that overhead supply "
            "is overwhelming demand, warning of a potential trend reversal."
        ),
        "confirmation_required": (
            "Bearish confirmation candle closing below the shooting star's "
            "body greatly improves reliability. A gap down on the next candle "
            "is the strongest confirmation."
        ),
        "volume_confirmation": (
            "High volume on the shooting star signals strong conviction in the "
            "rejection. Volume expanding during the upper wick formation and "
            "on the confirmation candle bolsters the signal."
        ),
        "volatility_conditions": (
            "Most reliable in moderate-to-elevated volatility after a clear "
            "uptrend. Less meaningful in choppy, range-bound conditions."
        ),
        "gap_requirement": "Preferred",
        "reliability": "Medium",
        "success_rate_range": "55-65%",
        "failure_conditions": [
            "No bearish confirmation follows",
            "Appears in a downtrend or sideways market",
            "Upper shadow less than 2x the body",
            "Strong bullish momentum continues with high volume",
            "Major support nearby limits downside follow-through",
        ],
        "entry_rules": (
            "Enter short on bearish confirmation candle closing below the "
            "shooting star's low. Aggressive: enter at the close of the "
            "shooting star if body is bearish."
        ),
        "stop_loss_rules": (
            "Above the shooting star's high. Conservative: 1-2 ATR above the "
            "pattern high."
        ),
        "take_profit_rules": (
            "Target nearest support or previous swing low. "
            "Use 1:2 to 1:3 risk-reward ratio."
        ),
        "risk_reward": "1:2",
        "best_timeframes": ["Daily", "4H", "Weekly"],
        "best_markets": ["Stocks", "Forex", "Crypto", "Futures", "Commodities"],
        "best_indicators": [
            "RSI (overbought)",
            "MACD (bearish divergence)",
            "Volume",
            "Resistance zones",
            "Fibonacci retracement levels",
        ],
        "common_mistakes": [
            "Confusing with Inverted Hammer (which requires a downtrend)",
            "Trading without confirmation",
            "Ignoring the prior uptrend requirement",
            "Placing stop below the low instead of above the high",
        ],
        "ai_features": [
            "body_ratio < 0.30",
            "upper_wick_ratio > 0.55",
            "lower_wick_ratio < 0.15",
            "prior_trend = uptrend",
            "upper_shadow / body >= 2.0",
        ],
        "ohlc_relationship": (
            "upper_wick = H - max(O,C) > 2 * |C-O|; "
            "lower_wick = min(O,C) - L < 0.15 * (H-L); "
            "body_ratio < 0.30; prior_trend = uptrend"
        ),
        "label": "Bearish",
        "confidence_score": 60,
        "probability_score": 60,
    },

    # -----------------------------------------------------------------
    # 5. Doji
    # -----------------------------------------------------------------
    {
        "id": 4,
        "pattern_name": "Doji",
        "alternative_names": ["Standard Doji", "Neutral Doji", "Common Doji"],
        "japanese_name": "Doji",
        "category": "Single Candle",
        "sub_category": "Indecision",
        "sentiment": "Neutral",
        "expected_direction": "INDECISION",
        "trend_required": "Any",
        "num_candles": 1,
        "pattern_structure": (
            "Open and close are virtually equal, creating a cross or plus-sign "
            "shape. Upper and lower shadows are roughly equal and moderate in "
            "length."
        ),
        "candle_by_candle": [
            "Candle 1: Open ≈ Close (body is extremely small or a thin line). "
            "Upper and lower shadows of roughly similar, moderate length. "
            "Visually resembles a cross."
        ],
        "market_psychology": (
            "Buyers and sellers are in equilibrium—neither side can gain "
            "control. After a sustained trend, a doji indicates the prevailing "
            "momentum is fading and a reversal or consolidation may follow. "
            "In isolation, it is purely indecision; context determines its "
            "significance."
        ),
        "confirmation_required": (
            "A directional confirmation candle is critical. Bullish close "
            "above doji high suggests upside; bearish close below doji low "
            "suggests downside."
        ),
        "volume_confirmation": (
            "High volume on a doji highlights significant indecision and "
            "makes the subsequent breakout direction more meaningful. Low "
            "volume dojis can be ignored in most cases."
        ),
        "volatility_conditions": (
            "Dojis after a strong trend in moderate-to-high volatility are "
            "most significant. Dojis in low-volatility consolidation zones "
            "carry little weight."
        ),
        "gap_requirement": "None",
        "reliability": "Low",
        "success_rate_range": "50-55%",
        "failure_conditions": [
            "No follow-through in either direction",
            "Appears in a choppy, range-bound market (noise)",
            "Very low volume—indicates lack of participation",
            "Multiple consecutive dojis (market is simply idle)",
            "Body is too large to qualify as a true doji",
        ],
        "entry_rules": (
            "Wait for confirmation. Enter long if next candle closes above "
            "doji high; enter short if next candle closes below doji low. "
            "Do not trade the doji in isolation."
        ),
        "stop_loss_rules": (
            "Opposite side of the doji range. Long: below doji low. "
            "Short: above doji high."
        ),
        "take_profit_rules": (
            "Target nearest support or resistance in the direction of the "
            "breakout. Use 1:1.5 to 1:2 risk-reward ratio."
        ),
        "risk_reward": "1:2",
        "best_timeframes": ["Daily", "4H", "Weekly"],
        "best_markets": ["Stocks", "Forex", "Futures", "Indices"],
        "best_indicators": [
            "RSI (extremes)",
            "Bollinger Bands",
            "Volume",
            "Support/Resistance",
            "ATR (context for volatility)",
        ],
        "common_mistakes": [
            "Trading the doji without waiting for confirmation",
            "Treating every doji as a reversal signal",
            "Ignoring the preceding trend context",
            "Failing to distinguish between doji subtypes",
        ],
        "ai_features": [
            "body_ratio < 0.05",
            "abs(O - C) / (H - L) < 0.05",
            "upper_wick_ratio ≈ lower_wick_ratio",
            "0.35 < upper_wick_ratio < 0.55",
            "0.35 < lower_wick_ratio < 0.55",
        ],
        "ohlc_relationship": (
            "|C - O| / (H - L) < 0.05; "
            "upper_wick = H - max(O,C); lower_wick = min(O,C) - L; "
            "abs(upper_wick - lower_wick) / (H - L) < 0.20"
        ),
        "label": "Neutral",
        "confidence_score": 35,
        "probability_score": 50,
    },

    # -----------------------------------------------------------------
    # 6. Dragonfly Doji
    # -----------------------------------------------------------------
    {
        "id": 5,
        "pattern_name": "Dragonfly Doji",
        "alternative_names": ["Dragonfly", "Tonbo Doji"],
        "japanese_name": "Tonbo",
        "category": "Single Candle",
        "sub_category": "Bullish Reversal",
        "sentiment": "Bullish",
        "expected_direction": "UP",
        "trend_required": "Downtrend",
        "num_candles": 1,
        "pattern_structure": (
            "Open, close, and high are at or very near the same price. Long "
            "lower shadow. No or negligible upper shadow. Resembles a T shape."
        ),
        "candle_by_candle": [
            "Candle 1: Open ≈ Close ≈ High (all near the session high). "
            "Long lower shadow showing strong intraday selling that was fully "
            "rejected. No meaningful upper shadow."
        ],
        "market_psychology": (
            "In a downtrend, sellers drive price significantly lower intraday, "
            "but powerful buying pressure pushes price all the way back to the "
            "high by the close. The complete recovery signals that sellers "
            "have been overwhelmed—demand is asserting itself, and a reversal "
            "is likely."
        ),
        "confirmation_required": (
            "A bullish confirmation candle closing above the dragonfly doji's "
            "high solidifies the reversal signal. This pattern is more "
            "reliable than a standard doji but still benefits from "
            "confirmation."
        ),
        "volume_confirmation": (
            "High volume on the dragonfly doji—especially during the lower "
            "wick recovery—signals institutional accumulation. Confirmation "
            "on rising volume strengthens the setup."
        ),
        "volatility_conditions": (
            "Most meaningful in moderate volatility after a notable downtrend. "
            "In extremely volatile markets the full recovery may be random "
            "noise."
        ),
        "gap_requirement": "None",
        "reliability": "Medium",
        "success_rate_range": "55-65%",
        "failure_conditions": [
            "No bullish follow-through on subsequent candles",
            "Appears in a sideways market or at the top of a range",
            "Lower shadow is too short to indicate meaningful rejection",
            "Heavy resistance directly overhead",
            "Volume is very low—indicates weak participation",
        ],
        "entry_rules": (
            "Enter long on confirmation candle closing above the dragonfly "
            "doji's high. Aggressive: enter at close of the dragonfly doji "
            "itself."
        ),
        "stop_loss_rules": (
            "Below the dragonfly doji's low (the tail). Conservative: "
            "1-2 ATR below the low."
        ),
        "take_profit_rules": (
            "Target nearest resistance, previous swing high, or use "
            "1:2 to 1:3 risk-reward ratio."
        ),
        "risk_reward": "1:2",
        "best_timeframes": ["Daily", "4H", "Weekly"],
        "best_markets": ["Stocks", "Forex", "Crypto", "Futures", "Commodities"],
        "best_indicators": [
            "RSI (oversold)",
            "MACD (bullish divergence)",
            "Volume",
            "Support levels",
            "Fibonacci retracement levels",
        ],
        "common_mistakes": [
            "Confusing with a standard Hammer—Dragonfly Doji has O ≈ C ≈ H",
            "Trading without confirmation in a shallow downtrend",
            "Ignoring overhead resistance that may cap the reversal",
            "Expecting large reversals from a single candle signal",
        ],
        "ai_features": [
            "body_ratio < 0.03",
            "upper_wick_ratio < 0.05",
            "lower_wick_ratio > 0.85",
            "abs(O - C) / (H - L) < 0.03",
            "H - max(O,C) < 0.05 * (H - L)",
        ],
        "ohlc_relationship": (
            "|C - O| / (H - L) < 0.03; "
            "H - max(O,C) < 0.05 * (H - L); "
            "min(O,C) - L > 0.85 * (H - L)"
        ),
        "label": "Bullish",
        "confidence_score": 60,
        "probability_score": 60,
    },

    # -----------------------------------------------------------------
    # 7. Gravestone Doji
    # -----------------------------------------------------------------
    {
        "id": 6,
        "pattern_name": "Gravestone Doji",
        "alternative_names": ["Gravestone", "Tohba Doji"],
        "japanese_name": "Hakaishi",
        "category": "Single Candle",
        "sub_category": "Bearish Reversal",
        "sentiment": "Bearish",
        "expected_direction": "DOWN",
        "trend_required": "Uptrend",
        "num_candles": 1,
        "pattern_structure": (
            "Open, close, and low are at or very near the same price. Long "
            "upper shadow. No or negligible lower shadow. Resembles an "
            "inverted T shape."
        ),
        "candle_by_candle": [
            "Candle 1: Open ≈ Close ≈ Low (all near the session low). "
            "Long upper shadow showing strong intraday buying that was fully "
            "rejected. No meaningful lower shadow."
        ],
        "market_psychology": (
            "During an uptrend, buyers push price to significant intraday "
            "highs, but sellers drive price all the way back down to the open "
            "by the close. The complete surrender of intraday gains reveals "
            "that bulls are losing power and bears are stepping in—a warning "
            "of potential reversal."
        ),
        "confirmation_required": (
            "Bearish confirmation candle closing below the gravestone doji's "
            "low is recommended. A gap down on the next session is the "
            "strongest confirmation."
        ),
        "volume_confirmation": (
            "High volume on the gravestone doji indicates meaningful selling "
            "pressure during the upper wick reversal. Rising volume on "
            "confirmation adds conviction."
        ),
        "volatility_conditions": (
            "Most effective after a sustained uptrend in moderate-to-elevated "
            "volatility. In low-volatility drift, the pattern may lack "
            "significance."
        ),
        "gap_requirement": "None",
        "reliability": "Medium",
        "success_rate_range": "55-65%",
        "failure_conditions": [
            "No bearish follow-through on subsequent candles",
            "Appears in a downtrend or near the bottom of a range",
            "Upper shadow is too short to demonstrate meaningful rejection",
            "Strong support or trendline directly below",
            "Very low volume—pattern lacks conviction",
        ],
        "entry_rules": (
            "Enter short on bearish confirmation candle closing below the "
            "gravestone doji's low. Aggressive: enter at close of the "
            "gravestone doji."
        ),
        "stop_loss_rules": (
            "Above the gravestone doji's high (the wick tip). Conservative: "
            "1-2 ATR above the high."
        ),
        "take_profit_rules": (
            "Target nearest support, previous swing low, or use "
            "1:2 to 1:3 risk-reward ratio."
        ),
        "risk_reward": "1:2",
        "best_timeframes": ["Daily", "4H", "Weekly"],
        "best_markets": ["Stocks", "Forex", "Crypto", "Futures", "Commodities"],
        "best_indicators": [
            "RSI (overbought)",
            "MACD (bearish crossover)",
            "Volume",
            "Resistance levels",
            "Fibonacci extension levels",
        ],
        "common_mistakes": [
            "Confusing with Shooting Star—Gravestone Doji has O ≈ C ≈ L",
            "Trading without confirmation",
            "Ignoring the prior uptrend requirement",
            "Expecting guaranteed reversals from a single-candle signal",
        ],
        "ai_features": [
            "body_ratio < 0.03",
            "lower_wick_ratio < 0.05",
            "upper_wick_ratio > 0.85",
            "abs(O - C) / (H - L) < 0.03",
            "min(O,C) - L < 0.05 * (H - L)",
        ],
        "ohlc_relationship": (
            "|C - O| / (H - L) < 0.03; "
            "min(O,C) - L < 0.05 * (H - L); "
            "H - max(O,C) > 0.85 * (H - L)"
        ),
        "label": "Bearish",
        "confidence_score": 60,
        "probability_score": 60,
    },

    # -----------------------------------------------------------------
    # 8. Long-Legged Doji
    # -----------------------------------------------------------------
    {
        "id": 7,
        "pattern_name": "Long-Legged Doji",
        "alternative_names": ["Long Legged Doji", "Juji Doji"],
        "japanese_name": "Juji",
        "category": "Single Candle",
        "sub_category": "Indecision",
        "sentiment": "Neutral",
        "expected_direction": "INDECISION",
        "trend_required": "Any",
        "num_candles": 1,
        "pattern_structure": (
            "Open and close are virtually equal, positioned near the middle "
            "of the candle's range. Both upper and lower shadows are "
            "exceptionally long, demonstrating extreme price volatility "
            "within the session."
        ),
        "candle_by_candle": [
            "Candle 1: Open ≈ Close, near the midpoint of the session range. "
            "Very long upper shadow AND very long lower shadow. The total "
            "range is large relative to recent candles."
        ],
        "market_psychology": (
            "Extreme tug-of-war between buyers and sellers within a single "
            "session. Price swings wildly in both directions but ultimately "
            "closes where it opened—neither side wins. This signals deep "
            "market uncertainty and often precedes a significant move once "
            "a direction is resolved."
        ),
        "confirmation_required": (
            "Directional confirmation is essential. Enter in the direction of "
            "the breakout candle. The long-legged doji alone provides no "
            "directional bias."
        ),
        "volume_confirmation": (
            "Very high volume on a long-legged doji underscores the intensity "
            "of the battle and makes the subsequent breakout more meaningful. "
            "Low volume reduces the pattern's significance."
        ),
        "volatility_conditions": (
            "By definition, this pattern occurs during elevated intraday "
            "volatility. It is most significant when it appears after a "
            "sustained trend, potentially marking a turning point."
        ),
        "gap_requirement": "None",
        "reliability": "Low",
        "success_rate_range": "50-55%",
        "failure_conditions": [
            "No follow-through breakout in either direction",
            "Appears during low-volume, low-interest sessions",
            "Market remains range-bound with more indecision candles",
            "Shadows are not significantly longer than recent candles",
            "Occurs in the middle of a consolidation (noise)",
        ],
        "entry_rules": (
            "Wait for a decisive close above the doji high (bullish) or below "
            "the doji low (bearish). The long range of the doji sets wide "
            "breakout levels—be patient."
        ),
        "stop_loss_rules": (
            "Opposite side of the doji range. Long: below doji low. "
            "Short: above doji high. Note: stops may be wide due to the long "
            "shadows."
        ),
        "take_profit_rules": (
            "Due to wide stops, aim for 1:2 or better risk-reward. Target "
            "next major support/resistance level in the breakout direction."
        ),
        "risk_reward": "1:2",
        "best_timeframes": ["Daily", "4H", "Weekly"],
        "best_markets": ["Stocks", "Forex", "Crypto", "Futures"],
        "best_indicators": [
            "Volume",
            "ATR (to assess range expansion)",
            "Bollinger Bands",
            "Support/Resistance",
            "RSI (extremes)",
        ],
        "common_mistakes": [
            "Trading the pattern without waiting for directional confirmation",
            "Ignoring the wide stop-loss implications",
            "Confusing with a standard doji—long-legged doji has notably larger shadows",
            "Over-trading multiple consecutive indecision candles",
        ],
        "ai_features": [
            "body_ratio < 0.05",
            "upper_wick_ratio > 0.40",
            "lower_wick_ratio > 0.40",
            "(H - L) > 1.5 * ATR(14)",
            "abs(O - C) / (H - L) < 0.05",
        ],
        "ohlc_relationship": (
            "|C - O| / (H - L) < 0.05; "
            "H - max(O,C) > 0.40 * (H - L); "
            "min(O,C) - L > 0.40 * (H - L)"
        ),
        "label": "Neutral",
        "confidence_score": 30,
        "probability_score": 50,
    },

    # -----------------------------------------------------------------
    # 9. Four Price Doji
    # -----------------------------------------------------------------
    {
        "id": 8,
        "pattern_name": "Four Price Doji",
        "alternative_names": ["Four-Price Doji", "Flat Doji", "Horizontal Line Doji"],
        "japanese_name": "Yonsen Doji",
        "category": "Single Candle",
        "sub_category": "Indecision",
        "sentiment": "Neutral",
        "expected_direction": "INDECISION",
        "trend_required": "Any",
        "num_candles": 1,
        "pattern_structure": (
            "Open, High, Low, and Close are all at the same price. The candle "
            "appears as a single horizontal line with no body and no shadows. "
            "Extremely rare on liquid instruments."
        ),
        "candle_by_candle": [
            "Candle 1: O = H = L = C. No body, no shadows. Single horizontal "
            "dash. Indicates zero price movement during the session."
        ],
        "market_psychology": (
            "Complete absence of price movement—no buying or selling pressure "
            "moved the market at all. This typically occurs in extremely "
            "illiquid instruments, during market holidays or pre-/post-market "
            "sessions with no participation. It signals total apathy and "
            "carries virtually no predictive value on its own."
        ),
        "confirmation_required": (
            "Any subsequent directional candle determines the next move. The "
            "four price doji itself is purely informational—it indicates "
            "illiquidity or extreme non-participation, not a trading signal."
        ),
        "volume_confirmation": (
            "Volume is typically zero or near-zero. If volume is meaningful, "
            "it may indicate a lock-limit scenario (futures) or halt, which "
            "has different implications."
        ),
        "volatility_conditions": (
            "Occurs only in zero-volatility conditions. Meaningful only as a "
            "liquidity or activity indicator, not as a directional signal."
        ),
        "gap_requirement": "None",
        "reliability": "Low",
        "success_rate_range": "50-50%",
        "failure_conditions": [
            "It is not a reliable trading signal in any context",
            "Appears on illiquid instruments—no actionable information",
            "Market is closed or halted—no real price discovery",
            "Cannot be meaningfully combined with indicators",
            "Multiple consecutive four-price dojis simply confirm illiquidity",
        ],
        "entry_rules": (
            "Do not trade this pattern directly. Use it as a liquidity filter "
            "—if a four price doji appears, the instrument may be too illiquid "
            "to trade."
        ),
        "stop_loss_rules": (
            "Not applicable—the pattern is not a trade signal."
        ),
        "take_profit_rules": (
            "Not applicable—the pattern is not a trade signal."
        ),
        "risk_reward": "1:1",
        "best_timeframes": ["1M", "5M", "15M"],
        "best_markets": ["Illiquid Stocks", "Pre-market Sessions", "Thinly Traded Futures"],
        "best_indicators": [
            "Volume (to confirm illiquidity)",
            "Bid-Ask Spread (to assess market depth)",
            "Order Book Depth",
        ],
        "common_mistakes": [
            "Treating this as a meaningful reversal or continuation signal",
            "Ignoring the illiquidity that typically causes it",
            "Confusing with a standard doji that has micro-shadows",
            "Attempting to apply trend analysis to a non-event candle",
        ],
        "ai_features": [
            "body_ratio == 0.0",
            "upper_wick_ratio == 0.0",
            "lower_wick_ratio == 0.0",
            "H == L == O == C",
            "(H - L) == 0",
        ],
        "ohlc_relationship": (
            "O == H == L == C; (H - L) == 0; body == 0; shadows == 0"
        ),
        "label": "Neutral",
        "confidence_score": 10,
        "probability_score": 50,
    },

    # -----------------------------------------------------------------
    # 10. Bullish Spinning Top
    # -----------------------------------------------------------------
    {
        "id": 9,
        "pattern_name": "Bullish Spinning Top",
        "alternative_names": ["Green Spinning Top", "Bullish Koma"],
        "japanese_name": "Koma",
        "category": "Single Candle",
        "sub_category": "Indecision",
        "sentiment": "Neutral",
        "expected_direction": "INDECISION",
        "trend_required": "Any",
        "num_candles": 1,
        "pattern_structure": (
            "Small bullish (green/white) real body in the center of the range "
            "with moderate upper and lower shadows. Shadows are longer than "
            "the body but not as extreme as a long-legged doji."
        ),
        "candle_by_candle": [
            "Candle 1: Small bullish body (C > O) centered within the range. "
            "Moderate upper and lower shadows, each longer than the body but "
            "not extremely long. Total range is moderate."
        ],
        "market_psychology": (
            "Mild indecision with a slight bullish lean. Buyers managed to "
            "close above the open but neither side dominated the session. "
            "In an uptrend, it suggests slowing momentum. In a downtrend, it "
            "hints at potential stabilization. Context determines whether this "
            "is a pause or an early warning."
        ),
        "confirmation_required": (
            "The next candle determines direction. A strong close in either "
            "direction provides the actionable signal. The spinning top alone "
            "is not a high-confidence entry."
        ),
        "volume_confirmation": (
            "Moderate to low volume is typical. High volume on a spinning top "
            "indicates notable uncertainty among participants with large "
            "positions."
        ),
        "volatility_conditions": (
            "Common in moderate volatility environments. Less significant in "
            "very low or very high volatility conditions."
        ),
        "gap_requirement": "None",
        "reliability": "Low",
        "success_rate_range": "50-55%",
        "failure_conditions": [
            "Market continues its prior trend without reversal",
            "Appears in a sideways range with no trend context",
            "No follow-through in either direction",
            "Body is too large relative to the shadows (not a spinning top)",
            "Very low volume indicates mere inactivity, not indecision",
        ],
        "entry_rules": (
            "Wait for confirmation candle. In a downtrend, a bullish "
            "confirmation above the spinning top's high may signal reversal. "
            "In an uptrend, treat as a warning and look for further bearish "
            "signals."
        ),
        "stop_loss_rules": (
            "Opposite end of the spinning top's range. Long: below the low. "
            "Short: above the high."
        ),
        "take_profit_rules": (
            "Target nearest support/resistance level in the breakout "
            "direction. Use 1:1.5 to 1:2 risk-reward ratio."
        ),
        "risk_reward": "1:1.5",
        "best_timeframes": ["Daily", "4H", "1H"],
        "best_markets": ["Stocks", "Forex", "Futures", "Indices"],
        "best_indicators": [
            "RSI",
            "MACD",
            "Volume",
            "Moving Averages",
            "Bollinger Bands",
        ],
        "common_mistakes": [
            "Treating it as a strong directional signal",
            "Ignoring the trend context that gives it meaning",
            "Confusing with a doji (spinning tops have a visible body)",
            "Trading without confirmation",
        ],
        "ai_features": [
            "0.10 < body_ratio < 0.30",
            "C > O (bullish body)",
            "upper_wick_ratio > 0.25",
            "lower_wick_ratio > 0.25",
            "body_ratio < upper_wick_ratio AND body_ratio < lower_wick_ratio",
        ],
        "ohlc_relationship": (
            "C > O; 0.10 < |C-O|/(H-L) < 0.30; "
            "H - C > |C-O|; O - L > |C-O|"
        ),
        "label": "Neutral",
        "confidence_score": 30,
        "probability_score": 50,
    },

    # -----------------------------------------------------------------
    # 11. Bearish Spinning Top
    # -----------------------------------------------------------------
    {
        "id": 10,
        "pattern_name": "Bearish Spinning Top",
        "alternative_names": ["Red Spinning Top", "Bearish Koma"],
        "japanese_name": "Koma",
        "category": "Single Candle",
        "sub_category": "Indecision",
        "sentiment": "Neutral",
        "expected_direction": "INDECISION",
        "trend_required": "Any",
        "num_candles": 1,
        "pattern_structure": (
            "Small bearish (red/black) real body in the center of the range "
            "with moderate upper and lower shadows. Shadows are longer than "
            "the body but not as extreme as a long-legged doji."
        ),
        "candle_by_candle": [
            "Candle 1: Small bearish body (C < O) centered within the range. "
            "Moderate upper and lower shadows, each longer than the body but "
            "not extremely long. Total range is moderate."
        ],
        "market_psychology": (
            "Mild indecision with a slight bearish lean. Sellers managed to "
            "close below the open but neither side dominated. In an uptrend, "
            "it may be an early reversal warning. In a downtrend, it could "
            "signal exhaustion. The pattern is a caution flag rather than an "
            "actionable signal."
        ),
        "confirmation_required": (
            "Direction must be confirmed by the next candle. A bearish close "
            "below the spinning top's low supports downside; a bullish close "
            "above the high supports upside."
        ),
        "volume_confirmation": (
            "Moderate to low volume is typical. High volume suggests a "
            "significant battle between buyers and sellers, making the "
            "subsequent move more meaningful."
        ),
        "volatility_conditions": (
            "Common in moderate volatility. In very calm markets, spinning "
            "tops are routine noise. In very volatile markets, the pattern is "
            "dwarfed by larger candles."
        ),
        "gap_requirement": "None",
        "reliability": "Low",
        "success_rate_range": "50-55%",
        "failure_conditions": [
            "Prior trend simply continues without pause",
            "Pattern appears in a listless sideways market",
            "No directional follow-through on subsequent candles",
            "Body is too large relative to shadows",
            "Very low volume means mere inactivity, not genuine indecision",
        ],
        "entry_rules": (
            "Wait for confirmation candle. In an uptrend, a bearish "
            "confirmation below the spinning top's low may signal reversal. "
            "In a downtrend, treat as a pause and await direction."
        ),
        "stop_loss_rules": (
            "Opposite end of the spinning top's range. Long: below low. "
            "Short: above high."
        ),
        "take_profit_rules": (
            "Target nearest support/resistance. Use 1:1.5 to 1:2 "
            "risk-reward ratio."
        ),
        "risk_reward": "1:1.5",
        "best_timeframes": ["Daily", "4H", "1H"],
        "best_markets": ["Stocks", "Forex", "Futures", "Indices"],
        "best_indicators": [
            "RSI",
            "MACD",
            "Volume",
            "Moving Averages",
            "Bollinger Bands",
        ],
        "common_mistakes": [
            "Treating it as a strong bearish reversal on its own",
            "Ignoring the trend that preceded it",
            "Confusing with a doji (spinning tops have a visible body)",
            "Over-weighting a single candle in a noisy market",
        ],
        "ai_features": [
            "0.10 < body_ratio < 0.30",
            "C < O (bearish body)",
            "upper_wick_ratio > 0.25",
            "lower_wick_ratio > 0.25",
            "body_ratio < upper_wick_ratio AND body_ratio < lower_wick_ratio",
        ],
        "ohlc_relationship": (
            "C < O; 0.10 < |C-O|/(H-L) < 0.30; "
            "H - O > |C-O|; C - L > |C-O|"
        ),
        "label": "Neutral",
        "confidence_score": 30,
        "probability_score": 50,
    },

    # -----------------------------------------------------------------
    # 12. Bullish Marubozu
    # -----------------------------------------------------------------
    {
        "id": 11,
        "pattern_name": "Bullish Marubozu",
        "alternative_names": ["White Marubozu", "Full Bullish Candle", "Shaved Head and Bottom Bull"],
        "japanese_name": "Marubozu",
        "category": "Single Candle",
        "sub_category": "Bullish Continuation",
        "sentiment": "Bullish",
        "expected_direction": "CONTINUATION_UP",
        "trend_required": "Any",
        "num_candles": 1,
        "pattern_structure": (
            "Very large bullish body with no upper shadow and no lower shadow "
            "(or only negligible wicks). Open equals the low; close equals "
            "the high. Represents complete buyer dominance."
        ),
        "candle_by_candle": [
            "Candle 1: Large bullish body. O = L (or near), C = H (or near). "
            "No meaningful upper or lower shadows. Buyers controlled the "
            "entire session from open to close."
        ],
        "market_psychology": (
            "Buyers dominated the session from open to close without any "
            "meaningful selling pressure at any point. This one-sided control "
            "indicates powerful bullish conviction. As a continuation signal, "
            "it suggests that the uptrend is strong and likely to persist. As "
            "a potential initiation signal, it can mark the beginning of a "
            "new uptrend."
        ),
        "confirmation_required": (
            "Generally considered a strong stand-alone signal but follow-"
            "through on the next candle (continued higher close) confirms "
            "sustained momentum."
        ),
        "volume_confirmation": (
            "Above-average or significantly high volume validates the "
            "conviction. A bullish marubozu on low volume may indicate a "
            "short squeeze or illiquid gap rather than genuine demand."
        ),
        "volatility_conditions": (
            "Effective in all volatility regimes. In low volatility, a "
            "marubozu can signal the start of a breakout. In high volatility, "
            "it confirms one-sided momentum."
        ),
        "gap_requirement": "None",
        "reliability": "High",
        "success_rate_range": "60-70%",
        "failure_conditions": [
            "Immediately followed by a bearish reversal candle with high volume",
            "Occurs at strong resistance (can trap longs)",
            "Volume is unusually low for the move size",
            "Pattern appears as a gap fill or dead-cat bounce in a downtrend",
            "Preceded by a parabolic move that is over-extended",
        ],
        "entry_rules": (
            "Enter long at close of the marubozu or on a pullback to the "
            "marubozu's midpoint. Avoid chasing if price has already moved "
            "significantly beyond the close."
        ),
        "stop_loss_rules": (
            "Below the marubozu's low (open price). Conservative: midpoint "
            "of the marubozu body."
        ),
        "take_profit_rules": (
            "Target next major resistance. Use 1:2 risk-reward ratio or "
            "trail stop using the body length as a measuring tool."
        ),
        "risk_reward": "1:2",
        "best_timeframes": ["Daily", "4H", "Weekly", "1H"],
        "best_markets": ["Stocks", "Forex", "Crypto", "Futures", "Commodities"],
        "best_indicators": [
            "Volume (critical)",
            "ADX (trend strength)",
            "Moving Averages (breakout above key MA)",
            "VWAP",
            "RSI (momentum confirmation)",
        ],
        "common_mistakes": [
            "Chasing entry far above the close price",
            "Ignoring strong resistance levels above",
            "Failing to check if the move was driven by news (fades quickly)",
            "Using too tight a stop—the low of a marubozu is the natural stop",
        ],
        "ai_features": [
            "body_ratio > 0.90",
            "upper_wick_ratio < 0.05",
            "lower_wick_ratio < 0.05",
            "C > O (bullish)",
            "(C - O) / (H - L) > 0.90",
        ],
        "ohlc_relationship": (
            "C > O; O ≈ L; C ≈ H; "
            "(C - O) / (H - L) > 0.90; "
            "H - C < 0.05 * (H - L); O - L < 0.05 * (H - L)"
        ),
        "label": "Bullish",
        "confidence_score": 75,
        "probability_score": 65,
    },

    # -----------------------------------------------------------------
    # 13. Bearish Marubozu
    # -----------------------------------------------------------------
    {
        "id": 12,
        "pattern_name": "Bearish Marubozu",
        "alternative_names": ["Black Marubozu", "Full Bearish Candle", "Shaved Head and Bottom Bear"],
        "japanese_name": "Marubozu",
        "category": "Single Candle",
        "sub_category": "Bearish Continuation",
        "sentiment": "Bearish",
        "expected_direction": "CONTINUATION_DOWN",
        "trend_required": "Any",
        "num_candles": 1,
        "pattern_structure": (
            "Very large bearish body with no upper shadow and no lower shadow "
            "(or only negligible wicks). Open equals the high; close equals "
            "the low. Represents complete seller dominance."
        ),
        "candle_by_candle": [
            "Candle 1: Large bearish body. O = H (or near), C = L (or near). "
            "No meaningful upper or lower shadows. Sellers controlled the "
            "entire session from open to close."
        ],
        "market_psychology": (
            "Sellers dominated the session from open to close with no "
            "meaningful buying pressure at any point. This total bearish "
            "control indicates panic selling or strong distribution. As a "
            "continuation signal, it confirms that the downtrend has strong "
            "momentum. It can also initiate a new downtrend if it breaks key "
            "support."
        ),
        "confirmation_required": (
            "Strong stand-alone signal, but a follow-through bearish candle "
            "on the next session confirms persistent selling pressure."
        ),
        "volume_confirmation": (
            "High volume is essential for validation. A bearish marubozu on "
            "high volume indicates genuine institutional selling. Low volume "
            "may indicate a thin-market slide that reverses quickly."
        ),
        "volatility_conditions": (
            "Effective across volatility regimes. Often marks the start of "
            "increased volatility as panic sets in. In low-volatility "
            "environments, a marubozu breakout can signal a regime change."
        ),
        "gap_requirement": "None",
        "reliability": "High",
        "success_rate_range": "60-70%",
        "failure_conditions": [
            "Immediately followed by a strong bullish reversal candle",
            "Occurs at strong support (can trigger a bounce)",
            "Volume is very low for the move size",
            "Market is deeply oversold with positive divergences forming",
            "Pattern follows an already exhausted, parabolic sell-off",
        ],
        "entry_rules": (
            "Enter short at close of the marubozu or on a pullback to the "
            "marubozu's midpoint. Avoid chasing if price has already fallen "
            "significantly beyond the close."
        ),
        "stop_loss_rules": (
            "Above the marubozu's high (open price). Conservative: midpoint "
            "of the marubozu body."
        ),
        "take_profit_rules": (
            "Target next major support level. Use 1:2 risk-reward ratio or "
            "trail stop using the body length as a measuring tool."
        ),
        "risk_reward": "1:2",
        "best_timeframes": ["Daily", "4H", "Weekly", "1H"],
        "best_markets": ["Stocks", "Forex", "Crypto", "Futures", "Commodities"],
        "best_indicators": [
            "Volume (critical)",
            "ADX (trend strength)",
            "Moving Averages (breakdown below key MA)",
            "VWAP",
            "RSI (momentum confirmation)",
        ],
        "common_mistakes": [
            "Chasing short entry far below the close price",
            "Ignoring strong support levels below",
            "Failing to check if selling was event-driven (gap fills fast)",
            "Using too tight a stop—the high of a marubozu is the natural stop",
        ],
        "ai_features": [
            "body_ratio > 0.90",
            "upper_wick_ratio < 0.05",
            "lower_wick_ratio < 0.05",
            "C < O (bearish)",
            "(O - C) / (H - L) > 0.90",
        ],
        "ohlc_relationship": (
            "C < O; O ≈ H; C ≈ L; "
            "(O - C) / (H - L) > 0.90; "
            "H - O < 0.05 * (H - L); C - L < 0.05 * (H - L)"
        ),
        "label": "Bearish",
        "confidence_score": 75,
        "probability_score": 65,
    },

    # -----------------------------------------------------------------
    # 14. High Wave Candle
    # -----------------------------------------------------------------
    {
        "id": 13,
        "pattern_name": "High Wave Candle",
        "alternative_names": ["High Wave", "Takane Nami"],
        "japanese_name": "Takane Nami",
        "category": "Single Candle",
        "sub_category": "Indecision",
        "sentiment": "Neutral",
        "expected_direction": "INDECISION",
        "trend_required": "Any",
        "num_candles": 1,
        "pattern_structure": (
            "Very small real body (bullish or bearish) positioned near the "
            "middle of the range, with extremely long upper AND lower shadows. "
            "Similar to a long-legged doji but the body is slightly larger, "
            "still very small relative to the total range."
        ),
        "candle_by_candle": [
            "Candle 1: Very small body (bullish or bearish) roughly centered. "
            "Extremely long upper shadow AND extremely long lower shadow. "
            "Total range is very large relative to the body and to recent "
            "candles. Body size distinguishes it from a long-legged doji—"
            "there is a visible, though tiny, real body."
        ],
        "market_psychology": (
            "Extreme confusion and indecision in the market. Price oscillated "
            "wildly in both directions during the session, with both buyers "
            "and sellers exerting tremendous pressure, but ultimately the "
            "close ended near the open. This extreme uncertainty after a "
            "trend often signals that a major turning point may be near—"
            "but direction is unknown until confirmed."
        ),
        "confirmation_required": (
            "Critical—do not trade this pattern without directional "
            "confirmation. A strong close above or below the high wave "
            "candle's extremes provides the entry signal."
        ),
        "volume_confirmation": (
            "Very high volume during a high wave candle suggests a climactic "
            "battle between buyers and sellers. This makes the eventual "
            "breakout direction more significant and tradeable."
        ),
        "volatility_conditions": (
            "By nature, this pattern represents extreme intraday volatility. "
            "Most meaningful at the end of a sustained trend or at key "
            "support/resistance levels where a reversal decision is being "
            "made."
        ),
        "gap_requirement": "None",
        "reliability": "Low",
        "success_rate_range": "50-55%",
        "failure_conditions": [
            "No decisive follow-through in either direction",
            "More indecision candles follow, creating a stalling zone",
            "Appears in a range-bound market without trend context",
            "Shadows are not significantly larger than surrounding candles",
            "Low volume reduces the significance of the volatility spike",
        ],
        "entry_rules": (
            "Wait for a decisive breakout candle. Long if next candle closes "
            "above the high wave high; short if it closes below the low. "
            "The pattern itself provides no directional bias."
        ),
        "stop_loss_rules": (
            "Opposite extreme of the high wave candle. Note: stop distances "
            "are very wide due to the extreme range."
        ),
        "take_profit_rules": (
            "Due to wide stops, target at least 1:2 risk-reward. Major "
            "support/resistance in the breakout direction."
        ),
        "risk_reward": "1:2",
        "best_timeframes": ["Daily", "4H", "Weekly"],
        "best_markets": ["Stocks", "Forex", "Crypto", "Futures"],
        "best_indicators": [
            "Volume (critical for assessing conviction)",
            "ATR (to contextualize the range expansion)",
            "RSI (extremes may hint at direction)",
            "Bollinger Bands (expansion signal)",
            "Support/Resistance levels",
        ],
        "common_mistakes": [
            "Trading the high wave candle without waiting for confirmation",
            "Ignoring the extremely wide stop-loss requirements",
            "Confusing with a long-legged doji—high wave has a small but visible body",
            "Expecting a specific direction without confirmation",
        ],
        "ai_features": [
            "0.03 < body_ratio < 0.15",
            "upper_wick_ratio > 0.35",
            "lower_wick_ratio > 0.35",
            "(H - L) > 2.0 * ATR(14)",
            "|C - O| / (H - L) < 0.15",
        ],
        "ohlc_relationship": (
            "0.03 < |C-O| / (H-L) < 0.15; "
            "H - max(O,C) > 0.35 * (H-L); "
            "min(O,C) - L > 0.35 * (H-L)"
        ),
        "label": "Neutral",
        "confidence_score": 30,
        "probability_score": 50,
    },

    # -----------------------------------------------------------------
    # 15. Bullish Belt Hold
    # -----------------------------------------------------------------
    {
        "id": 14,
        "pattern_name": "Bullish Belt Hold",
        "alternative_names": ["Belt Hold Line (Bullish)", "Bullish Yorikiri"],
        "japanese_name": "Yorikiri",
        "category": "Single Candle",
        "sub_category": "Bullish Reversal",
        "sentiment": "Bullish",
        "expected_direction": "UP",
        "trend_required": "Downtrend",
        "num_candles": 1,
        "pattern_structure": (
            "A tall bullish candle that opens at or very near its low, then "
            "rallies strongly to close at or near its high. No lower shadow "
            "(or negligible). May have a small upper shadow. The body is "
            "large and represents a decisive shift from selling to buying."
        ),
        "candle_by_candle": [
            "Candle 1: Large bullish body. Opens at or very near the session "
            "low (O ≈ L, no meaningful lower shadow). Closes near the session "
            "high. A small upper shadow is acceptable. The body is long "
            "relative to recent candles."
        ],
        "market_psychology": (
            "After a downtrend, the session opens at the extreme low—bears "
            "are in full control at the open. However, buyers aggressively "
            "step in immediately and drive price higher throughout the entire "
            "session, closing near the high. This immediate and sustained "
            "reversal from the opening low signals a decisive shift in "
            "sentiment and the potential start of an uptrend."
        ),
        "confirmation_required": (
            "A bullish confirmation candle on the following session (closing "
            "above the belt hold's high) strengthens the signal. The longer "
            "the body and the deeper the preceding downtrend, the less "
            "confirmation is needed."
        ),
        "volume_confirmation": (
            "Above-average volume on the belt hold is important for "
            "validating the buying conviction. High volume suggests "
            "institutional accumulation at the lows."
        ),
        "volatility_conditions": (
            "Most effective when volatility has been elevated during the "
            "preceding downtrend and the belt hold marks a volatility "
            "contraction. Effective in normal to elevated volatility."
        ),
        "gap_requirement": "Preferred",
        "reliability": "Medium",
        "success_rate_range": "55-65%",
        "failure_conditions": [
            "No follow-through—next candle reverses the gains",
            "Pattern body is too small relative to recent candles",
            "Lower shadow is noticeable (weakens the O ≈ L requirement)",
            "Strong overhead resistance limits upside potential",
            "Volume is below average—conviction is questionable",
        ],
        "entry_rules": (
            "Enter long at the close of the belt hold candle or on "
            "confirmation above the high. A gap up open on the next candle "
            "is a strong confirmation entry."
        ),
        "stop_loss_rules": (
            "Below the belt hold's low (which is approximately the open). "
            "Conservative: 1 ATR below the low."
        ),
        "take_profit_rules": (
            "Target nearest resistance, previous swing high, or "
            "use 1:2 to 1:3 risk-reward ratio."
        ),
        "risk_reward": "1:2",
        "best_timeframes": ["Daily", "4H", "Weekly"],
        "best_markets": ["Stocks", "Forex", "Futures", "Commodities", "Crypto"],
        "best_indicators": [
            "RSI (oversold)",
            "Volume",
            "Support levels",
            "MACD (bullish divergence)",
            "Moving Averages (potential reclaim of key MA)",
        ],
        "common_mistakes": [
            "Accepting a pattern with a significant lower shadow (O must ≈ L)",
            "Ignoring the preceding downtrend requirement",
            "Confusing with a standard large bullish candle that has a lower wick",
            "Trading without checking volume confirmation",
        ],
        "ai_features": [
            "body_ratio > 0.60",
            "lower_wick_ratio < 0.05",
            "C > O (bullish)",
            "O ≈ L: (O - L) / (H - L) < 0.05",
            "(C - O) / (H - L) > 0.60",
        ],
        "ohlc_relationship": (
            "C > O; O - L < 0.05 * (H - L); "
            "(C - O) / (H - L) > 0.60; body is large relative to recent candles"
        ),
        "label": "Bullish",
        "confidence_score": 55,
        "probability_score": 60,
    },

    # -----------------------------------------------------------------
    # 16. Bearish Belt Hold
    # -----------------------------------------------------------------
    {
        "id": 15,
        "pattern_name": "Bearish Belt Hold",
        "alternative_names": ["Belt Hold Line (Bearish)", "Bearish Yorikiri"],
        "japanese_name": "Yorikiri",
        "category": "Single Candle",
        "sub_category": "Bearish Reversal",
        "sentiment": "Bearish",
        "expected_direction": "DOWN",
        "trend_required": "Uptrend",
        "num_candles": 1,
        "pattern_structure": (
            "A tall bearish candle that opens at or very near its high, then "
            "sells off strongly to close at or near its low. No upper shadow "
            "(or negligible). May have a small lower shadow. The body is "
            "large and represents a decisive shift from buying to selling."
        ),
        "candle_by_candle": [
            "Candle 1: Large bearish body. Opens at or very near the session "
            "high (O ≈ H, no meaningful upper shadow). Closes near the "
            "session low. A small lower shadow is acceptable. The body is "
            "long relative to recent candles."
        ],
        "market_psychology": (
            "After an uptrend, the session opens at the extreme high—bulls "
            "are in full control at the open. However, sellers immediately "
            "overwhelm buyers and drive price lower throughout the entire "
            "session, closing near the low. This immediate and sustained "
            "sell-off from the opening high signals a decisive shift in "
            "sentiment and a potential trend reversal."
        ),
        "confirmation_required": (
            "A bearish confirmation candle on the following session (closing "
            "below the belt hold's low) strengthens the signal. The longer "
            "the body and the more extended the prior uptrend, the less "
            "confirmation is needed."
        ),
        "volume_confirmation": (
            "Above-average volume is important for validation. High volume "
            "signals institutional distribution at the highs. Low volume "
            "undermines the signal."
        ),
        "volatility_conditions": (
            "Most effective when volatility has been moderate during the "
            "preceding uptrend and the belt hold marks a shift. Effective in "
            "normal to elevated volatility."
        ),
        "gap_requirement": "Preferred",
        "reliability": "Medium",
        "success_rate_range": "55-65%",
        "failure_conditions": [
            "No follow-through—next candle reverses the losses",
            "Pattern body is too small relative to recent candles",
            "Upper shadow is noticeable (weakens the O ≈ H requirement)",
            "Strong support immediately below limits downside",
            "Volume is below average—selling conviction is weak",
        ],
        "entry_rules": (
            "Enter short at the close of the belt hold candle or on "
            "confirmation below the low. A gap down open on the next candle "
            "is a strong confirmation entry."
        ),
        "stop_loss_rules": (
            "Above the belt hold's high (which is approximately the open). "
            "Conservative: 1 ATR above the high."
        ),
        "take_profit_rules": (
            "Target nearest support, previous swing low, or "
            "use 1:2 to 1:3 risk-reward ratio."
        ),
        "risk_reward": "1:2",
        "best_timeframes": ["Daily", "4H", "Weekly"],
        "best_markets": ["Stocks", "Forex", "Futures", "Commodities", "Crypto"],
        "best_indicators": [
            "RSI (overbought)",
            "Volume",
            "Resistance levels",
            "MACD (bearish crossover)",
            "Moving Averages (potential loss of key MA)",
        ],
        "common_mistakes": [
            "Accepting a pattern with a significant upper shadow (O must ≈ H)",
            "Ignoring the preceding uptrend requirement",
            "Confusing with a standard large bearish candle that has an upper wick",
            "Trading without checking volume confirmation",
        ],
        "ai_features": [
            "body_ratio > 0.60",
            "upper_wick_ratio < 0.05",
            "C < O (bearish)",
            "O ≈ H: (H - O) / (H - L) < 0.05",
            "(O - C) / (H - L) > 0.60",
        ],
        "ohlc_relationship": (
            "C < O; H - O < 0.05 * (H - L); "
            "(O - C) / (H - L) > 0.60; body is large relative to recent candles"
        ),
        "label": "Bearish",
        "confidence_score": 55,
        "probability_score": 60,
    },
]
