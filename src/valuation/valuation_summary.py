import pandas as pd
class ValuationSummary:
    def __init__(
        self,
        enterprise_value,
        equity_value,
        target_price,
        current_price
    ):

        self.ev = enterprise_value
        self.eq = equity_value
        self.target = target_price
        self.current = current_price

    def upside(self):

        return (self.target - self.current) / self.current

    def recommendation(self):

        if self.upside() > 0.15:
            return "BUY"
        elif self.upside() > -0.1:
            return "HOLD"
        else:
            return "SELL"

    def report(self):

        data = {
            "Enterprise Value": self.ev,
            "Equity Value": self.eq,
            "Target Price": self.target,
            "Current Price": self.current,
            "Upside %": self.upside(),
            "Recommendation": self.recommendation()
        }

        return pd.DataFrame(data, index=[0])
