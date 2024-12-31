# This shit fuckin sucks
# Asshat datastructures getting imported as globs of shit!
# Fuck you yfinance and your library of shit

import yfinance as yf
import pandas as pd

def fetch_historical_data(symbol, start_date, end_date):
    """
    Fetches historical stock data using yfinance.

    :param symbol: Stock ticker symbol
    :param start_date: Start date for historical data (YYYY-MM-DD)
    :param end_date: End date for historical data (YYYY-MM-DD)
    :return: A standardized DataFrame with columns ['Close', 'Open', 'High', 'Low', 'Volume']
    """
    try:
        # Fetch data from yfinance
        data = yf.download(symbol, start=start_date, end=end_date)

        # Flatten multi-indexed columns
        if isinstance(data.columns, pd.MultiIndex):
            data.columns = data.columns.get_level_values(0)  # Use the first level (e.g., 'Close', 'High')

        # Ensure column names are consistent
        expected_columns = ['Close', 'Open', 'High', 'Low', 'Volume']
        if not set(expected_columns).issubset(data.columns):
            raise ValueError(f"Data is missing expected columns: {set(expected_columns) - set(data.columns)}")

        return data
    except Exception as e:
        print(f"Error fetching data for {symbol}: {e}")
        return pd.DataFrame()  # Return an empty DataFrame on failure
