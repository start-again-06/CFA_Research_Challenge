class EquityValue:
    def __init__(self, enterprise_value, debt, cash, shares_outstanding):

        self.ev = enterprise_value
        self.debt = debt
        self.cash = cash
        self.shares = shares_outstanding

    def equity_value(self):

        return self.ev - self.debt + self.cash

    def target_price(self):

        eq = self.equity_value()

        return eq / self.shares
