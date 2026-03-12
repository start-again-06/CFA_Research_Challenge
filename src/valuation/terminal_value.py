class TerminalValue:
    
    def __init__(self, final_fcff, wacc, growth_rate):

        self.fcff = final_fcff
        self.wacc = wacc
        self.g = growth_rate

    def compute(self):

        return (self.fcff * (1 + self.g)) / (self.wacc - self.g)
