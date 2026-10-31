"""
Two Candle Japanese Candlestick Patterns — Complete Database
============================================================
27 patterns with full 33-field schema for AI/ML training.
"""

PATTERNS = [
    # ──────────────────────────────────────────────────────────
    # 1. Bullish Engulfing
    # ──────────────────────────────────────────────────────────
    {
        "id": 0,
        "pattern_name": "Bullish Engulfing",
        "alternative_names": ["Bull Engulf", "Engulfing Bull Line"],
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
        "best_timeframes": ["Daily", "4H", "Weekly"],
        "best_markets": ["Stocks", "Forex", "Crypto", "Futures", "Commodities"],
        "best_indicators": ["RSI (oversold <30)", "MACD (bullish crossover)", "Volume", "Support levels", "Bollinger Bands (lower band touch)"],
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

    # ──────────────────────────────────────────────────────────
    # 2. Bearish Engulfing
    # ──────────────────────────────────────────────────────────
    {
        "id": 0,
        "pattern_name": "Bearish Engulfing",
        "alternative_names": ["Bear Engulf", "Engulfing Bear Line"],
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
        "best_timeframes": ["Daily", "4H", "Weekly"],
        "best_markets": ["Stocks", "Forex", "Crypto", "Futures", "Commodities"],
        "best_indicators": ["RSI (overbought >70)", "MACD (bearish crossover)", "Volume", "Resistance levels", "Bollinger Bands (upper band touch)"],
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

    # ──────────────────────────────────────────────────────────
    # 3. Bullish Harami
    # ──────────────────────────────────────────────────────────
    {
        "id": 0,
        "pattern_name": "Bullish Harami",
        "alternative_names": ["Bull Harami", "Inside Bar Bullish"],
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
        "best_timeframes": ["Daily", "4H", "1H"],
        "best_markets": ["Stocks", "Forex", "Crypto", "Futures"],
        "best_indicators": ["RSI (oversold)", "Stochastic (bullish crossover)", "Volume", "Support levels", "Moving Averages"],
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

    # ──────────────────────────────────────────────────────────
    # 4. Bearish Harami
    # ──────────────────────────────────────────────────────────
    {
        "id": 0,
        "pattern_name": "Bearish Harami",
        "alternative_names": ["Bear Harami", "Inside Bar Bearish"],
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
        "best_timeframes": ["Daily", "4H", "1H"],
        "best_markets": ["Stocks", "Forex", "Crypto", "Futures"],
        "best_indicators": ["RSI (overbought)", "Stochastic (bearish crossover)", "Volume", "Resistance levels"],
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

    # ──────────────────────────────────────────────────────────
    # 5. Bullish Harami Cross
    # ──────────────────────────────────────────────────────────
    {
        "id": 0,
        "pattern_name": "Bullish Harami Cross",
        "alternative_names": ["Harami Cross Bull", "Inside Doji Bullish"],
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
        "best_timeframes": ["Daily", "4H", "Weekly"],
        "best_markets": ["Stocks", "Forex", "Crypto", "Futures"],
        "best_indicators": ["RSI (oversold)", "MACD (divergence)", "Volume", "Support levels"],
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

    # ──────────────────────────────────────────────────────────
    # 6. Bearish Harami Cross
    # ──────────────────────────────────────────────────────────
    {
        "id": 0,
        "pattern_name": "Bearish Harami Cross",
        "alternative_names": ["Harami Cross Bear", "Inside Doji Bearish"],
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
        "best_timeframes": ["Daily", "4H", "Weekly"],
        "best_markets": ["Stocks", "Forex", "Crypto", "Futures"],
        "best_indicators": ["RSI (overbought)", "MACD (bearish divergence)", "Volume", "Resistance levels"],
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

    # ──────────────────────────────────────────────────────────
    # 7. Piercing Pattern
    # ──────────────────────────────────────────────────────────
    {
        "id": 0,
        "pattern_name": "Piercing Pattern",
        "alternative_names": ["Piercing Line", "Kirikomi"],
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
        "best_timeframes": ["Daily", "4H", "Weekly"],
        "best_markets": ["Stocks", "Futures", "Crypto", "Commodities"],
        "best_indicators": ["RSI (oversold)", "MACD (bullish divergence)", "Volume", "Support zones"],
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

    # ──────────────────────────────────────────────────────────
    # 8. Dark Cloud Cover
    # ──────────────────────────────────────────────────────────
    {
        "id": 0,
        "pattern_name": "Dark Cloud Cover",
        "alternative_names": ["Dark Cloud", "Kabuse"],
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
        "best_timeframes": ["Daily", "4H", "Weekly"],
        "best_markets": ["Stocks", "Futures", "Crypto", "Commodities"],
        "best_indicators": ["RSI (overbought)", "MACD (bearish divergence)", "Volume", "Resistance zones"],
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

    # ──────────────────────────────────────────────────────────
    # 9. Tweezer Top
    # ──────────────────────────────────────────────────────────
    {
        "id": 0,
        "pattern_name": "Tweezer Top",
        "alternative_names": ["Tweezer Tops", "Kenuki Top"],
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
        "best_timeframes": ["Daily", "4H", "1H"],
        "best_markets": ["Stocks", "Forex", "Crypto", "Futures"],
        "best_indicators": ["RSI (overbought)", "Volume at highs", "Resistance levels", "Moving Averages"],
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

    # ──────────────────────────────────────────────────────────
    # 10. Tweezer Bottom
    # ──────────────────────────────────────────────────────────
    {
        "id": 0,
        "pattern_name": "Tweezer Bottom",
        "alternative_names": ["Tweezer Bottoms", "Kenuki Bottom"],
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
        "best_timeframes": ["Daily", "4H", "1H"],
        "best_markets": ["Stocks", "Forex", "Crypto", "Futures"],
        "best_indicators": ["RSI (oversold)", "Volume at lows", "Support levels", "Moving Averages"],
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

    # ──────────────────────────────────────────────────────────
    # 11. Matching High
    # ──────────────────────────────────────────────────────────
    {
        "id": 0,
        "pattern_name": "Matching High",
        "alternative_names": ["Double Top Candle"],
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
        "best_timeframes": ["Daily", "Weekly"],
        "best_markets": ["Stocks", "Futures"],
        "best_indicators": ["RSI (overbought)", "Volume (declining)", "Resistance levels"],
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

    # ──────────────────────────────────────────────────────────
    # 12. Matching Low
    # ──────────────────────────────────────────────────────────
    {
        "id": 0,
        "pattern_name": "Matching Low",
        "alternative_names": ["Double Bottom Candle"],
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
        "best_timeframes": ["Daily", "Weekly"],
        "best_markets": ["Stocks", "Futures"],
        "best_indicators": ["RSI (oversold)", "Volume (declining)", "Support levels"],
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

    # ──────────────────────────────────────────────────────────
    # 13. Homing Pigeon
    # ──────────────────────────────────────────────────────────
    {
        "id": 0,
        "pattern_name": "Homing Pigeon",
        "alternative_names": ["Bearish Harami Variant"],
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
        "best_timeframes": ["Daily", "4H"],
        "best_markets": ["Stocks", "Futures"],
        "best_indicators": ["RSI (oversold)", "Volume", "Support levels"],
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

    # ──────────────────────────────────────────────────────────
    # 14. Bullish Meeting Lines
    # ──────────────────────────────────────────────────────────
    {
        "id": 0,
        "pattern_name": "Bullish Meeting Lines",
        "alternative_names": ["Bullish Counterattack Lines (sometimes confused)", "Deai Sen Bullish"],
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
        "best_timeframes": ["Daily", "Weekly"],
        "best_markets": ["Stocks", "Futures"],
        "best_indicators": ["RSI (oversold)", "Volume", "Support levels"],
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

    # ──────────────────────────────────────────────────────────
    # 15. Bearish Meeting Lines
    # ──────────────────────────────────────────────────────────
    {
        "id": 0,
        "pattern_name": "Bearish Meeting Lines",
        "alternative_names": ["Deai Sen Bearish"],
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
        "best_timeframes": ["Daily", "Weekly"],
        "best_markets": ["Stocks", "Futures"],
        "best_indicators": ["RSI (overbought)", "Volume", "Resistance levels"],
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

    # ──────────────────────────────────────────────────────────
    # 16. Bullish Separating Lines
    # ──────────────────────────────────────────────────────────
    {
        "id": 0,
        "pattern_name": "Bullish Separating Lines",
        "alternative_names": ["Iki Chigai Sen Bullish"],
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
        "best_timeframes": ["Daily", "4H"],
        "best_markets": ["Stocks", "Forex", "Futures"],
        "best_indicators": ["Moving Averages (trend)", "ADX (>25)", "Volume"],
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

    # ──────────────────────────────────────────────────────────
    # 17. Bearish Separating Lines
    # ──────────────────────────────────────────────────────────
    {
        "id": 0,
        "pattern_name": "Bearish Separating Lines",
        "alternative_names": ["Iki Chigai Sen Bearish"],
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
        "best_timeframes": ["Daily", "4H"],
        "best_markets": ["Stocks", "Forex", "Futures"],
        "best_indicators": ["Moving Averages (trend)", "ADX (>25)", "Volume"],
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

    # ──────────────────────────────────────────────────────────
    # 18. Bullish Counterattack
    # ──────────────────────────────────────────────────────────
    {
        "id": 0,
        "pattern_name": "Bullish Counterattack",
        "alternative_names": ["Bullish Counterattack Lines"],
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
        "best_timeframes": ["Daily", "Weekly"],
        "best_markets": ["Stocks", "Futures", "Commodities"],
        "best_indicators": ["RSI (oversold)", "Volume", "Support levels"],
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

    # ──────────────────────────────────────────────────────────
    # 19. Bearish Counterattack
    # ──────────────────────────────────────────────────────────
    {
        "id": 0,
        "pattern_name": "Bearish Counterattack",
        "alternative_names": ["Bearish Counterattack Lines"],
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
        "best_timeframes": ["Daily", "Weekly"],
        "best_markets": ["Stocks", "Futures", "Commodities"],
        "best_indicators": ["RSI (overbought)", "Volume", "Resistance levels"],
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

    # ──────────────────────────────────────────────────────────
    # 20. Bullish Kicking
    # ──────────────────────────────────────────────────────────
    {
        "id": 0,
        "pattern_name": "Bullish Kicking",
        "alternative_names": ["Kicking Bullish", "Keri Ashi Bullish"],
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
        "best_timeframes": ["Daily", "Weekly", "4H"],
        "best_markets": ["Stocks", "Futures", "Commodities", "Crypto"],
        "best_indicators": ["Volume", "Gap analysis", "ADX", "Momentum indicators"],
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

    # ──────────────────────────────────────────────────────────
    # 21. Bearish Kicking
    # ──────────────────────────────────────────────────────────
    {
        "id": 0,
        "pattern_name": "Bearish Kicking",
        "alternative_names": ["Kicking Bearish", "Keri Ashi Bearish"],
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
        "best_timeframes": ["Daily", "Weekly", "4H"],
        "best_markets": ["Stocks", "Futures", "Commodities", "Crypto"],
        "best_indicators": ["Volume", "Gap analysis", "ADX", "Momentum"],
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

    # ──────────────────────────────────────────────────────────
    # 22. On Neck Line
    # ──────────────────────────────────────────────────────────
    {
        "id": 0,
        "pattern_name": "On Neck Line",
        "alternative_names": ["On Neck", "Ate Kubi"],
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
        "best_timeframes": ["Daily", "4H"],
        "best_markets": ["Stocks", "Forex", "Futures"],
        "best_indicators": ["Moving Averages (downtrend)", "ADX", "Volume"],
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

    # ──────────────────────────────────────────────────────────
    # 23. In Neck Line
    # ──────────────────────────────────────────────────────────
    {
        "id": 0,
        "pattern_name": "In Neck Line",
        "alternative_names": ["In Neck", "Iri Kubi"],
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
        "best_timeframes": ["Daily", "4H"],
        "best_markets": ["Stocks", "Forex", "Futures"],
        "best_indicators": ["Moving Averages", "ADX", "Volume"],
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

    # ──────────────────────────────────────────────────────────
    # 24. Thrusting Pattern
    # ──────────────────────────────────────────────────────────
    {
        "id": 0,
        "pattern_name": "Thrusting Pattern",
        "alternative_names": ["Thrusting Line", "Sashikomi"],
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
        "best_timeframes": ["Daily", "4H"],
        "best_markets": ["Stocks", "Forex", "Futures"],
        "best_indicators": ["Moving Averages", "ADX", "Volume"],
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

    # ──────────────────────────────────────────────────────────
    # 25. Two Crows
    # ──────────────────────────────────────────────────────────
    {
        "id": 0,
        "pattern_name": "Two Crows",
        "alternative_names": ["Upside Gap Two Crows Simplified"],
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
        "best_timeframes": ["Daily", "Weekly"],
        "best_markets": ["Stocks", "Futures"],
        "best_indicators": ["RSI (overbought)", "Volume", "Resistance levels"],
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

    # ──────────────────────────────────────────────────────────
    # 26. Rising Window
    # ──────────────────────────────────────────────────────────
    {
        "id": 0,
        "pattern_name": "Rising Window",
        "alternative_names": ["Gap Up", "Window Rising", "Bullish Window"],
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
        "best_timeframes": ["Daily", "Weekly", "4H"],
        "best_markets": ["Stocks", "Futures", "Crypto"],
        "best_indicators": ["Volume", "Moving Averages (trend)", "Support at gap level"],
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

    # ──────────────────────────────────────────────────────────
    # 27. Falling Window
    # ──────────────────────────────────────────────────────────
    {
        "id": 0,
        "pattern_name": "Falling Window",
        "alternative_names": ["Gap Down", "Window Falling", "Bearish Window"],
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
        "best_timeframes": ["Daily", "Weekly", "4H"],
        "best_markets": ["Stocks", "Futures", "Crypto"],
        "best_indicators": ["Volume", "Moving Averages (trend)", "Resistance at gap level"],
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
]
