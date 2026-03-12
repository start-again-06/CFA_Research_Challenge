import unittest
from src.valuation.dcf_model import DCFModel


class TestDCF(unittest.TestCase):

    def test_dcf_value(self):

        fcff = [100, 120, 130, 150]
        wacc = 0.09
        growth = 0.025

        model = DCFModel(fcff, wacc, growth)

        value = model.compute_enterprise_value()

        self.assertTrue(value > 0)


if __name__ == "__main__":
    unittest.main()
