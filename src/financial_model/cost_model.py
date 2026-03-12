class CostModel:
    
    def __init__(self, cost_ratio: float):

        self.cost_ratio = cost_ratio

    def compute_cost(self, revenue):

        return revenue * self.cost_ratio

    def compute_series(self, revenue_projection):

        return [self.compute_cost(r) for r in revenue_projection]
