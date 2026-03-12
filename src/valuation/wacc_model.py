import numpy as np
class WACC:
   
    def __init__(
        self,
        risk_free_rate,
        beta,
        market_return,
        cost_of_debt,
        tax_rate,
        equity_value,
        debt_value
    ):

        self.rf = risk_free_rate
        self.beta = beta
        self.market_return = market_return
        self.cost_of_debt = cost_of_debt
        self.tax_rate = tax_rate
        self.E = equity_value
        self.D = debt_value

    def cost_of_equity(self):

        return self.rf + self.beta * (self.market_return - self.rf)

    def compute(self):

        ke = self.cost_of_equity()
        kd = self.cost_of_debt

        total = self.E + self.D

        wacc = (self.E / total) * ke + (self.D / total) * kd * (1 - self.tax_rate)

        return wacc
