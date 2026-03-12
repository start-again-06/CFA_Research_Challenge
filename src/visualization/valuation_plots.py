import matplotlib.pyplot as plt


class ValuationPlots:

    def dcf_components(self, fcff, terminal_value):

        labels = [f"Year {i+1}" for i in range(len(fcff))] + ["Terminal"]

        values = fcff + [terminal_value]

        plt.figure(figsize=(8,5))

        plt.bar(labels, values)

        plt.title("DCF Valuation Components")

        plt.ylabel("Value")

        plt.show()
