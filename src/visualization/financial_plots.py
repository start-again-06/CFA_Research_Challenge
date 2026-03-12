import matplotlib.pyplot as plt
class FinancialPlots:

    def revenue_forecast(self, years, revenue):

        plt.figure(figsize=(8,5))
        plt.plot(years, revenue, marker="o")
        plt.title("Revenue Forecast")
        plt.xlabel("Year")
        plt.ylabel("Revenue")
        plt.grid(True)

        plt.show()


    def ebitda_margin(self, years, margins):

        plt.figure(figsize=(8,5))
        plt.plot(years, margins, marker="o")
        plt.title("EBITDA Margin Trend")
        plt.xlabel("Year")
        plt.ylabel("Margin (%)")
        plt.grid(True)

        plt.show()
