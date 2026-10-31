"""
Complete Japanese Candlestick Pattern Database — Python Dictionary
Total Patterns: 80
Fields per Pattern: 33
Generated: 2026-07-08T23:53:39.256155

Usage:
    from candlestick_patterns_dict import CANDLESTICK_PATTERNS
    for p in CANDLESTICK_PATTERNS:
        print(p["pattern_name"], p["expected_direction"])
"""

CANDLESTICK_PATTERNS = [
    {
        "id": 1,
        "pattern_name": "Hammer",
        "alternative_names": [
            "Takuri",
            "Hammer Line"
        ],
        "japanese_name": "Takuri",
        "category": "Single Candle",
        "sub_category": "Bullish Reversal",
        "sentiment": "Bullish",
        "expected_direction": "UP",
        "trend_required": "Downtrend",
        "num_candles": 1,
        "pattern_structure": "Small real body near the top with a long lower shadow at least 2x the body and little or no upper shadow",
        "candle_by_candle": [
            "Candle 1: Small real body (bullish or bearish) near session high. Long lower shadow >= 2x body length. Little or no upper shadow."
        ],
        "market_psychology": "In a downtrend, sellers push price sharply lower intraday but strong buying emerges near the lows, pushing price back up to close near the open. This rejection of lower prices signals sellers losing control and potential reversal.",
        "confirmation_required": "Bullish confirmation candle closing above the hammer's high significantly increases reliability.",
        "volume_confirmation": "Higher than average volume on the hammer strengthens the signal. Volume spike during the lower wick formation indicates institutional buying.",
        "volatility_conditions": "Most effective in normal to moderately elevated volatility. Less reliable in extreme volatility or very low volatility.",
        "gap_requirement": "None",
        "reliability": "Medium",
        "success_rate_range": "55-65%",
        "failure_conditions": [
            "No bullish confirmation follows",
            "Appears in sideways market rather than downtrend",
            "Lower shadow less than 2x the body",
            "Very low volume",
            "Strong resistance immediately above"
        ],
        "entry_rules": "Enter long on close of confirmation candle (closes above hammer high). Aggressive: enter at hammer close.",
        "stop_loss_rules": "Below the hammer low. Conservative: 1-2 ATR below hammer low.",
        "take_profit_rules": "Target nearest resistance or previous swing high. Or use 1:2 to 1:3 RR ratio.",
        "risk_reward": "1:2",
        "best_timeframes": [
            "Daily",
            "4H",
            "Weekly"
        ],
        "best_markets": [
            "Stocks",
            "Forex",
            "Crypto",
            "Futures",
            "Commodities"
        ],
        "best_indicators": [
            "RSI (oversold)",
            "MACD (divergence)",
            "Volume",
            "Support/Resistance",
            "Moving Averages"
        ],
        "common_mistakes": [
            "Trading without confirmation",
            "Identifying in non-trending markets",
            "Ignoring prior trend context",
            "Confusing with Hanging Man (uptrend version)"
        ],
        "ai_features": [
            "body_ratio < 0.30",
            "lower_wick_ratio > 0.55",
            "upper_wick_ratio < 0.15",
            "prior_trend = downtrend",
            "lower_shadow / body >= 2.0"
        ],
        "ohlc_relationship": "lower_wick = min(O,C) - L > 2 * |C-O|; upper_wick = H - max(O,C) < 0.15 * (H-L); body_ratio < 0.30",
        "label": "Bullish",
        "confidence_score": 60,
        "probability_score": 60
    },
    {
        "id": 2,
        "pattern_name": "Inverted Hammer",
        "alternative_names": [
            "Inverted Hammer Line",
            "Reverse Hammer"
        ],
        "japanese_name": "Tohba",
        "category": "Single Candle",
        "sub_category": "Bullish Reversal",
        "sentiment": "Bullish",
        "expected_direction": "UP",
        "trend_required": "Downtrend",
        "num_candles": 1,
        "pattern_structure": "Small real body near the bottom of the candle with a long upper shadow at least 2x the body length and little or no lower shadow.",
        "candle_by_candle": [
            "Candle 1: Small real body (bullish or bearish) near session low. Long upper shadow >= 2x body length. Little or no lower shadow."
        ],
        "market_psychology": "During a downtrend, buyers attempt to push prices significantly higher intraday, but sellers still manage to pull the close back down near the open. However, the buying attempt itself suggests that bullish sentiment is building and a reversal may follow once buyers gain confidence.",
        "confirmation_required": "Strong bullish confirmation is essential—next candle should close above the inverted hammer's high. Without confirmation, this pattern is unreliable.",
        "volume_confirmation": "Above-average volume on the inverted hammer adds credibility. Rising volume on the confirmation candle further validates the reversal signal.",
        "volatility_conditions": "Works best in moderate volatility environments. In extremely volatile markets, the long upper shadow may be noise rather than a meaningful buying attempt.",
        "gap_requirement": "None",
        "reliability": "Low",
        "success_rate_range": "50-60%",
        "failure_conditions": [
            "No bullish confirmation candle follows",
            "Appears in a range-bound market",
            "Upper shadow less than 2x the body",
            "Heavy overhead resistance within the upper shadow range",
            "Declining volume on the pattern and confirmation"
        ],
        "entry_rules": "Enter long after bullish confirmation candle closes above the inverted hammer's high. Aggressive entry at the open of the next candle is higher risk.",
        "stop_loss_rules": "Below the inverted hammer's low. Conservative: 1-2 ATR below the pattern low.",
        "take_profit_rules": "Target previous swing high or nearest resistance level. Use 1:2 to 1:3 risk-reward ratio.",
        "risk_reward": "1:2",
        "best_timeframes": [
            "Daily",
            "4H",
            "Weekly"
        ],
        "best_markets": [
            "Stocks",
            "Forex",
            "Futures",
            "Commodities"
        ],
        "best_indicators": [
            "RSI (oversold)",
            "Stochastic (oversold)",
            "Volume",
            "Support levels",
            "Bollinger Bands (lower band touch)"
        ],
        "common_mistakes": [
            "Trading without confirmation—this is the most common error",
            "Confusing with Shooting Star (which appears in uptrends)",
            "Ignoring the prior downtrend requirement",
            "Over-relying on the pattern without confluence"
        ],
        "ai_features": [
            "body_ratio < 0.30",
            "upper_wick_ratio > 0.55",
            "lower_wick_ratio < 0.15",
            "prior_trend = downtrend",
            "upper_shadow / body >= 2.0"
        ],
        "ohlc_relationship": "upper_wick = H - max(O,C) > 2 * |C-O|; lower_wick = min(O,C) - L < 0.15 * (H-L); body_ratio < 0.30",
        "label": "Bullish",
        "confidence_score": 45,
        "probability_score": 55
    },
    {
        "id": 3,
        "pattern_name": "Hanging Man",
        "alternative_names": [
            "Hanging Man Line"
        ],
        "japanese_name": "Kubitsuri",
        "category": "Single Candle",
        "sub_category": "Bearish Reversal",
        "sentiment": "Bearish",
        "expected_direction": "DOWN",
        "trend_required": "Uptrend",
        "num_candles": 1,
        "pattern_structure": "Small real body near the top of the candle with a long lower shadow at least 2x the body length and little or no upper shadow. Identical shape to Hammer but appears in an uptrend.",
        "candle_by_candle": [
            "Candle 1: Small real body (bullish or bearish) near session high. Long lower shadow >= 2x body length. Little or no upper shadow. Appears after a sustained uptrend."
        ],
        "market_psychology": "After a rally, price drops sharply intraday—revealing that sellers are becoming more aggressive. Although buyers manage to push price back up near the open, the deep intraday selloff is an early warning that the uptrend may be exhausting. The pattern suggests distribution is beginning.",
        "confirmation_required": "Bearish confirmation candle closing below the hanging man's body (ideally below its low) is strongly recommended before acting.",
        "volume_confirmation": "Above-average volume strengthens the signal by indicating meaningful selling pressure. A bearish-body hanging man on high volume is more reliable than a bullish-body one.",
        "volatility_conditions": "Effective in normal volatility. In very high volatility, the long lower shadow may simply reflect market noise. Best when preceded by a clean, sustained uptrend.",
        "gap_requirement": "Optional",
        "reliability": "Medium",
        "success_rate_range": "50-60%",
        "failure_conditions": [
            "No bearish confirmation follows",
            "Appears in a sideways or weak uptrend",
            "Lower shadow shorter than 2x the body",
            "Strong support just below the pattern",
            "Volume is declining rather than expanding"
        ],
        "entry_rules": "Enter short on close of bearish confirmation candle (closes below hanging man's low). Aggressive: enter at hanging man close if body is bearish.",
        "stop_loss_rules": "Above the hanging man's high. Conservative: 1-2 ATR above the pattern high.",
        "take_profit_rules": "Target nearest support level or prior swing low. Use 1:2 to 1:3 risk-reward ratio.",
        "risk_reward": "1:2",
        "best_timeframes": [
            "Daily",
            "4H",
            "Weekly"
        ],
        "best_markets": [
            "Stocks",
            "Forex",
            "Crypto",
            "Futures",
            "Commodities"
        ],
        "best_indicators": [
            "RSI (overbought)",
            "MACD (bearish crossover)",
            "Volume",
            "Resistance/Supply zones",
            "Moving Averages"
        ],
        "common_mistakes": [
            "Confusing with Hammer (which requires a downtrend)",
            "Trading without bearish confirmation",
            "Ignoring the strength and duration of the prior uptrend",
            "Placing stop too tight—the high of the hanging man can be retested"
        ],
        "ai_features": [
            "body_ratio < 0.30",
            "lower_wick_ratio > 0.55",
            "upper_wick_ratio < 0.15",
            "prior_trend = uptrend",
            "lower_shadow / body >= 2.0"
        ],
        "ohlc_relationship": "lower_wick = min(O,C) - L > 2 * |C-O|; upper_wick = H - max(O,C) < 0.15 * (H-L); body_ratio < 0.30; prior_trend = uptrend",
        "label": "Bearish",
        "confidence_score": 55,
        "probability_score": 55
    },
    {
        "id": 4,
        "pattern_name": "Shooting Star",
        "alternative_names": [
            "Shooting Star Line"
        ],
        "japanese_name": "Nagare Boshi",
        "category": "Single Candle",
        "sub_category": "Bearish Reversal",
        "sentiment": "Bearish",
        "expected_direction": "DOWN",
        "trend_required": "Uptrend",
        "num_candles": 1,
        "pattern_structure": "Small real body near the bottom of the candle with a long upper shadow at least 2x the body length and little or no lower shadow. Identical shape to Inverted Hammer but appears in an uptrend.",
        "candle_by_candle": [
            "Candle 1: Small real body (bullish or bearish) near session low. Long upper shadow >= 2x body length. Little or no lower shadow. Appears after a sustained uptrend."
        ],
        "market_psychology": "During an uptrend, buyers push price to new intraday highs but sellers aggressively drive price back down to close near the open. The failed rally attempt demonstrates that overhead supply is overwhelming demand, warning of a potential trend reversal.",
        "confirmation_required": "Bearish confirmation candle closing below the shooting star's body greatly improves reliability. A gap down on the next candle is the strongest confirmation.",
        "volume_confirmation": "High volume on the shooting star signals strong conviction in the rejection. Volume expanding during the upper wick formation and on the confirmation candle bolsters the signal.",
        "volatility_conditions": "Most reliable in moderate-to-elevated volatility after a clear uptrend. Less meaningful in choppy, range-bound conditions.",
        "gap_requirement": "Preferred",
        "reliability": "Medium",
        "success_rate_range": "55-65%",
        "failure_conditions": [
            "No bearish confirmation follows",
            "Appears in a downtrend or sideways market",
            "Upper shadow less than 2x the body",
            "Strong bullish momentum continues with high volume",
            "Major support nearby limits downside follow-through"
        ],
        "entry_rules": "Enter short on bearish confirmation candle closing below the shooting star's low. Aggressive: enter at the close of the shooting star if body is bearish.",
        "stop_loss_rules": "Above the shooting star's high. Conservative: 1-2 ATR above the pattern high.",
        "take_profit_rules": "Target nearest support or previous swing low. Use 1:2 to 1:3 risk-reward ratio.",
        "risk_reward": "1:2",
        "best_timeframes": [
            "Daily",
            "4H",
            "Weekly"
        ],
        "best_markets": [
            "Stocks",
            "Forex",
            "Crypto",
            "Futures",
            "Commodities"
        ],
        "best_indicators": [
            "RSI (overbought)",
            "MACD (bearish divergence)",
            "Volume",
            "Resistance zones",
            "Fibonacci retracement levels"
        ],
        "common_mistakes": [
            "Confusing with Inverted Hammer (which requires a downtrend)",
            "Trading without confirmation",
            "Ignoring the prior uptrend requirement",
            "Placing stop below the low instead of above the high"
        ],
        "ai_features": [
            "body_ratio < 0.30",
            "upper_wick_ratio > 0.55",
            "lower_wick_ratio < 0.15",
            "prior_trend = uptrend",
            "upper_shadow / body >= 2.0"
        ],
        "ohlc_relationship": "upper_wick = H - max(O,C) > 2 * |C-O|; lower_wick = min(O,C) - L < 0.15 * (H-L); body_ratio < 0.30; prior_trend = uptrend",
        "label": "Bearish",
        "confidence_score": 60,
        "probability_score": 60
    },
    {
        "id": 5,
        "pattern_name": "Doji",
        "alternative_names": [
            "Standard Doji",
            "Neutral Doji",
            "Common Doji"
        ],
        "japanese_name": "Doji",
        "category": "Single Candle",
        "sub_category": "Indecision",
        "sentiment": "Neutral",
        "expected_direction": "INDECISION",
        "trend_required": "Any",
        "num_candles": 1,
        "pattern_structure": "Open and close are virtually equal, creating a cross or plus-sign shape. Upper and lower shadows are roughly equal and moderate in length.",
        "candle_by_candle": [
            "Candle 1: Open ≈ Close (body is extremely small or a thin line). Upper and lower shadows of roughly similar, moderate length. Visually resembles a cross."
        ],
        "market_psychology": "Buyers and sellers are in equilibrium—neither side can gain control. After a sustained trend, a doji indicates the prevailing momentum is fading and a reversal or consolidation may follow. In isolation, it is purely indecision; context determines its significance.",
        "confirmation_required": "A directional confirmation candle is critical. Bullish close above doji high suggests upside; bearish close below doji low suggests downside.",
        "volume_confirmation": "High volume on a doji highlights significant indecision and makes the subsequent breakout direction more meaningful. Low volume dojis can be ignored in most cases.",
        "volatility_conditions": "Dojis after a strong trend in moderate-to-high volatility are most significant. Dojis in low-volatility consolidation zones carry little weight.",
        "gap_requirement": "None",
        "reliability": "Low",
        "success_rate_range": "50-55%",
        "failure_conditions": [
            "No follow-through in either direction",
            "Appears in a choppy, range-bound market (noise)",
            "Very low volume—indicates lack of participation",
            "Multiple consecutive dojis (market is simply idle)",
            "Body is too large to qualify as a true doji"
        ],
        "entry_rules": "Wait for confirmation. Enter long if next candle closes above doji high; enter short if next candle closes below doji low. Do not trade the doji in isolation.",
        "stop_loss_rules": "Opposite side of the doji range. Long: below doji low. Short: above doji high.",
        "take_profit_rules": "Target nearest support or resistance in the direction of the breakout. Use 1:1.5 to 1:2 risk-reward ratio.",
        "risk_reward": "1:2",
        "best_timeframes": [
            "Daily",
            "4H",
            "Weekly"
        ],
        "best_markets": [
            "Stocks",
            "Forex",
            "Futures",
            "Indices"
        ],
        "best_indicators": [
            "RSI (extremes)",
            "Bollinger Bands",
            "Volume",
            "Support/Resistance",
            "ATR (context for volatility)"
        ],
        "common_mistakes": [
            "Trading the doji without waiting for confirmation",
            "Treating every doji as a reversal signal",
            "Ignoring the preceding trend context",
            "Failing to distinguish between doji subtypes"
        ],
        "ai_features": [
            "body_ratio < 0.05",
            "abs(O - C) / (H - L) < 0.05",
            "upper_wick_ratio ≈ lower_wick_ratio",
            "0.35 < upper_wick_ratio < 0.55",
            "0.35 < lower_wick_ratio < 0.55"
        ],
        "ohlc_relationship": "|C - O| / (H - L) < 0.05; upper_wick = H - max(O,C); lower_wick = min(O,C) - L; abs(upper_wick - lower_wick) / (H - L) < 0.20",
        "label": "Neutral",
        "confidence_score": 35,
        "probability_score": 50
    },
    {
        "id": 6,
        "pattern_name": "Dragonfly Doji",
        "alternative_names": [
            "Dragonfly",
            "Tonbo Doji"
        ],
        "japanese_name": "Tonbo",
        "category": "Single Candle",
        "sub_category": "Bullish Reversal",
        "sentiment": "Bullish",
        "expected_direction": "UP",
        "trend_required": "Downtrend",
        "num_candles": 1,
        "pattern_structure": "Open, close, and high are at or very near the same price. Long lower shadow. No or negligible upper shadow. Resembles a T shape.",
        "candle_by_candle": [
            "Candle 1: Open ≈ Close ≈ High (all near the session high). Long lower shadow showing strong intraday selling that was fully rejected. No meaningful upper shadow."
        ],
        "market_psychology": "In a downtrend, sellers drive price significantly lower intraday, but powerful buying pressure pushes price all the way back to the high by the close. The complete recovery signals that sellers have been overwhelmed—demand is asserting itself, and a reversal is likely.",
        "confirmation_required": "A bullish confirmation candle closing above the dragonfly doji's high solidifies the reversal signal. This pattern is more reliable than a standard doji but still benefits from confirmation.",
        "volume_confirmation": "High volume on the dragonfly doji—especially during the lower wick recovery—signals institutional accumulation. Confirmation on rising volume strengthens the setup.",
        "volatility_conditions": "Most meaningful in moderate volatility after a notable downtrend. In extremely volatile markets the full recovery may be random noise.",
        "gap_requirement": "None",
        "reliability": "Medium",
        "success_rate_range": "55-65%",
        "failure_conditions": [
            "No bullish follow-through on subsequent candles",
            "Appears in a sideways market or at the top of a range",
            "Lower shadow is too short to indicate meaningful rejection",
            "Heavy resistance directly overhead",
            "Volume is very low—indicates weak participation"
        ],
        "entry_rules": "Enter long on confirmation candle closing above the dragonfly doji's high. Aggressive: enter at close of the dragonfly doji itself.",
        "stop_loss_rules": "Below the dragonfly doji's low (the tail). Conservative: 1-2 ATR below the low.",
        "take_profit_rules": "Target nearest resistance, previous swing high, or use 1:2 to 1:3 risk-reward ratio.",
        "risk_reward": "1:2",
        "best_timeframes": [
            "Daily",
            "4H",
            "Weekly"
        ],
        "best_markets": [
            "Stocks",
            "Forex",
            "Crypto",
            "Futures",
            "Commodities"
        ],
        "best_indicators": [
            "RSI (oversold)",
            "MACD (bullish divergence)",
            "Volume",
            "Support levels",
            "Fibonacci retracement levels"
        ],
        "common_mistakes": [
            "Confusing with a standard Hammer—Dragonfly Doji has O ≈ C ≈ H",
            "Trading without confirmation in a shallow downtrend",
            "Ignoring overhead resistance that may cap the reversal",
            "Expecting large reversals from a single candle signal"
        ],
        "ai_features": [
            "body_ratio < 0.03",
            "upper_wick_ratio < 0.05",
            "lower_wick_ratio > 0.85",
            "abs(O - C) / (H - L) < 0.03",
            "H - max(O,C) < 0.05 * (H - L)"
        ],
        "ohlc_relationship": "|C - O| / (H - L) < 0.03; H - max(O,C) < 0.05 * (H - L); min(O,C) - L > 0.85 * (H - L)",
        "label": "Bullish",
        "confidence_score": 60,
        "probability_score": 60
    },
    {
        "id": 7,
        "pattern_name": "Gravestone Doji",
        "alternative_names": [
            "Gravestone",
            "Tohba Doji"
        ],
        "japanese_name": "Hakaishi",
        "category": "Single Candle",
        "sub_category": "Bearish Reversal",
        "sentiment": "Bearish",
        "expected_direction": "DOWN",
        "trend_required": "Uptrend",
        "num_candles": 1,
        "pattern_structure": "Open, close, and low are at or very near the same price. Long upper shadow. No or negligible lower shadow. Resembles an inverted T shape.",
        "candle_by_candle": [
            "Candle 1: Open ≈ Close ≈ Low (all near the session low). Long upper shadow showing strong intraday buying that was fully rejected. No meaningful lower shadow."
        ],
        "market_psychology": "During an uptrend, buyers push price to significant intraday highs, but sellers drive price all the way back down to the open by the close. The complete surrender of intraday gains reveals that bulls are losing power and bears are stepping in—a warning of potential reversal.",
        "confirmation_required": "Bearish confirmation candle closing below the gravestone doji's low is recommended. A gap down on the next session is the strongest confirmation.",
        "volume_confirmation": "High volume on the gravestone doji indicates meaningful selling pressure during the upper wick reversal. Rising volume on confirmation adds conviction.",
        "volatility_conditions": "Most effective after a sustained uptrend in moderate-to-elevated volatility. In low-volatility drift, the pattern may lack significance.",
        "gap_requirement": "None",
        "reliability": "Medium",
        "success_rate_range": "55-65%",
        "failure_conditions": [
            "No bearish follow-through on subsequent candles",
            "Appears in a downtrend or near the bottom of a range",
            "Upper shadow is too short to demonstrate meaningful rejection",
            "Strong support or trendline directly below",
            "Very low volume—pattern lacks conviction"
        ],
        "entry_rules": "Enter short on bearish confirmation candle closing below the gravestone doji's low. Aggressive: enter at close of the gravestone doji.",
        "stop_loss_rules": "Above the gravestone doji's high (the wick tip). Conservative: 1-2 ATR above the high.",
        "take_profit_rules": "Target nearest support, previous swing low, or use 1:2 to 1:3 risk-reward ratio.",
        "risk_reward": "1:2",
        "best_timeframes": [
            "Daily",
            "4H",
            "Weekly"
        ],
        "best_markets": [
            "Stocks",
            "Forex",
            "Crypto",
            "Futures",
            "Commodities"
        ],
        "best_indicators": [
            "RSI (overbought)",
            "MACD (bearish crossover)",
            "Volume",
            "Resistance levels",
            "Fibonacci extension levels"
        ],
        "common_mistakes": [
            "Confusing with Shooting Star—Gravestone Doji has O ≈ C ≈ L",
            "Trading without confirmation",
            "Ignoring the prior uptrend requirement",
            "Expecting guaranteed reversals from a single-candle signal"
        ],
        "ai_features": [
            "body_ratio < 0.03",
            "lower_wick_ratio < 0.05",
            "upper_wick_ratio > 0.85",
            "abs(O - C) / (H - L) < 0.03",
            "min(O,C) - L < 0.05 * (H - L)"
        ],
        "ohlc_relationship": "|C - O| / (H - L) < 0.03; min(O,C) - L < 0.05 * (H - L); H - max(O,C) > 0.85 * (H - L)",
        "label": "Bearish",
        "confidence_score": 60,
        "probability_score": 60
    },
    {
        "id": 8,
        "pattern_name": "Long-Legged Doji",
        "alternative_names": [
            "Long Legged Doji",
            "Juji Doji"
        ],
        "japanese_name": "Juji",
        "category": "Single Candle",
        "sub_category": "Indecision",
        "sentiment": "Neutral",
        "expected_direction": "INDECISION",
        "trend_required": "Any",
        "num_candles": 1,
        "pattern_structure": "Open and close are virtually equal, positioned near the middle of the candle's range. Both upper and lower shadows are exceptionally long, demonstrating extreme price volatility within the session.",
        "candle_by_candle": [
            "Candle 1: Open ≈ Close, near the midpoint of the session range. Very long upper shadow AND very long lower shadow. The total range is large relative to recent candles."
        ],
        "market_psychology": "Extreme tug-of-war between buyers and sellers within a single session. Price swings wildly in both directions but ultimately closes where it opened—neither side wins. This signals deep market uncertainty and often precedes a significant move once a direction is resolved.",
        "confirmation_required": "Directional confirmation is essential. Enter in the direction of the breakout candle. The long-legged doji alone provides no directional bias.",
        "volume_confirmation": "Very high volume on a long-legged doji underscores the intensity of the battle and makes the subsequent breakout more meaningful. Low volume reduces the pattern's significance.",
        "volatility_conditions": "By definition, this pattern occurs during elevated intraday volatility. It is most significant when it appears after a sustained trend, potentially marking a turning point.",
        "gap_requirement": "None",
        "reliability": "Low",
        "success_rate_range": "50-55%",
        "failure_conditions": [
            "No follow-through breakout in either direction",
            "Appears during low-volume, low-interest sessions",
            "Market remains range-bound with more indecision candles",
            "Shadows are not significantly longer than recent candles",
            "Occurs in the middle of a consolidation (noise)"
        ],
        "entry_rules": "Wait for a decisive close above the doji high (bullish) or below the doji low (bearish). The long range of the doji sets wide breakout levels—be patient.",
        "stop_loss_rules": "Opposite side of the doji range. Long: below doji low. Short: above doji high. Note: stops may be wide due to the long shadows.",
        "take_profit_rules": "Due to wide stops, aim for 1:2 or better risk-reward. Target next major support/resistance level in the breakout direction.",
        "risk_reward": "1:2",
        "best_timeframes": [
            "Daily",
            "4H",
            "Weekly"
        ],
        "best_markets": [
            "Stocks",
            "Forex",
            "Crypto",
            "Futures"
        ],
        "best_indicators": [
            "Volume",
            "ATR (to assess range expansion)",
            "Bollinger Bands",
            "Support/Resistance",
            "RSI (extremes)"
        ],
        "common_mistakes": [
            "Trading the pattern without waiting for directional confirmation",
            "Ignoring the wide stop-loss implications",
            "Confusing with a standard doji—long-legged doji has notably larger shadows",
            "Over-trading multiple consecutive indecision candles"
        ],
        "ai_features": [
            "body_ratio < 0.05",
            "upper_wick_ratio > 0.40",
            "lower_wick_ratio > 0.40",
            "(H - L) > 1.5 * ATR(14)",
            "abs(O - C) / (H - L) < 0.05"
        ],
        "ohlc_relationship": "|C - O| / (H - L) < 0.05; H - max(O,C) > 0.40 * (H - L); min(O,C) - L > 0.40 * (H - L)",
        "label": "Neutral",
        "confidence_score": 30,
        "probability_score": 50
    },
    {
        "id": 9,
        "pattern_name": "Four Price Doji",
        "alternative_names": [
            "Four-Price Doji",
            "Flat Doji",
            "Horizontal Line Doji"
        ],
        "japanese_name": "Yonsen Doji",
        "category": "Single Candle",
        "sub_category": "Indecision",
        "sentiment": "Neutral",
        "expected_direction": "INDECISION",
        "trend_required": "Any",
        "num_candles": 1,
        "pattern_structure": "Open, High, Low, and Close are all at the same price. The candle appears as a single horizontal line with no body and no shadows. Extremely rare on liquid instruments.",
        "candle_by_candle": [
            "Candle 1: O = H = L = C. No body, no shadows. Single horizontal dash. Indicates zero price movement during the session."
        ],
        "market_psychology": "Complete absence of price movement—no buying or selling pressure moved the market at all. This typically occurs in extremely illiquid instruments, during market holidays or pre-/post-market sessions with no participation. It signals total apathy and carries virtually no predictive value on its own.",
        "confirmation_required": "Any subsequent directional candle determines the next move. The four price doji itself is purely informational—it indicates illiquidity or extreme non-participation, not a trading signal.",
        "volume_confirmation": "Volume is typically zero or near-zero. If volume is meaningful, it may indicate a lock-limit scenario (futures) or halt, which has different implications.",
        "volatility_conditions": "Occurs only in zero-volatility conditions. Meaningful only as a liquidity or activity indicator, not as a directional signal.",
        "gap_requirement": "None",
        "reliability": "Low",
        "success_rate_range": "50-50%",
        "failure_conditions": [
            "It is not a reliable trading signal in any context",
            "Appears on illiquid instruments—no actionable information",
            "Market is closed or halted—no real price discovery",
            "Cannot be meaningfully combined with indicators",
            "Multiple consecutive four-price dojis simply confirm illiquidity"
        ],
        "entry_rules": "Do not trade this pattern directly. Use it as a liquidity filter —if a four price doji appears, the instrument may be too illiquid to trade.",
        "stop_loss_rules": "Not applicable—the pattern is not a trade signal.",
        "take_profit_rules": "Not applicable—the pattern is not a trade signal.",
        "risk_reward": "1:1",
        "best_timeframes": [
            "1M",
            "5M",
            "15M"
        ],
        "best_markets": [
            "Illiquid Stocks",
            "Pre-market Sessions",
            "Thinly Traded Futures"
        ],
        "best_indicators": [
            "Volume (to confirm illiquidity)",
            "Bid-Ask Spread (to assess market depth)",
            "Order Book Depth"
        ],
        "common_mistakes": [
            "Treating this as a meaningful reversal or continuation signal",
            "Ignoring the illiquidity that typically causes it",
            "Confusing with a standard doji that has micro-shadows",
            "Attempting to apply trend analysis to a non-event candle"
        ],
        "ai_features": [
            "body_ratio == 0.0",
            "upper_wick_ratio == 0.0",
            "lower_wick_ratio == 0.0",
            "H == L == O == C",
            "(H - L) == 0"
        ],
        "ohlc_relationship": "O == H == L == C; (H - L) == 0; body == 0; shadows == 0",
        "label": "Neutral",
        "confidence_score": 10,
        "probability_score": 50
    },
    {
        "id": 10,
        "pattern_name": "Bullish Spinning Top",
        "alternative_names": [
            "Green Spinning Top",
            "Bullish Koma"
        ],
        "japanese_name": "Koma",
        "category": "Single Candle",
        "sub_category": "Indecision",
        "sentiment": "Neutral",
        "expected_direction": "INDECISION",
        "trend_required": "Any",
        "num_candles": 1,
        "pattern_structure": "Small bullish (green/white) real body in the center of the range with moderate upper and lower shadows. Shadows are longer than the body but not as extreme as a long-legged doji.",
        "candle_by_candle": [
            "Candle 1: Small bullish body (C > O) centered within the range. Moderate upper and lower shadows, each longer than the body but not extremely long. Total range is moderate."
        ],
        "market_psychology": "Mild indecision with a slight bullish lean. Buyers managed to close above the open but neither side dominated the session. In an uptrend, it suggests slowing momentum. In a downtrend, it hints at potential stabilization. Context determines whether this is a pause or an early warning.",
        "confirmation_required": "The next candle determines direction. A strong close in either direction provides the actionable signal. The spinning top alone is not a high-confidence entry.",
        "volume_confirmation": "Moderate to low volume is typical. High volume on a spinning top indicates notable uncertainty among participants with large positions.",
        "volatility_conditions": "Common in moderate volatility environments. Less significant in very low or very high volatility conditions.",
        "gap_requirement": "None",
        "reliability": "Low",
        "success_rate_range": "50-55%",
        "failure_conditions": [
            "Market continues its prior trend without reversal",
            "Appears in a sideways range with no trend context",
            "No follow-through in either direction",
            "Body is too large relative to the shadows (not a spinning top)",
            "Very low volume indicates mere inactivity, not indecision"
        ],
        "entry_rules": "Wait for confirmation candle. In a downtrend, a bullish confirmation above the spinning top's high may signal reversal. In an uptrend, treat as a warning and look for further bearish signals.",
        "stop_loss_rules": "Opposite end of the spinning top's range. Long: below the low. Short: above the high.",
        "take_profit_rules": "Target nearest support/resistance level in the breakout direction. Use 1:1.5 to 1:2 risk-reward ratio.",
        "risk_reward": "1:1.5",
        "best_timeframes": [
            "Daily",
            "4H",
            "1H"
        ],
        "best_markets": [
            "Stocks",
            "Forex",
            "Futures",
            "Indices"
        ],
        "best_indicators": [
            "RSI",
            "MACD",
            "Volume",
            "Moving Averages",
            "Bollinger Bands"
        ],
        "common_mistakes": [
            "Treating it as a strong directional signal",
            "Ignoring the trend context that gives it meaning",
            "Confusing with a doji (spinning tops have a visible body)",
            "Trading without confirmation"
        ],
        "ai_features": [
            "0.10 < body_ratio < 0.30",
            "C > O (bullish body)",
            "upper_wick_ratio > 0.25",
            "lower_wick_ratio > 0.25",
            "body_ratio < upper_wick_ratio AND body_ratio < lower_wick_ratio"
        ],
        "ohlc_relationship": "C > O; 0.10 < |C-O|/(H-L) < 0.30; H - C > |C-O|; O - L > |C-O|",
        "label": "Neutral",
        "confidence_score": 30,
        "probability_score": 50
    },
    {
        "id": 11,
        "pattern_name": "Bearish Spinning Top",
        "alternative_names": [
            "Red Spinning Top",
            "Bearish Koma"
        ],
        "japanese_name": "Koma",
        "category": "Single Candle",
        "sub_category": "Indecision",
        "sentiment": "Neutral",
        "expected_direction": "INDECISION",
        "trend_required": "Any",
        "num_candles": 1,
        "pattern_structure": "Small bearish (red/black) real body in the center of the range with moderate upper and lower shadows. Shadows are longer than the body but not as extreme as a long-legged doji.",
        "candle_by_candle": [
            "Candle 1: Small bearish body (C < O) centered within the range. Moderate upper and lower shadows, each longer than the body but not extremely long. Total range is moderate."
        ],
        "market_psychology": "Mild indecision with a slight bearish lean. Sellers managed to close below the open but neither side dominated. In an uptrend, it may be an early reversal warning. In a downtrend, it could signal exhaustion. The pattern is a caution flag rather than an actionable signal.",
        "confirmation_required": "Direction must be confirmed by the next candle. A bearish close below the spinning top's low supports downside; a bullish close above the high supports upside.",
        "volume_confirmation": "Moderate to low volume is typical. High volume suggests a significant battle between buyers and sellers, making the subsequent move more meaningful.",
        "volatility_conditions": "Common in moderate volatility. In very calm markets, spinning tops are routine noise. In very volatile markets, the pattern is dwarfed by larger candles.",
        "gap_requirement": "None",
        "reliability": "Low",
        "success_rate_range": "50-55%",
        "failure_conditions": [
            "Prior trend simply continues without pause",
            "Pattern appears in a listless sideways market",
            "No directional follow-through on subsequent candles",
            "Body is too large relative to shadows",
            "Very low volume means mere inactivity, not genuine indecision"
        ],
        "entry_rules": "Wait for confirmation candle. In an uptrend, a bearish confirmation below the spinning top's low may signal reversal. In a downtrend, treat as a pause and await direction.",
        "stop_loss_rules": "Opposite end of the spinning top's range. Long: below low. Short: above high.",
        "take_profit_rules": "Target nearest support/resistance. Use 1:1.5 to 1:2 risk-reward ratio.",
        "risk_reward": "1:1.5",
        "best_timeframes": [
            "Daily",
            "4H",
            "1H"
        ],
        "best_markets": [
            "Stocks",
            "Forex",
            "Futures",
            "Indices"
        ],
        "best_indicators": [
            "RSI",
            "MACD",
            "Volume",
            "Moving Averages",
            "Bollinger Bands"
        ],
        "common_mistakes": [
            "Treating it as a strong bearish reversal on its own",
            "Ignoring the trend that preceded it",
            "Confusing with a doji (spinning tops have a visible body)",
            "Over-weighting a single candle in a noisy market"
        ],
        "ai_features": [
            "0.10 < body_ratio < 0.30",
            "C < O (bearish body)",
            "upper_wick_ratio > 0.25",
            "lower_wick_ratio > 0.25",
            "body_ratio < upper_wick_ratio AND body_ratio < lower_wick_ratio"
        ],
        "ohlc_relationship": "C < O; 0.10 < |C-O|/(H-L) < 0.30; H - O > |C-O|; C - L > |C-O|",
        "label": "Neutral",
        "confidence_score": 30,
        "probability_score": 50
    },
    {
        "id": 12,
        "pattern_name": "Bullish Marubozu",
        "alternative_names": [
            "White Marubozu",
            "Full Bullish Candle",
            "Shaved Head and Bottom Bull"
        ],
        "japanese_name": "Marubozu",
        "category": "Single Candle",
        "sub_category": "Bullish Continuation",
        "sentiment": "Bullish",
        "expected_direction": "CONTINUATION_UP",
        "trend_required": "Any",
        "num_candles": 1,
        "pattern_structure": "Very large bullish body with no upper shadow and no lower shadow (or only negligible wicks). Open equals the low; close equals the high. Represents complete buyer dominance.",
        "candle_by_candle": [
            "Candle 1: Large bullish body. O = L (or near), C = H (or near). No meaningful upper or lower shadows. Buyers controlled the entire session from open to close."
        ],
        "market_psychology": "Buyers dominated the session from open to close without any meaningful selling pressure at any point. This one-sided control indicates powerful bullish conviction. As a continuation signal, it suggests that the uptrend is strong and likely to persist. As a potential initiation signal, it can mark the beginning of a new uptrend.",
        "confirmation_required": "Generally considered a strong stand-alone signal but follow-through on the next candle (continued higher close) confirms sustained momentum.",
        "volume_confirmation": "Above-average or significantly high volume validates the conviction. A bullish marubozu on low volume may indicate a short squeeze or illiquid gap rather than genuine demand.",
        "volatility_conditions": "Effective in all volatility regimes. In low volatility, a marubozu can signal the start of a breakout. In high volatility, it confirms one-sided momentum.",
        "gap_requirement": "None",
        "reliability": "High",
        "success_rate_range": "60-70%",
        "failure_conditions": [
            "Immediately followed by a bearish reversal candle with high volume",
            "Occurs at strong resistance (can trap longs)",
            "Volume is unusually low for the move size",
            "Pattern appears as a gap fill or dead-cat bounce in a downtrend",
            "Preceded by a parabolic move that is over-extended"
        ],
        "entry_rules": "Enter long at close of the marubozu or on a pullback to the marubozu's midpoint. Avoid chasing if price has already moved significantly beyond the close.",
        "stop_loss_rules": "Below the marubozu's low (open price). Conservative: midpoint of the marubozu body.",
        "take_profit_rules": "Target next major resistance. Use 1:2 risk-reward ratio or trail stop using the body length as a measuring tool.",
        "risk_reward": "1:2",
        "best_timeframes": [
            "Daily",
            "4H",
            "Weekly",
            "1H"
        ],
        "best_markets": [
            "Stocks",
            "Forex",
            "Crypto",
            "Futures",
            "Commodities"
        ],
        "best_indicators": [
            "Volume (critical)",
            "ADX (trend strength)",
            "Moving Averages (breakout above key MA)",
            "VWAP",
            "RSI (momentum confirmation)"
        ],
        "common_mistakes": [
            "Chasing entry far above the close price",
            "Ignoring strong resistance levels above",
            "Failing to check if the move was driven by news (fades quickly)",
            "Using too tight a stop—the low of a marubozu is the natural stop"
        ],
        "ai_features": [
            "body_ratio > 0.90",
            "upper_wick_ratio < 0.05",
            "lower_wick_ratio < 0.05",
            "C > O (bullish)",
            "(C - O) / (H - L) > 0.90"
        ],
        "ohlc_relationship": "C > O; O ≈ L; C ≈ H; (C - O) / (H - L) > 0.90; H - C < 0.05 * (H - L); O - L < 0.05 * (H - L)",
        "label": "Bullish",
        "confidence_score": 75,
        "probability_score": 65
    },
    {
        "id": 13,
        "pattern_name": "Bearish Marubozu",
        "alternative_names": [
            "Black Marubozu",
            "Full Bearish Candle",
            "Shaved Head and Bottom Bear"
        ],
        "japanese_name": "Marubozu",
        "category": "Single Candle",
        "sub_category": "Bearish Continuation",
        "sentiment": "Bearish",
        "expected_direction": "CONTINUATION_DOWN",
        "trend_required": "Any",
        "num_candles": 1,
        "pattern_structure": "Very large bearish body with no upper shadow and no lower shadow (or only negligible wicks). Open equals the high; close equals the low. Represents complete seller dominance.",
        "candle_by_candle": [
            "Candle 1: Large bearish body. O = H (or near), C = L (or near). No meaningful upper or lower shadows. Sellers controlled the entire session from open to close."
        ],
        "market_psychology": "Sellers dominated the session from open to close with no meaningful buying pressure at any point. This total bearish control indicates panic selling or strong distribution. As a continuation signal, it confirms that the downtrend has strong momentum. It can also initiate a new downtrend if it breaks key support.",
        "confirmation_required": "Strong stand-alone signal, but a follow-through bearish candle on the next session confirms persistent selling pressure.",
        "volume_confirmation": "High volume is essential for validation. A bearish marubozu on high volume indicates genuine institutional selling. Low volume may indicate a thin-market slide that reverses quickly.",
        "volatility_conditions": "Effective across volatility regimes. Often marks the start of increased volatility as panic sets in. In low-volatility environments, a marubozu breakout can signal a regime change.",
        "gap_requirement": "None",
        "reliability": "High",
        "success_rate_range": "60-70%",
        "failure_conditions": [
            "Immediately followed by a strong bullish reversal candle",
            "Occurs at strong support (can trigger a bounce)",
            "Volume is very low for the move size",
            "Market is deeply oversold with positive divergences forming",
            "Pattern follows an already exhausted, parabolic sell-off"
        ],
        "entry_rules": "Enter short at close of the marubozu or on a pullback to the marubozu's midpoint. Avoid chasing if price has already fallen significantly beyond the close.",
        "stop_loss_rules": "Above the marubozu's high (open price). Conservative: midpoint of the marubozu body.",
        "take_profit_rules": "Target next major support level. Use 1:2 risk-reward ratio or trail stop using the body length as a measuring tool.",
        "risk_reward": "1:2",
        "best_timeframes": [
            "Daily",
            "4H",
            "Weekly",
            "1H"
        ],
        "best_markets": [
            "Stocks",
            "Forex",
            "Crypto",
            "Futures",
            "Commodities"
        ],
        "best_indicators": [
            "Volume (critical)",
            "ADX (trend strength)",
            "Moving Averages (breakdown below key MA)",
            "VWAP",
            "RSI (momentum confirmation)"
        ],
        "common_mistakes": [
            "Chasing short entry far below the close price",
            "Ignoring strong support levels below",
            "Failing to check if selling was event-driven (gap fills fast)",
            "Using too tight a stop—the high of a marubozu is the natural stop"
        ],
        "ai_features": [
            "body_ratio > 0.90",
            "upper_wick_ratio < 0.05",
            "lower_wick_ratio < 0.05",
            "C < O (bearish)",
            "(O - C) / (H - L) > 0.90"
        ],
        "ohlc_relationship": "C < O; O ≈ H; C ≈ L; (O - C) / (H - L) > 0.90; H - O < 0.05 * (H - L); C - L < 0.05 * (H - L)",
        "label": "Bearish",
        "confidence_score": 75,
        "probability_score": 65
    },
    {
        "id": 14,
        "pattern_name": "High Wave Candle",
        "alternative_names": [
            "High Wave",
            "Takane Nami"
        ],
        "japanese_name": "Takane Nami",
        "category": "Single Candle",
        "sub_category": "Indecision",
        "sentiment": "Neutral",
        "expected_direction": "INDECISION",
        "trend_required": "Any",
        "num_candles": 1,
        "pattern_structure": "Very small real body (bullish or bearish) positioned near the middle of the range, with extremely long upper AND lower shadows. Similar to a long-legged doji but the body is slightly larger, still very small relative to the total range.",
        "candle_by_candle": [
            "Candle 1: Very small body (bullish or bearish) roughly centered. Extremely long upper shadow AND extremely long lower shadow. Total range is very large relative to the body and to recent candles. Body size distinguishes it from a long-legged doji—there is a visible, though tiny, real body."
        ],
        "market_psychology": "Extreme confusion and indecision in the market. Price oscillated wildly in both directions during the session, with both buyers and sellers exerting tremendous pressure, but ultimately the close ended near the open. This extreme uncertainty after a trend often signals that a major turning point may be near—but direction is unknown until confirmed.",
        "confirmation_required": "Critical—do not trade this pattern without directional confirmation. A strong close above or below the high wave candle's extremes provides the entry signal.",
        "volume_confirmation": "Very high volume during a high wave candle suggests a climactic battle between buyers and sellers. This makes the eventual breakout direction more significant and tradeable.",
        "volatility_conditions": "By nature, this pattern represents extreme intraday volatility. Most meaningful at the end of a sustained trend or at key support/resistance levels where a reversal decision is being made.",
        "gap_requirement": "None",
        "reliability": "Low",
        "success_rate_range": "50-55%",
        "failure_conditions": [
            "No decisive follow-through in either direction",
            "More indecision candles follow, creating a stalling zone",
            "Appears in a range-bound market without trend context",
            "Shadows are not significantly larger than surrounding candles",
            "Low volume reduces the significance of the volatility spike"
        ],
        "entry_rules": "Wait for a decisive breakout candle. Long if next candle closes above the high wave high; short if it closes below the low. The pattern itself provides no directional bias.",
        "stop_loss_rules": "Opposite extreme of the high wave candle. Note: stop distances are very wide due to the extreme range.",
        "take_profit_rules": "Due to wide stops, target at least 1:2 risk-reward. Major support/resistance in the breakout direction.",
        "risk_reward": "1:2",
        "best_timeframes": [
            "Daily",
            "4H",
            "Weekly"
        ],
        "best_markets": [
            "Stocks",
            "Forex",
            "Crypto",
            "Futures"
        ],
        "best_indicators": [
            "Volume (critical for assessing conviction)",
            "ATR (to contextualize the range expansion)",
            "RSI (extremes may hint at direction)",
            "Bollinger Bands (expansion signal)",
            "Support/Resistance levels"
        ],
        "common_mistakes": [
            "Trading the high wave candle without waiting for confirmation",
            "Ignoring the extremely wide stop-loss requirements",
            "Confusing with a long-legged doji—high wave has a small but visible body",
            "Expecting a specific direction without confirmation"
        ],
        "ai_features": [
            "0.03 < body_ratio < 0.15",
            "upper_wick_ratio > 0.35",
            "lower_wick_ratio > 0.35",
            "(H - L) > 2.0 * ATR(14)",
            "|C - O| / (H - L) < 0.15"
        ],
        "ohlc_relationship": "0.03 < |C-O| / (H-L) < 0.15; H - max(O,C) > 0.35 * (H-L); min(O,C) - L > 0.35 * (H-L)",
        "label": "Neutral",
        "confidence_score": 30,
        "probability_score": 50
    },
    {
        "id": 15,
        "pattern_name": "Bullish Belt Hold",
        "alternative_names": [
            "Belt Hold Line (Bullish)",
            "Bullish Yorikiri"
        ],
        "japanese_name": "Yorikiri",
        "category": "Single Candle",
        "sub_category": "Bullish Reversal",
        "sentiment": "Bullish",
        "expected_direction": "UP",
        "trend_required": "Downtrend",
        "num_candles": 1,
        "pattern_structure": "A tall bullish candle that opens at or very near its low, then rallies strongly to close at or near its high. No lower shadow (or negligible). May have a small upper shadow. The body is large and represents a decisive shift from selling to buying.",
        "candle_by_candle": [
            "Candle 1: Large bullish body. Opens at or very near the session low (O ≈ L, no meaningful lower shadow). Closes near the session high. A small upper shadow is acceptable. The body is long relative to recent candles."
        ],
        "market_psychology": "After a downtrend, the session opens at the extreme low—bears are in full control at the open. However, buyers aggressively step in immediately and drive price higher throughout the entire session, closing near the high. This immediate and sustained reversal from the opening low signals a decisive shift in sentiment and the potential start of an uptrend.",
        "confirmation_required": "A bullish confirmation candle on the following session (closing above the belt hold's high) strengthens the signal. The longer the body and the deeper the preceding downtrend, the less confirmation is needed.",
        "volume_confirmation": "Above-average volume on the belt hold is important for validating the buying conviction. High volume suggests institutional accumulation at the lows.",
        "volatility_conditions": "Most effective when volatility has been elevated during the preceding downtrend and the belt hold marks a volatility contraction. Effective in normal to elevated volatility.",
        "gap_requirement": "Preferred",
        "reliability": "Medium",
        "success_rate_range": "55-65%",
        "failure_conditions": [
            "No follow-through—next candle reverses the gains",
            "Pattern body is too small relative to recent candles",
            "Lower shadow is noticeable (weakens the O ≈ L requirement)",
            "Strong overhead resistance limits upside potential",
            "Volume is below average—conviction is questionable"
        ],
        "entry_rules": "Enter long at the close of the belt hold candle or on confirmation above the high. A gap up open on the next candle is a strong confirmation entry.",
        "stop_loss_rules": "Below the belt hold's low (which is approximately the open). Conservative: 1 ATR below the low.",
        "take_profit_rules": "Target nearest resistance, previous swing high, or use 1:2 to 1:3 risk-reward ratio.",
        "risk_reward": "1:2",
        "best_timeframes": [
            "Daily",
            "4H",
            "Weekly"
        ],
        "best_markets": [
            "Stocks",
            "Forex",
            "Futures",
            "Commodities",
            "Crypto"
        ],
        "best_indicators": [
            "RSI (oversold)",
            "Volume",
            "Support levels",
            "MACD (bullish divergence)",
            "Moving Averages (potential reclaim of key MA)"
        ],
        "common_mistakes": [
            "Accepting a pattern with a significant lower shadow (O must ≈ L)",
            "Ignoring the preceding downtrend requirement",
            "Confusing with a standard large bullish candle that has a lower wick",
            "Trading without checking volume confirmation"
        ],
        "ai_features": [
            "body_ratio > 0.60",
            "lower_wick_ratio < 0.05",
            "C > O (bullish)",
            "O ≈ L: (O - L) / (H - L) < 0.05",
            "(C - O) / (H - L) > 0.60"
        ],
        "ohlc_relationship": "C > O; O - L < 0.05 * (H - L); (C - O) / (H - L) > 0.60; body is large relative to recent candles",
        "label": "Bullish",
        "confidence_score": 55,
        "probability_score": 60
    },
    {
        "id": 16,
        "pattern_name": "Bearish Belt Hold",
        "alternative_names": [
            "Belt Hold Line (Bearish)",
            "Bearish Yorikiri"
        ],
        "japanese_name": "Yorikiri",
        "category": "Single Candle",
        "sub_category": "Bearish Reversal",
        "sentiment": "Bearish",
        "expected_direction": "DOWN",
        "trend_required": "Uptrend",
        "num_candles": 1,
        "pattern_structure": "A tall bearish candle that opens at or very near its high, then sells off strongly to close at or near its low. No upper shadow (or negligible). May have a small lower shadow. The body is large and represents a decisive shift from buying to selling.",
        "candle_by_candle": [
            "Candle 1: Large bearish body. Opens at or very near the session high (O ≈ H, no meaningful upper shadow). Closes near the session low. A small lower shadow is acceptable. The body is long relative to recent candles."
        ],
        "market_psychology": "After an uptrend, the session opens at the extreme high—bulls are in full control at the open. However, sellers immediately overwhelm buyers and drive price lower throughout the entire session, closing near the low. This immediate and sustained sell-off from the opening high signals a decisive shift in sentiment and a potential trend reversal.",
        "confirmation_required": "A bearish confirmation candle on the following session (closing below the belt hold's low) strengthens the signal. The longer the body and the more extended the prior uptrend, the less confirmation is needed.",
        "volume_confirmation": "Above-average volume is important for validation. High volume signals institutional distribution at the highs. Low volume undermines the signal.",
        "volatility_conditions": "Most effective when volatility has been moderate during the preceding uptrend and the belt hold marks a shift. Effective in normal to elevated volatility.",
        "gap_requirement": "Preferred",
        "reliability": "Medium",
        "success_rate_range": "55-65%",
        "failure_conditions": [
            "No follow-through—next candle reverses the losses",
            "Pattern body is too small relative to recent candles",
            "Upper shadow is noticeable (weakens the O ≈ H requirement)",
            "Strong support immediately below limits downside",
            "Volume is below average—selling conviction is weak"
        ],
        "entry_rules": "Enter short at the close of the belt hold candle or on confirmation below the low. A gap down open on the next candle is a strong confirmation entry.",
        "stop_loss_rules": "Above the belt hold's high (which is approximately the open). Conservative: 1 ATR above the high.",
        "take_profit_rules": "Target nearest support, previous swing low, or use 1:2 to 1:3 risk-reward ratio.",
        "risk_reward": "1:2",
        "best_timeframes": [
            "Daily",
            "4H",
            "Weekly"
        ],
        "best_markets": [
            "Stocks",
            "Forex",
            "Futures",
            "Commodities",
            "Crypto"
        ],
        "best_indicators": [
            "RSI (overbought)",
            "Volume",
            "Resistance levels",
            "MACD (bearish crossover)",
            "Moving Averages (potential loss of key MA)"
        ],
        "common_mistakes": [
            "Accepting a pattern with a significant upper shadow (O must ≈ H)",
            "Ignoring the preceding uptrend requirement",
            "Confusing with a standard large bearish candle that has an upper wick",
            "Trading without checking volume confirmation"
        ],
        "ai_features": [
            "body_ratio > 0.60",
            "upper_wick_ratio < 0.05",
            "C < O (bearish)",
            "O ≈ H: (H - O) / (H - L) < 0.05",
            "(O - C) / (H - L) > 0.60"
        ],
        "ohlc_relationship": "C < O; H - O < 0.05 * (H - L); (O - C) / (H - L) > 0.60; body is large relative to recent candles",
        "label": "Bearish",
        "confidence_score": 55,
        "probability_score": 60
    },
    {
        "id": 17,
        "pattern_name": "Bullish Engulfing",
        "alternative_names": [
            "Bull Engulf",
            "Engulfing Bull Line"
        ],
        "japanese_name": "Tsutsumi",
        "category": "Two Candle",
        "sub_category": "Bullish Reversal",
        "sentiment": "Bullish",
        "expected_direction": "UP",
        "trend_required": "Downtrend",
        "num_candles": 2,
        "pattern_structure": "Small bearish candle followed by a larger bullish candle whose body completely engulfs the prior candle's body",
        "candle_by_candle": [
            "Candle 1: Small bearish candle continuing the downtrend. Relatively small body showing weakening selling momentum.",
            "Candle 2: Large bullish candle that opens below Candle 1's close and closes above Candle 1's open, completely engulfing the first body."
        ],
        "market_psychology": "After sustained selling, the market opens lower suggesting bears still dominate. However, aggressive buying overwhelms sellers throughout the session, pushing price well above the prior open. This dramatic intraday reversal signals a decisive shift in power from sellers to buyers.",
        "confirmation_required": "Third candle closing above the engulfing candle's high provides strong confirmation. Gap up open on third candle is ideal.",
        "volume_confirmation": "Volume on Candle 2 should be significantly higher than Candle 1. High volume engulfing indicates strong institutional participation.",
        "volatility_conditions": "Most reliable in normal volatility. Can produce false signals in extremely volatile choppy markets.",
        "gap_requirement": "Preferred",
        "reliability": "High",
        "success_rate_range": "63-75%",
        "failure_conditions": [
            "Candle 2 does not fully engulf Candle 1's body",
            "Low volume on the engulfing candle",
            "Appears in sideways market without clear downtrend",
            "Strong overhead resistance nearby",
            "No follow-through on the next candle"
        ],
        "entry_rules": "Enter long on close of Candle 2 or on break above Candle 2's high. Conservative: wait for third candle confirmation.",
        "stop_loss_rules": "Below the low of the engulfing pattern (lower of Candle 1 and Candle 2 lows).",
        "take_profit_rules": "Target nearest resistance, previous swing high, or use 1:2 to 1:3 RR ratio.",
        "risk_reward": "1:2",
        "best_timeframes": [
            "Daily",
            "4H",
            "Weekly"
        ],
        "best_markets": [
            "Stocks",
            "Forex",
            "Crypto",
            "Futures",
            "Commodities"
        ],
        "best_indicators": [
            "RSI (oversold <30)",
            "MACD (bullish crossover)",
            "Volume",
            "Support levels",
            "Bollinger Bands (lower band touch)"
        ],
        "common_mistakes": [
            "Not verifying prior downtrend exists",
            "Trading when Candle 2 only partially engulfs",
            "Ignoring volume confirmation",
            "Not waiting for next-candle confirmation"
        ],
        "ai_features": [
            "candle2.body > candle1.body",
            "candle2.open < candle1.close",
            "candle2.close > candle1.open",
            "candle1.is_bearish = True",
            "candle2.is_bullish = True",
            "candle2.body_ratio > 0.60",
            "volume_ratio_c2_c1 > 1.5"
        ],
        "ohlc_relationship": "C1: C1_close < C1_open (bearish); C2: C2_open < C1_close AND C2_close > C1_open; C2_body > C1_body",
        "label": "Bullish",
        "confidence_score": 75,
        "probability_score": 68
    },
    {
        "id": 18,
        "pattern_name": "Bearish Engulfing",
        "alternative_names": [
            "Bear Engulf",
            "Engulfing Bear Line"
        ],
        "japanese_name": "Tsutsumi",
        "category": "Two Candle",
        "sub_category": "Bearish Reversal",
        "sentiment": "Bearish",
        "expected_direction": "DOWN",
        "trend_required": "Uptrend",
        "num_candles": 2,
        "pattern_structure": "Small bullish candle followed by a larger bearish candle whose body completely engulfs the prior candle's body",
        "candle_by_candle": [
            "Candle 1: Small bullish candle continuing the uptrend. Relatively small body showing weakening buying momentum.",
            "Candle 2: Large bearish candle that opens above Candle 1's close and closes below Candle 1's open, completely engulfing the first body."
        ],
        "market_psychology": "After sustained buying, the market opens higher suggesting bulls still control. However, aggressive selling overwhelms buyers, pushing price well below the prior open. This intraday reversal signals a decisive shift from buyers to sellers.",
        "confirmation_required": "Third candle closing below the engulfing candle's low provides strong confirmation.",
        "volume_confirmation": "Volume on Candle 2 should be significantly higher than Candle 1. High volume confirms institutional selling.",
        "volatility_conditions": "Most reliable in normal volatility. Beware of false signals in extremely choppy environments.",
        "gap_requirement": "Preferred",
        "reliability": "High",
        "success_rate_range": "63-75%",
        "failure_conditions": [
            "Candle 2 does not fully engulf Candle 1's body",
            "Low volume on the engulfing candle",
            "Appears without clear uptrend",
            "Strong support nearby below",
            "No bearish follow-through"
        ],
        "entry_rules": "Enter short on close of Candle 2 or on break below Candle 2's low. Conservative: wait for third candle confirmation.",
        "stop_loss_rules": "Above the high of the engulfing pattern (higher of Candle 1 and Candle 2 highs).",
        "take_profit_rules": "Target nearest support, previous swing low, or use 1:2 to 1:3 RR ratio.",
        "risk_reward": "1:2",
        "best_timeframes": [
            "Daily",
            "4H",
            "Weekly"
        ],
        "best_markets": [
            "Stocks",
            "Forex",
            "Crypto",
            "Futures",
            "Commodities"
        ],
        "best_indicators": [
            "RSI (overbought >70)",
            "MACD (bearish crossover)",
            "Volume",
            "Resistance levels",
            "Bollinger Bands (upper band touch)"
        ],
        "common_mistakes": [
            "Not verifying prior uptrend exists",
            "Trading partial engulfing as full engulfing",
            "Ignoring volume divergence",
            "Entering before confirmation"
        ],
        "ai_features": [
            "candle2.body > candle1.body",
            "candle2.open > candle1.close",
            "candle2.close < candle1.open",
            "candle1.is_bullish = True",
            "candle2.is_bearish = True",
            "candle2.body_ratio > 0.60"
        ],
        "ohlc_relationship": "C1: C1_close > C1_open (bullish); C2: C2_open > C1_close AND C2_close < C1_open; C2_body > C1_body",
        "label": "Bearish",
        "confidence_score": 75,
        "probability_score": 68
    },
    {
        "id": 19,
        "pattern_name": "Bullish Harami",
        "alternative_names": [
            "Bull Harami",
            "Inside Bar Bullish"
        ],
        "japanese_name": "Harami",
        "category": "Two Candle",
        "sub_category": "Bullish Reversal",
        "sentiment": "Bullish",
        "expected_direction": "UP",
        "trend_required": "Downtrend",
        "num_candles": 2,
        "pattern_structure": "Large bearish candle followed by a smaller bullish candle whose body is entirely contained within Candle 1's body",
        "candle_by_candle": [
            "Candle 1: Long bearish candle with strong selling pressure, continuing the downtrend.",
            "Candle 2: Small bullish candle whose entire body fits within the body of Candle 1. Opens above C1's close and closes below C1's open."
        ],
        "market_psychology": "After heavy selling (C1), the next session opens higher and trades in a narrow range within the previous body. The inability of sellers to push prices lower shows exhaustion. The small bullish body hints at buyer emergence, signaling a potential reversal.",
        "confirmation_required": "Third candle closing above Candle 1's open (top of C1's body) confirms the reversal.",
        "volume_confirmation": "Volume should decline on Candle 2, indicating seller exhaustion. Increasing volume on the confirmation candle strengthens the signal.",
        "volatility_conditions": "Works in normal to moderate volatility. Less significant in highly volatile environments where inside bars are common.",
        "gap_requirement": "None",
        "reliability": "Medium",
        "success_rate_range": "50-63%",
        "failure_conditions": [
            "No confirmation candle follows",
            "Candle 2's body is not fully inside Candle 1's body",
            "High volume on Candle 2 suggests continuation not reversal",
            "Strong resistance overhead",
            "Broader market still strongly bearish"
        ],
        "entry_rules": "Enter long on break above Candle 1's open or on close of confirmation candle. Conservative: wait for third candle.",
        "stop_loss_rules": "Below the low of Candle 1 or the pattern low.",
        "take_profit_rules": "Target the nearest resistance or previous swing high. Use 1:2 RR ratio.",
        "risk_reward": "1:2",
        "best_timeframes": [
            "Daily",
            "4H",
            "1H"
        ],
        "best_markets": [
            "Stocks",
            "Forex",
            "Crypto",
            "Futures"
        ],
        "best_indicators": [
            "RSI (oversold)",
            "Stochastic (bullish crossover)",
            "Volume",
            "Support levels",
            "Moving Averages"
        ],
        "common_mistakes": [
            "Trading without confirmation",
            "Confusing with Bullish Engulfing (opposite structure)",
            "Ignoring the prior trend requirement",
            "Not checking if C2's body is truly contained within C1"
        ],
        "ai_features": [
            "candle1.is_bearish AND candle1.body_ratio > 0.50",
            "candle2.is_bullish",
            "candle2.open > candle1.close",
            "candle2.close < candle1.open",
            "candle2.body < candle1.body",
            "candle2.body_ratio < 0.40"
        ],
        "ohlc_relationship": "C1: bearish, large body; C2: bullish, C2_open > C1_close AND C2_close < C1_open; C2_body < C1_body",
        "label": "Bullish",
        "confidence_score": 55,
        "probability_score": 55
    },
    {
        "id": 20,
        "pattern_name": "Bearish Harami",
        "alternative_names": [
            "Bear Harami",
            "Inside Bar Bearish"
        ],
        "japanese_name": "Harami",
        "category": "Two Candle",
        "sub_category": "Bearish Reversal",
        "sentiment": "Bearish",
        "expected_direction": "DOWN",
        "trend_required": "Uptrend",
        "num_candles": 2,
        "pattern_structure": "Large bullish candle followed by a smaller bearish candle whose body is entirely contained within Candle 1's body",
        "candle_by_candle": [
            "Candle 1: Long bullish candle with strong buying pressure, continuing the uptrend.",
            "Candle 2: Small bearish candle whose entire body fits within the body of Candle 1. Opens below C1's close and closes above C1's open."
        ],
        "market_psychology": "After strong buying (C1), the next session opens lower and trades within the previous body. Buyers fail to push higher, and the small bearish close shows hesitation. Buying momentum is fading, potentially signaling a top.",
        "confirmation_required": "Third candle closing below Candle 1's open (bottom of C1's body) confirms the reversal.",
        "volume_confirmation": "Volume should decline on Candle 2. Rising volume on bearish confirmation strengthens signal.",
        "volatility_conditions": "Works in normal volatility. Less meaningful during extreme volatility.",
        "gap_requirement": "None",
        "reliability": "Medium",
        "success_rate_range": "50-63%",
        "failure_conditions": [
            "No bearish confirmation follows",
            "Candle 2 body not fully inside Candle 1",
            "Strong support below",
            "Uptrend too strong to reverse"
        ],
        "entry_rules": "Enter short on break below Candle 1's open or on close of bearish confirmation candle.",
        "stop_loss_rules": "Above the high of Candle 1 or the pattern high.",
        "take_profit_rules": "Target nearest support or previous swing low. Use 1:2 RR ratio.",
        "risk_reward": "1:2",
        "best_timeframes": [
            "Daily",
            "4H",
            "1H"
        ],
        "best_markets": [
            "Stocks",
            "Forex",
            "Crypto",
            "Futures"
        ],
        "best_indicators": [
            "RSI (overbought)",
            "Stochastic (bearish crossover)",
            "Volume",
            "Resistance levels"
        ],
        "common_mistakes": [
            "Trading without confirmation candle",
            "Not verifying uptrend precondition",
            "Confusing with Bearish Engulfing",
            "Taking signal when broader trend is strongly bullish"
        ],
        "ai_features": [
            "candle1.is_bullish AND candle1.body_ratio > 0.50",
            "candle2.is_bearish",
            "candle2.open < candle1.close",
            "candle2.close > candle1.open",
            "candle2.body < candle1.body"
        ],
        "ohlc_relationship": "C1: bullish, large body; C2: bearish, C2_open < C1_close AND C2_close > C1_open; C2_body < C1_body",
        "label": "Bearish",
        "confidence_score": 55,
        "probability_score": 55
    },
    {
        "id": 21,
        "pattern_name": "Bullish Harami Cross",
        "alternative_names": [
            "Harami Cross Bull",
            "Inside Doji Bullish"
        ],
        "japanese_name": "Harami Yose Sen",
        "category": "Two Candle",
        "sub_category": "Bullish Reversal",
        "sentiment": "Bullish",
        "expected_direction": "UP",
        "trend_required": "Downtrend",
        "num_candles": 2,
        "pattern_structure": "Large bearish candle followed by a doji whose body is entirely within Candle 1's body",
        "candle_by_candle": [
            "Candle 1: Long bearish candle with strong selling pressure.",
            "Candle 2: Doji (open approximately equals close) with the entire body inside Candle 1's body. Shadows may extend beyond C1's body but the open/close are contained."
        ],
        "market_psychology": "The doji inside the large bearish body shows complete indecision after strong selling. Sellers can no longer dominate, and the market pauses. This deadlock often precedes a reversal as new buyers enter at perceived value.",
        "confirmation_required": "Bullish candle following the doji, closing above C1's open, provides strong confirmation.",
        "volume_confirmation": "Lower volume on the doji shows conviction fading. Volume expansion on the confirmation candle is key.",
        "volatility_conditions": "Normal volatility. The doji is more meaningful when it represents a true pause, not random noise.",
        "gap_requirement": "None",
        "reliability": "Medium",
        "success_rate_range": "55-65%",
        "failure_conditions": [
            "No bullish confirmation follows the doji",
            "Doji appears in a sideways market",
            "Doji body not within C1's body",
            "Extreme low volume making doji meaningless"
        ],
        "entry_rules": "Enter long on bullish confirmation candle closing above C1's open.",
        "stop_loss_rules": "Below the low of the pattern (C1 or doji low, whichever is lower).",
        "take_profit_rules": "Nearest resistance or 1:2 RR from entry.",
        "risk_reward": "1:2",
        "best_timeframes": [
            "Daily",
            "4H",
            "Weekly"
        ],
        "best_markets": [
            "Stocks",
            "Forex",
            "Crypto",
            "Futures"
        ],
        "best_indicators": [
            "RSI (oversold)",
            "MACD (divergence)",
            "Volume",
            "Support levels"
        ],
        "common_mistakes": [
            "Trading the doji alone without confirmation",
            "Not verifying doji body is inside C1",
            "Ignoring prior downtrend requirement"
        ],
        "ai_features": [
            "candle1.is_bearish AND candle1.body_ratio > 0.50",
            "candle2.is_doji (body_ratio < 0.10)",
            "candle2.open > candle1.close",
            "candle2.close < candle1.open",
            "candle2.body < candle1.body * 0.10"
        ],
        "ohlc_relationship": "C1: bearish, body_ratio > 0.50; C2: doji (|C2_O - C2_C| / (C2_H - C2_L) < 0.10), C2_body inside C1_body",
        "label": "Bullish",
        "confidence_score": 60,
        "probability_score": 58
    },
    {
        "id": 22,
        "pattern_name": "Bearish Harami Cross",
        "alternative_names": [
            "Harami Cross Bear",
            "Inside Doji Bearish"
        ],
        "japanese_name": "Harami Yose Sen",
        "category": "Two Candle",
        "sub_category": "Bearish Reversal",
        "sentiment": "Bearish",
        "expected_direction": "DOWN",
        "trend_required": "Uptrend",
        "num_candles": 2,
        "pattern_structure": "Large bullish candle followed by a doji whose body is entirely within Candle 1's body",
        "candle_by_candle": [
            "Candle 1: Long bullish candle with strong buying pressure.",
            "Candle 2: Doji with open approximately equal to close, body inside Candle 1's body."
        ],
        "market_psychology": "After a strong bullish push, the doji signals that buying momentum has stalled completely. The balance of power is shifting, and the doji within the large body warns of potential reversal as buyers fail to extend the rally.",
        "confirmation_required": "Bearish candle following the doji, closing below C1's open, confirms the reversal.",
        "volume_confirmation": "Lower volume on doji, higher volume on bearish confirmation candle.",
        "volatility_conditions": "Normal volatility. More reliable on higher timeframes where dojis carry more weight.",
        "gap_requirement": "None",
        "reliability": "Medium",
        "success_rate_range": "55-65%",
        "failure_conditions": [
            "No bearish confirmation follows",
            "Doji body outside C1's body",
            "Strong uptrend with high momentum resumes"
        ],
        "entry_rules": "Enter short on bearish confirmation candle closing below C1's open.",
        "stop_loss_rules": "Above the high of the pattern (C1 high or doji high).",
        "take_profit_rules": "Nearest support or 1:2 RR ratio.",
        "risk_reward": "1:2",
        "best_timeframes": [
            "Daily",
            "4H",
            "Weekly"
        ],
        "best_markets": [
            "Stocks",
            "Forex",
            "Crypto",
            "Futures"
        ],
        "best_indicators": [
            "RSI (overbought)",
            "MACD (bearish divergence)",
            "Volume",
            "Resistance levels"
        ],
        "common_mistakes": [
            "Acting on the doji without waiting for confirmation",
            "Not verifying the doji body is inside C1's body",
            "Ignoring the uptrend requirement"
        ],
        "ai_features": [
            "candle1.is_bullish AND candle1.body_ratio > 0.50",
            "candle2.is_doji (body_ratio < 0.10)",
            "candle2.open < candle1.close",
            "candle2.close > candle1.open"
        ],
        "ohlc_relationship": "C1: bullish, body_ratio > 0.50; C2: doji, C2_body inside C1_body",
        "label": "Bearish",
        "confidence_score": 60,
        "probability_score": 58
    },
    {
        "id": 23,
        "pattern_name": "Piercing Pattern",
        "alternative_names": [
            "Piercing Line",
            "Kirikomi"
        ],
        "japanese_name": "Kirikomi",
        "category": "Two Candle",
        "sub_category": "Bullish Reversal",
        "sentiment": "Bullish",
        "expected_direction": "UP",
        "trend_required": "Downtrend",
        "num_candles": 2,
        "pattern_structure": "Long bearish candle followed by a bullish candle that opens below C1's low and closes above C1's midpoint",
        "candle_by_candle": [
            "Candle 1: Long bearish candle confirming the downtrend. Strong selling.",
            "Candle 2: Bullish candle that opens below Candle 1's low (gap down) and then rallies to close above the midpoint of Candle 1's body."
        ],
        "market_psychology": "Bears push price to new lows at C2's open, appearing in full control. However, strong buying emerges and drives price up to close above the prior candle's midpoint. This dramatic reversal from the session low shows buyer conviction emerging at lower prices.",
        "confirmation_required": "Third candle closing above C1's open provides confirmation. The higher C2 closes into C1's body, the stronger the signal.",
        "volume_confirmation": "High volume on Candle 2 confirms buyer conviction. Volume should exceed C1's volume.",
        "volatility_conditions": "Normal to moderate volatility. Gaps are more common in stocks than forex.",
        "gap_requirement": "Preferred",
        "reliability": "Medium",
        "success_rate_range": "55-68%",
        "failure_conditions": [
            "C2 closes below C1's midpoint",
            "No gap down on C2's open (in markets where gaps occur)",
            "Low volume on C2",
            "No confirmation candle follows",
            "Strong resistance immediately above"
        ],
        "entry_rules": "Enter long on C2's close or on break above C1's open. Wait for confirmation on lower timeframes.",
        "stop_loss_rules": "Below C2's low (the pattern low).",
        "take_profit_rules": "Target nearest resistance or previous swing high. Use 1:2 RR ratio.",
        "risk_reward": "1:2",
        "best_timeframes": [
            "Daily",
            "4H",
            "Weekly"
        ],
        "best_markets": [
            "Stocks",
            "Futures",
            "Crypto",
            "Commodities"
        ],
        "best_indicators": [
            "RSI (oversold)",
            "MACD (bullish divergence)",
            "Volume",
            "Support zones"
        ],
        "common_mistakes": [
            "Accepting C2 that closes below C1's midpoint (not a valid piercing)",
            "Trading without a gap down open",
            "Confusing with Bullish Engulfing (which closes above C1's open)"
        ],
        "ai_features": [
            "candle1.is_bearish AND candle1.body_ratio > 0.50",
            "candle2.is_bullish",
            "candle2.open < candle1.low",
            "candle2.close > (candle1.open + candle1.close) / 2",
            "candle2.close < candle1.open"
        ],
        "ohlc_relationship": "C1: bearish, body_ratio > 0.50; C2: bullish, C2_open < C1_low, C2_close > C1_midpoint, C2_close < C1_open",
        "label": "Bullish",
        "confidence_score": 62,
        "probability_score": 60
    },
    {
        "id": 24,
        "pattern_name": "Dark Cloud Cover",
        "alternative_names": [
            "Dark Cloud",
            "Kabuse"
        ],
        "japanese_name": "Kabuse",
        "category": "Two Candle",
        "sub_category": "Bearish Reversal",
        "sentiment": "Bearish",
        "expected_direction": "DOWN",
        "trend_required": "Uptrend",
        "num_candles": 2,
        "pattern_structure": "Long bullish candle followed by a bearish candle that opens above C1's high and closes below C1's midpoint",
        "candle_by_candle": [
            "Candle 1: Long bullish candle confirming the uptrend.",
            "Candle 2: Bearish candle that opens above Candle 1's high (gap up) and then sells off to close below the midpoint of Candle 1's body."
        ],
        "market_psychology": "Bulls gap price higher at C2's open, seeming in full control. However, heavy selling drives price down through C1's midpoint, showing bears have seized the session. This dramatic intraday failure signals potential exhaustion of the uptrend.",
        "confirmation_required": "Third candle closing below C1's open confirms the pattern. The deeper C2 penetrates into C1, the more bearish.",
        "volume_confirmation": "High volume on C2 confirms selling conviction. Should exceed C1 volume.",
        "volatility_conditions": "Normal to moderate volatility. Gap up open more common in stocks and futures.",
        "gap_requirement": "Preferred",
        "reliability": "Medium",
        "success_rate_range": "55-68%",
        "failure_conditions": [
            "C2 closes above C1's midpoint",
            "No gap up on C2 open",
            "Low volume on C2",
            "No bearish follow-through"
        ],
        "entry_rules": "Enter short on C2's close or break below C1's open.",
        "stop_loss_rules": "Above C2's high (pattern high).",
        "take_profit_rules": "Target nearest support or previous swing low.",
        "risk_reward": "1:2",
        "best_timeframes": [
            "Daily",
            "4H",
            "Weekly"
        ],
        "best_markets": [
            "Stocks",
            "Futures",
            "Crypto",
            "Commodities"
        ],
        "best_indicators": [
            "RSI (overbought)",
            "MACD (bearish divergence)",
            "Volume",
            "Resistance zones"
        ],
        "common_mistakes": [
            "Accepting C2 that closes above C1's midpoint",
            "Confusing with Bearish Engulfing",
            "Trading without gap up open"
        ],
        "ai_features": [
            "candle1.is_bullish AND candle1.body_ratio > 0.50",
            "candle2.is_bearish",
            "candle2.open > candle1.high",
            "candle2.close < (candle1.open + candle1.close) / 2",
            "candle2.close > candle1.open"
        ],
        "ohlc_relationship": "C1: bullish, body_ratio > 0.50; C2: bearish, C2_open > C1_high, C2_close < C1_midpoint, C2_close > C1_open",
        "label": "Bearish",
        "confidence_score": 62,
        "probability_score": 60
    },
    {
        "id": 25,
        "pattern_name": "Tweezer Top",
        "alternative_names": [
            "Tweezer Tops",
            "Kenuki Top"
        ],
        "japanese_name": "Kenuki",
        "category": "Two Candle",
        "sub_category": "Bearish Reversal",
        "sentiment": "Bearish",
        "expected_direction": "DOWN",
        "trend_required": "Uptrend",
        "num_candles": 2,
        "pattern_structure": "Two consecutive candles with matching or nearly matching highs, first bullish and second bearish",
        "candle_by_candle": [
            "Candle 1: Bullish candle in an uptrend that sets a high.",
            "Candle 2: Bearish candle that tests the same high as Candle 1 but fails, closing lower. The matching highs form a resistance level."
        ],
        "market_psychology": "Price hits a ceiling twice and is rejected both times. The second rejection with a bearish close confirms sellers are defending that level aggressively. Double rejection implies strong resistance and potential trend reversal.",
        "confirmation_required": "Third candle closing below C2's close and the pattern's support area confirms the reversal.",
        "volume_confirmation": "Volume on C2 should be equal to or higher than C1. Rejection at highs with volume confirms selling pressure.",
        "volatility_conditions": "Normal volatility. High volatility may produce matching highs by coincidence.",
        "gap_requirement": "None",
        "reliability": "Medium",
        "success_rate_range": "52-65%",
        "failure_conditions": [
            "Highs differ by more than a small tolerance",
            "No bearish confirmation follows",
            "Strong bullish momentum overcomes resistance",
            "Low volume at the highs"
        ],
        "entry_rules": "Enter short on break below C2's low or on bearish confirmation candle.",
        "stop_loss_rules": "Above the matching highs plus a small buffer.",
        "take_profit_rules": "Target nearest support or previous swing low. 1:2 RR ratio.",
        "risk_reward": "1:2",
        "best_timeframes": [
            "Daily",
            "4H",
            "1H"
        ],
        "best_markets": [
            "Stocks",
            "Forex",
            "Crypto",
            "Futures"
        ],
        "best_indicators": [
            "RSI (overbought)",
            "Volume at highs",
            "Resistance levels",
            "Moving Averages"
        ],
        "common_mistakes": [
            "Being too strict on matching highs (allow small tolerance)",
            "Not considering the prior uptrend",
            "Ignoring volume at the rejection levels"
        ],
        "ai_features": [
            "abs(candle1.high - candle2.high) < tolerance",
            "candle1.is_bullish",
            "candle2.is_bearish",
            "prior_trend = uptrend",
            "candle2.upper_wick_ratio > 0.20"
        ],
        "ohlc_relationship": "abs(C1_high - C2_high) < tolerance * max_range; C1 bullish; C2 bearish",
        "label": "Bearish",
        "confidence_score": 55,
        "probability_score": 55
    },
    {
        "id": 26,
        "pattern_name": "Tweezer Bottom",
        "alternative_names": [
            "Tweezer Bottoms",
            "Kenuki Bottom"
        ],
        "japanese_name": "Kenuki",
        "category": "Two Candle",
        "sub_category": "Bullish Reversal",
        "sentiment": "Bullish",
        "expected_direction": "UP",
        "trend_required": "Downtrend",
        "num_candles": 2,
        "pattern_structure": "Two consecutive candles with matching or nearly matching lows, first bearish and second bullish",
        "candle_by_candle": [
            "Candle 1: Bearish candle in a downtrend that sets a low.",
            "Candle 2: Bullish candle that tests the same low as Candle 1 but bounces, closing higher. The matching lows form a support level."
        ],
        "market_psychology": "Price hits a floor twice and bounces both times. The second bounce with a bullish close confirms buyers are defending that support. Double support holding signals potential bottom.",
        "confirmation_required": "Third candle closing above C2's high confirms the reversal.",
        "volume_confirmation": "Volume expansion on C2 confirms buying interest at support.",
        "volatility_conditions": "Normal volatility. More reliable when lows are precise.",
        "gap_requirement": "None",
        "reliability": "Medium",
        "success_rate_range": "52-65%",
        "failure_conditions": [
            "Lows differ significantly",
            "No bullish confirmation",
            "Strong bearish pressure breaks through",
            "Low volume at the lows"
        ],
        "entry_rules": "Enter long on break above C2's high or on bullish confirmation.",
        "stop_loss_rules": "Below the matching lows minus a small buffer.",
        "take_profit_rules": "Target nearest resistance or 1:2 RR ratio.",
        "risk_reward": "1:2",
        "best_timeframes": [
            "Daily",
            "4H",
            "1H"
        ],
        "best_markets": [
            "Stocks",
            "Forex",
            "Crypto",
            "Futures"
        ],
        "best_indicators": [
            "RSI (oversold)",
            "Volume at lows",
            "Support levels",
            "Moving Averages"
        ],
        "common_mistakes": [
            "Being too strict on matching lows",
            "Trading without downtrend context",
            "Ignoring volume confirmation"
        ],
        "ai_features": [
            "abs(candle1.low - candle2.low) < tolerance",
            "candle1.is_bearish",
            "candle2.is_bullish",
            "prior_trend = downtrend",
            "candle2.lower_wick_ratio > 0.20"
        ],
        "ohlc_relationship": "abs(C1_low - C2_low) < tolerance * max_range; C1 bearish; C2 bullish",
        "label": "Bullish",
        "confidence_score": 55,
        "probability_score": 55
    },
    {
        "id": 27,
        "pattern_name": "Matching High",
        "alternative_names": [
            "Double Top Candle"
        ],
        "japanese_name": "",
        "category": "Two Candle",
        "sub_category": "Bearish Reversal",
        "sentiment": "Bearish",
        "expected_direction": "DOWN",
        "trend_required": "Uptrend",
        "num_candles": 2,
        "pattern_structure": "Two bullish candles with the same or nearly identical closing prices, forming a resistance ceiling",
        "candle_by_candle": [
            "Candle 1: Bullish candle in an uptrend that closes at a certain price.",
            "Candle 2: Another bullish candle that closes at the same price as Candle 1, failing to push through that level."
        ],
        "market_psychology": "Bulls try twice to push past a price level and fail both times. Identical closes signal a price ceiling that buyers cannot overcome. This double failure at the same level suggests the uptrend is stalling and a pullback is likely.",
        "confirmation_required": "Bearish candle following, closing below both candles' opening prices.",
        "volume_confirmation": "Declining volume on C2 compared to C1 suggests waning buying interest.",
        "volatility_conditions": "Normal volatility. More significant on higher timeframes.",
        "gap_requirement": "None",
        "reliability": "Low",
        "success_rate_range": "45-55%",
        "failure_conditions": [
            "Closes are not close enough to match",
            "Strong bullish momentum breaks through on third candle",
            "Low significance on intraday timeframes"
        ],
        "entry_rules": "Enter short on break below C2's low or on bearish confirmation.",
        "stop_loss_rules": "Above the matching closes plus a buffer.",
        "take_profit_rules": "Target nearest support. Use 1:1.5 to 1:2 RR.",
        "risk_reward": "1:2",
        "best_timeframes": [
            "Daily",
            "Weekly"
        ],
        "best_markets": [
            "Stocks",
            "Futures"
        ],
        "best_indicators": [
            "RSI (overbought)",
            "Volume (declining)",
            "Resistance levels"
        ],
        "common_mistakes": [
            "Being too loose on what constitutes matching closes",
            "Trading without confirmation",
            "Ignoring the broader trend"
        ],
        "ai_features": [
            "abs(candle1.close - candle2.close) < tolerance",
            "candle1.is_bullish AND candle2.is_bullish",
            "prior_trend = uptrend"
        ],
        "ohlc_relationship": "C1 and C2 both bullish; abs(C1_close - C2_close) < tolerance",
        "label": "Bearish",
        "confidence_score": 40,
        "probability_score": 48
    },
    {
        "id": 28,
        "pattern_name": "Matching Low",
        "alternative_names": [
            "Double Bottom Candle"
        ],
        "japanese_name": "",
        "category": "Two Candle",
        "sub_category": "Bullish Reversal",
        "sentiment": "Bullish",
        "expected_direction": "UP",
        "trend_required": "Downtrend",
        "num_candles": 2,
        "pattern_structure": "Two bearish candles with the same or nearly identical closing prices, forming a support floor",
        "candle_by_candle": [
            "Candle 1: Bearish candle in a downtrend closing at a certain price.",
            "Candle 2: Another bearish candle that closes at the same price, unable to push lower."
        ],
        "market_psychology": "Sellers try twice to push past a support level and fail. The identical closes signal a price floor that sellers cannot break. This double failure suggests selling is exhausting and a bounce is likely.",
        "confirmation_required": "Bullish candle following, closing above both candles' opening prices.",
        "volume_confirmation": "Declining volume on C2 suggests selling is exhausting.",
        "volatility_conditions": "Normal volatility. More reliable on daily or weekly charts.",
        "gap_requirement": "None",
        "reliability": "Low",
        "success_rate_range": "45-55%",
        "failure_conditions": [
            "Closes not close enough to match",
            "Strong selling breaks through on third candle",
            "Pattern forms in strong downtrend with no support"
        ],
        "entry_rules": "Enter long on break above C2's high or bullish confirmation.",
        "stop_loss_rules": "Below the matching closes minus a buffer.",
        "take_profit_rules": "Target nearest resistance. Use 1:2 RR.",
        "risk_reward": "1:2",
        "best_timeframes": [
            "Daily",
            "Weekly"
        ],
        "best_markets": [
            "Stocks",
            "Futures"
        ],
        "best_indicators": [
            "RSI (oversold)",
            "Volume (declining)",
            "Support levels"
        ],
        "common_mistakes": [
            "Loose definition of matching closes",
            "Trading without confirmation",
            "Ignoring macro downtrend"
        ],
        "ai_features": [
            "abs(candle1.close - candle2.close) < tolerance",
            "candle1.is_bearish AND candle2.is_bearish",
            "prior_trend = downtrend"
        ],
        "ohlc_relationship": "C1 and C2 both bearish; abs(C1_close - C2_close) < tolerance",
        "label": "Bullish",
        "confidence_score": 40,
        "probability_score": 48
    },
    {
        "id": 29,
        "pattern_name": "Homing Pigeon",
        "alternative_names": [
            "Bearish Harami Variant"
        ],
        "japanese_name": "",
        "category": "Two Candle",
        "sub_category": "Bullish Reversal",
        "sentiment": "Bullish",
        "expected_direction": "UP",
        "trend_required": "Downtrend",
        "num_candles": 2,
        "pattern_structure": "Large bearish candle followed by a smaller bearish candle whose body is contained within Candle 1's body — like a harami but both candles are bearish",
        "candle_by_candle": [
            "Candle 1: Long bearish candle with strong selling.",
            "Candle 2: Smaller bearish candle whose body is entirely inside C1's body. Opens lower than C1 open but higher than C1 close, and closes higher than C1 close but lower than C1 open."
        ],
        "market_psychology": "Despite both candles being bearish, the second candle's smaller range within the first shows selling momentum is decelerating sharply. Sellers are losing strength, setting up for a potential reversal.",
        "confirmation_required": "Bullish candle closing above C1's open confirms the reversal.",
        "volume_confirmation": "Declining volume on C2 confirms seller exhaustion.",
        "volatility_conditions": "Normal volatility. Pattern shows contraction of range.",
        "gap_requirement": "None",
        "reliability": "Low",
        "success_rate_range": "45-58%",
        "failure_conditions": [
            "C2 body not inside C1 body",
            "No bullish confirmation",
            "Selling pressure resumes strongly"
        ],
        "entry_rules": "Enter long on bullish confirmation candle closing above C1's open.",
        "stop_loss_rules": "Below the low of the pattern.",
        "take_profit_rules": "Target nearest resistance or 1:2 RR.",
        "risk_reward": "1:2",
        "best_timeframes": [
            "Daily",
            "4H"
        ],
        "best_markets": [
            "Stocks",
            "Futures"
        ],
        "best_indicators": [
            "RSI (oversold)",
            "Volume",
            "Support levels"
        ],
        "common_mistakes": [
            "Confusing with regular Bearish Harami (harami has opposite color C2)",
            "Trading without confirmation",
            "Not verifying downtrend context"
        ],
        "ai_features": [
            "candle1.is_bearish AND candle1.body_ratio > 0.50",
            "candle2.is_bearish",
            "candle2.body < candle1.body",
            "candle2.open < candle1.open AND candle2.open > candle1.close",
            "candle2.close > candle1.close AND candle2.close < candle1.open"
        ],
        "ohlc_relationship": "C1: bearish, large; C2: bearish, smaller, C2_body inside C1_body; both bearish",
        "label": "Bullish",
        "confidence_score": 42,
        "probability_score": 50
    },
    {
        "id": 30,
        "pattern_name": "Bullish Meeting Lines",
        "alternative_names": [
            "Bullish Counterattack Lines (sometimes confused)",
            "Deai Sen Bullish"
        ],
        "japanese_name": "Deai Sen",
        "category": "Two Candle",
        "sub_category": "Bullish Reversal",
        "sentiment": "Bullish",
        "expected_direction": "UP",
        "trend_required": "Downtrend",
        "num_candles": 2,
        "pattern_structure": "Long bearish candle followed by a bullish candle that opens lower but closes at the same level as Candle 1's close",
        "candle_by_candle": [
            "Candle 1: Long bearish candle in a downtrend.",
            "Candle 2: Bullish candle that opens below C1's close (gaps down or opens lower) and rallies to close at approximately the same price as C1's close."
        ],
        "market_psychology": "Sellers push prices lower but buyers fight back to bring the close to exactly where sellers ended the previous session. This standoff at the same level shows bears are losing their edge.",
        "confirmation_required": "Bullish candle following, closing above the meeting point.",
        "volume_confirmation": "Higher volume on C2 confirms buyer strength.",
        "volatility_conditions": "Normal volatility. Gaps more common in stocks.",
        "gap_requirement": "Preferred",
        "reliability": "Low",
        "success_rate_range": "45-58%",
        "failure_conditions": [
            "Closes do not meet at same level",
            "No bullish follow-through",
            "C2 volume is weak"
        ],
        "entry_rules": "Enter long on confirmation candle above the meeting point.",
        "stop_loss_rules": "Below C2's low.",
        "take_profit_rules": "Nearest resistance or 1:2 RR.",
        "risk_reward": "1:2",
        "best_timeframes": [
            "Daily",
            "Weekly"
        ],
        "best_markets": [
            "Stocks",
            "Futures"
        ],
        "best_indicators": [
            "RSI (oversold)",
            "Volume",
            "Support levels"
        ],
        "common_mistakes": [
            "Confusing with Piercing Pattern (which closes into C1's body)",
            "Trading without confirmation",
            "Accepting non-matching closes"
        ],
        "ai_features": [
            "candle1.is_bearish AND candle1.body_ratio > 0.50",
            "candle2.is_bullish",
            "abs(candle1.close - candle2.close) < tolerance",
            "candle2.open < candle1.close"
        ],
        "ohlc_relationship": "C1: bearish; C2: bullish, C2_open < C1_close, abs(C1_close - C2_close) < tolerance",
        "label": "Bullish",
        "confidence_score": 42,
        "probability_score": 50
    },
    {
        "id": 31,
        "pattern_name": "Bearish Meeting Lines",
        "alternative_names": [
            "Deai Sen Bearish"
        ],
        "japanese_name": "Deai Sen",
        "category": "Two Candle",
        "sub_category": "Bearish Reversal",
        "sentiment": "Bearish",
        "expected_direction": "DOWN",
        "trend_required": "Uptrend",
        "num_candles": 2,
        "pattern_structure": "Long bullish candle followed by a bearish candle that opens higher but closes at the same level as Candle 1's close",
        "candle_by_candle": [
            "Candle 1: Long bullish candle in an uptrend.",
            "Candle 2: Bearish candle that opens above C1's close and drops to close at approximately the same price as C1's close."
        ],
        "market_psychology": "Buyers push prices higher but sellers fight back to close at the same level buyers achieved. The meeting shows bulls are losing their edge.",
        "confirmation_required": "Bearish candle closing below the meeting point.",
        "volume_confirmation": "Higher volume on C2 confirms selling strength.",
        "volatility_conditions": "Normal volatility.",
        "gap_requirement": "Preferred",
        "reliability": "Low",
        "success_rate_range": "45-58%",
        "failure_conditions": [
            "Closes do not match",
            "No bearish follow-through",
            "Strong bullish momentum resumes"
        ],
        "entry_rules": "Enter short on bearish confirmation below the meeting point.",
        "stop_loss_rules": "Above C2's high.",
        "take_profit_rules": "Nearest support or 1:2 RR.",
        "risk_reward": "1:2",
        "best_timeframes": [
            "Daily",
            "Weekly"
        ],
        "best_markets": [
            "Stocks",
            "Futures"
        ],
        "best_indicators": [
            "RSI (overbought)",
            "Volume",
            "Resistance levels"
        ],
        "common_mistakes": [
            "Confusing with Dark Cloud Cover",
            "Trading without confirmation",
            "Accepting non-matching closes"
        ],
        "ai_features": [
            "candle1.is_bullish AND candle1.body_ratio > 0.50",
            "candle2.is_bearish",
            "abs(candle1.close - candle2.close) < tolerance",
            "candle2.open > candle1.close"
        ],
        "ohlc_relationship": "C1: bullish; C2: bearish, C2_open > C1_close, abs(C1_close - C2_close) < tolerance",
        "label": "Bearish",
        "confidence_score": 42,
        "probability_score": 50
    },
    {
        "id": 32,
        "pattern_name": "Bullish Separating Lines",
        "alternative_names": [
            "Iki Chigai Sen Bullish"
        ],
        "japanese_name": "Iki Chigai Sen",
        "category": "Two Candle",
        "sub_category": "Bullish Continuation",
        "sentiment": "Bullish",
        "expected_direction": "CONTINUATION_UP",
        "trend_required": "Uptrend",
        "num_candles": 2,
        "pattern_structure": "Bearish candle followed by a bullish candle that opens at the same price as Candle 1's open and rallies",
        "candle_by_candle": [
            "Candle 1: Bearish candle appearing as a minor pullback in an uptrend. Opens at a certain price.",
            "Candle 2: Bullish candle (often marubozu-like) that opens at the same price as C1's open and rallies strongly upward."
        ],
        "market_psychology": "After a one-day pullback, the market reopens at the same level and buyers immediately take control, showing the pullback was just profit-taking and the uptrend resumes with conviction.",
        "confirmation_required": "Third candle continuing higher confirms the continuation.",
        "volume_confirmation": "Strong volume on C2 confirms the resumption of the uptrend.",
        "volatility_conditions": "Normal volatility. More reliable in established trends.",
        "gap_requirement": "None",
        "reliability": "Medium",
        "success_rate_range": "55-65%",
        "failure_conditions": [
            "Opens do not match",
            "C2 fails to close with a strong bullish body",
            "Uptrend is already exhausted"
        ],
        "entry_rules": "Enter long on C2's close or break above C2's high.",
        "stop_loss_rules": "Below C1's low.",
        "take_profit_rules": "Trail with the trend or target 1:2 RR.",
        "risk_reward": "1:2",
        "best_timeframes": [
            "Daily",
            "4H"
        ],
        "best_markets": [
            "Stocks",
            "Forex",
            "Futures"
        ],
        "best_indicators": [
            "Moving Averages (trend)",
            "ADX (>25)",
            "Volume"
        ],
        "common_mistakes": [
            "Trading in a downtrend (wrong context)",
            "Accepting non-matching opens",
            "Ignoring trend exhaustion signals"
        ],
        "ai_features": [
            "candle1.is_bearish",
            "candle2.is_bullish",
            "abs(candle1.open - candle2.open) < tolerance",
            "candle2.body_ratio > 0.60",
            "prior_trend = uptrend"
        ],
        "ohlc_relationship": "C1: bearish; C2: bullish, abs(C1_open - C2_open) < tolerance; C2 rallies from shared open",
        "label": "Bullish",
        "confidence_score": 55,
        "probability_score": 58
    },
    {
        "id": 33,
        "pattern_name": "Bearish Separating Lines",
        "alternative_names": [
            "Iki Chigai Sen Bearish"
        ],
        "japanese_name": "Iki Chigai Sen",
        "category": "Two Candle",
        "sub_category": "Bearish Continuation",
        "sentiment": "Bearish",
        "expected_direction": "CONTINUATION_DOWN",
        "trend_required": "Downtrend",
        "num_candles": 2,
        "pattern_structure": "Bullish candle followed by a bearish candle that opens at the same price as Candle 1's open and drops",
        "candle_by_candle": [
            "Candle 1: Bullish candle appearing as a minor bounce in a downtrend.",
            "Candle 2: Bearish candle (often marubozu-like) that opens at the same price as C1's open and drops strongly."
        ],
        "market_psychology": "After a one-day bounce, the market reopens at the same level and sellers immediately take control, showing the bounce was temporary and the downtrend resumes.",
        "confirmation_required": "Third candle continuing lower confirms continuation.",
        "volume_confirmation": "Strong volume on C2 confirms resumed selling.",
        "volatility_conditions": "Normal volatility.",
        "gap_requirement": "None",
        "reliability": "Medium",
        "success_rate_range": "55-65%",
        "failure_conditions": [
            "Opens do not match",
            "C2 fails to close with strong bearish body",
            "Downtrend is exhausted"
        ],
        "entry_rules": "Enter short on C2's close or break below C2's low.",
        "stop_loss_rules": "Above C1's high.",
        "take_profit_rules": "Trail with the trend or target 1:2 RR.",
        "risk_reward": "1:2",
        "best_timeframes": [
            "Daily",
            "4H"
        ],
        "best_markets": [
            "Stocks",
            "Forex",
            "Futures"
        ],
        "best_indicators": [
            "Moving Averages (trend)",
            "ADX (>25)",
            "Volume"
        ],
        "common_mistakes": [
            "Trading in an uptrend",
            "Accepting non-matching opens",
            "Ignoring trend exhaustion"
        ],
        "ai_features": [
            "candle1.is_bullish",
            "candle2.is_bearish",
            "abs(candle1.open - candle2.open) < tolerance",
            "candle2.body_ratio > 0.60",
            "prior_trend = downtrend"
        ],
        "ohlc_relationship": "C1: bullish; C2: bearish, abs(C1_open - C2_open) < tolerance; C2 drops from shared open",
        "label": "Bearish",
        "confidence_score": 55,
        "probability_score": 58
    },
    {
        "id": 34,
        "pattern_name": "Bullish Counterattack",
        "alternative_names": [
            "Bullish Counterattack Lines"
        ],
        "japanese_name": "",
        "category": "Two Candle",
        "sub_category": "Bullish Reversal",
        "sentiment": "Bullish",
        "expected_direction": "UP",
        "trend_required": "Downtrend",
        "num_candles": 2,
        "pattern_structure": "Long bearish candle followed by a long bullish candle that opens sharply lower but closes at approximately the same level as Candle 1's close",
        "candle_by_candle": [
            "Candle 1: Long bearish candle with strong selling pressure in a downtrend.",
            "Candle 2: Long bullish candle that opens significantly below C1's close (gap down) and rallies to close at approximately C1's close level."
        ],
        "market_psychology": "After bears push price sharply lower at C2's open, bulls mount a dramatic counter-offensive, reclaiming all lost ground. The long bullish body despite starting from a lower level shows strong buying conviction.",
        "confirmation_required": "Third candle closing above the counterattack close level confirms reversal.",
        "volume_confirmation": "High volume on C2 is essential to confirm the counterattack.",
        "volatility_conditions": "Works best with moderate to high volatility. Requires meaningful gap.",
        "gap_requirement": "Preferred",
        "reliability": "Medium",
        "success_rate_range": "50-62%",
        "failure_conditions": [
            "C2 close does not match C1 close",
            "C2 body is not long enough",
            "No gap down on C2 open",
            "No bullish follow-through"
        ],
        "entry_rules": "Enter long on bullish confirmation above the meeting close.",
        "stop_loss_rules": "Below C2's low.",
        "take_profit_rules": "Nearest resistance or 1:2 RR.",
        "risk_reward": "1:2",
        "best_timeframes": [
            "Daily",
            "Weekly"
        ],
        "best_markets": [
            "Stocks",
            "Futures",
            "Commodities"
        ],
        "best_indicators": [
            "RSI (oversold)",
            "Volume",
            "Support levels"
        ],
        "common_mistakes": [
            "Confusing with Meeting Lines (counterattack has larger C2 body)",
            "Not requiring the gap down open",
            "Trading without confirmation"
        ],
        "ai_features": [
            "candle1.is_bearish AND candle1.body_ratio > 0.50",
            "candle2.is_bullish AND candle2.body_ratio > 0.50",
            "candle2.open < candle1.close - gap_threshold",
            "abs(candle1.close - candle2.close) < tolerance"
        ],
        "ohlc_relationship": "C1: bearish, long body; C2: bullish, long body, C2_open << C1_close, abs(C1_close - C2_close) < tolerance",
        "label": "Bullish",
        "confidence_score": 52,
        "probability_score": 55
    },
    {
        "id": 35,
        "pattern_name": "Bearish Counterattack",
        "alternative_names": [
            "Bearish Counterattack Lines"
        ],
        "japanese_name": "",
        "category": "Two Candle",
        "sub_category": "Bearish Reversal",
        "sentiment": "Bearish",
        "expected_direction": "DOWN",
        "trend_required": "Uptrend",
        "num_candles": 2,
        "pattern_structure": "Long bullish candle followed by a long bearish candle that opens sharply higher but closes at approximately the same level as Candle 1's close",
        "candle_by_candle": [
            "Candle 1: Long bullish candle in an uptrend.",
            "Candle 2: Long bearish candle that opens significantly above C1's close (gap up) and sells off to close at approximately C1's close."
        ],
        "market_psychology": "Bulls gap price higher but sellers mount a dramatic counter-offensive, erasing all gains. The long bearish body starting from a higher level shows strong selling conviction.",
        "confirmation_required": "Third candle closing below the counterattack close level.",
        "volume_confirmation": "High volume on C2 confirms the counterattack.",
        "volatility_conditions": "Moderate to high volatility. Requires gap.",
        "gap_requirement": "Preferred",
        "reliability": "Medium",
        "success_rate_range": "50-62%",
        "failure_conditions": [
            "C2 close not matching C1 close",
            "C2 body too small",
            "No bearish follow-through"
        ],
        "entry_rules": "Enter short on bearish confirmation below the meeting close.",
        "stop_loss_rules": "Above C2's high.",
        "take_profit_rules": "Nearest support or 1:2 RR.",
        "risk_reward": "1:2",
        "best_timeframes": [
            "Daily",
            "Weekly"
        ],
        "best_markets": [
            "Stocks",
            "Futures",
            "Commodities"
        ],
        "best_indicators": [
            "RSI (overbought)",
            "Volume",
            "Resistance levels"
        ],
        "common_mistakes": [
            "Confusing with Bearish Meeting Lines",
            "Not requiring the gap up open",
            "Trading without confirmation"
        ],
        "ai_features": [
            "candle1.is_bullish AND candle1.body_ratio > 0.50",
            "candle2.is_bearish AND candle2.body_ratio > 0.50",
            "candle2.open > candle1.close + gap_threshold",
            "abs(candle1.close - candle2.close) < tolerance"
        ],
        "ohlc_relationship": "C1: bullish, long body; C2: bearish, long body, C2_open >> C1_close, abs(C1_close - C2_close) < tolerance",
        "label": "Bearish",
        "confidence_score": 52,
        "probability_score": 55
    },
    {
        "id": 36,
        "pattern_name": "Bullish Kicking",
        "alternative_names": [
            "Kicking Bullish",
            "Keri Ashi Bullish"
        ],
        "japanese_name": "Keri Ashi",
        "category": "Two Candle",
        "sub_category": "Bullish Reversal",
        "sentiment": "Bullish",
        "expected_direction": "UP",
        "trend_required": "Any",
        "num_candles": 2,
        "pattern_structure": "Bearish marubozu followed by a gap up and bullish marubozu — the most powerful two-candle reversal",
        "candle_by_candle": [
            "Candle 1: Bearish marubozu (or near-marubozu) — opens at high, closes at low with little or no shadows. Strong selling.",
            "Candle 2: Bullish marubozu (or near-marubozu) that gaps up above C1's open. Opens at low, closes at high. Strong buying with complete gap separation."
        ],
        "market_psychology": "An extreme bearish session is immediately followed by an extreme bullish session with a gap, indicating a violent and sudden shift in sentiment. This is one of the most powerful candlestick signals because both candles show maximum conviction in opposite directions, with the gap showing overnight sentiment change.",
        "confirmation_required": "The gap and marubozu nature are the confirmation themselves. Third candle continuing higher adds security.",
        "volume_confirmation": "High volume on both candles, especially C2, confirms conviction.",
        "volatility_conditions": "Can occur in any volatility but is strongest after periods of uncertainty.",
        "gap_requirement": "Required",
        "reliability": "High",
        "success_rate_range": "65-80%",
        "failure_conditions": [
            "No gap between C1 and C2",
            "C1 or C2 are not marubozu (have significant wicks)",
            "Gap fills immediately on next candle",
            "Pattern appears in range-bound choppy market"
        ],
        "entry_rules": "Enter long immediately on C2's close. The kicking pattern has built-in confirmation.",
        "stop_loss_rules": "Below C2's low (or C1's open if tight). The gap should hold.",
        "take_profit_rules": "Extended target — use 1:3 RR or trail. This pattern often signals strong moves.",
        "risk_reward": "1:3",
        "best_timeframes": [
            "Daily",
            "Weekly",
            "4H"
        ],
        "best_markets": [
            "Stocks",
            "Futures",
            "Commodities",
            "Crypto"
        ],
        "best_indicators": [
            "Volume",
            "Gap analysis",
            "ADX",
            "Momentum indicators"
        ],
        "common_mistakes": [
            "Accepting non-marubozu candles as kicking",
            "No gap present between the two candles",
            "Not trusting the signal and waiting too long"
        ],
        "ai_features": [
            "candle1.is_bearish AND candle1.body_ratio > 0.80",
            "candle2.is_bullish AND candle2.body_ratio > 0.80",
            "candle2.low > candle1.high (full gap up)",
            "gap_size > avg_body"
        ],
        "ohlc_relationship": "C1: bearish marubozu, body_ratio > 0.80; C2: bullish marubozu, body_ratio > 0.80; C2_low > C1_high (gap up)",
        "label": "Bullish",
        "confidence_score": 80,
        "probability_score": 72
    },
    {
        "id": 37,
        "pattern_name": "Bearish Kicking",
        "alternative_names": [
            "Kicking Bearish",
            "Keri Ashi Bearish"
        ],
        "japanese_name": "Keri Ashi",
        "category": "Two Candle",
        "sub_category": "Bearish Reversal",
        "sentiment": "Bearish",
        "expected_direction": "DOWN",
        "trend_required": "Any",
        "num_candles": 2,
        "pattern_structure": "Bullish marubozu followed by a gap down and bearish marubozu",
        "candle_by_candle": [
            "Candle 1: Bullish marubozu — opens at low, closes at high. Maximum buying.",
            "Candle 2: Bearish marubozu that gaps down below C1's open. Opens at high, closes at low. Complete gap separation."
        ],
        "market_psychology": "An extreme bullish session is immediately reversed by an extreme bearish session with a gap down. This violent reversal shows a complete collapse of bullish sentiment overnight, making it one of the most powerful bearish signals.",
        "confirmation_required": "The gap and marubozu nature serve as confirmation. Third candle continuing lower adds security.",
        "volume_confirmation": "High volume on both candles, especially C2.",
        "volatility_conditions": "Any volatility. Strongest after periods of uncertainty.",
        "gap_requirement": "Required",
        "reliability": "High",
        "success_rate_range": "65-80%",
        "failure_conditions": [
            "No gap between candles",
            "Candles are not marubozu",
            "Gap fills on next session",
            "Appears in choppy range"
        ],
        "entry_rules": "Enter short immediately on C2's close.",
        "stop_loss_rules": "Above C2's high or C1's close.",
        "take_profit_rules": "Extended target — 1:3 RR or trail.",
        "risk_reward": "1:3",
        "best_timeframes": [
            "Daily",
            "Weekly",
            "4H"
        ],
        "best_markets": [
            "Stocks",
            "Futures",
            "Commodities",
            "Crypto"
        ],
        "best_indicators": [
            "Volume",
            "Gap analysis",
            "ADX",
            "Momentum"
        ],
        "common_mistakes": [
            "Accepting non-marubozu candles",
            "No gap between the two candles",
            "Hesitating on entry"
        ],
        "ai_features": [
            "candle1.is_bullish AND candle1.body_ratio > 0.80",
            "candle2.is_bearish AND candle2.body_ratio > 0.80",
            "candle2.high < candle1.low (full gap down)",
            "gap_size > avg_body"
        ],
        "ohlc_relationship": "C1: bullish marubozu, body_ratio > 0.80; C2: bearish marubozu, body_ratio > 0.80; C2_high < C1_low (gap down)",
        "label": "Bearish",
        "confidence_score": 80,
        "probability_score": 72
    },
    {
        "id": 38,
        "pattern_name": "On Neck Line",
        "alternative_names": [
            "On Neck",
            "Ate Kubi"
        ],
        "japanese_name": "Ate Kubi",
        "category": "Two Candle",
        "sub_category": "Bearish Continuation",
        "sentiment": "Bearish",
        "expected_direction": "CONTINUATION_DOWN",
        "trend_required": "Downtrend",
        "num_candles": 2,
        "pattern_structure": "Long bearish candle followed by a small bullish candle that opens below C1's low and closes at or near C1's low — only touching the neck",
        "candle_by_candle": [
            "Candle 1: Long bearish candle with strong selling in a downtrend.",
            "Candle 2: Small bullish candle that opens below C1's low and closes at approximately C1's low. The bounce is minimal — only reaching the 'neck' of C1."
        ],
        "market_psychology": "After strong selling, a small bounce only reaches the prior low (not even into the body). This pathetically weak bounce shows buyers have no real power, and the downtrend is expected to continue.",
        "confirmation_required": "Next candle closing below C2's low confirms the continuation downward.",
        "volume_confirmation": "Low volume on C2 confirms the bounce is weak.",
        "volatility_conditions": "Normal volatility in a trending market.",
        "gap_requirement": "Preferred",
        "reliability": "Medium",
        "success_rate_range": "55-65%",
        "failure_conditions": [
            "C2 closes significantly into C1's body (becomes thrusting or piercing)",
            "Strong volume on C2 suggests real buying",
            "Downtrend already overextended"
        ],
        "entry_rules": "Enter short on break below C2's low.",
        "stop_loss_rules": "Above C2's high.",
        "take_profit_rules": "Next support level or 1:2 RR.",
        "risk_reward": "1:2",
        "best_timeframes": [
            "Daily",
            "4H"
        ],
        "best_markets": [
            "Stocks",
            "Forex",
            "Futures"
        ],
        "best_indicators": [
            "Moving Averages (downtrend)",
            "ADX",
            "Volume"
        ],
        "common_mistakes": [
            "Confusing with In Neck or Thrusting (different penetration depths)",
            "Misidentifying as a reversal pattern",
            "Not verifying the downtrend context"
        ],
        "ai_features": [
            "candle1.is_bearish AND candle1.body_ratio > 0.50",
            "candle2.is_bullish AND candle2.body_ratio < 0.40",
            "candle2.open < candle1.low",
            "abs(candle2.close - candle1.low) < tolerance"
        ],
        "ohlc_relationship": "C1: bearish, large; C2: bullish, small, C2_open < C1_low, C2_close ≈ C1_low",
        "label": "Bearish",
        "confidence_score": 55,
        "probability_score": 58
    },
    {
        "id": 39,
        "pattern_name": "In Neck Line",
        "alternative_names": [
            "In Neck",
            "Iri Kubi"
        ],
        "japanese_name": "Iri Kubi",
        "category": "Two Candle",
        "sub_category": "Bearish Continuation",
        "sentiment": "Bearish",
        "expected_direction": "CONTINUATION_DOWN",
        "trend_required": "Downtrend",
        "num_candles": 2,
        "pattern_structure": "Long bearish candle followed by a small bullish candle that opens below C1's low and closes slightly into C1's body — just inside the neck",
        "candle_by_candle": [
            "Candle 1: Long bearish candle in a downtrend.",
            "Candle 2: Small bullish candle that opens below C1's low and closes slightly above C1's close (just into C1's body, well below the midpoint)."
        ],
        "market_psychology": "Similar to On Neck but the bounce is marginally stronger — penetrating just into the body but not reaching the midpoint. Still signals a weak bounce insufficient to reverse the trend.",
        "confirmation_required": "Next candle closing below C2's low confirms continuation.",
        "volume_confirmation": "Low volume on C2 confirms weak bounce.",
        "volatility_conditions": "Normal volatility in trending market.",
        "gap_requirement": "Preferred",
        "reliability": "Medium",
        "success_rate_range": "52-62%",
        "failure_conditions": [
            "C2 closes above C1's midpoint (becomes Piercing)",
            "Strong volume on C2",
            "Downtrend overextended near strong support"
        ],
        "entry_rules": "Enter short on break below C2's low.",
        "stop_loss_rules": "Above C2's high.",
        "take_profit_rules": "Next support level or 1:2 RR.",
        "risk_reward": "1:2",
        "best_timeframes": [
            "Daily",
            "4H"
        ],
        "best_markets": [
            "Stocks",
            "Forex",
            "Futures"
        ],
        "best_indicators": [
            "Moving Averages",
            "ADX",
            "Volume"
        ],
        "common_mistakes": [
            "Confusing with On Neck (closes at C1 low) or Thrusting (closes deeper into body)",
            "Misreading as a reversal signal"
        ],
        "ai_features": [
            "candle1.is_bearish AND candle1.body_ratio > 0.50",
            "candle2.is_bullish",
            "candle2.open < candle1.low",
            "candle2.close > candle1.close",
            "candle2.close < (candle1.open + candle1.close) / 2"
        ],
        "ohlc_relationship": "C1: bearish; C2: bullish, C2_open < C1_low, C1_close < C2_close < C1_midpoint",
        "label": "Bearish",
        "confidence_score": 50,
        "probability_score": 55
    },
    {
        "id": 40,
        "pattern_name": "Thrusting Pattern",
        "alternative_names": [
            "Thrusting Line",
            "Sashikomi"
        ],
        "japanese_name": "Sashikomi",
        "category": "Two Candle",
        "sub_category": "Bearish Continuation",
        "sentiment": "Bearish",
        "expected_direction": "CONTINUATION_DOWN",
        "trend_required": "Downtrend",
        "num_candles": 2,
        "pattern_structure": "Long bearish candle followed by a bullish candle that opens below C1's low and closes into C1's body but below the midpoint",
        "candle_by_candle": [
            "Candle 1: Long bearish candle in a downtrend.",
            "Candle 2: Bullish candle that opens below C1's low and closes into C1's body, but does not reach C1's midpoint."
        ],
        "market_psychology": "The bounce is stronger than On Neck or In Neck but still insufficient to reach the midpoint. Buyers make progress but lack the conviction to push through. The downtrend is expected to continue. If C2 had closed above the midpoint, it would be a Piercing Pattern (bullish reversal).",
        "confirmation_required": "Next candle closing below C2's low confirms the continuation.",
        "volume_confirmation": "Moderate volume on C2. If volume is very high, the pattern may fail.",
        "volatility_conditions": "Normal volatility.",
        "gap_requirement": "Preferred",
        "reliability": "Low",
        "success_rate_range": "50-60%",
        "failure_conditions": [
            "C2 closes above C1's midpoint (becomes Piercing — bullish)",
            "High volume on C2 suggests real buying interest",
            "Near strong support level"
        ],
        "entry_rules": "Enter short on break below C2's low or bearish confirmation.",
        "stop_loss_rules": "Above C2's high.",
        "take_profit_rules": "Next support or 1:1.5 RR.",
        "risk_reward": "1:2",
        "best_timeframes": [
            "Daily",
            "4H"
        ],
        "best_markets": [
            "Stocks",
            "Forex",
            "Futures"
        ],
        "best_indicators": [
            "Moving Averages",
            "ADX",
            "Volume"
        ],
        "common_mistakes": [
            "Confusing with Piercing Pattern (which closes ABOVE midpoint and is bullish)",
            "Not checking if close is truly below midpoint",
            "Trading as a reversal instead of continuation"
        ],
        "ai_features": [
            "candle1.is_bearish AND candle1.body_ratio > 0.50",
            "candle2.is_bullish",
            "candle2.open < candle1.low",
            "candle2.close > candle1.close",
            "candle2.close < (candle1.open + candle1.close) / 2"
        ],
        "ohlc_relationship": "C1: bearish; C2: bullish, C2_open < C1_low, C1_close < C2_close < C1_midpoint (key: below midpoint)",
        "label": "Bearish",
        "confidence_score": 45,
        "probability_score": 52
    },
    {
        "id": 41,
        "pattern_name": "Two Crows",
        "alternative_names": [
            "Upside Gap Two Crows Simplified"
        ],
        "japanese_name": "Niwa Garasu",
        "category": "Three Candle",
        "sub_category": "Bearish Reversal",
        "sentiment": "Bearish",
        "expected_direction": "DOWN",
        "trend_required": "Uptrend",
        "num_candles": 3,
        "pattern_structure": "Long bullish C1 in uptrend, small bearish C2 that gaps above C1, larger bearish C3 that opens above C2's open and closes below C1's close",
        "candle_by_candle": [
            "Candle 1: Long bullish candle confirming the uptrend.",
            "Candle 2: Small bearish candle that gaps above C1's body. The first 'crow' appears at the top.",
            "Candle 3: Larger bearish candle that opens above C2's open but closes below C1's close, engulfing C2 and penetrating into C1's territory."
        ],
        "market_psychology": "After a strong uptrend, bears make two attempts to reverse. C2 shows initial hesitation at the highs with a gap up failure. C3 shows bears gaining strength as they open even higher but drive price down below C1's close, confirming a shift in control.",
        "confirmation_required": "Fourth candle closing below C3's low confirms the bearish reversal.",
        "volume_confirmation": "Increasing volume on C2 and C3 confirms growing bearish conviction.",
        "volatility_conditions": "Normal volatility. Gaps are essential.",
        "gap_requirement": "Required",
        "reliability": "Medium",
        "success_rate_range": "55-65%",
        "failure_conditions": [
            "No gap between C1 and C2",
            "C3 does not close below C1's close",
            "Bulls recover quickly after C3"
        ],
        "entry_rules": "Enter short on C3's close or break below C3's low.",
        "stop_loss_rules": "Above C2's high or the pattern high.",
        "take_profit_rules": "Prior swing low or 1:2 RR.",
        "risk_reward": "1:2",
        "best_timeframes": [
            "Daily",
            "Weekly"
        ],
        "best_markets": [
            "Stocks",
            "Futures"
        ],
        "best_indicators": [
            "RSI (overbought)",
            "Volume",
            "Resistance levels"
        ],
        "common_mistakes": [
            "Trading without the required gap",
            "Confusing with Upside Gap Two Crows (similar but different C3 close level)",
            "Not verifying uptrend context"
        ],
        "ai_features": [
            "candle1.is_bullish AND candle1.body_ratio > 0.50",
            "candle2.is_bearish AND candle2.low > candle1.high",
            "candle3.is_bearish",
            "candle3.open > candle2.open",
            "candle3.close < candle1.close"
        ],
        "ohlc_relationship": "C1: bullish, large; C2: bearish, gaps above C1; C3: bearish, C3_open > C2_open, C3_close < C1_close",
        "label": "Bearish",
        "confidence_score": 55,
        "probability_score": 58
    },
    {
        "id": 42,
        "pattern_name": "Rising Window",
        "alternative_names": [
            "Gap Up",
            "Window Rising",
            "Bullish Window"
        ],
        "japanese_name": "Mado",
        "category": "Two Candle",
        "sub_category": "Bullish Continuation",
        "sentiment": "Bullish",
        "expected_direction": "CONTINUATION_UP",
        "trend_required": "Uptrend",
        "num_candles": 2,
        "pattern_structure": "An upward gap (window) between Candle 1's high and Candle 2's low — the gap acts as future support",
        "candle_by_candle": [
            "Candle 1: Candle in an uptrend that sets a high.",
            "Candle 2: Candle that opens above C1's high, creating a gap (window) between C1's high and C2's low. This gap should not be filled."
        ],
        "market_psychology": "A gap up represents such strong demand that no trading occurs at those gap prices. The window acts as a support zone — Japanese analysts consider open windows as continuation signals. As long as the gap is not filled, the bullish trend continues.",
        "confirmation_required": "The gap remaining unfilled on subsequent candles confirms it as a support level.",
        "volume_confirmation": "High volume on the gap confirms strong buying demand.",
        "volatility_conditions": "Most common in stocks and futures. Rare in 24-hour forex markets.",
        "gap_requirement": "Required",
        "reliability": "Medium",
        "success_rate_range": "55-70%",
        "failure_conditions": [
            "Gap is filled (price returns into the window) — negates the signal",
            "Very small gap with no follow-through",
            "Low volume on the gap"
        ],
        "entry_rules": "Buy on pullback to the top of the gap (window support). Or buy on confirmation of gap holding.",
        "stop_loss_rules": "Below the bottom of the gap (C1's high). If gap fills, exit.",
        "take_profit_rules": "Ride the trend with trailing stop. Target next resistance.",
        "risk_reward": "1:3",
        "best_timeframes": [
            "Daily",
            "Weekly",
            "4H"
        ],
        "best_markets": [
            "Stocks",
            "Futures",
            "Crypto"
        ],
        "best_indicators": [
            "Volume",
            "Moving Averages (trend)",
            "Support at gap level"
        ],
        "common_mistakes": [
            "Ignoring gap fills (which negate the pattern)",
            "Trading tiny gaps that have no significance",
            "Not using the gap as a support reference"
        ],
        "ai_features": [
            "candle2.low > candle1.high (gap exists)",
            "gap_size = candle2.low - candle1.high",
            "gap_size > avg_range * 0.10",
            "prior_trend = uptrend"
        ],
        "ohlc_relationship": "C2_low > C1_high (gap up window); gap_size = C2_low - C1_high > 0",
        "label": "Bullish",
        "confidence_score": 60,
        "probability_score": 60
    },
    {
        "id": 43,
        "pattern_name": "Falling Window",
        "alternative_names": [
            "Gap Down",
            "Window Falling",
            "Bearish Window"
        ],
        "japanese_name": "Mado",
        "category": "Two Candle",
        "sub_category": "Bearish Continuation",
        "sentiment": "Bearish",
        "expected_direction": "CONTINUATION_DOWN",
        "trend_required": "Downtrend",
        "num_candles": 2,
        "pattern_structure": "A downward gap (window) between Candle 1's low and Candle 2's high — the gap acts as future resistance",
        "candle_by_candle": [
            "Candle 1: Candle in a downtrend that sets a low.",
            "Candle 2: Candle that opens below C1's low, creating a gap (window) between C1's low and C2's high. This gap should not be filled."
        ],
        "market_psychology": "A gap down represents such strong supply that no trading occurs at gap prices. The window acts as resistance. As long as the gap is unfilled, selling pressure continues and bears maintain control.",
        "confirmation_required": "The gap remaining unfilled on subsequent candles confirms it as resistance.",
        "volume_confirmation": "High volume on the gap down confirms strong selling.",
        "volatility_conditions": "Most common in stocks and futures. Rare in 24-hour forex.",
        "gap_requirement": "Required",
        "reliability": "Medium",
        "success_rate_range": "55-70%",
        "failure_conditions": [
            "Gap fills — negates the signal",
            "Very small gap with no follow-through",
            "Low volume"
        ],
        "entry_rules": "Sell on rally to the bottom of the gap (window resistance). Or sell on confirmation of gap holding.",
        "stop_loss_rules": "Above the top of the gap (C1's low). If gap fills, exit.",
        "take_profit_rules": "Ride the trend with trailing stop. Target next support.",
        "risk_reward": "1:3",
        "best_timeframes": [
            "Daily",
            "Weekly",
            "4H"
        ],
        "best_markets": [
            "Stocks",
            "Futures",
            "Crypto"
        ],
        "best_indicators": [
            "Volume",
            "Moving Averages (trend)",
            "Resistance at gap level"
        ],
        "common_mistakes": [
            "Ignoring gap fills",
            "Trading tiny insignificant gaps",
            "Not using the gap as resistance reference"
        ],
        "ai_features": [
            "candle2.high < candle1.low (gap exists)",
            "gap_size = candle1.low - candle2.high",
            "gap_size > avg_range * 0.10",
            "prior_trend = downtrend"
        ],
        "ohlc_relationship": "C2_high < C1_low (gap down window); gap_size = C1_low - C2_high > 0",
        "label": "Bearish",
        "confidence_score": 60,
        "probability_score": 60
    },
    {
        "id": 44,
        "pattern_name": "Morning Star",
        "alternative_names": [
            "Morning Star Pattern"
        ],
        "japanese_name": "Ake No Myojyo",
        "category": "Three Candle",
        "sub_category": "Bullish Reversal",
        "sentiment": "Bullish",
        "expected_direction": "UP",
        "trend_required": "Downtrend",
        "num_candles": 3,
        "pattern_structure": "Long bearish C1, small-bodied C2 (gap down), long bullish C3 (gap up) closing into C1's body",
        "candle_by_candle": [
            "Candle 1: Long bearish candle confirming the existing downtrend. Strong selling pressure.",
            "Candle 2: Small-bodied candle (spinning top or doji) that ideally gaps below C1's close. Shows indecision — selling pressure exhausting.",
            "Candle 3: Long bullish candle that ideally gaps above C2's body and closes well into C1's body (above C1's midpoint). Confirms buyer takeover."
        ],
        "market_psychology": "C1 shows bears in full control. C2's small body signals indecision and selling exhaustion. C3's strong bullish surge confirms buyers have seized control. The star formation between two large candles shows the decisive transfer of power from sellers to buyers.",
        "confirmation_required": "C3 should close above C1's midpoint. Fourth candle closing above C3's high provides extra confirmation.",
        "volume_confirmation": "Volume should decline on C2 (indecision) and increase significantly on C3 (conviction).",
        "volatility_conditions": "Works well in normal to moderate volatility. Gaps are more common in stocks and futures than forex.",
        "gap_requirement": "Preferred",
        "reliability": "High",
        "success_rate_range": "65-78%",
        "failure_conditions": [
            "C3 does not close above C1's midpoint",
            "No gap between C1 and C2",
            "Low volume on C3",
            "Appears without clear prior downtrend",
            "Very short C1 and C3 bodies"
        ],
        "entry_rules": "Enter long on C3's close or on break above C3's high. Conservative: wait for fourth candle confirmation.",
        "stop_loss_rules": "Below the low of C2 (the star candle). Conservative: below the lowest low of the entire pattern.",
        "take_profit_rules": "Target the prior swing high, nearest resistance, or 1:2 to 1:3 RR ratio.",
        "risk_reward": "1:2",
        "best_timeframes": [
            "Daily",
            "Weekly",
            "4H"
        ],
        "best_markets": [
            "Stocks",
            "Futures",
            "Crypto",
            "Forex",
            "Commodities"
        ],
        "best_indicators": [
            "RSI (oversold <30)",
            "MACD (bullish divergence)",
            "Volume",
            "Support levels",
            "Stochastic (oversold crossover)"
        ],
        "common_mistakes": [
            "Not requiring C3 to close into C1's body",
            "Trading without verifying prior downtrend",
            "Ignoring volume on C3",
            "Confusing with Evening Star (bearish version)"
        ],
        "ai_features": [
            "c1.is_bearish AND c1.body_ratio > 0.50",
            "c2.body_ratio < 0.25",
            "c3.is_bullish AND c3.body_ratio > 0.50",
            "c3.close > (c1.open + c1.close) / 2",
            "c2.high < c1.close (gap down ideal)"
        ],
        "ohlc_relationship": "C1: bearish, body_ratio > 0.50; C2: body_ratio < 0.25, ideally C2_high < C1_close; C3: bullish, C3_close > C1_midpoint",
        "label": "Bullish",
        "confidence_score": 78,
        "probability_score": 72
    },
    {
        "id": 45,
        "pattern_name": "Evening Star",
        "alternative_names": [
            "Evening Star Pattern"
        ],
        "japanese_name": "Yoi No Myojyo",
        "category": "Three Candle",
        "sub_category": "Bearish Reversal",
        "sentiment": "Bearish",
        "expected_direction": "DOWN",
        "trend_required": "Uptrend",
        "num_candles": 3,
        "pattern_structure": "Long bullish C1, small-bodied C2 (gap up), long bearish C3 (gap down) closing into C1's body",
        "candle_by_candle": [
            "Candle 1: Long bullish candle confirming the uptrend.",
            "Candle 2: Small-bodied candle that ideally gaps above C1's close. Indecision at the top.",
            "Candle 3: Long bearish candle that ideally gaps below C2 and closes well into C1's body (below C1's midpoint)."
        ],
        "market_psychology": "C1 shows bulls in control. C2's small body signals buyers are exhausting at the top. C3's bearish plunge confirms sellers have taken over. The star at the top marks the transition point.",
        "confirmation_required": "C3 should close below C1's midpoint. Fourth candle closing below C3's low confirms.",
        "volume_confirmation": "Declining volume on C2, increasing on C3.",
        "volatility_conditions": "Normal to moderate volatility. Gaps more common in stocks.",
        "gap_requirement": "Preferred",
        "reliability": "High",
        "success_rate_range": "65-78%",
        "failure_conditions": [
            "C3 does not close below C1's midpoint",
            "No gap between C1 and C2",
            "Low volume on C3",
            "No clear prior uptrend"
        ],
        "entry_rules": "Enter short on C3's close or break below C3's low.",
        "stop_loss_rules": "Above C2's high.",
        "take_profit_rules": "Prior swing low, nearest support, or 1:2 RR.",
        "risk_reward": "1:2",
        "best_timeframes": [
            "Daily",
            "Weekly",
            "4H"
        ],
        "best_markets": [
            "Stocks",
            "Futures",
            "Crypto",
            "Forex",
            "Commodities"
        ],
        "best_indicators": [
            "RSI (overbought >70)",
            "MACD (bearish divergence)",
            "Volume",
            "Resistance levels"
        ],
        "common_mistakes": [
            "Not requiring C3 to close into C1's body",
            "Trading without uptrend context",
            "Confusing with Morning Star"
        ],
        "ai_features": [
            "c1.is_bullish AND c1.body_ratio > 0.50",
            "c2.body_ratio < 0.25",
            "c3.is_bearish AND c3.body_ratio > 0.50",
            "c3.close < (c1.open + c1.close) / 2"
        ],
        "ohlc_relationship": "C1: bullish, body_ratio > 0.50; C2: body_ratio < 0.25, ideally C2_low > C1_close; C3: bearish, C3_close < C1_midpoint",
        "label": "Bearish",
        "confidence_score": 78,
        "probability_score": 72
    },
    {
        "id": 46,
        "pattern_name": "Morning Doji Star",
        "alternative_names": [
            "Doji Morning Star"
        ],
        "japanese_name": "Ake No Myojyo Doji",
        "category": "Three Candle",
        "sub_category": "Bullish Reversal",
        "sentiment": "Bullish",
        "expected_direction": "UP",
        "trend_required": "Downtrend",
        "num_candles": 3,
        "pattern_structure": "Long bearish C1, doji C2 gapping below, long bullish C3 gapping above — stronger variant of Morning Star",
        "candle_by_candle": [
            "Candle 1: Long bearish candle in a downtrend.",
            "Candle 2: Doji (open ≈ close) gapping below C1. The doji shows perfect indecision.",
            "Candle 3: Long bullish candle gapping above C2 and closing into C1's body above the midpoint."
        ],
        "market_psychology": "Like the Morning Star but the doji in the middle shows even more extreme indecision — the perfect equilibrium between buyers and sellers before the bullish reversal. This makes it slightly more reliable than a standard Morning Star.",
        "confirmation_required": "C3 closing above C1's midpoint is the confirmation itself. Fourth candle adds security.",
        "volume_confirmation": "Low volume on doji, high volume on C3.",
        "volatility_conditions": "Normal volatility. Doji should be a genuine indecision, not noise.",
        "gap_requirement": "Preferred",
        "reliability": "High",
        "success_rate_range": "68-80%",
        "failure_conditions": [
            "C3 fails to close above C1's midpoint",
            "C2 is not a doji (body too large)",
            "No gaps present",
            "Low volume on C3"
        ],
        "entry_rules": "Enter long on C3's close or break above C3's high.",
        "stop_loss_rules": "Below the doji low (C2).",
        "take_profit_rules": "Prior swing high or 1:2 to 1:3 RR.",
        "risk_reward": "1:2",
        "best_timeframes": [
            "Daily",
            "Weekly",
            "4H"
        ],
        "best_markets": [
            "Stocks",
            "Futures",
            "Crypto",
            "Commodities"
        ],
        "best_indicators": [
            "RSI (oversold)",
            "MACD (bullish divergence)",
            "Volume",
            "Support levels"
        ],
        "common_mistakes": [
            "Accepting a small-bodied candle instead of a true doji for C2",
            "Trading without gaps",
            "Ignoring volume"
        ],
        "ai_features": [
            "c1.is_bearish AND c1.body_ratio > 0.50",
            "c2.is_doji (body_ratio < 0.10)",
            "c3.is_bullish AND c3.body_ratio > 0.50",
            "c3.close > c1_midpoint"
        ],
        "ohlc_relationship": "C1: bearish, body_ratio > 0.50; C2: doji, body_ratio < 0.10; C3: bullish, C3_close > C1_midpoint",
        "label": "Bullish",
        "confidence_score": 80,
        "probability_score": 75
    },
    {
        "id": 47,
        "pattern_name": "Evening Doji Star",
        "alternative_names": [
            "Doji Evening Star"
        ],
        "japanese_name": "Yoi No Myojyo Doji",
        "category": "Three Candle",
        "sub_category": "Bearish Reversal",
        "sentiment": "Bearish",
        "expected_direction": "DOWN",
        "trend_required": "Uptrend",
        "num_candles": 3,
        "pattern_structure": "Long bullish C1, doji C2 gapping above, long bearish C3 gapping below — stronger variant of Evening Star",
        "candle_by_candle": [
            "Candle 1: Long bullish candle in an uptrend.",
            "Candle 2: Doji gapping above C1. Perfect indecision at the top.",
            "Candle 3: Long bearish candle gapping below C2 and closing into C1's body below the midpoint."
        ],
        "market_psychology": "The doji at the top of an uptrend shows perfect equilibrium between exhausted buyers and emerging sellers. C3 confirms the bearish takeover. Slightly more reliable than standard Evening Star.",
        "confirmation_required": "C3 closing below C1's midpoint. Fourth bearish candle adds confirmation.",
        "volume_confirmation": "Low volume on doji, high volume on C3.",
        "volatility_conditions": "Normal volatility.",
        "gap_requirement": "Preferred",
        "reliability": "High",
        "success_rate_range": "68-80%",
        "failure_conditions": [
            "C3 fails to close below C1's midpoint",
            "C2 not a true doji",
            "No gaps",
            "Low volume on C3"
        ],
        "entry_rules": "Enter short on C3's close or break below C3's low.",
        "stop_loss_rules": "Above C2's high.",
        "take_profit_rules": "Prior swing low or 1:2 RR.",
        "risk_reward": "1:2",
        "best_timeframes": [
            "Daily",
            "Weekly",
            "4H"
        ],
        "best_markets": [
            "Stocks",
            "Futures",
            "Crypto",
            "Commodities"
        ],
        "best_indicators": [
            "RSI (overbought)",
            "MACD (bearish divergence)",
            "Volume",
            "Resistance levels"
        ],
        "common_mistakes": [
            "Accepting non-doji C2",
            "Trading without gaps",
            "Ignoring volume on C3"
        ],
        "ai_features": [
            "c1.is_bullish AND c1.body_ratio > 0.50",
            "c2.is_doji (body_ratio < 0.10)",
            "c3.is_bearish AND c3.body_ratio > 0.50",
            "c3.close < c1_midpoint"
        ],
        "ohlc_relationship": "C1: bullish, body_ratio > 0.50; C2: doji; C3: bearish, C3_close < C1_midpoint",
        "label": "Bearish",
        "confidence_score": 80,
        "probability_score": 75
    },
    {
        "id": 48,
        "pattern_name": "Bullish Abandoned Baby",
        "alternative_names": [
            "Abandoned Baby Bottom"
        ],
        "japanese_name": "Sute Go",
        "category": "Three Candle",
        "sub_category": "Bullish Reversal",
        "sentiment": "Bullish",
        "expected_direction": "UP",
        "trend_required": "Downtrend",
        "num_candles": 3,
        "pattern_structure": "Bearish C1, doji C2 that gaps below C1 AND below C3, bullish C3 that gaps above C2 — gaps on BOTH sides of the doji",
        "candle_by_candle": [
            "Candle 1: Long bearish candle in a downtrend.",
            "Candle 2: Doji that gaps below C1 (C2's high < C1's low) — the 'abandoned baby'. Completely isolated by gaps.",
            "Candle 3: Long bullish candle that gaps above C2 (C3's low > C2's high). Strong buying resumes."
        ],
        "market_psychology": "The doji is 'abandoned' between two gaps — sellers cannot continue lower and buyers aggressively gap up. This extreme isolation of the indecision point signals a dramatic and decisive reversal. Very rare but very powerful.",
        "confirmation_required": "The double gap structure is the confirmation. Very high reliability pattern.",
        "volume_confirmation": "Low volume on doji, high volume on C3.",
        "volatility_conditions": "Requires gapping markets. Very rare in forex.",
        "gap_requirement": "Required",
        "reliability": "High",
        "success_rate_range": "70-85%",
        "failure_conditions": [
            "No gap on one or both sides of the doji",
            "C2 is not a doji",
            "Gap fills immediately",
            "Very rare — often misidentified"
        ],
        "entry_rules": "Enter long on C3's close. High confidence entry.",
        "stop_loss_rules": "Below C2's low.",
        "take_profit_rules": "Extended target — 1:3 RR or trail the move.",
        "risk_reward": "1:3",
        "best_timeframes": [
            "Daily",
            "Weekly"
        ],
        "best_markets": [
            "Stocks",
            "Futures"
        ],
        "best_indicators": [
            "Volume",
            "Gap analysis",
            "RSI (oversold)"
        ],
        "common_mistakes": [
            "Identifying without true gaps on BOTH sides",
            "C2 not being a proper doji",
            "Confusing with Morning Doji Star (which doesn't require gaps on both sides)"
        ],
        "ai_features": [
            "c1.is_bearish AND c1.body_ratio > 0.50",
            "c2.is_doji",
            "c2.high < c1.low (gap down from C1)",
            "c3.low > c2.high (gap up from C2)",
            "c3.is_bullish AND c3.body_ratio > 0.50"
        ],
        "ohlc_relationship": "C1: bearish; C2: doji, C2_high < C1_low AND C3_low > C2_high (double gap); C3: bullish",
        "label": "Bullish",
        "confidence_score": 85,
        "probability_score": 78
    },
    {
        "id": 49,
        "pattern_name": "Bearish Abandoned Baby",
        "alternative_names": [
            "Abandoned Baby Top"
        ],
        "japanese_name": "Sute Go",
        "category": "Three Candle",
        "sub_category": "Bearish Reversal",
        "sentiment": "Bearish",
        "expected_direction": "DOWN",
        "trend_required": "Uptrend",
        "num_candles": 3,
        "pattern_structure": "Bullish C1, doji C2 that gaps above C1 AND above C3, bearish C3 that gaps below C2",
        "candle_by_candle": [
            "Candle 1: Long bullish candle in an uptrend.",
            "Candle 2: Doji that gaps above C1 (C2's low > C1's high). Isolated at the top.",
            "Candle 3: Long bearish candle that gaps below C2 (C3's high < C2's low). Strong selling resumes."
        ],
        "market_psychology": "The doji is abandoned at the top between two gaps. Buyers exhaust and sellers aggressively take over with a gap down. Very rare but very powerful bearish reversal.",
        "confirmation_required": "Double gap structure is self-confirming.",
        "volume_confirmation": "Low volume on doji, high volume on C3.",
        "volatility_conditions": "Requires gapping markets.",
        "gap_requirement": "Required",
        "reliability": "High",
        "success_rate_range": "70-85%",
        "failure_conditions": [
            "Missing gaps on either side",
            "C2 not a doji",
            "Gap fills immediately"
        ],
        "entry_rules": "Enter short on C3's close.",
        "stop_loss_rules": "Above C2's high.",
        "take_profit_rules": "Extended target — 1:3 RR or trail.",
        "risk_reward": "1:3",
        "best_timeframes": [
            "Daily",
            "Weekly"
        ],
        "best_markets": [
            "Stocks",
            "Futures"
        ],
        "best_indicators": [
            "Volume",
            "Gap analysis",
            "RSI (overbought)"
        ],
        "common_mistakes": [
            "Identifying without gaps on both sides",
            "C2 not a proper doji",
            "Confusing with Evening Doji Star"
        ],
        "ai_features": [
            "c1.is_bullish AND c1.body_ratio > 0.50",
            "c2.is_doji",
            "c2.low > c1.high",
            "c3.high < c2.low",
            "c3.is_bearish AND c3.body_ratio > 0.50"
        ],
        "ohlc_relationship": "C1: bullish; C2: doji, C2_low > C1_high AND C3_high < C2_low; C3: bearish",
        "label": "Bearish",
        "confidence_score": 85,
        "probability_score": 78
    },
    {
        "id": 50,
        "pattern_name": "Three White Soldiers",
        "alternative_names": [
            "Three Advancing Soldiers",
            "Sanpei"
        ],
        "japanese_name": "Sanpei",
        "category": "Three Candle",
        "sub_category": "Bullish Reversal",
        "sentiment": "Bullish",
        "expected_direction": "UP",
        "trend_required": "Downtrend",
        "num_candles": 3,
        "pattern_structure": "Three consecutive long bullish candles, each opening within the prior body and closing progressively higher with small upper shadows",
        "candle_by_candle": [
            "Candle 1: Long bullish candle, potentially ending a downtrend. Small upper shadow.",
            "Candle 2: Long bullish candle opening within C1's body and closing above C1's high. Small upper shadow.",
            "Candle 3: Long bullish candle opening within C2's body and closing above C2's high. Small upper shadow."
        ],
        "market_psychology": "Three sessions of sustained, determined buying with each session building on the last. The pattern shows strong conviction from buyers who are steadily taking control. Opening within the prior body shows orderly accumulation, not panic buying.",
        "confirmation_required": "The three candles themselves are the confirmation. Fourth bullish candle adds extra confidence.",
        "volume_confirmation": "Progressively increasing volume across all three candles is ideal.",
        "volatility_conditions": "Normal volatility. Works after downtrend or consolidation.",
        "gap_requirement": "None",
        "reliability": "High",
        "success_rate_range": "65-77%",
        "failure_conditions": [
            "Bodies becoming progressively shorter (stalling)",
            "Long upper shadows on C2 or C3 (advance block instead)",
            "Very overbought RSI already",
            "Near major resistance"
        ],
        "entry_rules": "Enter long on C3's close. Aggressive entry on C2's close.",
        "stop_loss_rules": "Below C1's low.",
        "take_profit_rules": "Trail with the move. Target next resistance or 1:2 RR.",
        "risk_reward": "1:2",
        "best_timeframes": [
            "Daily",
            "Weekly",
            "4H"
        ],
        "best_markets": [
            "Stocks",
            "Forex",
            "Crypto",
            "Futures",
            "Commodities"
        ],
        "best_indicators": [
            "Volume (increasing)",
            "RSI (not yet overbought)",
            "Moving Averages",
            "ADX"
        ],
        "common_mistakes": [
            "Accepting candles with long upper shadows (that's an Advance Block)",
            "Trading when bodies are shortening",
            "Not checking if RSI is already overbought"
        ],
        "ai_features": [
            "c1.is_bullish AND c2.is_bullish AND c3.is_bullish",
            "c2.open > c1.open AND c2.open < c1.close",
            "c3.open > c2.open AND c3.open < c2.close",
            "c2.close > c1.close AND c3.close > c2.close",
            "all bodies have body_ratio > 0.50",
            "upper_wick_ratio < 0.15 for all candles"
        ],
        "ohlc_relationship": "All three bullish; each opens within prior body; each closes progressively higher; small upper shadows",
        "label": "Bullish",
        "confidence_score": 75,
        "probability_score": 70
    },
    {
        "id": 51,
        "pattern_name": "Three Black Crows",
        "alternative_names": [
            "Three Crows"
        ],
        "japanese_name": "Sanba Garasu",
        "category": "Three Candle",
        "sub_category": "Bearish Reversal",
        "sentiment": "Bearish",
        "expected_direction": "DOWN",
        "trend_required": "Uptrend",
        "num_candles": 3,
        "pattern_structure": "Three consecutive long bearish candles, each opening within the prior body and closing progressively lower with small lower shadows",
        "candle_by_candle": [
            "Candle 1: Long bearish candle, potentially ending an uptrend. Small lower shadow.",
            "Candle 2: Long bearish candle opening within C1's body and closing below C1's low.",
            "Candle 3: Long bearish candle opening within C2's body and closing below C2's low."
        ],
        "market_psychology": "Three sessions of relentless, orderly selling. Each session opens within the prior body showing methodical distribution, not panic selling. Sellers are in complete control and systematically driving prices lower.",
        "confirmation_required": "The three candles are the confirmation. Fourth bearish candle adds security.",
        "volume_confirmation": "Increasing volume across all three candles.",
        "volatility_conditions": "Normal volatility.",
        "gap_requirement": "None",
        "reliability": "High",
        "success_rate_range": "65-77%",
        "failure_conditions": [
            "Bodies becoming progressively shorter",
            "Long lower shadows showing buying support",
            "RSI already deeply oversold",
            "Near major support"
        ],
        "entry_rules": "Enter short on C3's close.",
        "stop_loss_rules": "Above C1's high.",
        "take_profit_rules": "Trail the move. Target next support or 1:2 RR.",
        "risk_reward": "1:2",
        "best_timeframes": [
            "Daily",
            "Weekly",
            "4H"
        ],
        "best_markets": [
            "Stocks",
            "Forex",
            "Crypto",
            "Futures",
            "Commodities"
        ],
        "best_indicators": [
            "Volume (increasing)",
            "RSI (not yet oversold)",
            "Moving Averages",
            "ADX"
        ],
        "common_mistakes": [
            "Accepting shortening bodies",
            "Ignoring long lower shadows",
            "Trading when RSI already oversold"
        ],
        "ai_features": [
            "c1.is_bearish AND c2.is_bearish AND c3.is_bearish",
            "c2.open < c1.open AND c2.open > c1.close",
            "c3.open < c2.open AND c3.open > c2.close",
            "c2.close < c1.close AND c3.close < c2.close",
            "all body_ratio > 0.50",
            "lower_wick_ratio < 0.15 for all"
        ],
        "ohlc_relationship": "All three bearish; each opens within prior body; each closes progressively lower; small lower shadows",
        "label": "Bearish",
        "confidence_score": 75,
        "probability_score": 70
    },
    {
        "id": 52,
        "pattern_name": "Three Inside Up",
        "alternative_names": [
            "Confirmed Bullish Harami"
        ],
        "japanese_name": "",
        "category": "Three Candle",
        "sub_category": "Bullish Reversal",
        "sentiment": "Bullish",
        "expected_direction": "UP",
        "trend_required": "Downtrend",
        "num_candles": 3,
        "pattern_structure": "Large bearish C1, small bullish C2 inside C1 (harami), bullish C3 closing above C1's high",
        "candle_by_candle": [
            "Candle 1: Large bearish candle in a downtrend.",
            "Candle 2: Small bullish candle whose body is within C1's body (bullish harami formation).",
            "Candle 3: Bullish candle that closes above C1's high, confirming the harami reversal."
        ],
        "market_psychology": "C1-C2 form a bullish harami (selling exhaustion + small bullish body). C3 provides the confirmation that many traders wait for, closing decisively above the harami's mother candle. This is essentially a confirmed harami.",
        "confirmation_required": "C3 itself is the confirmation of the C1-C2 harami. Pattern is self-confirming.",
        "volume_confirmation": "Volume should increase on C3.",
        "volatility_conditions": "Normal volatility.",
        "gap_requirement": "None",
        "reliability": "High",
        "success_rate_range": "60-72%",
        "failure_conditions": [
            "C3 fails to close above C1's high",
            "C2 not contained within C1",
            "No prior downtrend",
            "Low volume on C3"
        ],
        "entry_rules": "Enter long on C3's close.",
        "stop_loss_rules": "Below the pattern low (C1's low).",
        "take_profit_rules": "Nearest resistance or 1:2 RR.",
        "risk_reward": "1:2",
        "best_timeframes": [
            "Daily",
            "4H",
            "1H"
        ],
        "best_markets": [
            "Stocks",
            "Forex",
            "Crypto",
            "Futures"
        ],
        "best_indicators": [
            "RSI (oversold)",
            "Volume",
            "Support levels",
            "Moving Averages"
        ],
        "common_mistakes": [
            "Not verifying C2 is inside C1",
            "C3 not closing above C1's high",
            "Ignoring trend context"
        ],
        "ai_features": [
            "c1.is_bearish AND c1.body_ratio > 0.50",
            "c2.is_bullish AND c2.body < c1.body",
            "c2.open > c1.close AND c2.close < c1.open",
            "c3.is_bullish AND c3.close > c1.high"
        ],
        "ohlc_relationship": "C1: bearish, large; C2: bullish, inside C1 body; C3: bullish, C3_close > C1_high",
        "label": "Bullish",
        "confidence_score": 70,
        "probability_score": 65
    },
    {
        "id": 53,
        "pattern_name": "Three Inside Down",
        "alternative_names": [
            "Confirmed Bearish Harami"
        ],
        "japanese_name": "",
        "category": "Three Candle",
        "sub_category": "Bearish Reversal",
        "sentiment": "Bearish",
        "expected_direction": "DOWN",
        "trend_required": "Uptrend",
        "num_candles": 3,
        "pattern_structure": "Large bullish C1, small bearish C2 inside C1 (harami), bearish C3 closing below C1's low",
        "candle_by_candle": [
            "Candle 1: Large bullish candle in an uptrend.",
            "Candle 2: Small bearish candle whose body is within C1's body (bearish harami).",
            "Candle 3: Bearish candle that closes below C1's low, confirming the harami reversal."
        ],
        "market_psychology": "C1-C2 form a bearish harami. C3 confirms it with a decisive close below the mother candle's low. The pattern shows buying exhaustion, indecision, then seller takeover.",
        "confirmation_required": "C3 is the confirmation. Self-confirming pattern.",
        "volume_confirmation": "Volume should increase on C3.",
        "volatility_conditions": "Normal volatility.",
        "gap_requirement": "None",
        "reliability": "High",
        "success_rate_range": "60-72%",
        "failure_conditions": [
            "C3 fails to close below C1's low",
            "C2 not inside C1",
            "No prior uptrend"
        ],
        "entry_rules": "Enter short on C3's close.",
        "stop_loss_rules": "Above the pattern high (C1's high).",
        "take_profit_rules": "Nearest support or 1:2 RR.",
        "risk_reward": "1:2",
        "best_timeframes": [
            "Daily",
            "4H",
            "1H"
        ],
        "best_markets": [
            "Stocks",
            "Forex",
            "Crypto",
            "Futures"
        ],
        "best_indicators": [
            "RSI (overbought)",
            "Volume",
            "Resistance levels"
        ],
        "common_mistakes": [
            "C2 not inside C1",
            "C3 not closing below C1's low",
            "Trading without uptrend"
        ],
        "ai_features": [
            "c1.is_bullish AND c1.body_ratio > 0.50",
            "c2.is_bearish AND c2.body < c1.body",
            "c2.open < c1.close AND c2.close > c1.open",
            "c3.is_bearish AND c3.close < c1.low"
        ],
        "ohlc_relationship": "C1: bullish, large; C2: bearish, inside C1 body; C3: bearish, C3_close < C1_low",
        "label": "Bearish",
        "confidence_score": 70,
        "probability_score": 65
    },
    {
        "id": 54,
        "pattern_name": "Three Outside Up",
        "alternative_names": [
            "Confirmed Bullish Engulfing"
        ],
        "japanese_name": "",
        "category": "Three Candle",
        "sub_category": "Bullish Reversal",
        "sentiment": "Bullish",
        "expected_direction": "UP",
        "trend_required": "Downtrend",
        "num_candles": 3,
        "pattern_structure": "Small bearish C1, large bullish C2 engulfing C1, bullish C3 closing higher",
        "candle_by_candle": [
            "Candle 1: Small bearish candle in a downtrend.",
            "Candle 2: Large bullish candle that engulfs C1's body completely (bullish engulfing).",
            "Candle 3: Bullish candle closing above C2's high, confirming the engulfing reversal."
        ],
        "market_psychology": "C1-C2 form a bullish engulfing. C3 provides the follow-through, confirming that the reversal has genuine momentum. This three-candle confirmation is more reliable than the two-candle engulfing alone.",
        "confirmation_required": "C3 is the confirmation. Self-confirming pattern.",
        "volume_confirmation": "Volume should be high on C2 and C3.",
        "volatility_conditions": "Normal volatility.",
        "gap_requirement": "None",
        "reliability": "High",
        "success_rate_range": "63-75%",
        "failure_conditions": [
            "C2 doesn't fully engulf C1",
            "C3 fails to close above C2's high",
            "Low volume on C2 and C3"
        ],
        "entry_rules": "Enter long on C3's close.",
        "stop_loss_rules": "Below the pattern low.",
        "take_profit_rules": "Nearest resistance or 1:2 RR.",
        "risk_reward": "1:2",
        "best_timeframes": [
            "Daily",
            "4H",
            "1H"
        ],
        "best_markets": [
            "Stocks",
            "Forex",
            "Crypto",
            "Futures"
        ],
        "best_indicators": [
            "RSI (oversold)",
            "Volume",
            "Support levels",
            "MACD"
        ],
        "common_mistakes": [
            "C2 not fully engulfing C1",
            "C3 not making a higher close",
            "Not verifying downtrend"
        ],
        "ai_features": [
            "c1.is_bearish",
            "c2.is_bullish AND c2.open < c1.close AND c2.close > c1.open",
            "c2.body > c1.body",
            "c3.is_bullish AND c3.close > c2.high"
        ],
        "ohlc_relationship": "C1: small bearish; C2: large bullish engulfing C1; C3: bullish, C3_close > C2_high",
        "label": "Bullish",
        "confidence_score": 72,
        "probability_score": 68
    },
    {
        "id": 55,
        "pattern_name": "Three Outside Down",
        "alternative_names": [
            "Confirmed Bearish Engulfing"
        ],
        "japanese_name": "",
        "category": "Three Candle",
        "sub_category": "Bearish Reversal",
        "sentiment": "Bearish",
        "expected_direction": "DOWN",
        "trend_required": "Uptrend",
        "num_candles": 3,
        "pattern_structure": "Small bullish C1, large bearish C2 engulfing C1, bearish C3 closing lower",
        "candle_by_candle": [
            "Candle 1: Small bullish candle in an uptrend.",
            "Candle 2: Large bearish candle engulfing C1's body (bearish engulfing).",
            "Candle 3: Bearish candle closing below C2's low, confirming the reversal."
        ],
        "market_psychology": "C1-C2 form a bearish engulfing. C3 confirms with follow-through selling, validating the reversal signal.",
        "confirmation_required": "C3 is the confirmation.",
        "volume_confirmation": "High volume on C2 and C3.",
        "volatility_conditions": "Normal volatility.",
        "gap_requirement": "None",
        "reliability": "High",
        "success_rate_range": "63-75%",
        "failure_conditions": [
            "C2 doesn't fully engulf C1",
            "C3 fails to close below C2's low",
            "Low volume"
        ],
        "entry_rules": "Enter short on C3's close.",
        "stop_loss_rules": "Above the pattern high.",
        "take_profit_rules": "Nearest support or 1:2 RR.",
        "risk_reward": "1:2",
        "best_timeframes": [
            "Daily",
            "4H",
            "1H"
        ],
        "best_markets": [
            "Stocks",
            "Forex",
            "Crypto",
            "Futures"
        ],
        "best_indicators": [
            "RSI (overbought)",
            "Volume",
            "Resistance levels",
            "MACD"
        ],
        "common_mistakes": [
            "C2 not fully engulfing C1",
            "C3 not making lower close",
            "Not verifying uptrend"
        ],
        "ai_features": [
            "c1.is_bullish",
            "c2.is_bearish AND c2.open > c1.close AND c2.close < c1.open",
            "c2.body > c1.body",
            "c3.is_bearish AND c3.close < c2.low"
        ],
        "ohlc_relationship": "C1: small bullish; C2: large bearish engulfing C1; C3: bearish, C3_close < C2_low",
        "label": "Bearish",
        "confidence_score": 72,
        "probability_score": 68
    },
    {
        "id": 56,
        "pattern_name": "Bullish Tri-Star",
        "alternative_names": [
            "Tri-Star Bottom"
        ],
        "japanese_name": "",
        "category": "Three Candle",
        "sub_category": "Bullish Reversal",
        "sentiment": "Bullish",
        "expected_direction": "UP",
        "trend_required": "Downtrend",
        "num_candles": 3,
        "pattern_structure": "Three consecutive dojis with the middle doji gapping below the other two — very rare, high reliability",
        "candle_by_candle": [
            "Candle 1: Doji in a downtrend.",
            "Candle 2: Doji that gaps below C1. The star doji at the lowest point.",
            "Candle 3: Doji that gaps above C2, at or near C1's level."
        ],
        "market_psychology": "Three consecutive sessions of complete indecision with the middle one isolated at the bottom. This triple indecision at a market low is extremely rare and signals a critical turning point where bears have completely exhausted themselves.",
        "confirmation_required": "Bullish candle following the three dojis provides confirmation.",
        "volume_confirmation": "Declining volume across all three dojis, volume expansion on confirmation.",
        "volatility_conditions": "Can occur in any volatility. Very rare pattern.",
        "gap_requirement": "Required",
        "reliability": "High",
        "success_rate_range": "65-80%",
        "failure_conditions": [
            "One or more candles are not dojis",
            "No gap on the middle doji",
            "No confirmation candle"
        ],
        "entry_rules": "Enter long on bullish confirmation candle.",
        "stop_loss_rules": "Below the lowest doji low.",
        "take_profit_rules": "Extended target — 1:3 RR.",
        "risk_reward": "1:3",
        "best_timeframes": [
            "Daily",
            "Weekly"
        ],
        "best_markets": [
            "Stocks",
            "Futures"
        ],
        "best_indicators": [
            "RSI (oversold)",
            "Volume",
            "Support levels"
        ],
        "common_mistakes": [
            "Accepting non-doji candles",
            "No gap on middle doji",
            "Pattern is very rare — don't force identification"
        ],
        "ai_features": [
            "c1.is_doji AND c2.is_doji AND c3.is_doji",
            "c2.high < c1.low (gap down)",
            "c3.low > c2.high (gap up)",
            "all body_ratio < 0.10"
        ],
        "ohlc_relationship": "All three dojis; C2 gaps below C1; C3 gaps above C2",
        "label": "Bullish",
        "confidence_score": 75,
        "probability_score": 70
    },
    {
        "id": 57,
        "pattern_name": "Bearish Tri-Star",
        "alternative_names": [
            "Tri-Star Top"
        ],
        "japanese_name": "",
        "category": "Three Candle",
        "sub_category": "Bearish Reversal",
        "sentiment": "Bearish",
        "expected_direction": "DOWN",
        "trend_required": "Uptrend",
        "num_candles": 3,
        "pattern_structure": "Three consecutive dojis with the middle doji gapping above the other two",
        "candle_by_candle": [
            "Candle 1: Doji in an uptrend.",
            "Candle 2: Doji that gaps above C1. The star doji at the highest point.",
            "Candle 3: Doji that gaps below C2, at or near C1's level."
        ],
        "market_psychology": "Triple indecision at a market top. Extremely rare and signals buyers have completely exhausted themselves. Critical turning point.",
        "confirmation_required": "Bearish candle following confirms.",
        "volume_confirmation": "Declining volume on dojis, expansion on confirmation.",
        "volatility_conditions": "Any volatility. Very rare.",
        "gap_requirement": "Required",
        "reliability": "High",
        "success_rate_range": "65-80%",
        "failure_conditions": [
            "Candles not dojis",
            "No gap on middle doji",
            "No confirmation"
        ],
        "entry_rules": "Enter short on bearish confirmation.",
        "stop_loss_rules": "Above the highest doji high.",
        "take_profit_rules": "Extended target — 1:3 RR.",
        "risk_reward": "1:3",
        "best_timeframes": [
            "Daily",
            "Weekly"
        ],
        "best_markets": [
            "Stocks",
            "Futures"
        ],
        "best_indicators": [
            "RSI (overbought)",
            "Volume",
            "Resistance levels"
        ],
        "common_mistakes": [
            "Accepting non-doji candles",
            "No gaps",
            "Forcing identification of very rare pattern"
        ],
        "ai_features": [
            "c1.is_doji AND c2.is_doji AND c3.is_doji",
            "c2.low > c1.high (gap up)",
            "c3.high < c2.low (gap down)",
            "all body_ratio < 0.10"
        ],
        "ohlc_relationship": "All three dojis; C2 gaps above C1; C3 gaps below C2",
        "label": "Bearish",
        "confidence_score": 75,
        "probability_score": 70
    },
    {
        "id": 58,
        "pattern_name": "Three Stars in the South",
        "alternative_names": [
            "Minami No Sansei"
        ],
        "japanese_name": "Minami No Sansei",
        "category": "Three Candle",
        "sub_category": "Bullish Reversal",
        "sentiment": "Bullish",
        "expected_direction": "UP",
        "trend_required": "Downtrend",
        "num_candles": 3,
        "pattern_structure": "Three bearish candles with progressively shorter bodies and shorter lower shadows, showing selling exhaustion",
        "candle_by_candle": [
            "Candle 1: Long bearish candle with a long lower shadow in a downtrend.",
            "Candle 2: Shorter bearish candle with a shorter lower shadow, whose low is above C1's low.",
            "Candle 3: Short bearish marubozu (no lower shadow) or near-marubozu, contained within C2's range."
        ],
        "market_psychology": "Each successive candle shows diminishing selling force. Shorter bodies and shorter lower shadows indicate bears are progressively losing momentum. By C3, the range has contracted significantly — a spring coiling for a potential bullish reversal.",
        "confirmation_required": "Bullish candle closing above C1's open confirms the reversal.",
        "volume_confirmation": "Declining volume confirms diminishing selling pressure.",
        "volatility_conditions": "Contracting volatility through the pattern.",
        "gap_requirement": "None",
        "reliability": "Medium",
        "success_rate_range": "55-65%",
        "failure_conditions": [
            "Bodies not progressively shorter",
            "Lower shadows not decreasing",
            "No bullish confirmation",
            "Strong selling resumes"
        ],
        "entry_rules": "Enter long on bullish confirmation candle.",
        "stop_loss_rules": "Below C1's low (the pattern low).",
        "take_profit_rules": "Nearest resistance or 1:2 RR.",
        "risk_reward": "1:2",
        "best_timeframes": [
            "Daily",
            "Weekly"
        ],
        "best_markets": [
            "Stocks",
            "Futures"
        ],
        "best_indicators": [
            "RSI (oversold)",
            "Volume (declining)",
            "Support levels"
        ],
        "common_mistakes": [
            "Not verifying progressive shortening of bodies and shadows",
            "Trading without confirmation",
            "Rare pattern — don't force identification"
        ],
        "ai_features": [
            "c1.is_bearish AND c2.is_bearish AND c3.is_bearish",
            "c1.body > c2.body > c3.body",
            "c1.lower_wick > c2.lower_wick > c3.lower_wick",
            "c2.low > c1.low",
            "c3 contained within c2 range"
        ],
        "ohlc_relationship": "All bearish; C1_body > C2_body > C3_body; lower shadows decreasing; C2_low > C1_low; C3 within C2 range",
        "label": "Bullish",
        "confidence_score": 55,
        "probability_score": 58
    },
    {
        "id": 59,
        "pattern_name": "Unique Three River Bottom",
        "alternative_names": [
            "Three River Bottom"
        ],
        "japanese_name": "",
        "category": "Three Candle",
        "sub_category": "Bullish Reversal",
        "sentiment": "Bullish",
        "expected_direction": "UP",
        "trend_required": "Downtrend",
        "num_candles": 3,
        "pattern_structure": "Long bearish C1, harami bearish C2 with long lower shadow, small bullish C3 below C2's body",
        "candle_by_candle": [
            "Candle 1: Long bearish candle in a downtrend.",
            "Candle 2: Bearish candle with body inside C1 (harami) but with a long lower shadow testing new lows and bouncing back.",
            "Candle 3: Small bullish candle closing below C2's body but above C2's low."
        ],
        "market_psychology": "C1 shows strong selling. C2 tests new lows via the long shadow but recovers, showing buying interest at the extremes. C3's small bullish body near the lows confirms that selling pressure has been absorbed. A rare pattern signaling exhaustion.",
        "confirmation_required": "Bullish candle closing above C1's close confirms the reversal.",
        "volume_confirmation": "High volume on C2's lower shadow bounce, declining on C3.",
        "volatility_conditions": "Normal volatility. The long shadow on C2 is key.",
        "gap_requirement": "None",
        "reliability": "Low",
        "success_rate_range": "45-58%",
        "failure_conditions": [
            "C2 not a harami within C1",
            "C2 lacks the long lower shadow",
            "No bullish confirmation",
            "Very rare pattern — often misidentified"
        ],
        "entry_rules": "Enter long on bullish confirmation above C1's close.",
        "stop_loss_rules": "Below C2's low (the pattern low).",
        "take_profit_rules": "Nearest resistance or 1:2 RR.",
        "risk_reward": "1:2",
        "best_timeframes": [
            "Daily",
            "Weekly"
        ],
        "best_markets": [
            "Stocks",
            "Futures"
        ],
        "best_indicators": [
            "RSI (oversold)",
            "Volume",
            "Support levels"
        ],
        "common_mistakes": [
            "Misidentifying — this is a rare pattern",
            "Not verifying the harami relationship of C2",
            "Trading without confirmation"
        ],
        "ai_features": [
            "c1.is_bearish AND c1.body_ratio > 0.50",
            "c2.is_bearish AND c2.body inside c1.body",
            "c2.lower_wick_ratio > 0.40",
            "c3.is_bullish AND c3.body_ratio < 0.30",
            "c3.close < c2.open"
        ],
        "ohlc_relationship": "C1: bearish, large; C2: bearish harami inside C1, long lower shadow; C3: small bullish, close < C2 body",
        "label": "Bullish",
        "confidence_score": 45,
        "probability_score": 50
    },
    {
        "id": 60,
        "pattern_name": "Upside Gap Two Crows",
        "alternative_names": [
            "Gap Two Crows"
        ],
        "japanese_name": "",
        "category": "Three Candle",
        "sub_category": "Bearish Reversal",
        "sentiment": "Bearish",
        "expected_direction": "DOWN",
        "trend_required": "Uptrend",
        "num_candles": 3,
        "pattern_structure": "Long bullish C1, small bearish C2 gapping above C1, larger bearish C3 engulfing C2 but staying above C1's close",
        "candle_by_candle": [
            "Candle 1: Long bullish candle in an uptrend.",
            "Candle 2: Small bearish candle that gaps above C1's body — the first crow.",
            "Candle 3: Larger bearish candle that opens above C2's open and closes below C2's close, engulfing C2, but ideally still above C1's close."
        ],
        "market_psychology": "After a strong uptrend, two consecutive bearish candles appear at the top, with the second one engulfing the first. Despite the gap up on C2, sellers are gaining strength. The growing bearish pressure at the top warns of reversal.",
        "confirmation_required": "Fourth candle closing below C1's close confirms the reversal.",
        "volume_confirmation": "Increasing volume on C2 and C3.",
        "volatility_conditions": "Normal volatility. Gap required.",
        "gap_requirement": "Required",
        "reliability": "Medium",
        "success_rate_range": "55-68%",
        "failure_conditions": [
            "No gap between C1 and C2",
            "C3 doesn't engulf C2",
            "Bulls recover quickly",
            "No follow-through below C1's close"
        ],
        "entry_rules": "Enter short on break below C1's close or bearish confirmation.",
        "stop_loss_rules": "Above C3's high.",
        "take_profit_rules": "Prior swing low or 1:2 RR.",
        "risk_reward": "1:2",
        "best_timeframes": [
            "Daily",
            "Weekly"
        ],
        "best_markets": [
            "Stocks",
            "Futures"
        ],
        "best_indicators": [
            "RSI (overbought)",
            "Volume",
            "Resistance levels"
        ],
        "common_mistakes": [
            "No gap present",
            "Confusing with Two Crows pattern (different C3 close level)",
            "Not waiting for confirmation below C1 close"
        ],
        "ai_features": [
            "c1.is_bullish AND c1.body_ratio > 0.50",
            "c2.is_bearish AND c2.low > c1.high",
            "c3.is_bearish AND c3.open > c2.open AND c3.close < c2.close",
            "c3.close > c1.close (still above C1)"
        ],
        "ohlc_relationship": "C1: bullish; C2: bearish, gaps above C1; C3: bearish, engulfs C2, C3_close > C1_close",
        "label": "Bearish",
        "confidence_score": 58,
        "probability_score": 60
    },
    {
        "id": 61,
        "pattern_name": "Identical Three Crows",
        "alternative_names": [
            "Three Identical Crows"
        ],
        "japanese_name": "",
        "category": "Three Candle",
        "sub_category": "Bearish Reversal",
        "sentiment": "Bearish",
        "expected_direction": "DOWN",
        "trend_required": "Uptrend",
        "num_candles": 3,
        "pattern_structure": "Three long bearish candles with each opening at or very near the previous close — no gaps between them",
        "candle_by_candle": [
            "Candle 1: Long bearish candle beginning the reversal.",
            "Candle 2: Long bearish candle opening at or near C1's close. No gap.",
            "Candle 3: Long bearish candle opening at or near C2's close. No gap."
        ],
        "market_psychology": "Similar to Three Black Crows but with the critical difference that each opens at the prior close, showing relentless, gap-less selling. There is no overnight recovery — sellers maintain pressure continuously. Very strong bearish conviction.",
        "confirmation_required": "The three candles are the confirmation. Pattern is self-confirming.",
        "volume_confirmation": "High and sustained or increasing volume across all three.",
        "volatility_conditions": "Normal to elevated volatility showing strong directional move.",
        "gap_requirement": "None",
        "reliability": "High",
        "success_rate_range": "65-78%",
        "failure_conditions": [
            "Significant gaps between candles (becomes Three Black Crows instead)",
            "Bodies shortening",
            "RSI deeply oversold already",
            "Strong support immediately below"
        ],
        "entry_rules": "Enter short on C3's close.",
        "stop_loss_rules": "Above C1's open (pattern high).",
        "take_profit_rules": "Next support level or trail with trend.",
        "risk_reward": "1:2",
        "best_timeframes": [
            "Daily",
            "Weekly"
        ],
        "best_markets": [
            "Stocks",
            "Futures",
            "Crypto"
        ],
        "best_indicators": [
            "Volume (sustained high)",
            "ADX (strong trend)",
            "Moving Averages"
        ],
        "common_mistakes": [
            "Confusing with Three Black Crows (which can have gaps between opens)",
            "Not verifying opens match prior closes",
            "Trading when already deeply oversold"
        ],
        "ai_features": [
            "c1.is_bearish AND c2.is_bearish AND c3.is_bearish",
            "abs(c2.open - c1.close) < tolerance",
            "abs(c3.open - c2.close) < tolerance",
            "all body_ratio > 0.50"
        ],
        "ohlc_relationship": "All bearish; C2_open ≈ C1_close; C3_open ≈ C2_close; all large bodies",
        "label": "Bearish",
        "confidence_score": 75,
        "probability_score": 72
    },
    {
        "id": 62,
        "pattern_name": "Deliberation",
        "alternative_names": [
            "Stalling Pattern",
            "Aka Sanpo Daioji"
        ],
        "japanese_name": "Aka Sanpo",
        "category": "Three Candle",
        "sub_category": "Bearish Reversal",
        "sentiment": "Bearish",
        "expected_direction": "DOWN",
        "trend_required": "Uptrend",
        "num_candles": 3,
        "pattern_structure": "Two long bullish candles followed by a small-bodied or spinning top C3 near highs — hesitation signals potential reversal",
        "candle_by_candle": [
            "Candle 1: Long bullish candle in an uptrend.",
            "Candle 2: Long bullish candle continuing higher. Opens within C1's body.",
            "Candle 3: Small-bodied candle (spinning top, doji, or small candle) that opens near C2's close. May gap up slightly. Shows hesitation at the top."
        ],
        "market_psychology": "After two strong bullish sessions, C3's small body shows that buying momentum is stalling. The advance is 'deliberating' — bulls are losing conviction at the highs. This hesitation often precedes a pullback or reversal.",
        "confirmation_required": "Bearish candle following C3, closing below C2's close, confirms the reversal.",
        "volume_confirmation": "Declining volume on C3 shows fading interest.",
        "volatility_conditions": "Normal volatility. The stalling is more significant on higher timeframes.",
        "gap_requirement": "Optional",
        "reliability": "Low",
        "success_rate_range": "45-58%",
        "failure_conditions": [
            "C3 is a strong bullish candle (not stalling)",
            "Bullish momentum resumes on fourth candle",
            "High volume on C3 contradicts the hesitation"
        ],
        "entry_rules": "Enter short on bearish confirmation below C2's close.",
        "stop_loss_rules": "Above C3's high.",
        "take_profit_rules": "Nearest support or 1:1.5 RR.",
        "risk_reward": "1:2",
        "best_timeframes": [
            "Daily",
            "Weekly"
        ],
        "best_markets": [
            "Stocks",
            "Futures"
        ],
        "best_indicators": [
            "RSI (overbought)",
            "Volume (declining)",
            "Resistance levels"
        ],
        "common_mistakes": [
            "Trading without bearish confirmation",
            "Confusing with Advance Block (which has long upper shadows)",
            "Treating any small C3 as deliberation without context"
        ],
        "ai_features": [
            "c1.is_bullish AND c1.body_ratio > 0.50",
            "c2.is_bullish AND c2.body_ratio > 0.50",
            "c3.body_ratio < 0.25",
            "c3.open >= c2.close * 0.98"
        ],
        "ohlc_relationship": "C1 and C2: bullish, large bodies; C3: small body near C2's close; stalling at highs",
        "label": "Bearish",
        "confidence_score": 45,
        "probability_score": 50
    },
    {
        "id": 63,
        "pattern_name": "Advance Block",
        "alternative_names": [
            "Advancing Block"
        ],
        "japanese_name": "",
        "category": "Three Candle",
        "sub_category": "Bearish Reversal",
        "sentiment": "Bearish",
        "expected_direction": "DOWN",
        "trend_required": "Uptrend",
        "num_candles": 3,
        "pattern_structure": "Three bullish candles with progressively shorter bodies and progressively longer upper shadows — momentum fading",
        "candle_by_candle": [
            "Candle 1: Long bullish candle in the uptrend. Small upper shadow.",
            "Candle 2: Shorter bullish candle opening within C1's body. Longer upper shadow than C1.",
            "Candle 3: Even shorter bullish candle opening within C2's body. Longest upper shadow. The advance is being blocked."
        ],
        "market_psychology": "Despite three consecutive bullish closes, each candle shows diminishing buying power (shorter bodies) and increasing selling pressure at the highs (longer upper shadows). This is the opposite of strong Three White Soldiers — the advance is being blocked by emerging sellers.",
        "confirmation_required": "Bearish candle confirming the block is necessary.",
        "volume_confirmation": "Declining volume supports the weakening advance.",
        "volatility_conditions": "Normal volatility.",
        "gap_requirement": "None",
        "reliability": "Medium",
        "success_rate_range": "50-63%",
        "failure_conditions": [
            "Bodies not progressively shorter",
            "Upper shadows not progressively longer",
            "Strong volume on C3 contradicts weakness",
            "Bulls push through with strong C4"
        ],
        "entry_rules": "Enter short on bearish confirmation candle.",
        "stop_loss_rules": "Above the highest high of the pattern.",
        "take_profit_rules": "Nearest support or 1:2 RR.",
        "risk_reward": "1:2",
        "best_timeframes": [
            "Daily",
            "Weekly"
        ],
        "best_markets": [
            "Stocks",
            "Futures",
            "Crypto"
        ],
        "best_indicators": [
            "RSI (overbought)",
            "Volume (declining)",
            "Resistance levels"
        ],
        "common_mistakes": [
            "Confusing with Three White Soldiers (which has small upper shadows)",
            "Not verifying progressive shadow growth",
            "Trading without confirmation"
        ],
        "ai_features": [
            "c1.is_bullish AND c2.is_bullish AND c3.is_bullish",
            "c1.body > c2.body > c3.body",
            "c1.upper_wick < c2.upper_wick < c3.upper_wick",
            "c3.upper_wick_ratio > 0.30"
        ],
        "ohlc_relationship": "All bullish; C1_body > C2_body > C3_body; upper shadows increasing; momentum fading",
        "label": "Bearish",
        "confidence_score": 55,
        "probability_score": 55
    },
    {
        "id": 64,
        "pattern_name": "Stick Sandwich",
        "alternative_names": [
            "Sandwich Pattern"
        ],
        "japanese_name": "",
        "category": "Three Candle",
        "sub_category": "Bullish Reversal",
        "sentiment": "Bullish",
        "expected_direction": "UP",
        "trend_required": "Downtrend",
        "num_candles": 3,
        "pattern_structure": "Bearish C1, bullish C2, bearish C3 where C1 and C3 have the same closing price — the matching closes sandwich the bullish candle",
        "candle_by_candle": [
            "Candle 1: Bearish candle in a downtrend closing at a certain price.",
            "Candle 2: Bullish candle that rallies up.",
            "Candle 3: Bearish candle that returns to close at the same price as C1 — establishing support."
        ],
        "market_psychology": "The matching closes of C1 and C3 define a support level that has been tested twice. Despite a rally (C2) and retreat (C3), the same price holds. This double-tested support sandwiching a rally suggests the downside is limited and a reversal may follow.",
        "confirmation_required": "Bullish candle closing above C2's high confirms the reversal.",
        "volume_confirmation": "Volume on C3 should be lower than C1, suggesting reduced selling.",
        "volatility_conditions": "Normal volatility.",
        "gap_requirement": "None",
        "reliability": "Low",
        "success_rate_range": "45-55%",
        "failure_conditions": [
            "C1 and C3 closes not matching",
            "No bullish confirmation",
            "C3 breaks below C1's close (support fails)"
        ],
        "entry_rules": "Enter long on bullish confirmation above C2's high.",
        "stop_loss_rules": "Below the matching closes (C1/C3 close level).",
        "take_profit_rules": "Nearest resistance or 1:2 RR.",
        "risk_reward": "1:2",
        "best_timeframes": [
            "Daily",
            "4H"
        ],
        "best_markets": [
            "Stocks",
            "Futures"
        ],
        "best_indicators": [
            "RSI (oversold)",
            "Volume",
            "Support levels"
        ],
        "common_mistakes": [
            "Closes not truly matching",
            "Trading without confirmation",
            "Rare pattern — avoid forcing identification"
        ],
        "ai_features": [
            "c1.is_bearish AND c3.is_bearish",
            "c2.is_bullish",
            "abs(c1.close - c3.close) < tolerance",
            "c2.close > c1.open"
        ],
        "ohlc_relationship": "C1: bearish; C2: bullish; C3: bearish; abs(C1_close - C3_close) < tolerance (sandwich)",
        "label": "Bullish",
        "confidence_score": 42,
        "probability_score": 48
    },
    {
        "id": 65,
        "pattern_name": "Concealing Baby Swallow",
        "alternative_names": [
            "Baby Swallow"
        ],
        "japanese_name": "",
        "category": "Four Candle",
        "sub_category": "Bullish Reversal",
        "sentiment": "Bullish",
        "expected_direction": "UP",
        "trend_required": "Downtrend",
        "num_candles": 4,
        "pattern_structure": "Two bearish marubozu, then C3 gaps down as a harami star inside C2 with long upper shadow reaching into C2, then C4 bearish engulfs C3 including shadows",
        "candle_by_candle": [
            "Candle 1: Bearish marubozu (no or minimal shadows) in a downtrend.",
            "Candle 2: Bearish marubozu continuing the strong selling.",
            "Candle 3: Gaps down, opens below C2's close. Has a long upper shadow that reaches into C2's body. Small body. The 'baby' being concealed.",
            "Candle 4: Large bearish candle that opens above C3's high and closes below C3's low, completely engulfing C3 including its shadows."
        ],
        "market_psychology": "Two strong bearish sessions establish a severe downtrend. C3 gaps down but its long upper shadow probes back into C2 — buyers are trying to emerge from the bottom. C4 conceals this baby rally attempt by engulfing C3, but the buying attempt itself signals an impending reversal.",
        "confirmation_required": "Bullish candle following C4 confirms the reversal. This is a very rare pattern.",
        "volume_confirmation": "High volume on C1-C2, declining on C3, volume on C4 showing final capitulation.",
        "volatility_conditions": "Elevated volatility with strong trending market.",
        "gap_requirement": "Required",
        "reliability": "Medium",
        "success_rate_range": "55-68%",
        "failure_conditions": [
            "C1 and C2 are not marubozu",
            "C3 does not gap down",
            "C3's upper shadow doesn't reach into C2's body",
            "C4 doesn't engulf C3",
            "Very rare — often misidentified"
        ],
        "entry_rules": "Enter long on bullish confirmation following C4.",
        "stop_loss_rules": "Below C4's low.",
        "take_profit_rules": "Prior swing high or 1:2 RR.",
        "risk_reward": "1:2",
        "best_timeframes": [
            "Daily",
            "Weekly"
        ],
        "best_markets": [
            "Stocks",
            "Futures"
        ],
        "best_indicators": [
            "RSI (deeply oversold)",
            "Volume (capitulation)",
            "Support levels"
        ],
        "common_mistakes": [
            "C1/C2 not being proper marubozu",
            "Missing the gap on C3",
            "Extremely rare — must match all criteria precisely"
        ],
        "ai_features": [
            "c1.is_bearish AND c1.body_ratio > 0.85 (marubozu)",
            "c2.is_bearish AND c2.body_ratio > 0.85",
            "c3.open < c2.close (gap down)",
            "c3.upper_wick extends into c2.body",
            "c4.is_bearish AND c4.open > c3.high AND c4.close < c3.low"
        ],
        "ohlc_relationship": "C1-C2: bearish marubozu; C3: gaps down, upper shadow into C2 body; C4: engulfs C3 entirely",
        "label": "Bullish",
        "confidence_score": 55,
        "probability_score": 58
    },
    {
        "id": 66,
        "pattern_name": "Bullish Side-by-Side White Lines",
        "alternative_names": [
            "Side by Side Lines Bullish"
        ],
        "japanese_name": "Narabi Aka",
        "category": "Three Candle",
        "sub_category": "Bullish Continuation",
        "sentiment": "Bullish",
        "expected_direction": "CONTINUATION_UP",
        "trend_required": "Uptrend",
        "num_candles": 3,
        "pattern_structure": "Bullish C1 gaps up, then two bullish candles C2 and C3 with similar opening prices side-by-side in the gap",
        "candle_by_candle": [
            "Candle 1: Bullish candle that gaps up in an uptrend.",
            "Candle 2: Bullish candle opening near C1's close level.",
            "Candle 3: Bullish candle opening near C2's open, approximately same size as C2 — side by side."
        ],
        "market_psychology": "After a bullish gap up, two candles of similar size and open position confirm that the gap level is being defended as support. The side-by-side formation shows consistent buying at the gap level, supporting continuation.",
        "confirmation_required": "Fourth candle continuing higher confirms.",
        "volume_confirmation": "Sustained volume on C2 and C3.",
        "volatility_conditions": "Normal volatility in a trending market.",
        "gap_requirement": "Required",
        "reliability": "Medium",
        "success_rate_range": "55-65%",
        "failure_conditions": [
            "No gap present",
            "C2 and C3 not similar in size or open",
            "Gap fills on subsequent candles"
        ],
        "entry_rules": "Enter long on break above C3's high.",
        "stop_loss_rules": "Below the gap (C1's high or lower).",
        "take_profit_rules": "Trail with trend or 1:2 RR.",
        "risk_reward": "1:2",
        "best_timeframes": [
            "Daily",
            "4H"
        ],
        "best_markets": [
            "Stocks",
            "Futures"
        ],
        "best_indicators": [
            "Moving Averages",
            "Volume",
            "ADX"
        ],
        "common_mistakes": [
            "No gap before the side-by-side lines",
            "C2 and C3 very different in size",
            "Confusing with other continuation patterns"
        ],
        "ai_features": [
            "c1.is_bullish",
            "gap between c1.high and c2.low (or c2.open near c1.close after gap)",
            "c2.is_bullish AND c3.is_bullish",
            "abs(c2.open - c3.open) < tolerance",
            "abs(c2.body - c3.body) < tolerance"
        ],
        "ohlc_relationship": "C1: bullish, gaps up; C2 & C3: bullish, similar opens and body sizes, side by side",
        "label": "Bullish",
        "confidence_score": 52,
        "probability_score": 55
    },
    {
        "id": 67,
        "pattern_name": "Bearish Side-by-Side White Lines",
        "alternative_names": [
            "Side by Side Lines Bearish"
        ],
        "japanese_name": "Narabi Aka",
        "category": "Three Candle",
        "sub_category": "Bearish Continuation",
        "sentiment": "Bearish",
        "expected_direction": "CONTINUATION_DOWN",
        "trend_required": "Downtrend",
        "num_candles": 3,
        "pattern_structure": "Bearish C1 gaps down, then two small bullish candles C2 and C3 side-by-side that fail to fill the gap",
        "candle_by_candle": [
            "Candle 1: Bearish candle that gaps down in a downtrend.",
            "Candle 2: Small bullish candle opening near C1's close.",
            "Candle 3: Small bullish candle opening near C2's open — side by side with C2. Both fail to fill the gap."
        ],
        "market_psychology": "After a bearish gap down, two small bullish attempts fail to fill the gap. The weak, side-by-side bounces show buyers have no real strength. The gap acts as resistance and the downtrend is expected to continue.",
        "confirmation_required": "Bearish candle breaking below C2/C3's lows confirms.",
        "volume_confirmation": "Low volume on C2/C3 confirms the bounces are weak.",
        "volatility_conditions": "Normal volatility.",
        "gap_requirement": "Required",
        "reliability": "Medium",
        "success_rate_range": "52-62%",
        "failure_conditions": [
            "Gap fills (C2/C3 close above C1's open)",
            "No gap present",
            "C2/C3 show strong buying volume"
        ],
        "entry_rules": "Enter short on break below C2/C3 lows.",
        "stop_loss_rules": "Above the gap (C1's low).",
        "take_profit_rules": "Next support or 1:2 RR.",
        "risk_reward": "1:2",
        "best_timeframes": [
            "Daily",
            "4H"
        ],
        "best_markets": [
            "Stocks",
            "Futures"
        ],
        "best_indicators": [
            "Moving Averages",
            "Volume (weak on bounces)",
            "ADX"
        ],
        "common_mistakes": [
            "No gap before side-by-side lines",
            "Bounces fill the gap (invalidates pattern)",
            "Confusing with a reversal"
        ],
        "ai_features": [
            "c1.is_bearish",
            "gap down present",
            "c2.is_bullish AND c3.is_bullish",
            "abs(c2.open - c3.open) < tolerance",
            "c2.close < c1.open AND c3.close < c1.open (gap not filled)"
        ],
        "ohlc_relationship": "C1: bearish, gaps down; C2 & C3: small bullish, similar opens, fail to fill gap",
        "label": "Bearish",
        "confidence_score": 50,
        "probability_score": 55
    },
    {
        "id": 68,
        "pattern_name": "Upside Tasuki Gap",
        "alternative_names": [
            "Tasuki Gap Bullish"
        ],
        "japanese_name": "Uwa Banare Tasuki",
        "category": "Three Candle",
        "sub_category": "Bullish Continuation",
        "sentiment": "Bullish",
        "expected_direction": "CONTINUATION_UP",
        "trend_required": "Uptrend",
        "num_candles": 3,
        "pattern_structure": "Bullish C1, bullish C2 gaps above C1, bearish C3 opens within C2 and closes into the gap but doesn't fill it",
        "candle_by_candle": [
            "Candle 1: Bullish candle in an uptrend.",
            "Candle 2: Bullish candle that gaps above C1 (C2's low > C1's high).",
            "Candle 3: Bearish candle that opens within C2's body and closes into the gap between C1 and C2, but does NOT fill it completely (C3's close > C1's high)."
        ],
        "market_psychology": "After a bullish gap, a bearish pullback tests the gap but fails to fill it. The gap holding as support confirms strong demand at those levels. The unfilled gap becomes a launching pad for further upside.",
        "confirmation_required": "The gap holding (not being filled) is the confirmation. Fourth bullish candle adds conviction.",
        "volume_confirmation": "Lower volume on C3 (the pullback) compared to C1 and C2.",
        "volatility_conditions": "Normal volatility in trending market.",
        "gap_requirement": "Required",
        "reliability": "Medium",
        "success_rate_range": "55-68%",
        "failure_conditions": [
            "C3 fills the gap completely (C3 close < C1 high)",
            "No gap between C1 and C2",
            "High volume on C3 suggests real selling",
            "Downtrend follows despite unfilled gap"
        ],
        "entry_rules": "Enter long near C3's close or on break above C3's high.",
        "stop_loss_rules": "Below C1's high (gap support). If gap fills, exit.",
        "take_profit_rules": "Trail the uptrend or target 1:2 RR.",
        "risk_reward": "1:2",
        "best_timeframes": [
            "Daily",
            "4H"
        ],
        "best_markets": [
            "Stocks",
            "Futures",
            "Crypto"
        ],
        "best_indicators": [
            "Volume",
            "Moving Averages",
            "Gap analysis"
        ],
        "common_mistakes": [
            "Gap fills completely (invalidates pattern)",
            "No actual gap present",
            "Confusing with Downside Tasuki Gap"
        ],
        "ai_features": [
            "c1.is_bullish",
            "c2.is_bullish AND c2.low > c1.high (gap up)",
            "c3.is_bearish AND c3.open < c2.close AND c3.open > c2.open",
            "c3.close > c1.high (gap not filled)"
        ],
        "ohlc_relationship": "C1: bullish; C2: bullish, gaps up; C3: bearish, closes into gap but C3_close > C1_high (gap holds)",
        "label": "Bullish",
        "confidence_score": 58,
        "probability_score": 60
    },
    {
        "id": 69,
        "pattern_name": "Downside Tasuki Gap",
        "alternative_names": [
            "Tasuki Gap Bearish"
        ],
        "japanese_name": "Shita Banare Tasuki",
        "category": "Three Candle",
        "sub_category": "Bearish Continuation",
        "sentiment": "Bearish",
        "expected_direction": "CONTINUATION_DOWN",
        "trend_required": "Downtrend",
        "num_candles": 3,
        "pattern_structure": "Bearish C1, bearish C2 gaps below C1, bullish C3 opens within C2 and closes into the gap but doesn't fill it",
        "candle_by_candle": [
            "Candle 1: Bearish candle in a downtrend.",
            "Candle 2: Bearish candle that gaps below C1 (C2's high < C1's low).",
            "Candle 3: Bullish candle that opens within C2's body and closes into the gap but does NOT fill it completely (C3's close < C1's low)."
        ],
        "market_psychology": "After a bearish gap, a bullish bounce tests the gap but fails to fill it. The gap holding as resistance confirms supply at those levels. The downtrend is expected to continue.",
        "confirmation_required": "Gap holding is the confirmation. Fourth bearish candle adds conviction.",
        "volume_confirmation": "Lower volume on C3.",
        "volatility_conditions": "Normal volatility.",
        "gap_requirement": "Required",
        "reliability": "Medium",
        "success_rate_range": "55-68%",
        "failure_conditions": [
            "C3 fills the gap (C3 close > C1 low)",
            "No gap between C1 and C2",
            "High volume on C3"
        ],
        "entry_rules": "Enter short near C3's close or break below C3's low.",
        "stop_loss_rules": "Above C1's low (gap resistance).",
        "take_profit_rules": "Trail the downtrend or 1:2 RR.",
        "risk_reward": "1:2",
        "best_timeframes": [
            "Daily",
            "4H"
        ],
        "best_markets": [
            "Stocks",
            "Futures",
            "Crypto"
        ],
        "best_indicators": [
            "Volume",
            "Moving Averages",
            "Gap analysis"
        ],
        "common_mistakes": [
            "Gap fills completely",
            "No gap present",
            "Confusing with Upside Tasuki Gap"
        ],
        "ai_features": [
            "c1.is_bearish",
            "c2.is_bearish AND c2.high < c1.low (gap down)",
            "c3.is_bullish AND c3.open > c2.close AND c3.open < c2.open",
            "c3.close < c1.low (gap not filled)"
        ],
        "ohlc_relationship": "C1: bearish; C2: bearish, gaps down; C3: bullish, closes into gap but C3_close < C1_low",
        "label": "Bearish",
        "confidence_score": 58,
        "probability_score": 60
    },
    {
        "id": 70,
        "pattern_name": "Upside Gap Three Methods",
        "alternative_names": [
            "Gap Three Methods Bullish"
        ],
        "japanese_name": "Uwa Banare Sanpoo Hatsu Oshi",
        "category": "Three Candle",
        "sub_category": "Bullish Continuation",
        "sentiment": "Bullish",
        "expected_direction": "CONTINUATION_UP",
        "trend_required": "Uptrend",
        "num_candles": 3,
        "pattern_structure": "Bullish C1, bullish C2 gaps up, bearish C3 opens within C2 and closes within C1, filling the gap — the filled gap acts as a bridge, not a breakdown",
        "candle_by_candle": [
            "Candle 1: Bullish candle in an uptrend.",
            "Candle 2: Bullish candle that gaps up above C1.",
            "Candle 3: Bearish candle that opens within C2's body and closes within C1's body, filling the gap between C1 and C2."
        ],
        "market_psychology": "Unlike Upside Tasuki Gap (where the gap holds), here the gap is fully filled by C3. In Japanese candlestick theory, this filling of the gap is seen as a 'rest' in the uptrend — the gap has been tested and the uptrend can resume from a stronger base.",
        "confirmation_required": "Fourth bullish candle closing above C2's high confirms continuation.",
        "volume_confirmation": "Low volume on C3 (gap fill is profit-taking, not trend change).",
        "volatility_conditions": "Normal volatility.",
        "gap_requirement": "Required",
        "reliability": "Low",
        "success_rate_range": "50-60%",
        "failure_conditions": [
            "No gap between C1 and C2",
            "C3 closes below C1's low (breaks through, not just filling)",
            "High volume on C3 suggests real selling",
            "No bullish follow-through"
        ],
        "entry_rules": "Enter long on bullish confirmation above C2's high.",
        "stop_loss_rules": "Below C1's low.",
        "take_profit_rules": "Next resistance or 1:2 RR.",
        "risk_reward": "1:2",
        "best_timeframes": [
            "Daily",
            "4H"
        ],
        "best_markets": [
            "Stocks",
            "Futures"
        ],
        "best_indicators": [
            "Volume",
            "Moving Averages",
            "ADX"
        ],
        "common_mistakes": [
            "Confusing with Upside Tasuki Gap (which does NOT fill the gap)",
            "C3 breaking below C1's low (not a gap fill — it's a breakdown)",
            "Trading without confirmation"
        ],
        "ai_features": [
            "c1.is_bullish",
            "c2.is_bullish AND c2.low > c1.high (gap up)",
            "c3.is_bearish AND c3.open < c2.close",
            "c3.close > c1.open AND c3.close < c1.close (fills gap, stays in C1 body)"
        ],
        "ohlc_relationship": "C1: bullish; C2: bullish, gaps up; C3: bearish, fills the gap (C3 close within C1 body)",
        "label": "Bullish",
        "confidence_score": 48,
        "probability_score": 52
    },
    {
        "id": 71,
        "pattern_name": "Downside Gap Three Methods",
        "alternative_names": [
            "Gap Three Methods Bearish"
        ],
        "japanese_name": "Shita Banare Sanpoo Hatsu Oshi",
        "category": "Three Candle",
        "sub_category": "Bearish Continuation",
        "sentiment": "Bearish",
        "expected_direction": "CONTINUATION_DOWN",
        "trend_required": "Downtrend",
        "num_candles": 3,
        "pattern_structure": "Bearish C1, bearish C2 gaps down, bullish C3 opens within C2 and closes within C1, filling the gap",
        "candle_by_candle": [
            "Candle 1: Bearish candle in a downtrend.",
            "Candle 2: Bearish candle that gaps down below C1.",
            "Candle 3: Bullish candle that opens within C2's body and closes within C1's body, filling the gap between C1 and C2."
        ],
        "market_psychology": "The gap is filled by the bullish C3, but this is seen as a rest in the downtrend rather than a reversal. The filling provides a brief consolidation before the downtrend resumes.",
        "confirmation_required": "Fourth bearish candle closing below C2's low confirms continuation.",
        "volume_confirmation": "Low volume on C3.",
        "volatility_conditions": "Normal volatility.",
        "gap_requirement": "Required",
        "reliability": "Low",
        "success_rate_range": "50-60%",
        "failure_conditions": [
            "No gap between C1 and C2",
            "C3 closes above C1's high",
            "High volume on C3",
            "No bearish follow-through"
        ],
        "entry_rules": "Enter short on bearish confirmation below C2's low.",
        "stop_loss_rules": "Above C1's high.",
        "take_profit_rules": "Next support or 1:2 RR.",
        "risk_reward": "1:2",
        "best_timeframes": [
            "Daily",
            "4H"
        ],
        "best_markets": [
            "Stocks",
            "Futures"
        ],
        "best_indicators": [
            "Volume",
            "Moving Averages",
            "ADX"
        ],
        "common_mistakes": [
            "Confusing with Downside Tasuki Gap",
            "C3 breaking above C1's high",
            "Trading without confirmation"
        ],
        "ai_features": [
            "c1.is_bearish",
            "c2.is_bearish AND c2.high < c1.low (gap down)",
            "c3.is_bullish AND c3.open > c2.close",
            "c3.close < c1.close AND c3.close > c1.open (fills gap, in C1 body)"
        ],
        "ohlc_relationship": "C1: bearish; C2: bearish, gaps down; C3: bullish, fills the gap (C3 close within C1 body)",
        "label": "Bearish",
        "confidence_score": 48,
        "probability_score": 52
    },
    {
        "id": 72,
        "pattern_name": "Rising Three Methods",
        "alternative_names": [
            "Rising 3 Methods",
            "Bullish Three Methods"
        ],
        "japanese_name": "Uwa Banare Sanpoo Ohdatekomi",
        "category": "Five Candle",
        "sub_category": "Bullish Continuation",
        "sentiment": "Bullish",
        "expected_direction": "CONTINUATION_UP",
        "trend_required": "Uptrend",
        "num_candles": 5,
        "pattern_structure": "Long bullish C1, three small bearish candles (C2-C4) contained within C1's range, then long bullish C5 closing above C1's high",
        "candle_by_candle": [
            "Candle 1: Long bullish candle establishing the uptrend direction. Strong buying pressure with large body.",
            "Candle 2: Small bearish candle that trades within C1's range. Mild profit-taking begins.",
            "Candle 3: Small bearish candle continuing the consolidation within C1's range. Sellers unable to push below C1's low.",
            "Candle 4: Small bearish candle, still contained within C1's high-low range. The retracement loses momentum.",
            "Candle 5: Long bullish candle that opens within or near C4's body and closes above C1's high. Strong buying resumes, confirming the uptrend continuation."
        ],
        "market_psychology": "C1 shows strong buying. C2-C4 represent a brief rest or consolidation where short-term traders take profits, but the pullback is shallow (contained within C1). C5 confirms that the resting phase is over and bulls resume control, often trapping shorts who entered during the pullback.",
        "confirmation_required": "C5 must close above C1's high. Sixth candle continuing higher provides extra confirmation.",
        "volume_confirmation": "Volume should be high on C1 and C5, and decline during C2-C4 consolidation phase. Rising volume on C5 confirms conviction.",
        "volatility_conditions": "Works best in trending markets with moderate volatility. The consolidation candles should show compression.",
        "gap_requirement": "None",
        "reliability": "High",
        "success_rate_range": "65-79%",
        "failure_conditions": [
            "C2-C4 break below C1's low (invalidates containment)",
            "C5 fails to close above C1's high",
            "Volume remains high during C2-C4 (selling pressure too strong)",
            "Broader market turning bearish",
            "Pattern forms near major resistance"
        ],
        "entry_rules": "Enter long on C5's close or on break above C5's high. Stop and reverse if C5 fails.",
        "stop_loss_rules": "Below the lowest low of the entire 5-candle pattern (typically C3 or C4 low).",
        "take_profit_rules": "Measure C1's body height and project from C5's close. Or target next resistance level. Use trailing stop.",
        "risk_reward": "1:3",
        "best_timeframes": [
            "Daily",
            "Weekly",
            "4H"
        ],
        "best_markets": [
            "Stocks",
            "Futures",
            "Commodities",
            "Forex"
        ],
        "best_indicators": [
            "Moving Averages (trend confirmation)",
            "Volume",
            "ADX (trending >25)",
            "Bollinger Bands (squeeze during C2-C4)"
        ],
        "common_mistakes": [
            "Not verifying C2-C4 are contained within C1's range",
            "Trading before C5 confirms",
            "Ignoring volume pattern",
            "Confusing with Falling Three Methods"
        ],
        "ai_features": [
            "c1.is_bullish AND c1.body_ratio > 0.60",
            "c2.is_bearish AND c3.is_bearish AND c4.is_bearish",
            "all(c.high <= c1.high AND c.low >= c1.low for c in [c2,c3,c4])",
            "c5.is_bullish AND c5.close > c1.high",
            "c5.body_ratio > 0.50"
        ],
        "ohlc_relationship": "C1: bullish, body_ratio > 0.60; C2-C4: small bearish, all contained within C1 H-L range; C5: bullish, C5_close > C1_high, body_ratio > 0.50",
        "label": "Bullish",
        "confidence_score": 78,
        "probability_score": 72
    },
    {
        "id": 73,
        "pattern_name": "Falling Three Methods",
        "alternative_names": [
            "Falling 3 Methods",
            "Bearish Three Methods"
        ],
        "japanese_name": "Shita Banare Sanpoo Ohdatekomi",
        "category": "Five Candle",
        "sub_category": "Bearish Continuation",
        "sentiment": "Bearish",
        "expected_direction": "CONTINUATION_DOWN",
        "trend_required": "Downtrend",
        "num_candles": 5,
        "pattern_structure": "Long bearish C1, three small bullish candles (C2-C4) contained within C1's range, then long bearish C5 closing below C1's low",
        "candle_by_candle": [
            "Candle 1: Long bearish candle establishing strong downward momentum. Heavy selling pressure with a large real body.",
            "Candle 2: Small bullish candle that opens within or near C1's low and rallies modestly. Short-covering or minor bottom-fishing begins, but remains within C1's range.",
            "Candle 3: Small bullish candle continuing the counter-rally within C1's range. Buyers are unable to push above C1's high, indicating limited bullish conviction.",
            "Candle 4: Small bullish candle, still contained within C1's high-low range. The relief rally is losing steam and buying pressure fades.",
            "Candle 5: Long bearish candle that opens within or near C4's body and closes below C1's low. Selling resumes with force, confirming the downtrend continuation and trapping bottom-fishers from C2-C4."
        ],
        "market_psychology": "C1 demonstrates dominant selling pressure. C2-C4 are a brief pause where short-covering and bargain hunters create a shallow bounce, but it never threatens C1's high, revealing the lack of genuine bullish conviction. C5 shows bears reasserting control, trapping anyone who bought the bounce and accelerating the downtrend.",
        "confirmation_required": "C5 must close below C1's low. A sixth candle continuing lower, especially on increased volume, provides strong additional confirmation.",
        "volume_confirmation": "Volume should be high on C1 and C5, reflecting strong selling conviction. Volume during C2-C4 should noticeably decline, confirming the bounce is merely a low-participation rest. Expanding volume on C5 confirms the resumption of selling.",
        "volatility_conditions": "Works best in established downtrends with moderate to high volatility. The consolidation candles C2-C4 should show reduced range (volatility compression) before C5 expands the range again.",
        "gap_requirement": "None",
        "reliability": "High",
        "success_rate_range": "65-78%",
        "failure_conditions": [
            "C2-C4 break above C1's high (invalidates containment)",
            "C5 fails to close below C1's low",
            "Volume increases during C2-C4 (genuine buying emerging)",
            "Strong bullish divergence on RSI or MACD during C2-C4",
            "Pattern forms near major support level",
            "Broader market sentiment shifting bullish"
        ],
        "entry_rules": "Enter short on C5's close or on break below C5's low. Confirm with volume expansion on C5. Consider a stop-and-reverse if C5 fails and price reclaims C1's high.",
        "stop_loss_rules": "Above the highest high of the entire 5-candle pattern (typically the high of C3 or C4). A tighter stop can be placed above C5's open.",
        "take_profit_rules": "Measure C1's body height and project downward from C5's close for a minimum target. Target next support level or use a trailing stop to ride the continuation move.",
        "risk_reward": "1:3",
        "best_timeframes": [
            "Daily",
            "Weekly",
            "4H"
        ],
        "best_markets": [
            "Stocks",
            "Futures",
            "Commodities",
            "Forex"
        ],
        "best_indicators": [
            "Moving Averages (trend confirmation, price below MA)",
            "Volume (declining C2-C4, expanding C5)",
            "ADX (trending >25 confirms strong trend)",
            "Bollinger Bands (squeeze during C2-C4 consolidation)",
            "MACD (bearish histogram confirmation)"
        ],
        "common_mistakes": [
            "Not verifying C2-C4 are contained within C1's range",
            "Shorting before C5 confirms the pattern",
            "Ignoring the volume signature (must decline then expand)",
            "Confusing with Rising Three Methods",
            "Trading the pattern near strong historical support"
        ],
        "ai_features": [
            "c1.is_bearish AND c1.body_ratio > 0.60",
            "c2.is_bullish AND c3.is_bullish AND c4.is_bullish",
            "all(c.high <= c1.high AND c.low >= c1.low for c in [c2,c3,c4])",
            "c5.is_bearish AND c5.close < c1.low",
            "c5.body_ratio > 0.50"
        ],
        "ohlc_relationship": "C1: bearish, body_ratio > 0.60; C2-C4: small bullish, all contained within C1 H-L range; C5: bearish, C5_close < C1_low, body_ratio > 0.50",
        "label": "Bearish",
        "confidence_score": 77,
        "probability_score": 71
    },
    {
        "id": 74,
        "pattern_name": "Bullish Breakaway",
        "alternative_names": [
            "Breakaway Bullish",
            "Five Candle Bullish Breakaway"
        ],
        "japanese_name": "Hanare Sante No Shinte Zukae",
        "category": "Five Candle",
        "sub_category": "Bullish Reversal",
        "sentiment": "Bullish",
        "expected_direction": "UP",
        "trend_required": "Downtrend",
        "num_candles": 5,
        "pattern_structure": "Long bearish C1, C2 gaps down and is bearish, small C3 bearish or doji, small C4 bearish or bullish, large bullish C5 that closes into the gap between C1 and C2 but does not fully fill it",
        "candle_by_candle": [
            "Candle 1: Long bearish candle in an established downtrend. Strong selling pressure drives price sharply lower, establishing the bearish tone for the pattern.",
            "Candle 2: Bearish candle that gaps down below C1's close, creating a visible window. Continuation of panic selling or bearish momentum that creates the gap.",
            "Candle 3: Small bearish candle or doji. The downward momentum is clearly fading. Bodies are small, showing indecision and exhaustion of selling pressure.",
            "Candle 4: Small candle, can be bearish or bullish. Further deceleration of the downtrend. If bullish, it hints at emerging buying interest. Price stalls near the lows.",
            "Candle 5: Large bullish candle that rallies strongly, closing into the gap area between C1's close and C2's open. Critically, it does NOT fully close the gap — it closes between C2's open and C1's close."
        ],
        "market_psychology": "C1 and the gap into C2 represent climactic selling and bearish capitulation. C3-C4 show the selling exhausting itself as bears run out of ammunition. C5 represents a strong bullish response as value buyers step in. The fact that C5 reclaims much of the gap territory signals that the bearish momentum is broken, but the partial gap fill suggests measured buying rather than a panic short squeeze.",
        "confirmation_required": "C5 must close within the gap between C1's close and C2's open. A sixth bullish candle continuing higher provides additional confirmation. Full gap fill on subsequent candles further validates the reversal.",
        "volume_confirmation": "Volume should be elevated on C1 and C2 (panic selling), decline on C3-C4 (exhaustion), and increase on C5 (new buying interest). High volume on C5 is key.",
        "volatility_conditions": "Typically appears after high-volatility selling. The deceleration on C3-C4 shows volatility compressing before C5 releases it in the opposite direction.",
        "gap_requirement": "Required",
        "reliability": "Medium",
        "success_rate_range": "55-70%",
        "failure_conditions": [
            "C5 fails to close into the gap area",
            "C5 fully closes the gap (different pattern interpretation)",
            "No gap exists between C1 and C2",
            "Volume does not increase on C5",
            "Pattern forms in a sideways market (no prior downtrend)",
            "Strong resistance exists at the gap fill level"
        ],
        "entry_rules": "Enter long on C5's close or on the next candle's open if C5 closes within the gap. Aggressive entry: at C5 mid-point if it's clearly bullish. Wait for sixth candle confirmation for conservative approach.",
        "stop_loss_rules": "Below the lowest low of the pattern (typically C3 or C4 low). Tighter stop below C5's low if risk-reward permits.",
        "take_profit_rules": "First target: full gap fill (C1's close level). Second target: C1's open level. Use measured move of C5's body projected upward for extended targets.",
        "risk_reward": "1:2.5",
        "best_timeframes": [
            "Daily",
            "Weekly"
        ],
        "best_markets": [
            "Stocks",
            "Futures",
            "Indices"
        ],
        "best_indicators": [
            "RSI (oversold <30 condition before C5)",
            "Volume (exhaustion then expansion pattern)",
            "MACD (bullish divergence during C3-C4)",
            "Stochastic (oversold crossover)",
            "Support levels (pattern near key support adds weight)"
        ],
        "common_mistakes": [
            "Ignoring the gap requirement between C1 and C2",
            "Accepting a C5 that fully closes the gap",
            "Trading the pattern without a prior established downtrend",
            "Not checking volume signature for exhaustion and renewal",
            "Confusing with Morning Star or other reversal patterns"
        ],
        "ai_features": [
            "c1.is_bearish AND c1.body_ratio > 0.55",
            "c2.is_bearish AND c2.open < c1.close (gap down)",
            "c3.body_ratio < 0.30 OR c3.is_doji",
            "c4.body_ratio < 0.35",
            "c5.is_bullish AND c5.body_ratio > 0.55",
            "c5.close > c2.open AND c5.close < c1.close"
        ],
        "ohlc_relationship": "C1: bearish, body_ratio > 0.55; C2: bearish, C2_open < C1_close (gap); C3: small bearish/doji; C4: small body; C5: bullish, C5_close > C2_open AND C5_close < C1_close (partial gap fill)",
        "label": "Bullish",
        "confidence_score": 62,
        "probability_score": 60
    },
    {
        "id": 75,
        "pattern_name": "Bearish Breakaway",
        "alternative_names": [
            "Breakaway Bearish",
            "Five Candle Bearish Breakaway"
        ],
        "japanese_name": "Hanare Sante No Shinte Zukae (Bearish)",
        "category": "Five Candle",
        "sub_category": "Bearish Reversal",
        "sentiment": "Bearish",
        "expected_direction": "DOWN",
        "trend_required": "Uptrend",
        "num_candles": 5,
        "pattern_structure": "Long bullish C1, C2 gaps up and is bullish, small C3 bullish or doji, small C4 bullish or bearish, large bearish C5 that closes into the gap between C1 and C2 but does not fully fill it",
        "candle_by_candle": [
            "Candle 1: Long bullish candle in an established uptrend. Strong buying drives price sharply higher, establishing the bullish tone for the pattern.",
            "Candle 2: Bullish candle that gaps up above C1's close, creating a visible window. Exuberant buying or momentum chasing drives the gap higher.",
            "Candle 3: Small bullish candle or doji. Upward momentum is clearly fading. Small bodies reveal indecision and waning buying pressure at these elevated levels.",
            "Candle 4: Small candle, can be bullish or bearish. The uptrend deceleration continues. If bearish, early selling interest emerges. Price stalls near the highs.",
            "Candle 5: Large bearish candle that declines strongly, closing into the gap area between C1's close and C2's open. It does NOT fully close the gap, closing between C2's open and C1's close."
        ],
        "market_psychology": "C1 and the gap into C2 represent euphoric or climactic buying. C3-C4 show the buying exhausting itself as late longs run out of conviction. C5 represents a sharp bearish response as profit-takers and new shorts enter. The partial gap fill signals that bullish momentum is broken, and the market is transitioning from buyers' to sellers' control.",
        "confirmation_required": "C5 must close within the gap between C1's close and C2's open. A sixth bearish candle continuing lower confirms the reversal. Full gap fill on subsequent candles adds conviction.",
        "volume_confirmation": "Volume should be elevated on C1 and C2 (euphoric buying), decline on C3-C4 (exhaustion), and increase sharply on C5 (distribution and new selling). Heavy volume on C5 validates the shift.",
        "volatility_conditions": "Often appears after high-volatility buying phases. C3-C4 compress volatility before C5 expands it in the bearish direction.",
        "gap_requirement": "Required",
        "reliability": "Medium",
        "success_rate_range": "55-68%",
        "failure_conditions": [
            "C5 fails to close into the gap area",
            "C5 fully closes the gap (different pattern dynamics)",
            "No gap exists between C1 and C2",
            "Volume does not increase on C5",
            "Pattern forms in a sideways market (no prior uptrend)",
            "Strong support exists at the gap fill level",
            "Major bullish catalyst overrides technical picture"
        ],
        "entry_rules": "Enter short on C5's close or on the next candle's open if C5 closes within the gap. Conservative approach: wait for sixth candle confirmation below C5's close.",
        "stop_loss_rules": "Above the highest high of the pattern (typically C3 or C4 high). Tighter stop above C5's open if risk-reward allows.",
        "take_profit_rules": "First target: full gap fill (C1's close level). Second target: C1's open level. Use measured move of C5's body projected downward for extended targets.",
        "risk_reward": "1:2.5",
        "best_timeframes": [
            "Daily",
            "Weekly"
        ],
        "best_markets": [
            "Stocks",
            "Futures",
            "Indices"
        ],
        "best_indicators": [
            "RSI (overbought >70 condition before C5)",
            "Volume (euphoria then distribution pattern)",
            "MACD (bearish divergence during C3-C4)",
            "Stochastic (overbought crossover)",
            "Resistance levels (pattern near key resistance adds weight)"
        ],
        "common_mistakes": [
            "Ignoring the gap requirement between C1 and C2",
            "Accepting a C5 that fully closes the gap",
            "Trading the pattern without a prior established uptrend",
            "Not confirming volume shift from buying to selling",
            "Confusing with Evening Star or other top reversal patterns"
        ],
        "ai_features": [
            "c1.is_bullish AND c1.body_ratio > 0.55",
            "c2.is_bullish AND c2.open > c1.close (gap up)",
            "c3.body_ratio < 0.30 OR c3.is_doji",
            "c4.body_ratio < 0.35",
            "c5.is_bearish AND c5.body_ratio > 0.55",
            "c5.close < c2.open AND c5.close > c1.close"
        ],
        "ohlc_relationship": "C1: bullish, body_ratio > 0.55; C2: bullish, C2_open > C1_close (gap); C3: small bullish/doji; C4: small body; C5: bearish, C5_close < C2_open AND C5_close > C1_close (partial gap fill)",
        "label": "Bearish",
        "confidence_score": 60,
        "probability_score": 58
    },
    {
        "id": 76,
        "pattern_name": "Mat Hold",
        "alternative_names": [
            "Mat Hold Pattern",
            "Mat-Hold Bullish"
        ],
        "japanese_name": "Uwazumi",
        "category": "Five Candle",
        "sub_category": "Bullish Continuation",
        "sentiment": "Bullish",
        "expected_direction": "CONTINUATION_UP",
        "trend_required": "Uptrend",
        "num_candles": 5,
        "pattern_structure": "Long bullish C1, C2 gaps up then forms a small bearish candle, C3 small bearish, C4 small bearish or doji, C5 long bullish candle closing above C1's high. Similar to Rising Three Methods but with an initial gap up between C1 and C2.",
        "candle_by_candle": [
            "Candle 1: Long bullish candle in an uptrend. Strong buying conviction creates a large real body, reinforcing the bullish trend.",
            "Candle 2: Small bearish candle that gaps up from C1's close. Despite the gap up, a small bearish body forms — early profit-taking after the gap. The low of C2 stays above C1's midpoint.",
            "Candle 3: Small bearish candle continuing the shallow pullback. The decline is controlled, with C3's low remaining above C1's low. Selling pressure is weak.",
            "Candle 4: Small bearish candle or doji. The pullback is exhausting itself. C4 often makes the lowest low of the consolidation but holds above C1's open or midpoint.",
            "Candle 5: Long bullish candle that opens near C4 and closes above C1's high (and ideally above C2's high). A decisive resumption of the uptrend with strong volume."
        ],
        "market_psychology": "C1 shows dominant buying. The gap up into C2 reflects continued bullish enthusiasm, but the small bearish C2 body shows some profit-taking at higher levels. C3-C4 are a controlled decline — the gap and underlying support hold, indicating that bulls are resting rather than retreating. C5 demonstrates that the pause was just a consolidation, and the trend resumes with conviction, often catching late shorts off guard.",
        "confirmation_required": "C5 must close above C1's high. The gap from C1 to C2 should remain at least partially open during the consolidation. A sixth candle continuing higher confirms the pattern.",
        "volume_confirmation": "High volume on C1 and C5. Volume should contract during C2-C4 consolidation. C5's volume should ideally exceed C1's volume, showing fresh buying commitment.",
        "volatility_conditions": "Best in trending markets with moderate volatility. The gap up distinguishes Mat Hold from Rising Three Methods and suggests stronger underlying momentum.",
        "gap_requirement": "Required",
        "reliability": "High",
        "success_rate_range": "65-80%",
        "failure_conditions": [
            "C2-C4 fill the gap and close below C1's close",
            "C4 closes below C1's midpoint or open",
            "C5 fails to close above C1's high",
            "Volume expands during C2-C4 (serious distribution)",
            "C2 does not gap up from C1",
            "Pattern forms at major resistance zone"
        ],
        "entry_rules": "Enter long on C5's close or on break above C5's high. More aggressive entry at C5's midpoint once bullish intent is clear. Ensure C2-C4 held above C1's lower half.",
        "stop_loss_rules": "Below the lowest low of C2-C4 consolidation phase. Alternatively, below C1's midpoint for a wider stop.",
        "take_profit_rules": "Project C1's body range from C5's close. Target next resistance level. Trail stop below each subsequent candle's low. Consider 1.5x to 2x the pattern height.",
        "risk_reward": "1:3.5",
        "best_timeframes": [
            "Daily",
            "Weekly",
            "4H"
        ],
        "best_markets": [
            "Stocks",
            "Futures",
            "Forex",
            "Commodities"
        ],
        "best_indicators": [
            "Moving Averages (price above 20 and 50 MA)",
            "Volume (contraction-expansion signature)",
            "ADX (>25 confirming trend strength)",
            "Bollinger Bands (price riding upper band)",
            "RSI (staying above 50 during consolidation)"
        ],
        "common_mistakes": [
            "Confusing with Rising Three Methods (Mat Hold requires gap)",
            "Ignoring the gap requirement between C1 and C2",
            "Not ensuring C2-C4 hold above C1's lower half",
            "Entering before C5 confirms with a strong close",
            "Overlooking volume pattern during consolidation"
        ],
        "ai_features": [
            "c1.is_bullish AND c1.body_ratio > 0.55",
            "c2.open > c1.close (gap up) AND c2.is_bearish AND c2.body_ratio < 0.40",
            "c3.is_bearish AND c3.body_ratio < 0.35",
            "c4.body_ratio < 0.30 AND c4.low > c1.open",
            "c5.is_bullish AND c5.close > c1.high AND c5.body_ratio > 0.50"
        ],
        "ohlc_relationship": "C1: bullish, body_ratio > 0.55; C2: gap up (C2_open > C1_close), small bearish; C3: small bearish, C3_low > C1_low; C4: small bearish/doji, C4_low > C1_open; C5: bullish, C5_close > C1_high, body_ratio > 0.50",
        "label": "Bullish",
        "confidence_score": 80,
        "probability_score": 74
    },
    {
        "id": 77,
        "pattern_name": "Bullish Three Line Strike",
        "alternative_names": [
            "Three Line Strike Bullish",
            "Bullish Strike",
            "Sanpei Uchi Kaeshi (Bullish)"
        ],
        "japanese_name": "Sanpei Uchi Kaeshi",
        "category": "Four Candle",
        "sub_category": "Bullish Reversal",
        "sentiment": "Bullish",
        "expected_direction": "UP",
        "trend_required": "Downtrend",
        "num_candles": 4,
        "pattern_structure": "Three consecutive bearish candles (like Three Black Crows), each closing lower than the previous, then C4 is a large bullish candle that opens below C3's close and closes above C1's open, engulfing all three bearish candles.",
        "candle_by_candle": [
            "Candle 1: Long bearish candle in a downtrend. Sellers control price action with a substantial close below the open. Each candle opens within the previous candle's body.",
            "Candle 2: Long bearish candle that opens within or near C1's body and closes below C1's low. Sustained selling pressure pushes price further down.",
            "Candle 3: Long bearish candle that opens within or near C2's body and closes below C2's low. The three consecutive bearish candles resemble Three Black Crows.",
            "Candle 4: Large bullish candle that opens at or below C3's close and rallies sharply, closing above C1's open. This single candle engulfs the entire range of the prior three bearish candles, representing a dramatic reversal."
        ],
        "market_psychology": "C1-C3 represent a controlled sell-off that lures more shorts and creates a sense of inevitable decline. C4 is a dramatic reversal — a massive bullish candle that traps all the shorts from C1-C3 period and forces aggressive short-covering. The psychology shifts from bearish dominance to panic covering. The pattern works because the extended three-candle decline creates a climactic exhaustion point.",
        "confirmation_required": "C4 must close above C1's open to fully engulf all three bearish candles. A fifth bullish candle with a higher close provides important confirmation, as the pattern has a notable failure rate without it.",
        "volume_confirmation": "Volume should be moderate during C1-C3 and spike significantly on C4. The volume surge on C4 reflects short-covering and new buying. Low volume on C4 is a warning sign.",
        "volatility_conditions": "Can appear in various volatility conditions. Most reliable when forming after a sharp decline with expanding volatility. C4's range should be notably larger than any individual candle in C1-C3.",
        "gap_requirement": "None",
        "reliability": "Medium",
        "success_rate_range": "60-72%",
        "failure_conditions": [
            "C4 does not close above C1's open (incomplete engulfing)",
            "Volume on C4 is weak",
            "C1-C3 are not progressively lower (not stair-stepped)",
            "Pattern forms in a sideways range (no prior downtrend)",
            "Fifth candle reverses lower (bull trap)",
            "C4 has excessive upper shadow (rejection at highs)"
        ],
        "entry_rules": "Enter long on C4's close or on break above C4's high. Conservative: wait for fifth candle to confirm direction. Set alert if C4 forms intraday and shows engulfing potential.",
        "stop_loss_rules": "Below C3's low (the lowest point of the pattern) or below C4's low if C4 opened below C3's close.",
        "take_profit_rules": "Measure the total height of C1-C3 decline and project upward from C4's close. Or target the pre-decline swing high. Use trailing stop as momentum may extend the rally.",
        "risk_reward": "1:2",
        "best_timeframes": [
            "Daily",
            "4H",
            "1H"
        ],
        "best_markets": [
            "Stocks",
            "Futures",
            "Forex",
            "Indices"
        ],
        "best_indicators": [
            "RSI (oversold before C4, divergence on C3)",
            "Volume (spike on C4)",
            "MACD (bullish crossover near C4)",
            "Moving Averages (proximity to major MA support)",
            "Fibonacci retracement (C3 low near key level)"
        ],
        "common_mistakes": [
            "Not requiring full engulfment of all three bearish candles",
            "Ignoring that C4 must close above C1's open",
            "Treating C1-C3 as just any three bearish candles (they should be stair-stepped)",
            "Not waiting for fifth candle confirmation",
            "Confusing with bearish continuation if context is ignored"
        ],
        "ai_features": [
            "c1.is_bearish AND c1.body_ratio > 0.50",
            "c2.is_bearish AND c2.close < c1.close",
            "c3.is_bearish AND c3.close < c2.close",
            "c4.is_bullish AND c4.open <= c3.close AND c4.close >= c1.open",
            "c4.body_size > (c1.body_size + c2.body_size + c3.body_size) * 0.8"
        ],
        "ohlc_relationship": "C1: bearish; C2: bearish, C2_close < C1_close; C3: bearish, C3_close < C2_close; C4: bullish, C4_open <= C3_close, C4_close >= C1_open (engulfs all three)",
        "label": "Bullish",
        "confidence_score": 65,
        "probability_score": 63
    },
    {
        "id": 78,
        "pattern_name": "Bearish Three Line Strike",
        "alternative_names": [
            "Three Line Strike Bearish",
            "Bearish Strike",
            "Sanpei Uchi Kaeshi (Bearish)"
        ],
        "japanese_name": "Sanpei Uchi Kaeshi (Bearish)",
        "category": "Four Candle",
        "sub_category": "Bearish Reversal",
        "sentiment": "Bearish",
        "expected_direction": "DOWN",
        "trend_required": "Uptrend",
        "num_candles": 4,
        "pattern_structure": "Three consecutive bullish candles (like Three White Soldiers), each closing higher than the previous, then C4 is a large bearish candle that opens above C3's close and closes below C1's open, engulfing all three bullish candles.",
        "candle_by_candle": [
            "Candle 1: Long bullish candle in an uptrend. Buyers control price with a substantial close above the open. Establishes the first step of the ascending sequence.",
            "Candle 2: Long bullish candle that opens within or near C1's body and closes above C1's high. Sustained buying pushes price higher in a stair-step fashion.",
            "Candle 3: Long bullish candle that opens within or near C2's body and closes above C2's high. Three consecutive bullish candles resemble Three White Soldiers, creating maximum bullish complacency.",
            "Candle 4: Large bearish candle that opens at or above C3's close and sells off sharply, closing below C1's open. This single candle engulfs the entire range of the prior three bullish candles — a dramatic reversal."
        ],
        "market_psychology": "C1-C3 represent a persistent rally that creates bullish complacency and draws in late buyers. C4 is a shock reversal — a massive bearish candle that wipes out three sessions of gains in a single candle. This traps all the longs from C1-C3, triggers margin calls and stop-losses, and shifts the market's psychological state from greed to fear.",
        "confirmation_required": "C4 must close below C1's open to fully engulf all three bullish candles. A fifth bearish candle confirms the reversal. Without confirmation, the pattern may be a one-day shakeout rather than a genuine top.",
        "volume_confirmation": "Volume should be moderate during C1-C3 and spike dramatically on C4. High C4 volume confirms institutional distribution and panic selling. Weak C4 volume suggests a possible false reversal.",
        "volatility_conditions": "Most reliable after a steady rally with gradually declining volatility, where C4 represents a volatility expansion in the bearish direction. Works in various volatility environments.",
        "gap_requirement": "None",
        "reliability": "Medium",
        "success_rate_range": "58-70%",
        "failure_conditions": [
            "C4 does not close below C1's open (incomplete engulfing)",
            "Volume on C4 is low",
            "C1-C3 are not progressively higher (not stair-stepped)",
            "Pattern forms in a sideways range (no prior uptrend)",
            "Fifth candle reverses higher (bear trap)",
            "C4 has excessive lower shadow (buying at lows)",
            "Strong bullish fundamental catalyst overrides the signal"
        ],
        "entry_rules": "Enter short on C4's close or on break below C4's low. Conservative: wait for fifth candle to confirm the reversal. Set initial position size smaller given moderate reliability.",
        "stop_loss_rules": "Above C3's high (the highest point of the pattern) or above C4's high if C4 opened above C3's close.",
        "take_profit_rules": "Measure the total height of C1-C3 advance and project downward from C4's close. Target the pre-rally swing low. Use trailing stop as selling may intensify.",
        "risk_reward": "1:2",
        "best_timeframes": [
            "Daily",
            "4H",
            "1H"
        ],
        "best_markets": [
            "Stocks",
            "Futures",
            "Forex",
            "Indices"
        ],
        "best_indicators": [
            "RSI (overbought before C4, divergence on C3)",
            "Volume (spike on C4)",
            "MACD (bearish crossover near C4)",
            "Moving Averages (proximity to major MA resistance)",
            "Fibonacci extension (C3 high near key level)"
        ],
        "common_mistakes": [
            "Not requiring full engulfment of all three bullish candles",
            "Ignoring that C4 must close below C1's open",
            "Treating C1-C3 as any three bullish candles (they should be stair-stepped)",
            "Not waiting for fifth candle confirmation",
            "Confusing with bullish continuation in a strong uptrend"
        ],
        "ai_features": [
            "c1.is_bullish AND c1.body_ratio > 0.50",
            "c2.is_bullish AND c2.close > c1.close",
            "c3.is_bullish AND c3.close > c2.close",
            "c4.is_bearish AND c4.open >= c3.close AND c4.close <= c1.open",
            "c4.body_size > (c1.body_size + c2.body_size + c3.body_size) * 0.8"
        ],
        "ohlc_relationship": "C1: bullish; C2: bullish, C2_close > C1_close; C3: bullish, C3_close > C2_close; C4: bearish, C4_open >= C3_close, C4_close <= C1_open (engulfs all three)",
        "label": "Bearish",
        "confidence_score": 63,
        "probability_score": 61
    },
    {
        "id": 79,
        "pattern_name": "Ladder Bottom",
        "alternative_names": [
            "Ladder Bottom Reversal",
            "Bullish Ladder Bottom"
        ],
        "japanese_name": "Hashigo Gaeshi",
        "category": "Five Candle",
        "sub_category": "Bullish Reversal",
        "sentiment": "Bullish",
        "expected_direction": "UP",
        "trend_required": "Downtrend",
        "num_candles": 5,
        "pattern_structure": "Three long bearish candles descending stair-step fashion (C1-C3), C4 is bearish with a prominent upper shadow showing hesitation, C5 is bullish and opens above C4's body, gapping up.",
        "candle_by_candle": [
            "Candle 1: Long bearish candle in a downtrend. Opens near the high and closes near the low, establishing the descending ladder. Strong, committed selling.",
            "Candle 2: Long bearish candle that opens within C1's body and closes below C1's low. Another step down in the descending ladder. Sellers remain in firm control.",
            "Candle 3: Long bearish candle that opens within C2's body and closes below C2's low. The third descending step. The sequence resembles Three Black Crows.",
            "Candle 4: Bearish candle with a notably long upper shadow (wick). While it still closes lower, the long upper shadow reveals that buyers attempted to push prices higher during the session — the first sign of buying interest. This is the key hesitation candle.",
            "Candle 5: Bullish candle that opens above C4's real body, gapping up. It closes well above C4's close, confirming the reversal. The gap up signals that overnight sentiment has shifted from bearish to bullish."
        ],
        "market_psychology": "C1-C3 represent relentless, stair-step selling that creates deep bearish sentiment. C4's long upper shadow is the critical clue — within the session, buyers tried to push higher, even though the close was still bearish. This intra-session rejection of lower prices signals that the selling is exhausting. C5's gap up confirms the transition as overnight positioning shifts bullish and trapped shorts begin covering.",
        "confirmation_required": "C5 must gap up and close bullish above C4's body. A sixth candle closing higher provides strong confirmation. Volume should increase on C5.",
        "volume_confirmation": "Volume should be moderate to declining during C1-C3 descent. C4 may show mixed volume as buying attempts emerge. C5 should have increased volume confirming the bullish shift. A volume climax on C3 or C4 adds to the pattern's significance.",
        "volatility_conditions": "Works best when the downtrend shows signs of volatility expansion on C4 (long shadow). C5's gap is most meaningful in markets that normally exhibit gaps (stocks, futures).",
        "gap_requirement": "Preferred",
        "reliability": "Medium",
        "success_rate_range": "58-72%",
        "failure_conditions": [
            "C4 lacks a significant upper shadow (no hesitation signal)",
            "C5 does not gap up or open above C4's body",
            "C5 closes with a bearish body (reversal fails)",
            "Volume continues to decline on C5",
            "C1-C3 are not progressively lower",
            "Pattern forms in a sideways range, not a downtrend",
            "Major bearish news invalidates the technical setup"
        ],
        "entry_rules": "Enter long on C5's close or on break above C5's high. Conservative: wait for sixth candle confirmation above C5's close. Ensure C4 has a genuine upper shadow (at least 40% of candle range).",
        "stop_loss_rules": "Below C4's low or C3's low for a wider stop. The lowest point of the pattern represents the invalidation level.",
        "take_profit_rules": "Measure the total decline from C1's open to C3's close and project 50-100% of that distance upward from C5's close. Target C1's open area or prior swing high.",
        "risk_reward": "1:2.5",
        "best_timeframes": [
            "Daily",
            "Weekly"
        ],
        "best_markets": [
            "Stocks",
            "Futures",
            "Indices",
            "Commodities"
        ],
        "best_indicators": [
            "RSI (oversold divergence on C4-C5)",
            "Volume (climax and shift pattern)",
            "MACD (bullish histogram divergence)",
            "Stochastic (oversold crossover)",
            "Support levels (C3-C4 low near key support)"
        ],
        "common_mistakes": [
            "Ignoring C4's upper shadow requirement (critical element)",
            "Not requiring C5 to gap up above C4's body",
            "Confusing with simple Three Black Crows",
            "Trading before C5 confirms the reversal",
            "Not verifying C1-C3 are progressively lower",
            "Trading in markets that rarely gap (C5 gap less meaningful)"
        ],
        "ai_features": [
            "c1.is_bearish AND c1.body_ratio > 0.55",
            "c2.is_bearish AND c2.close < c1.close AND c2.body_ratio > 0.50",
            "c3.is_bearish AND c3.close < c2.close AND c3.body_ratio > 0.50",
            "c4.is_bearish AND c4.upper_shadow_ratio > 0.40",
            "c5.is_bullish AND c5.open > c4.close AND c5.close > c4.open"
        ],
        "ohlc_relationship": "C1: bearish, body_ratio > 0.55; C2: bearish, C2_close < C1_close; C3: bearish, C3_close < C2_close; C4: bearish, upper_shadow_ratio > 0.40; C5: bullish, C5_open > max(C4_open, C4_close), gap up",
        "label": "Bullish",
        "confidence_score": 63,
        "probability_score": 62
    },
    {
        "id": 80,
        "pattern_name": "Ladder Top",
        "alternative_names": [
            "Ladder Top Reversal",
            "Bearish Ladder Top"
        ],
        "japanese_name": "Hashigo Tenjo",
        "category": "Five Candle",
        "sub_category": "Bearish Reversal",
        "sentiment": "Bearish",
        "expected_direction": "DOWN",
        "trend_required": "Uptrend",
        "num_candles": 5,
        "pattern_structure": "Three long bullish candles ascending stair-step fashion (C1-C3), C4 is bullish with a prominent lower shadow showing hesitation, C5 is bearish and opens below C4's body, gapping down.",
        "candle_by_candle": [
            "Candle 1: Long bullish candle in an uptrend. Opens near the low and closes near the high, establishing the first rung of the ascending ladder. Strong, committed buying.",
            "Candle 2: Long bullish candle that opens within C1's body and closes above C1's high. Another step up in the ascending ladder. Buyers remain in firm control.",
            "Candle 3: Long bullish candle that opens within C2's body and closes above C2's high. The third ascending step. The sequence resembles Three White Soldiers.",
            "Candle 4: Bullish candle with a notably long lower shadow (wick). While it still closes higher, the long lower shadow reveals that sellers pushed prices down significantly during the session before buyers recovered — the first sign of selling pressure. This is the key hesitation candle.",
            "Candle 5: Bearish candle that opens below C4's real body, gapping down. It closes well below C4's close, confirming the reversal. The gap down signals that overnight sentiment has shifted from bullish to bearish."
        ],
        "market_psychology": "C1-C3 represent persistent, stair-step buying that builds bullish confidence and complacency. C4's long lower shadow is the critical warning — within the session, sellers made a meaningful push lower, even though the close recovered. This intra-session test of lower prices signals that the rally is becoming fragile. C5's gap down confirms the transition as overnight positioning shifts bearish and trapped longs begin liquidating.",
        "confirmation_required": "C5 must gap down and close bearish below C4's body. A sixth candle closing lower provides strong confirmation. Volume should increase on C5.",
        "volume_confirmation": "Volume should be moderate to declining during C1-C3 advance. C4 may show mixed volume as selling attempts emerge. C5 should have increased volume confirming the bearish shift. A volume climax on C4 or C5 strengthens the signal.",
        "volatility_conditions": "Works best when the uptrend shows signs of volatility expansion on C4 (long lower shadow). C5's gap down is most meaningful in markets that normally exhibit gaps (stocks, futures).",
        "gap_requirement": "Preferred",
        "reliability": "Medium",
        "success_rate_range": "57-70%",
        "failure_conditions": [
            "C4 lacks a significant lower shadow (no hesitation signal)",
            "C5 does not gap down or open below C4's body",
            "C5 closes with a bullish body (reversal fails)",
            "Volume continues to decline on C5",
            "C1-C3 are not progressively higher",
            "Pattern forms in a sideways range, not an uptrend",
            "Major bullish catalyst invalidates the technical setup"
        ],
        "entry_rules": "Enter short on C5's close or on break below C5's low. Conservative: wait for sixth candle confirmation below C5's close. Ensure C4 has a genuine lower shadow (at least 40% of candle range).",
        "stop_loss_rules": "Above C4's high or C3's high for a wider stop. The highest point of the pattern represents the invalidation level.",
        "take_profit_rules": "Measure the total advance from C1's open to C3's close and project 50-100% of that distance downward from C5's close. Target C1's open area or prior swing low.",
        "risk_reward": "1:2.5",
        "best_timeframes": [
            "Daily",
            "Weekly"
        ],
        "best_markets": [
            "Stocks",
            "Futures",
            "Indices",
            "Commodities"
        ],
        "best_indicators": [
            "RSI (overbought divergence on C4-C5)",
            "Volume (climax and shift pattern)",
            "MACD (bearish histogram divergence)",
            "Stochastic (overbought crossover)",
            "Resistance levels (C3-C4 high near key resistance)"
        ],
        "common_mistakes": [
            "Ignoring C4's lower shadow requirement (critical element)",
            "Not requiring C5 to gap down below C4's body",
            "Confusing with simple Three White Soldiers",
            "Trading before C5 confirms the reversal",
            "Not verifying C1-C3 are progressively higher",
            "Trading in markets that rarely gap (C5 gap less meaningful)"
        ],
        "ai_features": [
            "c1.is_bullish AND c1.body_ratio > 0.55",
            "c2.is_bullish AND c2.close > c1.close AND c2.body_ratio > 0.50",
            "c3.is_bullish AND c3.close > c2.close AND c3.body_ratio > 0.50",
            "c4.is_bullish AND c4.lower_shadow_ratio > 0.40",
            "c5.is_bearish AND c5.open < c4.close AND c5.close < c4.open"
        ],
        "ohlc_relationship": "C1: bullish, body_ratio > 0.55; C2: bullish, C2_close > C1_close; C3: bullish, C3_close > C2_close; C4: bullish, lower_shadow_ratio > 0.40; C5: bearish, C5_open < min(C4_open, C4_close), gap down",
        "label": "Bearish",
        "confidence_score": 61,
        "probability_score": 60
    }
]
