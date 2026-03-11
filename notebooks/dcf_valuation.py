from src.valuation.wacc_model import WACC
from src.valuation.dcf_model import DCF
wacc_model = WACC(
    rf=0.04,
    beta=1.2,
    market_return=0.09,
    debt_cost=0.05,
    tax_rate=0.21,
    E=500,
    D=200
)
wacc = wacc_model.compute()
print("WACC:", wacc)
fcff = [100,120,140,160,180]
dcf = DCF(
    fcff=fcff,
    wacc=wacc,
    g=0.025
)
enterprise_value = dcf.enterprise_value()
print("Enterprise Value:", enterprise_value)


