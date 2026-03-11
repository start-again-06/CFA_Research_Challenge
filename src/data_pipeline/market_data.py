import yfinance as yf
import pandas as pd

class MarketData:

    def __init__(self, ticker: str):

        self.ticker = ticker

    def get_current_price(self):

        data = yf.download(self.ticker, period="1d")

        return data["Close"].iloc[-1]

    def get_historical_prices(self, period="5y"):

        return yf.download(self.ticker, period=period)

    def get_returns(self, period="5y"):

        prices = self.get_historical_prices(period)

        returns = prices["Close"].pct_change().dropna()

        return returns

    def get_beta(self, market_ticker="^GSPC"):

        stock = yf.download(self.ticker, period="5y")["Close"].pct_change()
        market = yf.download(market_ticker, period="5y")["Close"].pct_change()

        df = pd.concat([stock, market], axis=1).dropna()
        df.columns = ["stock", "market"]

        covariance = df.cov().iloc[0, 1]
        market_variance = df["market"].var()

        beta = covariance / market_variance

        return beta
