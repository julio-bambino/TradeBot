import pandas as pd
from trading.paper_trading import PaperTrading

def execute_trades(data, portfolio):
    """
    Executes trades based on RSI and MACD signals.

    :param data: DataFrame containing historical data with 'Close', 'RSI', 'MACD', and 'Signal_Line' columns
    :param portfolio: Instance of PaperTrading to simulate trades
    """
    for i in range(1, len(data)):
        row = data.iloc[i]

        # Detect buy/sell signals (mock logic; replace with actual logic)
        if row['RSI'] < 30 and not portfolio.is_in_position():
            portfolio.buy(symbol="TEST", quantity=10, price=row['Close'])
            portfolio.append_trade_log({
                'date': row.name,
                'type': 'buy',
                'price': row['Close'],
                'quantity': 10
            })
        elif row['RSI'] > 70 and portfolio.is_in_position():
            portfolio.sell(symbol="TEST", quantity=10, price=row['Close'])
            portfolio.append_trade_log({
                'date': row.name,
                'type': 'sell',
                'price': row['Close'],
                'quantity': 10
            })