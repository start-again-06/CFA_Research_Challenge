import pandas as pd
class RevenueForecast:
   
    def __init__(self, base_revenue: float, growth_rates: list):

        self.base_revenue = base_revenue
        self.growth_rates = growth_rates

    def forecast(self):

        revenue = []
        current = self.base_revenue

        for g in self.growth_rates:

            current = current * (1 + g)
            revenue.append(current)

        return revenue

    def forecast_dataframe(self):

        rev = self.forecast()

        df = pd.DataFrame({
            "Year": range(1, len(rev) + 1),
            "Revenue": rev
        })

        return df
