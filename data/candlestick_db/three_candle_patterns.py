"""
Three Candle Japanese Candlestick Patterns — Complete Database
==============================================================
28 patterns with full 33-field schema for AI/ML training.
"""

PATTERNS = [
    # ──────────────────────────────────────────────────────────
    # 1. Morning Star
    # ──────────────────────────────────────────────────────────
    {
        "id": 0,
        "pattern_name": "Morning Star",
        "alternative_names": ["Morning Star Pattern"],
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
        "best_timeframes": ["Daily", "Weekly", "4H"],
        "best_markets": ["Stocks", "Futures", "Crypto", "Forex", "Commodities"],
        "best_indicators": ["RSI (oversold <30)", "MACD (bullish divergence)", "Volume", "Support levels", "Stochastic (oversold crossover)"],
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

    # ──────────────────────────────────────────────────────────
    # 2. Evening Star
    # ──────────────────────────────────────────────────────────
    {
        "id": 0,
        "pattern_name": "Evening Star",
        "alternative_names": ["Evening Star Pattern"],
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
        "best_timeframes": ["Daily", "Weekly", "4H"],
        "best_markets": ["Stocks", "Futures", "Crypto", "Forex", "Commodities"],
        "best_indicators": ["RSI (overbought >70)", "MACD (bearish divergence)", "Volume", "Resistance levels"],
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

    # ──────────────────────────────────────────────────────────
    # 3. Morning Doji Star
    # ──────────────────────────────────────────────────────────
    {
        "id": 0,
        "pattern_name": "Morning Doji Star",
        "alternative_names": ["Doji Morning Star"],
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
        "best_timeframes": ["Daily", "Weekly", "4H"],
        "best_markets": ["Stocks", "Futures", "Crypto", "Commodities"],
        "best_indicators": ["RSI (oversold)", "MACD (bullish divergence)", "Volume", "Support levels"],
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

    # ──────────────────────────────────────────────────────────
    # 4. Evening Doji Star
    # ──────────────────────────────────────────────────────────
    {
        "id": 0,
        "pattern_name": "Evening Doji Star",
        "alternative_names": ["Doji Evening Star"],
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
        "best_timeframes": ["Daily", "Weekly", "4H"],
        "best_markets": ["Stocks", "Futures", "Crypto", "Commodities"],
        "best_indicators": ["RSI (overbought)", "MACD (bearish divergence)", "Volume", "Resistance levels"],
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

    # ──────────────────────────────────────────────────────────
    # 5. Bullish Abandoned Baby
    # ──────────────────────────────────────────────────────────
    {
        "id": 0,
        "pattern_name": "Bullish Abandoned Baby",
        "alternative_names": ["Abandoned Baby Bottom"],
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
        "best_timeframes": ["Daily", "Weekly"],
        "best_markets": ["Stocks", "Futures"],
        "best_indicators": ["Volume", "Gap analysis", "RSI (oversold)"],
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

    # ──────────────────────────────────────────────────────────
    # 6. Bearish Abandoned Baby
    # ──────────────────────────────────────────────────────────
    {
        "id": 0,
        "pattern_name": "Bearish Abandoned Baby",
        "alternative_names": ["Abandoned Baby Top"],
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
        "best_timeframes": ["Daily", "Weekly"],
        "best_markets": ["Stocks", "Futures"],
        "best_indicators": ["Volume", "Gap analysis", "RSI (overbought)"],
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

    # ──────────────────────────────────────────────────────────
    # 7. Three White Soldiers
    # ──────────────────────────────────────────────────────────
    {
        "id": 0,
        "pattern_name": "Three White Soldiers",
        "alternative_names": ["Three Advancing Soldiers", "Sanpei"],
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
        "best_timeframes": ["Daily", "Weekly", "4H"],
        "best_markets": ["Stocks", "Forex", "Crypto", "Futures", "Commodities"],
        "best_indicators": ["Volume (increasing)", "RSI (not yet overbought)", "Moving Averages", "ADX"],
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

    # ──────────────────────────────────────────────────────────
    # 8. Three Black Crows
    # ──────────────────────────────────────────────────────────
    {
        "id": 0,
        "pattern_name": "Three Black Crows",
        "alternative_names": ["Three Crows"],
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
        "best_timeframes": ["Daily", "Weekly", "4H"],
        "best_markets": ["Stocks", "Forex", "Crypto", "Futures", "Commodities"],
        "best_indicators": ["Volume (increasing)", "RSI (not yet oversold)", "Moving Averages", "ADX"],
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

    # ──────────────────────────────────────────────────────────
    # 9. Three Inside Up
    # ──────────────────────────────────────────────────────────
    {
        "id": 0,
        "pattern_name": "Three Inside Up",
        "alternative_names": ["Confirmed Bullish Harami"],
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
        "best_timeframes": ["Daily", "4H", "1H"],
        "best_markets": ["Stocks", "Forex", "Crypto", "Futures"],
        "best_indicators": ["RSI (oversold)", "Volume", "Support levels", "Moving Averages"],
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

    # ──────────────────────────────────────────────────────────
    # 10. Three Inside Down
    # ──────────────────────────────────────────────────────────
    {
        "id": 0,
        "pattern_name": "Three Inside Down",
        "alternative_names": ["Confirmed Bearish Harami"],
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
        "best_timeframes": ["Daily", "4H", "1H"],
        "best_markets": ["Stocks", "Forex", "Crypto", "Futures"],
        "best_indicators": ["RSI (overbought)", "Volume", "Resistance levels"],
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

    # ──────────────────────────────────────────────────────────
    # 11. Three Outside Up
    # ──────────────────────────────────────────────────────────
    {
        "id": 0,
        "pattern_name": "Three Outside Up",
        "alternative_names": ["Confirmed Bullish Engulfing"],
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
        "best_timeframes": ["Daily", "4H", "1H"],
        "best_markets": ["Stocks", "Forex", "Crypto", "Futures"],
        "best_indicators": ["RSI (oversold)", "Volume", "Support levels", "MACD"],
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

    # ──────────────────────────────────────────────────────────
    # 12. Three Outside Down
    # ──────────────────────────────────────────────────────────
    {
        "id": 0,
        "pattern_name": "Three Outside Down",
        "alternative_names": ["Confirmed Bearish Engulfing"],
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
        "best_timeframes": ["Daily", "4H", "1H"],
        "best_markets": ["Stocks", "Forex", "Crypto", "Futures"],
        "best_indicators": ["RSI (overbought)", "Volume", "Resistance levels", "MACD"],
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

    # ──────────────────────────────────────────────────────────
    # 13. Bullish Tri-Star
    # ──────────────────────────────────────────────────────────
    {
        "id": 0,
        "pattern_name": "Bullish Tri-Star",
        "alternative_names": ["Tri-Star Bottom"],
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
        "best_timeframes": ["Daily", "Weekly"],
        "best_markets": ["Stocks", "Futures"],
        "best_indicators": ["RSI (oversold)", "Volume", "Support levels"],
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

    # ──────────────────────────────────────────────────────────
    # 14. Bearish Tri-Star
    # ──────────────────────────────────────────────────────────
    {
        "id": 0,
        "pattern_name": "Bearish Tri-Star",
        "alternative_names": ["Tri-Star Top"],
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
        "best_timeframes": ["Daily", "Weekly"],
        "best_markets": ["Stocks", "Futures"],
        "best_indicators": ["RSI (overbought)", "Volume", "Resistance levels"],
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

    # ──────────────────────────────────────────────────────────
    # 15. Three Stars in the South
    # ──────────────────────────────────────────────────────────
    {
        "id": 0,
        "pattern_name": "Three Stars in the South",
        "alternative_names": ["Minami No Sansei"],
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
        "best_timeframes": ["Daily", "Weekly"],
        "best_markets": ["Stocks", "Futures"],
        "best_indicators": ["RSI (oversold)", "Volume (declining)", "Support levels"],
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

    # ──────────────────────────────────────────────────────────
    # 16. Unique Three River Bottom
    # ──────────────────────────────────────────────────────────
    {
        "id": 0,
        "pattern_name": "Unique Three River Bottom",
        "alternative_names": ["Three River Bottom"],
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
        "best_timeframes": ["Daily", "Weekly"],
        "best_markets": ["Stocks", "Futures"],
        "best_indicators": ["RSI (oversold)", "Volume", "Support levels"],
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

    # ──────────────────────────────────────────────────────────
    # 17. Upside Gap Two Crows
    # ──────────────────────────────────────────────────────────
    {
        "id": 0,
        "pattern_name": "Upside Gap Two Crows",
        "alternative_names": ["Gap Two Crows"],
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
        "best_timeframes": ["Daily", "Weekly"],
        "best_markets": ["Stocks", "Futures"],
        "best_indicators": ["RSI (overbought)", "Volume", "Resistance levels"],
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

    # ──────────────────────────────────────────────────────────
    # 18. Identical Three Crows
    # ──────────────────────────────────────────────────────────
    {
        "id": 0,
        "pattern_name": "Identical Three Crows",
        "alternative_names": ["Three Identical Crows"],
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
        "best_timeframes": ["Daily", "Weekly"],
        "best_markets": ["Stocks", "Futures", "Crypto"],
        "best_indicators": ["Volume (sustained high)", "ADX (strong trend)", "Moving Averages"],
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

    # ──────────────────────────────────────────────────────────
    # 19. Deliberation
    # ──────────────────────────────────────────────────────────
    {
        "id": 0,
        "pattern_name": "Deliberation",
        "alternative_names": ["Stalling Pattern", "Aka Sanpo Daioji"],
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
        "best_timeframes": ["Daily", "Weekly"],
        "best_markets": ["Stocks", "Futures"],
        "best_indicators": ["RSI (overbought)", "Volume (declining)", "Resistance levels"],
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

    # ──────────────────────────────────────────────────────────
    # 20. Advance Block
    # ──────────────────────────────────────────────────────────
    {
        "id": 0,
        "pattern_name": "Advance Block",
        "alternative_names": ["Advancing Block"],
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
        "best_timeframes": ["Daily", "Weekly"],
        "best_markets": ["Stocks", "Futures", "Crypto"],
        "best_indicators": ["RSI (overbought)", "Volume (declining)", "Resistance levels"],
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

    # ──────────────────────────────────────────────────────────
    # 21. Stick Sandwich
    # ──────────────────────────────────────────────────────────
    {
        "id": 0,
        "pattern_name": "Stick Sandwich",
        "alternative_names": ["Sandwich Pattern"],
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
        "best_timeframes": ["Daily", "4H"],
        "best_markets": ["Stocks", "Futures"],
        "best_indicators": ["RSI (oversold)", "Volume", "Support levels"],
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

    # ──────────────────────────────────────────────────────────
    # 22. Concealing Baby Swallow (4 candles)
    # ──────────────────────────────────────────────────────────
    {
        "id": 0,
        "pattern_name": "Concealing Baby Swallow",
        "alternative_names": ["Baby Swallow"],
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
        "best_timeframes": ["Daily", "Weekly"],
        "best_markets": ["Stocks", "Futures"],
        "best_indicators": ["RSI (deeply oversold)", "Volume (capitulation)", "Support levels"],
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

    # ──────────────────────────────────────────────────────────
    # 23. Bullish Side-by-Side White Lines
    # ──────────────────────────────────────────────────────────
    {
        "id": 0,
        "pattern_name": "Bullish Side-by-Side White Lines",
        "alternative_names": ["Side by Side Lines Bullish"],
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
        "best_timeframes": ["Daily", "4H"],
        "best_markets": ["Stocks", "Futures"],
        "best_indicators": ["Moving Averages", "Volume", "ADX"],
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

    # ──────────────────────────────────────────────────────────
    # 24. Bearish Side-by-Side White Lines
    # ──────────────────────────────────────────────────────────
    {
        "id": 0,
        "pattern_name": "Bearish Side-by-Side White Lines",
        "alternative_names": ["Side by Side Lines Bearish"],
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
        "best_timeframes": ["Daily", "4H"],
        "best_markets": ["Stocks", "Futures"],
        "best_indicators": ["Moving Averages", "Volume (weak on bounces)", "ADX"],
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

    # ──────────────────────────────────────────────────────────
    # 25. Upside Tasuki Gap
    # ──────────────────────────────────────────────────────────
    {
        "id": 0,
        "pattern_name": "Upside Tasuki Gap",
        "alternative_names": ["Tasuki Gap Bullish"],
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
        "best_timeframes": ["Daily", "4H"],
        "best_markets": ["Stocks", "Futures", "Crypto"],
        "best_indicators": ["Volume", "Moving Averages", "Gap analysis"],
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

    # ──────────────────────────────────────────────────────────
    # 26. Downside Tasuki Gap
    # ──────────────────────────────────────────────────────────
    {
        "id": 0,
        "pattern_name": "Downside Tasuki Gap",
        "alternative_names": ["Tasuki Gap Bearish"],
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
        "best_timeframes": ["Daily", "4H"],
        "best_markets": ["Stocks", "Futures", "Crypto"],
        "best_indicators": ["Volume", "Moving Averages", "Gap analysis"],
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

    # ──────────────────────────────────────────────────────────
    # 27. Upside Gap Three Methods
    # ──────────────────────────────────────────────────────────
    {
        "id": 0,
        "pattern_name": "Upside Gap Three Methods",
        "alternative_names": ["Gap Three Methods Bullish"],
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
        "best_timeframes": ["Daily", "4H"],
        "best_markets": ["Stocks", "Futures"],
        "best_indicators": ["Volume", "Moving Averages", "ADX"],
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

    # ──────────────────────────────────────────────────────────
    # 28. Downside Gap Three Methods
    # ──────────────────────────────────────────────────────────
    {
        "id": 0,
        "pattern_name": "Downside Gap Three Methods",
        "alternative_names": ["Gap Three Methods Bearish"],
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
        "best_timeframes": ["Daily", "4H"],
        "best_markets": ["Stocks", "Futures"],
        "best_indicators": ["Volume", "Moving Averages", "ADX"],
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
]
