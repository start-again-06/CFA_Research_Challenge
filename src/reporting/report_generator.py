import pandas as pd


class ReportGenerator:
    def __init__(self):

        self.sections = {}

    def add_company_overview(self, name, industry, description):

        self.sections["Company Overview"] = {
            "Name": name,
            "Industry": industry,
            "Description": description
        }

    def add_financial_summary(self, revenue, ebitda, net_income):

        self.sections["Financial Summary"] = {
            "Revenue Forecast": revenue,
            "EBITDA Forecast": ebitda,
            "Net Income Forecast": net_income
        }

    def add_dcf_valuation(self, enterprise_value, equity_value, price_target):

        self.sections["DCF Valuation"] = {
            "Enterprise Value": enterprise_value,
            "Equity Value": equity_value,
            "Target Price": price_target
        }

    def add_comparables(self, valuation_dict):

        self.sections["Comparable Valuation"] = valuation_dict

    def add_risk_analysis(self, scenario_results):

        self.sections["Risk Analysis"] = scenario_results

    def generate(self):

        return self.sections
