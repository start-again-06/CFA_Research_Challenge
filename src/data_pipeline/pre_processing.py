import pandas as pd
import numpy as np
class DataPreprocessor:

    @staticmethod
    def remove_missing(df: pd.DataFrame):

        return df.dropna()

    @staticmethod
    def normalize(series: pd.Series):

        return (series - series.mean()) / series.std()

    @staticmethod
    def log_returns(price_series: pd.Series):

        return np.log(price_series / price_series.shift(1)).dropna()

    @staticmethod
    def rolling_volatility(returns: pd.Series, window=30):

        return returns.rolling(window).std() * np.sqrt(252)

    @staticmethod
    def moving_average(series: pd.Series, window=50):

        return series.rolling(window).mean()

    @staticmethod
    def detect_outliers(series: pd.Series):

        z_scores = (series - series.mean()) / series.std()

        return series[abs(z_scores) > 3]
