import pytest
from trading.paper_trading import PaperTrading

@pytest.fixture
def paper_trading():
    return PaperTrading(initial_balance=10000)

def test_buy(paper_trading):
    assert paper_trading.buy('AAPL', 10, 100), "Buy should succeed"
    assert paper_trading.get_balance() == 9000, "Balance should update correctly after buy"
    positions = paper_trading.get_positions()
    assert 'AAPL' in positions, "Position should be added"
    assert positions['AAPL']['quantity'] == 10, "Quantity should be updated correctly"
    assert positions['AAPL']['average_price'] == 100, "Average price should be updated correctly"

def test_sell(paper_trading):
    paper_trading.buy('AAPL', 10, 100)
    assert paper_trading.sell('AAPL', 5, 150), "Sell should succeed"
    assert paper_trading.get_balance() == 9750, "Balance should update correctly after sell"
    positions = paper_trading.get_positions()
    assert positions['AAPL']['quantity'] == 5, "Quantity should update correctly after sell"

def test_insufficient_balance(paper_trading):
    assert not paper_trading.buy('AAPL', 200, 100), "Buy should fail due to insufficient balance"
    assert paper_trading.get_balance() == 10000, "Balance should remain unchanged"

def test_insufficient_shares(paper_trading):
    paper_trading.buy('AAPL', 10, 100)
    assert not paper_trading.sell('AAPL', 15, 150), "Sell should fail due to insufficient shares"
    assert paper_trading.get_balance() == 9000, "Balance should remain unchanged after failed sell"
