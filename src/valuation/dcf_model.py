import numpy as np
from .terminal_value import TerminalValue
class DCF:
    def __init__(self, fcff_projection, wacc, terminal_growth):

        self.fcff = fcff_projection
        self.wacc = wacc
        self.g = terminal_growth

    def discount_fcff(self):

        discounted = []

        for t, f in enumerate(self.fcff):

            pv = f / ((1 + self.wacc) ** (t + 1))

            discounted.append(pv)

        return discounted

    def enterprise_value(self):

        discounted_fcff = self.discount_fcff()

        terminal_model = TerminalValue(
            self.fcff[-1],
            self.wacc,
            self.g
        )

        terminal_value = terminal_model.compute()

        pv_terminal = terminal_value / ((1 + self.wacc) ** len(self.fcff))

        ev = sum(discounted_fcff) + pv_terminal

        return ev
