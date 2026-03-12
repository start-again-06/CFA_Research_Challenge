import numpy as np
import pandas as pd
from scipy.optimize import minimize


class PortfolioOptimizer:
  

    def __init__(self, returns):

        self.returns = returns

    def portfolio_return(self, weights):

        return np.sum(self.returns.mean() * weights) * 252

    def portfolio_volatility(self, weights):

        cov = self.returns.cov() * 252

        return np.sqrt(np.dot(weights.T, np.dot(cov, weights)))

    def optimize(self):

        num_assets = self.returns.shape[1]

        init_weights = np.ones(num_assets) / num_assets

        bounds = tuple((0,1) for _ in range(num_assets))

        constraints = {
            "type": "eq",
            "fun": lambda w: np.sum(w) - 1
        }

        result = minimize(
            self.portfolio_volatility,
            init_weights,
            bounds=bounds,
            constraints=constraints
        )

        return result.x
