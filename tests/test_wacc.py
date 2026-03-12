import unittest
from src.valuation.wacc_model import WACCModel


class TestWACC(unittest.TestCase):

    def test_wacc(self):

        model = WACCModel(
            equity=500,
            debt=200,
            cost_of_equity=0.11,
            cost_of_debt=0.05,
            tax_rate=0.25
        )

        wacc = model.compute_wacc()

        self.assertTrue(0 < wacc < 0.2)


if __name__ == "__main__":
    unittest.main()
