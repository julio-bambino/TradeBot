import pandas as pd
from trading.paper_trading import PaperTrading
from trading.trade_executor import execute_trades

def run_backtest(data, initial_balance=10000):
    """
    Runs a backtest on the given historical data.

    :param data: DataFrame containing historical stock data with indicators (RSI, MACD, etc.)
    :param initial_balance: Starting balance for the backtest
    :return: Dictionary containing performance metrics and portfolio details
    """
    # Initialize paper trading portfolio
    portfolio = PaperTrading(initial_balance=initial_balance)

    # Execute trades based on indicators
    execute_trades(data, portfolio)

    # Calculate performance metrics
    trade_log = portfolio.get_trade_log()
    total_return = calculate_total_return(trade_log, initial_balance)
    win_rate = calculate_win_rate(trade_log)
    max_drawdown = calculate_max_drawdown(data['Close'])

    # Return backtest results
    return {
        'initial_balance': initial_balance,
        'final_balance': portfolio.get_balance(),
        'total_return': total_return,
        'win_rate': win_rate,
        'max_drawdown': max_drawdown,
        'trade_log': trade_log,
    }

def calculate_total_return(trade_log, initial_balance):
    """
    Calculates the total return from the trade log.

    :param trade_log: List of executed trades
    :param initial_balance: Starting balance for the backtest
    :return: Total return as a percentage
    """
    net_profit = sum(
        trade['quantity'] * (trade['price'] if trade['type'] == 'sell' else -trade['price'])
        for trade in trade_log
    )
    return (net_profit / initial_balance) * 100

def calculate_win_rate(trade_log):
    """
    Calculates the win rate from the trade log.

    :param trade_log: List of executed trades
    :return: Win rate as a percentage
    """
    wins = 0
    total_trades = 0

    for trade in trade_log:
        if trade['type'] == 'sell':
            total_trades += 1
            # A win is defined as selling at a higher price than the average buy price
            if trade['price'] > trade.get('average_price', 0):
                wins += 1

    return (wins / total_trades * 100) if total_trades > 0 else 0

def calculate_max_drawdown(prices):
    """
    Calculates the maximum drawdown from the price series.

    :param prices: Series of stock prices
    :return: Maximum drawdown as a percentage
    """
    cumulative_max = prices.cummax()
    drawdowns = (prices - cumulative_max) / cumulative_max
    return drawdowns.min() * 100
