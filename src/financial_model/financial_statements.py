import pandas as pd
class FinancialStatements:

    def __init__(
        self,
        revenue,
        ebit,
        tax_rate,
        depreciation,
        capex,
        wc_change
    ):

        self.revenue = revenue
        self.ebit = ebit
        self.tax_rate = tax_rate
        self.depreciation = depreciation
        self.capex = capex
        self.wc_change = wc_change

    def nopat(self):

        return [e * (1 - self.tax_rate) for e in self.ebit]

    def fcff(self):

        nopat = self.nopat()

        fcff = []

        for i in range(len(nopat)):

            f = nopat[i] + self.depreciation[i] - self.capex[i] - self.wc_change[i]

            fcff.append(f)

        return fcff

    def financial_projection(self):

        nopat = self.nopat()
        fcff = self.fcff()

        df = pd.DataFrame({

            "Revenue": self.revenue,
            "EBIT": self.ebit,
            "NOPAT": nopat,
            "Depreciation": self.depreciation,
            "CapEx": self.capex,
            "Change_in_WC": self.wc_change,
            "FCFF": fcff
        })

        return df
