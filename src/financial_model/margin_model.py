class MarginModel:
   
    def __init__(self, ebit_margin: float):

        self.ebit_margin = ebit_margin

    def ebit(self, revenue):

        return revenue * self.ebit_margin

    def ebit_series(self, revenue_projection):

        return [self.ebit(r) for r in revenue_projection]
