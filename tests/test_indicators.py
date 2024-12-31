import pytest
import pandas as pd
from data.indicators import calculate_rsi, calculate_macd

@pytest.fixture
def sample_data():
    return pd.DataFrame({'Close': [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]})


def test_calculate_rsi(sample_data):
    data = calculate_rsi(sample_data)
    assert 'RSI' in data.columns, "RSI column should be added"
    
    # Check that RSI contains valid (non-NaN) values after the rolling period
    valid_rsi = data['RSI'].dropna()
    assert not valid_rsi.empty, "RSI values should not be all NaN after the rolling period"
    assert valid_rsi.iloc[-1] > 0, "Last RSI value should be greater than 0"



def test_calculate_macd(sample_data):
    data = calculate_macd(sample_data)
    assert 'MACD' in data.columns, "MACD column should be added"
    assert 'Signal_Line' in data.columns, "Signal Line column should be added"
    assert not data['MACD'].isnull().all(), "MACD values should not be all NaN"
    assert not data['Signal_Line'].isnull().all(), "Signal Line values should not be all NaN"
