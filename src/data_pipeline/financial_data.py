import pandas as pd
class FinancialData:
    def __init__(self, income_statement: pd.DataFrame,
                 balance_sheet: pd.DataFrame,
                 cashflow_statement: pd.DataFrame):

        self.income = income_statement
        self.balance = balance_sheet
        self.cashflow = cashflow_statement

    def revenue(self):

        return self.income["Revenue"]

    def ebit(self):

        return self.income["EBIT"]

    def net_income(self):

        return self.income["NetIncome"]

    def total_debt(self):

        return self.balance["TotalDebt"]

    def cash(self):

        return self.balance["Cash"]

    def capex(self):

        return self.cashflow["CapEx"]

    def depreciation(self):

        return self.cashflow["Depreciation"]

    def working_capital(self):

        return self.balance["WorkingCapital"]

    def summary(self):

        return {
            "Revenue": self.revenue().iloc[-1],
            "EBIT": self.ebit().iloc[-1],
            "Net Income": self.net_income().iloc[-1],
            "Total Debt": self.total_debt().iloc[-1],
            "Cash": self.cash().iloc[-1]
        }
