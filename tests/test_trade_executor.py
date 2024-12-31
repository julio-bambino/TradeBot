import pytest
import pandas as pd
from data.indicators import calculate_rsi, calculate_macd
from trading.trade_executor import execute_trades
from trading.paper_trading import PaperTrading

@pytest.fixture
def sample_data():
    # Sample data for testing RSI and MACD signals
    data = pd.DataFrame({
        'Close': [10, 11, 12, 13, 12, 11, 10, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    })
    data = calculate_rsi(data, period=5)
    data = calculate_macd(data, short_period=3, long_period=6, signal_period=2)
    return data

def test_execute_trades(sample_data):
    portfolio = PaperTrading(initial_balance=10000)
    execute_trades(sample_data, portfolio)

    # Validate trade log
    trade_log = portfolio.get_trade_log()
    assert len(trade_log) > 0, "There should be trades executed"
    assert any(trade['type'] == 'buy' for trade in trade_log), "There should be at least one buy trade"
    assert any(trade['type'] == 'sell' for trade in trade_log), "There should be at least one sell trade"

    # Validate final balance
    initial_balance = 10000
    net_profit = sum(
        trade['quantity'] * (trade['price'] if trade['type'] == 'sell' else -trade['price'])
        for trade in trade_log
    )
    expected_balance = initial_balance + net_profit
    assert portfolio.get_balance() == expected_balance, (
        f"Final balance {portfolio.get_balance()} does not match expected balance {expected_balance}"
    )
