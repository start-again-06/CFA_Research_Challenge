class PeerSelection:
    def __init__(self, companies):

        self.companies = companies

    def select_by_industry(self, industry):

        return [c for c in self.companies if c["industry"] == industry]

    def select_by_market_cap(self, min_cap, max_cap):

        return [
            c for c in self.companies
            if min_cap <= c["market_cap"] <= max_cap
        ]
