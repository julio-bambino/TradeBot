import matplotlib.pyplot as plt

def plot_stock_with_trades(data, trade_log, symbol):
    """
    Plots stock prices with buy/sell markers.

    :param data: DataFrame containing stock data with a 'Close' column
    :param trade_log: List of executed trades (buy/sell with dates and prices)
    :param symbol: Stock ticker symbol
    """
    plt.figure(figsize=(12, 6))
    plt.plot(data.index, data['Close'], label=f'{symbol} Close Price', linewidth=1)

    # Add buy/sell markers
    for trade in trade_log:
        if trade['type'] == 'buy':
            plt.scatter(trade['date'], trade['price'], color='green', marker='^', label='Buy', zorder=5)
        elif trade['type'] == 'sell':
            plt.scatter(trade['date'], trade['price'], color='red', marker='v', label='Sell', zorder=5)

    # Avoid duplicate labels in legend
    handles, labels = plt.gca().get_legend_handles_labels()
    by_label = dict(zip(labels, handles))
    plt.legend(by_label.values(), by_label.keys())

    plt.title(f"{symbol} Stock Price with Trades")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.grid()
    plt.show()
