class DepreciationModel:
    
    def __init__(self, depreciation_ratio):

        self.depreciation_ratio = depreciation_ratio

    def compute(self, revenue):

        return revenue * self.depreciation_ratio

    def series(self, revenue_projection):

        return [self.compute(r) for r in revenue_projection]
