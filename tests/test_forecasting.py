import unittest
from src.financial_model.revenue_model import RevenueModel


class TestForecasting(unittest.TestCase):

    def test_revenue_growth(self):

        model = RevenueModel(base_revenue=100, growth_rate=0.1, years=3)

        forecast = model.forecast()

        self.assertEqual(len(forecast), 3)


if __name__ == "__main__":
    unittest.main()
