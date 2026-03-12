class CapexModel:
    
    def __init__(self, capex_ratio):

        self.capex_ratio = capex_ratio

    def compute(self, revenue):

        return revenue * self.capex_ratio

    def series(self, revenue_projection):

        return [self.compute(r) for r in revenue_projection]
