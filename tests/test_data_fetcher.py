import pytest
from data.data_fetcher import fetch_historical_data

def test_fetch_historical_data():
    # Test fetching historical data for a valid stock symbol
    data = fetch_historical_data("GOOG", "2023-01-01", "2023-01-31")
    assert data is not None, "Data should not be None"
    assert not data.empty, "Data should not be empty"
    assert "Close" in data.columns, "Data should contain a 'Close' column"

    # Test fetching data for an invalid stock symbol
    invalid_data = fetch_historical_data("INVALID", "2023-01-01", "2023-01-31")
    assert invalid_data is None, "Invalid stock symbol should return None"
