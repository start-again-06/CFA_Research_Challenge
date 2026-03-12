import numpy as np
import pandas as pd
class SensitivityAnalysis:
    def __init__(self, fcff_projection):

        self.fcff = fcff_projection

    def compute_value(self, wacc, g):

        pv = 0

        for t, f in enumerate(self.fcff):

            pv += f / ((1 + wacc) ** (t + 1))

        terminal = (self.fcff[-1] * (1 + g)) / (wacc - g)

        pv_terminal = terminal / ((1 + wacc) ** len(self.fcff))

        return pv + pv_terminal

    def matrix(self, wacc_range, growth_range):

        table = pd.DataFrame(index=wacc_range, columns=growth_range)

        for w in wacc_range:

            for g in growth_range:

                table.loc[w, g] = self.compute_value(w, g)

        return table
