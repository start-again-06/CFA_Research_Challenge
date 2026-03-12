import matplotlib.pyplot as plt


class RiskPlots:

    def monte_carlo_distribution(self, valuations):

        plt.figure(figsize=(8,5))

        plt.hist(valuations, bins=50)

        plt.title("Monte Carlo Valuation Distribution")

        plt.xlabel("Valuation")

        plt.ylabel("Frequency")

        plt.show()
