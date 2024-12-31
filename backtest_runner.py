from data.data_fetcher import fetch_historical_data
from data.indicators import calculate_rsi, calculate_macd
from strategy.backtester import run_backtest
from utils.visualizer import plot_stock_with_trades
from trading.live_trading import LiveTrading

# Initialize Robinhood Live Trading
robinhood_trader = LiveTrading()

def run_backtest_on_symbol(symbol, start_date, end_date, initial_balance=10000):
    """
    Runs a backtest on a given symbol, visualizes results, and displays key metrics.

    :param symbol: Stock ticker symbol
    :param start_date: Start date for historical data (YYYY-MM-DD)
    :param end_date: End date for historical data (YYYY-MM-DD)
    :param initial_balance: Starting balance for the backtest
    """
    print(f"Fetching data for {symbol}...")
    data = fetch_historical_data(symbol, start_date, end_date)

    if data.empty:
        print(f"No data fetched for {symbol}. Please check the ticker or date range.")
        return

    print("Data preview:")
    print(data.head())  # Verify structure of fetched data

    # Add RSI and MACD indicators
    data = calculate_rsi(data)
    data = calculate_macd(data)

    print("Running backtest...")
    results = run_backtest(data, initial_balance=initial_balance)

    # Display backtest results
    print("\n=== Backtest Results ===")
    print(f"Initial Balance: ${results['initial_balance']:.2f}")
    print(f"Final Balance: ${results['final_balance']:.2f}")
    print(f"Total Return: {results['total_return']:.2f}%")
    print(f"Win Rate: {results['win_rate']:.2f}%")
    print(f"Max Drawdown: {results['max_drawdown']:.2f}%")
    print(f"Number of Trades: {len(results['trade_log'])}")

    # Generate visualizations
    plot_stock_with_trades(data, results['trade_log'], symbol)

def execute_live_trades(symbol, strategy):
    """
    Executes live trades based on a strategy.

    :param symbol: Stock ticker symbol
    :param strategy: Trading strategy logic
    """
    print(f"Fetching live data for {symbol}...")
    live_data = robinhood_trader.get_historical_data(symbol, interval="day", span="week")

    # Example: Print live data preview
    print(f"Live Data for {symbol}:")
    print(live_data)

    # Execute trades based on strategy
    if strategy(live_data):
        print("Placing buy order...")
        order = robinhood_trader.place_order(symbol=symbol, quantity=1, side="buy")
        print(f"Order placed: {order}")
    else:
        print("No trade signal.")

if __name__ == "__main__":
    # Uncomment to run backtest
    run_backtest_on_symbol(
        symbol="GOOG",
        start_date="2023-01-01",
        end_date="2023-12-31",
        initial_balance=10000,
    )

    # Uncomment to run live trading
    # def simple_strategy(data):
    #     last_close = float(data[-1]["close_price"])
    #     return last_close < 100

    # execute_live_trades("AAPL", simple_strategy)
