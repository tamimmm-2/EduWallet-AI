import unittest
from finance_logic import (
    calculate_total_cost, calculate_funding_gap, calculate_surplus,
    calculate_coverage_percent, calculate_stress_scenario, estimate_conversion
)

class FinanceLogicTests(unittest.TestCase):
    def test_total_cost(self):
        self.assertEqual(calculate_total_cost(15000, 1500, 900, 12), 27300)

    def test_funding_gap(self):
        self.assertEqual(calculate_funding_gap(27300, 20000), 7300)
        self.assertEqual(calculate_funding_gap(10000, 12000), 0)

    def test_surplus(self):
        self.assertEqual(calculate_surplus(10000, 12000), 2000)

    def test_coverage(self):
        self.assertAlmostEqual(calculate_coverage_percent(24000, 20000), 83.3333333, places=5)
        self.assertEqual(calculate_coverage_percent(0, 20000), 0)

    def test_stress_scenario(self):
        result = calculate_stress_scenario(
            15000, 1500, 900, 12, 20000,
            monthly_cost_increase=100,
            cost_increase_percent=5,
            support_reduction=1000
        )
        self.assertEqual(result["baseline_cost"], 27300)
        self.assertEqual(result["stressed_cost"], 29925)
        self.assertEqual(result["stressed_funds"], 19000)
        self.assertEqual(result["funding_gap"], 10925)

    def test_conversion(self):
        self.assertEqual(estimate_conversion(1000, 150, 500), 150500)

    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):
            calculate_total_cost(-1, 0, 0, 12)
        with self.assertRaises(ValueError):
            calculate_total_cost(1, 0, 0, 0)
        with self.assertRaises(ValueError):
            estimate_conversion(100, 0, 0)

if __name__ == "__main__":
    unittest.main()


import pytest

from finance_logic import (
    calculate_total_cost,
    estimate_conversion,
)


@pytest.mark.parametrize("bad_value", [float("nan"), float("inf"), float("-inf")])
def test_total_cost_rejects_non_finite_values(bad_value):
    with pytest.raises(ValueError):
        calculate_total_cost(bad_value, 100, 200, 12)


@pytest.mark.parametrize("bad_months", [0, -1, 1.5, True])
def test_total_cost_rejects_invalid_months(bad_months):
    with pytest.raises(ValueError):
        calculate_total_cost(1000, 500, 300, bad_months)


@pytest.mark.parametrize("bad_rate", [0, -1, float("nan"), float("inf")])
def test_conversion_rejects_invalid_exchange_rates(bad_rate):
    with pytest.raises(ValueError):
        estimate_conversion(100, bad_rate, 0)


def test_conversion_rejects_negative_fee():
    with pytest.raises(ValueError):
        estimate_conversion(100, 150, -5)
