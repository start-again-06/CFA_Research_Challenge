class WorkingCapitalModel:
   
    def __init__(self, wc_ratio):

        self.wc_ratio = wc_ratio

    def compute_wc(self, revenue):

        return revenue * self.wc_ratio

    def wc_series(self, revenue_projection):

        return [self.compute_wc(r) for r in revenue_projection]

    def change_in_wc(self, wc_projection):

        changes = [0]

        for i in range(1, len(wc_projection)):
            changes.append(wc_projection[i] - wc_projection[i-1])

        return changes
