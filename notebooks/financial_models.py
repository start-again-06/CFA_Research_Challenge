import pandas as pd
import numpy as np
from src.financial_model.revenue_model import RevenueForecast
from src.financial_model.margin_model import MarginModel
from src.financial_model.capex_model import CapexModel
current_revenue = 100000
growth_rates = [0.08,0.07,0.06,0.05,0.04]
ebit_margin = 0.22
capex_ratio = 0.05
rev_model = RevenueForecast(current_revenue, growth_rates)
revenue_projection = rev_model.forecast()
margin_model = MarginModel(ebit_margin)
ebit = [margin_model.ebit(r) for r in revenue_projection]
capex_model = CapexModel(capex_ratio)
capex = [capex_model.compute(r) for r in revenue_projection]


