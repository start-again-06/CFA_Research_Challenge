import numpy as np
import pandas as pd
class MultiplesAnalysis:
   
    def __init__(self, peer_multiples: pd.DataFrame):

        self.peers = peer_multiples

    def average_multiple(self, column):

        return self.peers[column].mean()

    def median_multiple(self, column):

        return self.peers[column].median()

    def target_price_pe(self, company_eps):

        avg_pe = self.average_multiple("PE")

        return company_eps * avg_pe

    def enterprise_value_ev_ebitda(self, company_ebitda):

        avg_multiple = self.average_multiple("EV_EBITDA")

        return company_ebitda * avg_multiple

    def enterprise_value_ev_sales(self, company_sales):

        avg_multiple = self.average_multiple("EV_Sales")

        return company_sales * avg_multiple

    def valuation_summary(self, eps, ebitda, sales):

        pe_val = self.target_price_pe(eps)
        ev_ebitda = self.enterprise_value_ev_ebitda(ebitda)
        ev_sales = self.enterprise_value_ev_sales(sales)

        summary = {

            "PE Valuation": pe_val,
            "EV/EBITDA Valuation": ev_ebitda,
            "EV/Sales Valuation": ev_sales
        }

        return summary
