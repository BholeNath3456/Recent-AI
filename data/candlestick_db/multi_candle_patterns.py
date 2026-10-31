"""
Multi-Candle Candlestick Patterns Database (4 and 5 Candle Patterns)
====================================================================

Part of the comprehensive candlestick pattern database for
a quantitative trading AI system.

Contains 9 patterns:
    - Rising Three Methods (5 candle, Bullish Continuation)
    - Falling Three Methods (5 candle, Bearish Continuation)
    - Bullish Breakaway (5 candle, Bullish Reversal)
    - Bearish Breakaway (5 candle, Bearish Reversal)
    - Mat Hold (5 candle, Bullish Continuation)
    - Bullish Three Line Strike (4 candle, Bullish Reversal)
    - Bearish Three Line Strike (4 candle, Bearish Reversal)
    - Ladder Bottom (5 candle, Bullish Reversal)
    - Ladder Top (5 candle, Bearish Reversal)

DISCLAIMER:
    No pattern predicts market direction with certainty. All success
    rates and confidence scores are conservative estimates based on
    general technical analysis literature. Actual performance varies
    by market, timeframe, and conditions. Always use proper risk
    management.
"""

PATTERNS = [
    # ──────────────────────────────────────────────────────────────
    # Pattern 1: Rising Three Methods
    # ──────────────────────────────────────────────────────────────
    {
        "id": 0,
        "pattern_name": "Rising Three Methods",
        "alternative_names": ["Rising 3 Methods", "Bullish Three Methods"],
        "japanese_name": "Uwa Banare Sanpoo Ohdatekomi",
        "category": "Five Candle",
        "sub_category": "Bullish Continuation",
        "sentiment": "Bullish",
        "expected_direction": "CONTINUATION_UP",
        "trend_required": "Uptrend",
        "num_candles": 5,
        "pattern_structure": (
            "Long bullish C1, three small bearish candles (C2-C4) contained "
            "within C1's range, then long bullish C5 closing above C1's high"
        ),
        "candle_by_candle": [
            (
                "Candle 1: Long bullish candle establishing the uptrend "
                "direction. Strong buying pressure with large body."
            ),
            (
                "Candle 2: Small bearish candle that trades within C1's "
                "range. Mild profit-taking begins."
            ),
            (
                "Candle 3: Small bearish candle continuing the consolidation "
                "within C1's range. Sellers unable to push below C1's low."
            ),
            (
                "Candle 4: Small bearish candle, still contained within "
                "C1's high-low range. The retracement loses momentum."
            ),
            (
                "Candle 5: Long bullish candle that opens within or near "
                "C4's body and closes above C1's high. Strong buying "
                "resumes, confirming the uptrend continuation."
            ),
        ],
        "market_psychology": (
            "C1 shows strong buying. C2-C4 represent a brief rest or "
            "consolidation where short-term traders take profits, but the "
            "pullback is shallow (contained within C1). C5 confirms that "
            "the resting phase is over and bulls resume control, often "
            "trapping shorts who entered during the pullback."
        ),
        "confirmation_required": (
            "C5 must close above C1's high. Sixth candle continuing higher "
            "provides extra confirmation."
        ),
        "volume_confirmation": (
            "Volume should be high on C1 and C5, and decline during C2-C4 "
            "consolidation phase. Rising volume on C5 confirms conviction."
        ),
        "volatility_conditions": (
            "Works best in trending markets with moderate volatility. The "
            "consolidation candles should show compression."
        ),
        "gap_requirement": "None",
        "reliability": "High",
        "success_rate_range": "65-79%",
        "failure_conditions": [
            "C2-C4 break below C1's low (invalidates containment)",
            "C5 fails to close above C1's high",
            "Volume remains high during C2-C4 (selling pressure too strong)",
            "Broader market turning bearish",
            "Pattern forms near major resistance",
        ],
        "entry_rules": (
            "Enter long on C5's close or on break above C5's high. "
            "Stop and reverse if C5 fails."
        ),
        "stop_loss_rules": (
            "Below the lowest low of the entire 5-candle pattern "
            "(typically C3 or C4 low)."
        ),
        "take_profit_rules": (
            "Measure C1's body height and project from C5's close. Or "
            "target next resistance level. Use trailing stop."
        ),
        "risk_reward": "1:3",
        "best_timeframes": ["Daily", "Weekly", "4H"],
        "best_markets": ["Stocks", "Futures", "Commodities", "Forex"],
        "best_indicators": [
            "Moving Averages (trend confirmation)",
            "Volume",
            "ADX (trending >25)",
            "Bollinger Bands (squeeze during C2-C4)",
        ],
        "common_mistakes": [
            "Not verifying C2-C4 are contained within C1's range",
            "Trading before C5 confirms",
            "Ignoring volume pattern",
            "Confusing with Falling Three Methods",
        ],
        "ai_features": [
            "c1.is_bullish AND c1.body_ratio > 0.60",
            "c2.is_bearish AND c3.is_bearish AND c4.is_bearish",
            "all(c.high <= c1.high AND c.low >= c1.low for c in [c2,c3,c4])",
            "c5.is_bullish AND c5.close > c1.high",
            "c5.body_ratio > 0.50",
        ],
        "ohlc_relationship": (
            "C1: bullish, body_ratio > 0.60; C2-C4: small bearish, all "
            "contained within C1 H-L range; C5: bullish, C5_close > "
            "C1_high, body_ratio > 0.50"
        ),
        "label": "Bullish",
        "confidence_score": 78,
        "probability_score": 72,
    },

    # ──────────────────────────────────────────────────────────────
    # Pattern 2: Falling Three Methods
    # ──────────────────────────────────────────────────────────────
    {
        "id": 1,
        "pattern_name": "Falling Three Methods",
        "alternative_names": ["Falling 3 Methods", "Bearish Three Methods"],
        "japanese_name": "Shita Banare Sanpoo Ohdatekomi",
        "category": "Five Candle",
        "sub_category": "Bearish Continuation",
        "sentiment": "Bearish",
        "expected_direction": "CONTINUATION_DOWN",
        "trend_required": "Downtrend",
        "num_candles": 5,
        "pattern_structure": (
            "Long bearish C1, three small bullish candles (C2-C4) contained "
            "within C1's range, then long bearish C5 closing below C1's low"
        ),
        "candle_by_candle": [
            (
                "Candle 1: Long bearish candle establishing strong downward "
                "momentum. Heavy selling pressure with a large real body."
            ),
            (
                "Candle 2: Small bullish candle that opens within or near "
                "C1's low and rallies modestly. Short-covering or minor "
                "bottom-fishing begins, but remains within C1's range."
            ),
            (
                "Candle 3: Small bullish candle continuing the counter-rally "
                "within C1's range. Buyers are unable to push above C1's "
                "high, indicating limited bullish conviction."
            ),
            (
                "Candle 4: Small bullish candle, still contained within "
                "C1's high-low range. The relief rally is losing steam and "
                "buying pressure fades."
            ),
            (
                "Candle 5: Long bearish candle that opens within or near "
                "C4's body and closes below C1's low. Selling resumes with "
                "force, confirming the downtrend continuation and trapping "
                "bottom-fishers from C2-C4."
            ),
        ],
        "market_psychology": (
            "C1 demonstrates dominant selling pressure. C2-C4 are a brief "
            "pause where short-covering and bargain hunters create a shallow "
            "bounce, but it never threatens C1's high, revealing the lack "
            "of genuine bullish conviction. C5 shows bears reasserting "
            "control, trapping anyone who bought the bounce and accelerating "
            "the downtrend."
        ),
        "confirmation_required": (
            "C5 must close below C1's low. A sixth candle continuing "
            "lower, especially on increased volume, provides strong "
            "additional confirmation."
        ),
        "volume_confirmation": (
            "Volume should be high on C1 and C5, reflecting strong selling "
            "conviction. Volume during C2-C4 should noticeably decline, "
            "confirming the bounce is merely a low-participation rest. "
            "Expanding volume on C5 confirms the resumption of selling."
        ),
        "volatility_conditions": (
            "Works best in established downtrends with moderate to high "
            "volatility. The consolidation candles C2-C4 should show "
            "reduced range (volatility compression) before C5 expands "
            "the range again."
        ),
        "gap_requirement": "None",
        "reliability": "High",
        "success_rate_range": "65-78%",
        "failure_conditions": [
            "C2-C4 break above C1's high (invalidates containment)",
            "C5 fails to close below C1's low",
            "Volume increases during C2-C4 (genuine buying emerging)",
            "Strong bullish divergence on RSI or MACD during C2-C4",
            "Pattern forms near major support level",
            "Broader market sentiment shifting bullish",
        ],
        "entry_rules": (
            "Enter short on C5's close or on break below C5's low. "
            "Confirm with volume expansion on C5. Consider a stop-and-"
            "reverse if C5 fails and price reclaims C1's high."
        ),
        "stop_loss_rules": (
            "Above the highest high of the entire 5-candle pattern "
            "(typically the high of C3 or C4). A tighter stop can be "
            "placed above C5's open."
        ),
        "take_profit_rules": (
            "Measure C1's body height and project downward from C5's "
            "close for a minimum target. Target next support level or "
            "use a trailing stop to ride the continuation move."
        ),
        "risk_reward": "1:3",
        "best_timeframes": ["Daily", "Weekly", "4H"],
        "best_markets": ["Stocks", "Futures", "Commodities", "Forex"],
        "best_indicators": [
            "Moving Averages (trend confirmation, price below MA)",
            "Volume (declining C2-C4, expanding C5)",
            "ADX (trending >25 confirms strong trend)",
            "Bollinger Bands (squeeze during C2-C4 consolidation)",
            "MACD (bearish histogram confirmation)",
        ],
        "common_mistakes": [
            "Not verifying C2-C4 are contained within C1's range",
            "Shorting before C5 confirms the pattern",
            "Ignoring the volume signature (must decline then expand)",
            "Confusing with Rising Three Methods",
            "Trading the pattern near strong historical support",
        ],
        "ai_features": [
            "c1.is_bearish AND c1.body_ratio > 0.60",
            "c2.is_bullish AND c3.is_bullish AND c4.is_bullish",
            "all(c.high <= c1.high AND c.low >= c1.low for c in [c2,c3,c4])",
            "c5.is_bearish AND c5.close < c1.low",
            "c5.body_ratio > 0.50",
        ],
        "ohlc_relationship": (
            "C1: bearish, body_ratio > 0.60; C2-C4: small bullish, all "
            "contained within C1 H-L range; C5: bearish, C5_close < "
            "C1_low, body_ratio > 0.50"
        ),
        "label": "Bearish",
        "confidence_score": 77,
        "probability_score": 71,
    },

    # ──────────────────────────────────────────────────────────────
    # Pattern 3: Bullish Breakaway
    # ──────────────────────────────────────────────────────────────
    {
        "id": 2,
        "pattern_name": "Bullish Breakaway",
        "alternative_names": ["Breakaway Bullish", "Five Candle Bullish Breakaway"],
        "japanese_name": "Hanare Sante No Shinte Zukae",
        "category": "Five Candle",
        "sub_category": "Bullish Reversal",
        "sentiment": "Bullish",
        "expected_direction": "UP",
        "trend_required": "Downtrend",
        "num_candles": 5,
        "pattern_structure": (
            "Long bearish C1, C2 gaps down and is bearish, small C3 "
            "bearish or doji, small C4 bearish or bullish, large bullish "
            "C5 that closes into the gap between C1 and C2 but does not "
            "fully fill it"
        ),
        "candle_by_candle": [
            (
                "Candle 1: Long bearish candle in an established downtrend. "
                "Strong selling pressure drives price sharply lower, "
                "establishing the bearish tone for the pattern."
            ),
            (
                "Candle 2: Bearish candle that gaps down below C1's close, "
                "creating a visible window. Continuation of panic selling "
                "or bearish momentum that creates the gap."
            ),
            (
                "Candle 3: Small bearish candle or doji. The downward "
                "momentum is clearly fading. Bodies are small, showing "
                "indecision and exhaustion of selling pressure."
            ),
            (
                "Candle 4: Small candle, can be bearish or bullish. Further "
                "deceleration of the downtrend. If bullish, it hints at "
                "emerging buying interest. Price stalls near the lows."
            ),
            (
                "Candle 5: Large bullish candle that rallies strongly, "
                "closing into the gap area between C1's close and C2's "
                "open. Critically, it does NOT fully close the gap — it "
                "closes between C2's open and C1's close."
            ),
        ],
        "market_psychology": (
            "C1 and the gap into C2 represent climactic selling and bearish "
            "capitulation. C3-C4 show the selling exhausting itself as bears "
            "run out of ammunition. C5 represents a strong bullish response "
            "as value buyers step in. The fact that C5 reclaims much of the "
            "gap territory signals that the bearish momentum is broken, "
            "but the partial gap fill suggests measured buying rather than "
            "a panic short squeeze."
        ),
        "confirmation_required": (
            "C5 must close within the gap between C1's close and C2's open. "
            "A sixth bullish candle continuing higher provides additional "
            "confirmation. Full gap fill on subsequent candles further "
            "validates the reversal."
        ),
        "volume_confirmation": (
            "Volume should be elevated on C1 and C2 (panic selling), "
            "decline on C3-C4 (exhaustion), and increase on C5 (new "
            "buying interest). High volume on C5 is key."
        ),
        "volatility_conditions": (
            "Typically appears after high-volatility selling. The "
            "deceleration on C3-C4 shows volatility compressing before "
            "C5 releases it in the opposite direction."
        ),
        "gap_requirement": "Required",
        "reliability": "Medium",
        "success_rate_range": "55-70%",
        "failure_conditions": [
            "C5 fails to close into the gap area",
            "C5 fully closes the gap (different pattern interpretation)",
            "No gap exists between C1 and C2",
            "Volume does not increase on C5",
            "Pattern forms in a sideways market (no prior downtrend)",
            "Strong resistance exists at the gap fill level",
        ],
        "entry_rules": (
            "Enter long on C5's close or on the next candle's open if C5 "
            "closes within the gap. Aggressive entry: at C5 mid-point "
            "if it's clearly bullish. Wait for sixth candle confirmation "
            "for conservative approach."
        ),
        "stop_loss_rules": (
            "Below the lowest low of the pattern (typically C3 or C4 low). "
            "Tighter stop below C5's low if risk-reward permits."
        ),
        "take_profit_rules": (
            "First target: full gap fill (C1's close level). Second target: "
            "C1's open level. Use measured move of C5's body projected "
            "upward for extended targets."
        ),
        "risk_reward": "1:2.5",
        "best_timeframes": ["Daily", "Weekly"],
        "best_markets": ["Stocks", "Futures", "Indices"],
        "best_indicators": [
            "RSI (oversold <30 condition before C5)",
            "Volume (exhaustion then expansion pattern)",
            "MACD (bullish divergence during C3-C4)",
            "Stochastic (oversold crossover)",
            "Support levels (pattern near key support adds weight)",
        ],
        "common_mistakes": [
            "Ignoring the gap requirement between C1 and C2",
            "Accepting a C5 that fully closes the gap",
            "Trading the pattern without a prior established downtrend",
            "Not checking volume signature for exhaustion and renewal",
            "Confusing with Morning Star or other reversal patterns",
        ],
        "ai_features": [
            "c1.is_bearish AND c1.body_ratio > 0.55",
            "c2.is_bearish AND c2.open < c1.close (gap down)",
            "c3.body_ratio < 0.30 OR c3.is_doji",
            "c4.body_ratio < 0.35",
            "c5.is_bullish AND c5.body_ratio > 0.55",
            "c5.close > c2.open AND c5.close < c1.close",
        ],
        "ohlc_relationship": (
            "C1: bearish, body_ratio > 0.55; C2: bearish, C2_open < "
            "C1_close (gap); C3: small bearish/doji; C4: small body; "
            "C5: bullish, C5_close > C2_open AND C5_close < C1_close "
            "(partial gap fill)"
        ),
        "label": "Bullish",
        "confidence_score": 62,
        "probability_score": 60,
    },

    # ──────────────────────────────────────────────────────────────
    # Pattern 4: Bearish Breakaway
    # ──────────────────────────────────────────────────────────────
    {
        "id": 3,
        "pattern_name": "Bearish Breakaway",
        "alternative_names": ["Breakaway Bearish", "Five Candle Bearish Breakaway"],
        "japanese_name": "Hanare Sante No Shinte Zukae (Bearish)",
        "category": "Five Candle",
        "sub_category": "Bearish Reversal",
        "sentiment": "Bearish",
        "expected_direction": "DOWN",
        "trend_required": "Uptrend",
        "num_candles": 5,
        "pattern_structure": (
            "Long bullish C1, C2 gaps up and is bullish, small C3 "
            "bullish or doji, small C4 bullish or bearish, large bearish "
            "C5 that closes into the gap between C1 and C2 but does not "
            "fully fill it"
        ),
        "candle_by_candle": [
            (
                "Candle 1: Long bullish candle in an established uptrend. "
                "Strong buying drives price sharply higher, establishing "
                "the bullish tone for the pattern."
            ),
            (
                "Candle 2: Bullish candle that gaps up above C1's close, "
                "creating a visible window. Exuberant buying or momentum "
                "chasing drives the gap higher."
            ),
            (
                "Candle 3: Small bullish candle or doji. Upward momentum "
                "is clearly fading. Small bodies reveal indecision and "
                "waning buying pressure at these elevated levels."
            ),
            (
                "Candle 4: Small candle, can be bullish or bearish. The "
                "uptrend deceleration continues. If bearish, early selling "
                "interest emerges. Price stalls near the highs."
            ),
            (
                "Candle 5: Large bearish candle that declines strongly, "
                "closing into the gap area between C1's close and C2's "
                "open. It does NOT fully close the gap, closing between "
                "C2's open and C1's close."
            ),
        ],
        "market_psychology": (
            "C1 and the gap into C2 represent euphoric or climactic buying. "
            "C3-C4 show the buying exhausting itself as late longs run out "
            "of conviction. C5 represents a sharp bearish response as "
            "profit-takers and new shorts enter. The partial gap fill "
            "signals that bullish momentum is broken, and the market is "
            "transitioning from buyers' to sellers' control."
        ),
        "confirmation_required": (
            "C5 must close within the gap between C1's close and C2's open. "
            "A sixth bearish candle continuing lower confirms the reversal. "
            "Full gap fill on subsequent candles adds conviction."
        ),
        "volume_confirmation": (
            "Volume should be elevated on C1 and C2 (euphoric buying), "
            "decline on C3-C4 (exhaustion), and increase sharply on C5 "
            "(distribution and new selling). Heavy volume on C5 validates "
            "the shift."
        ),
        "volatility_conditions": (
            "Often appears after high-volatility buying phases. C3-C4 "
            "compress volatility before C5 expands it in the bearish "
            "direction."
        ),
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
            "Major bullish catalyst overrides technical picture",
        ],
        "entry_rules": (
            "Enter short on C5's close or on the next candle's open if "
            "C5 closes within the gap. Conservative approach: wait for "
            "sixth candle confirmation below C5's close."
        ),
        "stop_loss_rules": (
            "Above the highest high of the pattern (typically C3 or C4 "
            "high). Tighter stop above C5's open if risk-reward allows."
        ),
        "take_profit_rules": (
            "First target: full gap fill (C1's close level). Second "
            "target: C1's open level. Use measured move of C5's body "
            "projected downward for extended targets."
        ),
        "risk_reward": "1:2.5",
        "best_timeframes": ["Daily", "Weekly"],
        "best_markets": ["Stocks", "Futures", "Indices"],
        "best_indicators": [
            "RSI (overbought >70 condition before C5)",
            "Volume (euphoria then distribution pattern)",
            "MACD (bearish divergence during C3-C4)",
            "Stochastic (overbought crossover)",
            "Resistance levels (pattern near key resistance adds weight)",
        ],
        "common_mistakes": [
            "Ignoring the gap requirement between C1 and C2",
            "Accepting a C5 that fully closes the gap",
            "Trading the pattern without a prior established uptrend",
            "Not confirming volume shift from buying to selling",
            "Confusing with Evening Star or other top reversal patterns",
        ],
        "ai_features": [
            "c1.is_bullish AND c1.body_ratio > 0.55",
            "c2.is_bullish AND c2.open > c1.close (gap up)",
            "c3.body_ratio < 0.30 OR c3.is_doji",
            "c4.body_ratio < 0.35",
            "c5.is_bearish AND c5.body_ratio > 0.55",
            "c5.close < c2.open AND c5.close > c1.close",
        ],
        "ohlc_relationship": (
            "C1: bullish, body_ratio > 0.55; C2: bullish, C2_open > "
            "C1_close (gap); C3: small bullish/doji; C4: small body; "
            "C5: bearish, C5_close < C2_open AND C5_close > C1_close "
            "(partial gap fill)"
        ),
        "label": "Bearish",
        "confidence_score": 60,
        "probability_score": 58,
    },

    # ──────────────────────────────────────────────────────────────
    # Pattern 5: Mat Hold
    # ──────────────────────────────────────────────────────────────
    {
        "id": 4,
        "pattern_name": "Mat Hold",
        "alternative_names": ["Mat Hold Pattern", "Mat-Hold Bullish"],
        "japanese_name": "Uwazumi",
        "category": "Five Candle",
        "sub_category": "Bullish Continuation",
        "sentiment": "Bullish",
        "expected_direction": "CONTINUATION_UP",
        "trend_required": "Uptrend",
        "num_candles": 5,
        "pattern_structure": (
            "Long bullish C1, C2 gaps up then forms a small bearish candle, "
            "C3 small bearish, C4 small bearish or doji, C5 long bullish "
            "candle closing above C1's high. Similar to Rising Three "
            "Methods but with an initial gap up between C1 and C2."
        ),
        "candle_by_candle": [
            (
                "Candle 1: Long bullish candle in an uptrend. Strong "
                "buying conviction creates a large real body, reinforcing "
                "the bullish trend."
            ),
            (
                "Candle 2: Small bearish candle that gaps up from C1's "
                "close. Despite the gap up, a small bearish body forms — "
                "early profit-taking after the gap. The low of C2 stays "
                "above C1's midpoint."
            ),
            (
                "Candle 3: Small bearish candle continuing the shallow "
                "pullback. The decline is controlled, with C3's low "
                "remaining above C1's low. Selling pressure is weak."
            ),
            (
                "Candle 4: Small bearish candle or doji. The pullback is "
                "exhausting itself. C4 often makes the lowest low of the "
                "consolidation but holds above C1's open or midpoint."
            ),
            (
                "Candle 5: Long bullish candle that opens near C4 and "
                "closes above C1's high (and ideally above C2's high). "
                "A decisive resumption of the uptrend with strong volume."
            ),
        ],
        "market_psychology": (
            "C1 shows dominant buying. The gap up into C2 reflects continued "
            "bullish enthusiasm, but the small bearish C2 body shows some "
            "profit-taking at higher levels. C3-C4 are a controlled decline "
            "— the gap and underlying support hold, indicating that bulls "
            "are resting rather than retreating. C5 demonstrates that the "
            "pause was just a consolidation, and the trend resumes with "
            "conviction, often catching late shorts off guard."
        ),
        "confirmation_required": (
            "C5 must close above C1's high. The gap from C1 to C2 should "
            "remain at least partially open during the consolidation. "
            "A sixth candle continuing higher confirms the pattern."
        ),
        "volume_confirmation": (
            "High volume on C1 and C5. Volume should contract during "
            "C2-C4 consolidation. C5's volume should ideally exceed C1's "
            "volume, showing fresh buying commitment."
        ),
        "volatility_conditions": (
            "Best in trending markets with moderate volatility. The gap "
            "up distinguishes Mat Hold from Rising Three Methods and "
            "suggests stronger underlying momentum."
        ),
        "gap_requirement": "Required",
        "reliability": "High",
        "success_rate_range": "65-80%",
        "failure_conditions": [
            "C2-C4 fill the gap and close below C1's close",
            "C4 closes below C1's midpoint or open",
            "C5 fails to close above C1's high",
            "Volume expands during C2-C4 (serious distribution)",
            "C2 does not gap up from C1",
            "Pattern forms at major resistance zone",
        ],
        "entry_rules": (
            "Enter long on C5's close or on break above C5's high. "
            "More aggressive entry at C5's midpoint once bullish intent "
            "is clear. Ensure C2-C4 held above C1's lower half."
        ),
        "stop_loss_rules": (
            "Below the lowest low of C2-C4 consolidation phase. "
            "Alternatively, below C1's midpoint for a wider stop."
        ),
        "take_profit_rules": (
            "Project C1's body range from C5's close. Target next "
            "resistance level. Trail stop below each subsequent candle's "
            "low. Consider 1.5x to 2x the pattern height."
        ),
        "risk_reward": "1:3.5",
        "best_timeframes": ["Daily", "Weekly", "4H"],
        "best_markets": ["Stocks", "Futures", "Forex", "Commodities"],
        "best_indicators": [
            "Moving Averages (price above 20 and 50 MA)",
            "Volume (contraction-expansion signature)",
            "ADX (>25 confirming trend strength)",
            "Bollinger Bands (price riding upper band)",
            "RSI (staying above 50 during consolidation)",
        ],
        "common_mistakes": [
            "Confusing with Rising Three Methods (Mat Hold requires gap)",
            "Ignoring the gap requirement between C1 and C2",
            "Not ensuring C2-C4 hold above C1's lower half",
            "Entering before C5 confirms with a strong close",
            "Overlooking volume pattern during consolidation",
        ],
        "ai_features": [
            "c1.is_bullish AND c1.body_ratio > 0.55",
            "c2.open > c1.close (gap up) AND c2.is_bearish AND c2.body_ratio < 0.40",
            "c3.is_bearish AND c3.body_ratio < 0.35",
            "c4.body_ratio < 0.30 AND c4.low > c1.open",
            "c5.is_bullish AND c5.close > c1.high AND c5.body_ratio > 0.50",
        ],
        "ohlc_relationship": (
            "C1: bullish, body_ratio > 0.55; C2: gap up (C2_open > C1_close), "
            "small bearish; C3: small bearish, C3_low > C1_low; C4: small "
            "bearish/doji, C4_low > C1_open; C5: bullish, C5_close > C1_high, "
            "body_ratio > 0.50"
        ),
        "label": "Bullish",
        "confidence_score": 80,
        "probability_score": 74,
    },

    # ──────────────────────────────────────────────────────────────
    # Pattern 6: Bullish Three Line Strike
    # ──────────────────────────────────────────────────────────────
    {
        "id": 5,
        "pattern_name": "Bullish Three Line Strike",
        "alternative_names": [
            "Three Line Strike Bullish",
            "Bullish Strike",
            "Sanpei Uchi Kaeshi (Bullish)",
        ],
        "japanese_name": "Sanpei Uchi Kaeshi",
        "category": "Four Candle",
        "sub_category": "Bullish Reversal",
        "sentiment": "Bullish",
        "expected_direction": "UP",
        "trend_required": "Downtrend",
        "num_candles": 4,
        "pattern_structure": (
            "Three consecutive bearish candles (like Three Black Crows), "
            "each closing lower than the previous, then C4 is a large "
            "bullish candle that opens below C3's close and closes above "
            "C1's open, engulfing all three bearish candles."
        ),
        "candle_by_candle": [
            (
                "Candle 1: Long bearish candle in a downtrend. Sellers "
                "control price action with a substantial close below the "
                "open. Each candle opens within the previous candle's body."
            ),
            (
                "Candle 2: Long bearish candle that opens within or near "
                "C1's body and closes below C1's low. Sustained selling "
                "pressure pushes price further down."
            ),
            (
                "Candle 3: Long bearish candle that opens within or near "
                "C2's body and closes below C2's low. The three consecutive "
                "bearish candles resemble Three Black Crows."
            ),
            (
                "Candle 4: Large bullish candle that opens at or below "
                "C3's close and rallies sharply, closing above C1's open. "
                "This single candle engulfs the entire range of the prior "
                "three bearish candles, representing a dramatic reversal."
            ),
        ],
        "market_psychology": (
            "C1-C3 represent a controlled sell-off that lures more shorts "
            "and creates a sense of inevitable decline. C4 is a dramatic "
            "reversal — a massive bullish candle that traps all the shorts "
            "from C1-C3 period and forces aggressive short-covering. The "
            "psychology shifts from bearish dominance to panic covering. "
            "The pattern works because the extended three-candle decline "
            "creates a climactic exhaustion point."
        ),
        "confirmation_required": (
            "C4 must close above C1's open to fully engulf all three "
            "bearish candles. A fifth bullish candle with a higher close "
            "provides important confirmation, as the pattern has a notable "
            "failure rate without it."
        ),
        "volume_confirmation": (
            "Volume should be moderate during C1-C3 and spike significantly "
            "on C4. The volume surge on C4 reflects short-covering and new "
            "buying. Low volume on C4 is a warning sign."
        ),
        "volatility_conditions": (
            "Can appear in various volatility conditions. Most reliable "
            "when forming after a sharp decline with expanding volatility. "
            "C4's range should be notably larger than any individual "
            "candle in C1-C3."
        ),
        "gap_requirement": "None",
        "reliability": "Medium",
        "success_rate_range": "60-72%",
        "failure_conditions": [
            "C4 does not close above C1's open (incomplete engulfing)",
            "Volume on C4 is weak",
            "C1-C3 are not progressively lower (not stair-stepped)",
            "Pattern forms in a sideways range (no prior downtrend)",
            "Fifth candle reverses lower (bull trap)",
            "C4 has excessive upper shadow (rejection at highs)",
        ],
        "entry_rules": (
            "Enter long on C4's close or on break above C4's high. "
            "Conservative: wait for fifth candle to confirm direction. "
            "Set alert if C4 forms intraday and shows engulfing potential."
        ),
        "stop_loss_rules": (
            "Below C3's low (the lowest point of the pattern) or below "
            "C4's low if C4 opened below C3's close."
        ),
        "take_profit_rules": (
            "Measure the total height of C1-C3 decline and project upward "
            "from C4's close. Or target the pre-decline swing high. "
            "Use trailing stop as momentum may extend the rally."
        ),
        "risk_reward": "1:2",
        "best_timeframes": ["Daily", "4H", "1H"],
        "best_markets": ["Stocks", "Futures", "Forex", "Indices"],
        "best_indicators": [
            "RSI (oversold before C4, divergence on C3)",
            "Volume (spike on C4)",
            "MACD (bullish crossover near C4)",
            "Moving Averages (proximity to major MA support)",
            "Fibonacci retracement (C3 low near key level)",
        ],
        "common_mistakes": [
            "Not requiring full engulfment of all three bearish candles",
            "Ignoring that C4 must close above C1's open",
            "Treating C1-C3 as just any three bearish candles (they should be stair-stepped)",
            "Not waiting for fifth candle confirmation",
            "Confusing with bearish continuation if context is ignored",
        ],
        "ai_features": [
            "c1.is_bearish AND c1.body_ratio > 0.50",
            "c2.is_bearish AND c2.close < c1.close",
            "c3.is_bearish AND c3.close < c2.close",
            "c4.is_bullish AND c4.open <= c3.close AND c4.close >= c1.open",
            "c4.body_size > (c1.body_size + c2.body_size + c3.body_size) * 0.8",
        ],
        "ohlc_relationship": (
            "C1: bearish; C2: bearish, C2_close < C1_close; C3: bearish, "
            "C3_close < C2_close; C4: bullish, C4_open <= C3_close, "
            "C4_close >= C1_open (engulfs all three)"
        ),
        "label": "Bullish",
        "confidence_score": 65,
        "probability_score": 63,
    },

    # ──────────────────────────────────────────────────────────────
    # Pattern 7: Bearish Three Line Strike
    # ──────────────────────────────────────────────────────────────
    {
        "id": 6,
        "pattern_name": "Bearish Three Line Strike",
        "alternative_names": [
            "Three Line Strike Bearish",
            "Bearish Strike",
            "Sanpei Uchi Kaeshi (Bearish)",
        ],
        "japanese_name": "Sanpei Uchi Kaeshi (Bearish)",
        "category": "Four Candle",
        "sub_category": "Bearish Reversal",
        "sentiment": "Bearish",
        "expected_direction": "DOWN",
        "trend_required": "Uptrend",
        "num_candles": 4,
        "pattern_structure": (
            "Three consecutive bullish candles (like Three White Soldiers), "
            "each closing higher than the previous, then C4 is a large "
            "bearish candle that opens above C3's close and closes below "
            "C1's open, engulfing all three bullish candles."
        ),
        "candle_by_candle": [
            (
                "Candle 1: Long bullish candle in an uptrend. Buyers "
                "control price with a substantial close above the open. "
                "Establishes the first step of the ascending sequence."
            ),
            (
                "Candle 2: Long bullish candle that opens within or near "
                "C1's body and closes above C1's high. Sustained buying "
                "pushes price higher in a stair-step fashion."
            ),
            (
                "Candle 3: Long bullish candle that opens within or near "
                "C2's body and closes above C2's high. Three consecutive "
                "bullish candles resemble Three White Soldiers, creating "
                "maximum bullish complacency."
            ),
            (
                "Candle 4: Large bearish candle that opens at or above "
                "C3's close and sells off sharply, closing below C1's "
                "open. This single candle engulfs the entire range of "
                "the prior three bullish candles — a dramatic reversal."
            ),
        ],
        "market_psychology": (
            "C1-C3 represent a persistent rally that creates bullish "
            "complacency and draws in late buyers. C4 is a shock reversal "
            "— a massive bearish candle that wipes out three sessions of "
            "gains in a single candle. This traps all the longs from "
            "C1-C3, triggers margin calls and stop-losses, and shifts "
            "the market's psychological state from greed to fear."
        ),
        "confirmation_required": (
            "C4 must close below C1's open to fully engulf all three "
            "bullish candles. A fifth bearish candle confirms the reversal. "
            "Without confirmation, the pattern may be a one-day shakeout "
            "rather than a genuine top."
        ),
        "volume_confirmation": (
            "Volume should be moderate during C1-C3 and spike dramatically "
            "on C4. High C4 volume confirms institutional distribution "
            "and panic selling. Weak C4 volume suggests a possible "
            "false reversal."
        ),
        "volatility_conditions": (
            "Most reliable after a steady rally with gradually declining "
            "volatility, where C4 represents a volatility expansion in "
            "the bearish direction. Works in various volatility environments."
        ),
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
            "Strong bullish fundamental catalyst overrides the signal",
        ],
        "entry_rules": (
            "Enter short on C4's close or on break below C4's low. "
            "Conservative: wait for fifth candle to confirm the reversal. "
            "Set initial position size smaller given moderate reliability."
        ),
        "stop_loss_rules": (
            "Above C3's high (the highest point of the pattern) or above "
            "C4's high if C4 opened above C3's close."
        ),
        "take_profit_rules": (
            "Measure the total height of C1-C3 advance and project "
            "downward from C4's close. Target the pre-rally swing low. "
            "Use trailing stop as selling may intensify."
        ),
        "risk_reward": "1:2",
        "best_timeframes": ["Daily", "4H", "1H"],
        "best_markets": ["Stocks", "Futures", "Forex", "Indices"],
        "best_indicators": [
            "RSI (overbought before C4, divergence on C3)",
            "Volume (spike on C4)",
            "MACD (bearish crossover near C4)",
            "Moving Averages (proximity to major MA resistance)",
            "Fibonacci extension (C3 high near key level)",
        ],
        "common_mistakes": [
            "Not requiring full engulfment of all three bullish candles",
            "Ignoring that C4 must close below C1's open",
            "Treating C1-C3 as any three bullish candles (they should be stair-stepped)",
            "Not waiting for fifth candle confirmation",
            "Confusing with bullish continuation in a strong uptrend",
        ],
        "ai_features": [
            "c1.is_bullish AND c1.body_ratio > 0.50",
            "c2.is_bullish AND c2.close > c1.close",
            "c3.is_bullish AND c3.close > c2.close",
            "c4.is_bearish AND c4.open >= c3.close AND c4.close <= c1.open",
            "c4.body_size > (c1.body_size + c2.body_size + c3.body_size) * 0.8",
        ],
        "ohlc_relationship": (
            "C1: bullish; C2: bullish, C2_close > C1_close; C3: bullish, "
            "C3_close > C2_close; C4: bearish, C4_open >= C3_close, "
            "C4_close <= C1_open (engulfs all three)"
        ),
        "label": "Bearish",
        "confidence_score": 63,
        "probability_score": 61,
    },

    # ──────────────────────────────────────────────────────────────
    # Pattern 8: Ladder Bottom
    # ──────────────────────────────────────────────────────────────
    {
        "id": 7,
        "pattern_name": "Ladder Bottom",
        "alternative_names": ["Ladder Bottom Reversal", "Bullish Ladder Bottom"],
        "japanese_name": "Hashigo Gaeshi",
        "category": "Five Candle",
        "sub_category": "Bullish Reversal",
        "sentiment": "Bullish",
        "expected_direction": "UP",
        "trend_required": "Downtrend",
        "num_candles": 5,
        "pattern_structure": (
            "Three long bearish candles descending stair-step fashion "
            "(C1-C3), C4 is bearish with a prominent upper shadow showing "
            "hesitation, C5 is bullish and opens above C4's body, gapping "
            "up."
        ),
        "candle_by_candle": [
            (
                "Candle 1: Long bearish candle in a downtrend. Opens near "
                "the high and closes near the low, establishing the "
                "descending ladder. Strong, committed selling."
            ),
            (
                "Candle 2: Long bearish candle that opens within C1's body "
                "and closes below C1's low. Another step down in the "
                "descending ladder. Sellers remain in firm control."
            ),
            (
                "Candle 3: Long bearish candle that opens within C2's body "
                "and closes below C2's low. The third descending step. "
                "The sequence resembles Three Black Crows."
            ),
            (
                "Candle 4: Bearish candle with a notably long upper shadow "
                "(wick). While it still closes lower, the long upper shadow "
                "reveals that buyers attempted to push prices higher during "
                "the session — the first sign of buying interest. This is "
                "the key hesitation candle."
            ),
            (
                "Candle 5: Bullish candle that opens above C4's real body, "
                "gapping up. It closes well above C4's close, confirming "
                "the reversal. The gap up signals that overnight sentiment "
                "has shifted from bearish to bullish."
            ),
        ],
        "market_psychology": (
            "C1-C3 represent relentless, stair-step selling that creates "
            "deep bearish sentiment. C4's long upper shadow is the critical "
            "clue — within the session, buyers tried to push higher, even "
            "though the close was still bearish. This intra-session "
            "rejection of lower prices signals that the selling is "
            "exhausting. C5's gap up confirms the transition as overnight "
            "positioning shifts bullish and trapped shorts begin covering."
        ),
        "confirmation_required": (
            "C5 must gap up and close bullish above C4's body. A sixth "
            "candle closing higher provides strong confirmation. Volume "
            "should increase on C5."
        ),
        "volume_confirmation": (
            "Volume should be moderate to declining during C1-C3 descent. "
            "C4 may show mixed volume as buying attempts emerge. C5 "
            "should have increased volume confirming the bullish shift. "
            "A volume climax on C3 or C4 adds to the pattern's significance."
        ),
        "volatility_conditions": (
            "Works best when the downtrend shows signs of volatility "
            "expansion on C4 (long shadow). C5's gap is most meaningful "
            "in markets that normally exhibit gaps (stocks, futures)."
        ),
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
            "Major bearish news invalidates the technical setup",
        ],
        "entry_rules": (
            "Enter long on C5's close or on break above C5's high. "
            "Conservative: wait for sixth candle confirmation above C5's "
            "close. Ensure C4 has a genuine upper shadow (at least 40% "
            "of candle range)."
        ),
        "stop_loss_rules": (
            "Below C4's low or C3's low for a wider stop. The lowest "
            "point of the pattern represents the invalidation level."
        ),
        "take_profit_rules": (
            "Measure the total decline from C1's open to C3's close and "
            "project 50-100% of that distance upward from C5's close. "
            "Target C1's open area or prior swing high."
        ),
        "risk_reward": "1:2.5",
        "best_timeframes": ["Daily", "Weekly"],
        "best_markets": ["Stocks", "Futures", "Indices", "Commodities"],
        "best_indicators": [
            "RSI (oversold divergence on C4-C5)",
            "Volume (climax and shift pattern)",
            "MACD (bullish histogram divergence)",
            "Stochastic (oversold crossover)",
            "Support levels (C3-C4 low near key support)",
        ],
        "common_mistakes": [
            "Ignoring C4's upper shadow requirement (critical element)",
            "Not requiring C5 to gap up above C4's body",
            "Confusing with simple Three Black Crows",
            "Trading before C5 confirms the reversal",
            "Not verifying C1-C3 are progressively lower",
            "Trading in markets that rarely gap (C5 gap less meaningful)",
        ],
        "ai_features": [
            "c1.is_bearish AND c1.body_ratio > 0.55",
            "c2.is_bearish AND c2.close < c1.close AND c2.body_ratio > 0.50",
            "c3.is_bearish AND c3.close < c2.close AND c3.body_ratio > 0.50",
            "c4.is_bearish AND c4.upper_shadow_ratio > 0.40",
            "c5.is_bullish AND c5.open > c4.close AND c5.close > c4.open",
        ],
        "ohlc_relationship": (
            "C1: bearish, body_ratio > 0.55; C2: bearish, C2_close < "
            "C1_close; C3: bearish, C3_close < C2_close; C4: bearish, "
            "upper_shadow_ratio > 0.40; C5: bullish, C5_open > "
            "max(C4_open, C4_close), gap up"
        ),
        "label": "Bullish",
        "confidence_score": 63,
        "probability_score": 62,
    },

    # ──────────────────────────────────────────────────────────────
    # Pattern 9: Ladder Top
    # ──────────────────────────────────────────────────────────────
    {
        "id": 8,
        "pattern_name": "Ladder Top",
        "alternative_names": ["Ladder Top Reversal", "Bearish Ladder Top"],
        "japanese_name": "Hashigo Tenjo",
        "category": "Five Candle",
        "sub_category": "Bearish Reversal",
        "sentiment": "Bearish",
        "expected_direction": "DOWN",
        "trend_required": "Uptrend",
        "num_candles": 5,
        "pattern_structure": (
            "Three long bullish candles ascending stair-step fashion "
            "(C1-C3), C4 is bullish with a prominent lower shadow showing "
            "hesitation, C5 is bearish and opens below C4's body, gapping "
            "down."
        ),
        "candle_by_candle": [
            (
                "Candle 1: Long bullish candle in an uptrend. Opens near "
                "the low and closes near the high, establishing the first "
                "rung of the ascending ladder. Strong, committed buying."
            ),
            (
                "Candle 2: Long bullish candle that opens within C1's body "
                "and closes above C1's high. Another step up in the "
                "ascending ladder. Buyers remain in firm control."
            ),
            (
                "Candle 3: Long bullish candle that opens within C2's body "
                "and closes above C2's high. The third ascending step. "
                "The sequence resembles Three White Soldiers."
            ),
            (
                "Candle 4: Bullish candle with a notably long lower shadow "
                "(wick). While it still closes higher, the long lower "
                "shadow reveals that sellers pushed prices down significantly "
                "during the session before buyers recovered — the first sign "
                "of selling pressure. This is the key hesitation candle."
            ),
            (
                "Candle 5: Bearish candle that opens below C4's real body, "
                "gapping down. It closes well below C4's close, confirming "
                "the reversal. The gap down signals that overnight sentiment "
                "has shifted from bullish to bearish."
            ),
        ],
        "market_psychology": (
            "C1-C3 represent persistent, stair-step buying that builds "
            "bullish confidence and complacency. C4's long lower shadow is "
            "the critical warning — within the session, sellers made a "
            "meaningful push lower, even though the close recovered. This "
            "intra-session test of lower prices signals that the rally is "
            "becoming fragile. C5's gap down confirms the transition as "
            "overnight positioning shifts bearish and trapped longs begin "
            "liquidating."
        ),
        "confirmation_required": (
            "C5 must gap down and close bearish below C4's body. A sixth "
            "candle closing lower provides strong confirmation. Volume "
            "should increase on C5."
        ),
        "volume_confirmation": (
            "Volume should be moderate to declining during C1-C3 advance. "
            "C4 may show mixed volume as selling attempts emerge. C5 "
            "should have increased volume confirming the bearish shift. "
            "A volume climax on C4 or C5 strengthens the signal."
        ),
        "volatility_conditions": (
            "Works best when the uptrend shows signs of volatility "
            "expansion on C4 (long lower shadow). C5's gap down is most "
            "meaningful in markets that normally exhibit gaps (stocks, "
            "futures)."
        ),
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
            "Major bullish catalyst invalidates the technical setup",
        ],
        "entry_rules": (
            "Enter short on C5's close or on break below C5's low. "
            "Conservative: wait for sixth candle confirmation below C5's "
            "close. Ensure C4 has a genuine lower shadow (at least 40% "
            "of candle range)."
        ),
        "stop_loss_rules": (
            "Above C4's high or C3's high for a wider stop. The highest "
            "point of the pattern represents the invalidation level."
        ),
        "take_profit_rules": (
            "Measure the total advance from C1's open to C3's close and "
            "project 50-100% of that distance downward from C5's close. "
            "Target C1's open area or prior swing low."
        ),
        "risk_reward": "1:2.5",
        "best_timeframes": ["Daily", "Weekly"],
        "best_markets": ["Stocks", "Futures", "Indices", "Commodities"],
        "best_indicators": [
            "RSI (overbought divergence on C4-C5)",
            "Volume (climax and shift pattern)",
            "MACD (bearish histogram divergence)",
            "Stochastic (overbought crossover)",
            "Resistance levels (C3-C4 high near key resistance)",
        ],
        "common_mistakes": [
            "Ignoring C4's lower shadow requirement (critical element)",
            "Not requiring C5 to gap down below C4's body",
            "Confusing with simple Three White Soldiers",
            "Trading before C5 confirms the reversal",
            "Not verifying C1-C3 are progressively higher",
            "Trading in markets that rarely gap (C5 gap less meaningful)",
        ],
        "ai_features": [
            "c1.is_bullish AND c1.body_ratio > 0.55",
            "c2.is_bullish AND c2.close > c1.close AND c2.body_ratio > 0.50",
            "c3.is_bullish AND c3.close > c2.close AND c3.body_ratio > 0.50",
            "c4.is_bullish AND c4.lower_shadow_ratio > 0.40",
            "c5.is_bearish AND c5.open < c4.close AND c5.close < c4.open",
        ],
        "ohlc_relationship": (
            "C1: bullish, body_ratio > 0.55; C2: bullish, C2_close > "
            "C1_close; C3: bullish, C3_close > C2_close; C4: bullish, "
            "lower_shadow_ratio > 0.40; C5: bearish, C5_open < "
            "min(C4_open, C4_close), gap down"
        ),
        "label": "Bearish",
        "confidence_score": 61,
        "probability_score": 60,
    },
]
