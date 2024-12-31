import robin_stocks.robinhood as r
import os

class LiveTrading:
    """
    A class to handle live trading using the Robinhood API.
    """

    def __init__(self, username=None, password=None):
        """
        Initializes the Robinhood API client.

        :param username: Robinhood username (email)
        :param password: Robinhood password
        """
        #self.username = username or os.getenv("ROBINHOOD_USERNAME")
        #self.password = password or os.getenv("ROBINHOOD_PASSWORD")
        
        #FUCKIT, WE'LL DO IT LIVE!
        self.username = "derrick.cullen1@gmail.com"
        self.password = "3plus3RatRace33!!"
        
        if not self.username or not self.password:
            raise ValueError("Robinhood username and password must be provided.")
        self.login()

    def login(self):
        """
        Logs in to the Robinhood API.
        """
        try:
            r.login(username=self.username, password=self.password)
            print("Successfully logged in to Robinhood.")
        except Exception as e:
            print(f"Login failed: {e}")
            raise

    def get_account_info(self):
        """
        Retrieves account details.

        :return: Account information as a dictionary
        """
        return r.profiles.load_account_profile()

    def get_positions(self):
        """
        Retrieves all open positions.

        :return: List of open positions
        """
        return r.account.build_holdings()

    def place_order(self, symbol, quantity, side, order_type="market", time_in_force="gtc"):
        """
        Places an order.

        :param symbol: Stock ticker symbol
        :param quantity: Number of shares
        :param side: "buy" or "sell"
        :param order_type: "market" (default) or "limit"
        :param time_in_force: "gtc" (good till canceled) or "day"
        :return: Order confirmation
        """
        if side == "buy":
            return r.orders.order_buy_market(symbol, quantity, time_in_force)
        elif side == "sell":
            return r.orders.order_sell_market(symbol, quantity, time_in_force)
        else:
            raise ValueError("Side must be 'buy' or 'sell'.")

    def get_historical_data(self, symbol, interval="day", span="week"):
        """
        Retrieves historical data for a stock.

        :param symbol: Stock ticker symbol
        :param interval: Data interval ("5minute", "10minute", "day", etc.)
        :param span: Time span ("day", "week", "month", etc.)
        :return: Historical data as a list of dictionaries
        """
        return r.stocks.get_stock_historicals(symbol, interval=interval, span=span)
