class ScenarioAnalysis:
    def __init__(self, base_fcff, wacc, growth_rates):

        self.fcff = base_fcff
        self.wacc = wacc
        self.growth_rates = growth_rates

    def compute_terminal(self, fcff, g):

        return (fcff * (1 + g)) / (self.wacc - g)

    def scenario_value(self, growth_rate):

        pv = 0

        for t, f in enumerate(self.fcff):

            pv += f / ((1 + self.wacc) ** (t + 1))

        terminal = self.compute_terminal(self.fcff[-1], growth_rate)

        pv_terminal = terminal / ((1 + self.wacc) ** len(self.fcff))

        return pv + pv_terminal

    def run(self):

        results = {}

        for name, g in self.growth_rates.items():

            results[name] = self.scenario_value(g)

        return results
