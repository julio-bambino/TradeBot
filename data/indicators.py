import pandas as pd

def calculate_rsi(data, period=14):
    """
    Calculates the Relative Strength Index (RSI).
    :param data: DataFrame containing at least a 'Close' column
    :param period: Number of periods to calculate RSI
    :return: DataFrame with an added 'RSI' column
    """
    delta = data['Close'].diff()

    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()

    rs = gain / loss
    data['RSI'] = 100 - (100 / (1 + rs))
    return data


def calculate_macd(data, short_period=12, long_period=26, signal_period=9):
    """
    Calculates the MACD and Signal Line.
    :param data: DataFrame containing at least a 'Close' column
    :param short_period: Period for the short-term EMA
    :param long_period: Period for the long-term EMA
    :param signal_period: Period for the Signal Line EMA
    :return: DataFrame with added 'MACD' and 'Signal_Line' columns
    """
    short_ema = data['Close'].ewm(span=short_period, adjust=False).mean()
    long_ema = data['Close'].ewm(span=long_period, adjust=False).mean()

    data['MACD'] = short_ema - long_ema
    data['Signal_Line'] = data['MACD'].ewm(span=signal_period, adjust=False).mean()
    return data
