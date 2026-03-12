import pandas as pd
import statsmodels.api as sm
class FactorModel:
    

    def __init__(self, asset_returns, factor_data):

        self.asset_returns = asset_returns
        self.factor_data = factor_data

    def run_regression(self):

        df = pd.concat([self.asset_returns, self.factor_data], axis=1).dropna()

        y = df.iloc[:, 0]
        X = df.iloc[:, 1:]

        X = sm.add_constant(X)

        model = sm.OLS(y, X).fit()

        return model.summary()

    def factor_exposures(self):

        df = pd.concat([self.asset_returns, self.factor_data], axis=1).dropna()

        y = df.iloc[:, 0]
        X = df.iloc[:, 1:]

        X = sm.add_constant(X)

        model = sm.OLS(y, X).fit()

        return model.params
