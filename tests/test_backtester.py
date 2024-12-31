import pytest
import pandas as pd
from strategy.backtester import run_backtest

@pytest.fixture
def sample_data():
    # Generate sample data with calculated indicators
    data = pd.DataFrame({
        'Close': [10, 11, 12, 13, 12, 11, 10, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    })
    data['RSI'] = [50, 40, 30, 20, 30, 40, 50, 60, 70, 80, 50, 40, 30, 20, 30, 40, 50, 60, 70]
    data['MACD'] = [0, 0.5, 1, 0.8, 0.6, 0.4, 0.2, -0.1, 0, 0.5, 1, 1.2, 1.5, 1.4, 1.2, 1, 0.8, 0.6, 0.4]
    data['Signal_Line'] = [0, 0.4, 0.8, 0.7, 0.6, 0.5, 0.4, 0.2, 0, 0.3, 0.8, 1, 1.3, 1.4, 1.3, 1.1, 0.9, 0.7, 0.5]
    return data

def test_run_backtest(sample_data):
    results = run_backtest(sample_data, initial_balance=10000)

    # Validate backtest results
    assert results['initial_balance'] == 10000, "Initial balance should match"
    assert results['final_balance'] > 0, "Final balance should be positive"
    assert 0 <= results['total_return'] <= 100, "Total return should be within a reasonable range"
    assert 0 <= results['win_rate'] <= 100, "Win rate should be within 0-100%"
    assert results['max_drawdown'] <= 0, "Max drawdown should be negative or zero"
    assert len(results['trade_log']) > 0, "Trade log should not be empty"

