import numpy as np
class MonteCarloDCF:
    def __init__(self, base_fcff, wacc, growth_rate, volatility=0.1, simulations=10000):

        self.fcff = base_fcff
        self.wacc = wacc
        self.g = growth_rate
        self.vol = volatility
        self.simulations = simulations

    def run(self):

        valuations = []

        for _ in range(self.simulations):

            simulated_fcff = []

            for f in self.fcff:

                shock = np.random.normal(1, self.vol)
                simulated_fcff.append(f * shock)

            terminal_value = (
                simulated_fcff[-1] * (1 + self.g)
            ) / (self.wacc - self.g)

            pv = 0

            for t, f in enumerate(simulated_fcff):

                pv += f / ((1 + self.wacc) ** (t + 1))

            pv_terminal = terminal_value / ((1 + self.wacc) ** len(simulated_fcff))

            valuations.append(pv + pv_terminal)

        return valuations
