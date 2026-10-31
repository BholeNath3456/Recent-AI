import sys
sys.path.insert(0, '.')
from core.candle import Candle
from main import SignalEngine
import time

def test_run():
    engine = SignalEngine()
    
    # 5 synthetic candles (strong downtrend)
    candles = [
        Candle(time_start=0.0, open_=105.0, high=105.5, low=103.0, close_=103.5, volume=20, is_bullish=False, is_bearish=True, body=1.5, body_ratio=0.6, wick_rejection_pressure=0.0, reversal_probability=0.1, volatility=1.0),
        Candle(time_start=1.0, open_=103.5, high=104.0, low=102.0, close_=102.5, volume=18, is_bullish=False, is_bearish=True, body=1.0, body_ratio=0.5, wick_rejection_pressure=-0.1, reversal_probability=0.1, volatility=1.0),
        Candle(time_start=2.0, open_=102.5, high=103.0, low=101.0, close_=101.5, volume=15, is_bullish=False, is_bearish=True, body=1.0, body_ratio=0.5, wick_rejection_pressure=-0.1, reversal_probability=0.1, volatility=1.0),
        Candle(time_start=3.0, open_=101.5, high=102.0, low=99.0, close_=99.5, volume=12, is_bullish=False, is_bearish=True, body=2.0, body_ratio=0.7, wick_rejection_pressure=-0.1, reversal_probability=0.1, volatility=1.0),
        Candle(time_start=4.0, open_=99.5, high=100.0, low=97.0, close_=97.5, volume=10, is_bullish=False, is_bearish=True, body=2.0, body_ratio=0.7, wick_rejection_pressure=-0.1, reversal_probability=0.1, volatility=1.0)
    ]
    
    # Initialize atr_history for displacement check
    engine.volatility_engine.analyze(candles)
    
    # Call run_pipeline directly
    result, ctx = engine.run_pipeline(candles)
    print("Grade:", getattr(result.grade, 'value', result.grade))
    print("Conf:", result.confidence)
    print("Dir:", result.direction)
    print("Rejections:", result.rejection_reasons)
    print("Risk flags:", result.risk_flags)
    print("Entry factors:", result.entry_factors)
    print("Is Tradeable?", result.is_tradeable)

if __name__ == '__main__':
    test_run()
