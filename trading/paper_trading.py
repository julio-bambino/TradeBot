class PaperTrading:
    """
    A class to simulate paper trading for backtesting purposes.
    """

    def __init__(self, initial_balance=10000):
        self.balance = initial_balance
        self.positions = []  # List to track open positions
        self.trade_log = []  # List to log executed trades

    def buy(self, symbol, quantity, price):
        """
        Executes a buy order.

        :param symbol: Stock ticker symbol
        :param quantity: Number of shares to buy
        :param price: Price per share
        """
        cost = quantity * price
        if cost > self.balance:
            raise ValueError("Insufficient balance to execute buy order.")
        self.balance -= cost
        self.positions.append({'symbol': symbol, 'quantity': quantity, 'price': price})
        print(f"BUY: {symbol} | Quantity: {quantity} | Price: {price} | Remaining Balance: {self.balance}")

    def sell(self, symbol, quantity, price):
        """
        Executes a sell order.

        :param symbol: Stock ticker symbol
        :param quantity: Number of shares to sell
        :param price: Price per share
        """
        for position in self.positions:
            if position['symbol'] == symbol and position['quantity'] >= quantity:
                self.positions.remove(position)
                revenue = quantity * price
                self.balance += revenue
                print(f"SELL: {symbol} | Quantity: {quantity} | Price: {price} | New Balance: {self.balance}")
                return

        raise ValueError("No matching position to execute sell order.")

    def is_in_position(self):
        """
        Checks if the portfolio holds any open positions.

        :return: True if there are open positions, False otherwise
        """
        return len(self.positions) > 0

    def get_balance(self):
        """
        Retrieves the current balance.

        :return: Current portfolio balance
        """
        return self.balance

    def append_trade_log(self, trade):
        """
        Appends a trade to the trade log.

        :param trade: A dictionary representing a trade
        """
        self.trade_log.append(trade)

    def get_trade_log(self):
        """
        Retrieves the trade log.

        :return: List of executed trades
        """
        return self.trade_log

