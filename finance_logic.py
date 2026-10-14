
"""Pure calculation functions for EduWallet AI. No UI dependencies."""

import math
from numbers import Real


def _validate_number(name, value):
    """Require a finite, real number; reject booleans."""
    if isinstance(value, bool) or not isinstance(value, Real):
        raise ValueError(f"{name} must be a valid number")
    if not math.isfinite(value):
        raise ValueError(f"{name} must be finite")


def _nonnegative(name, value):
    _validate_number(name, value)
    if value < 0:
        raise ValueError(f"{name} must be non-negative")


def calculate_total_cost(tuition, one_off, monthly_living, months):
    _nonnegative("tuition", tuition)
    _nonnegative("one_off", one_off)
    _nonnegative("monthly_living", monthly_living)
    _validate_number("months", months)
    if not isinstance(months, int) or isinstance(months, bool) or months < 1:
        raise ValueError("months must be a positive integer")
    return tuition + one_off + monthly_living * months


def calculate_funding_gap(total_cost, available_funds):
    _nonnegative("total_cost", total_cost)
    _nonnegative("available_funds", available_funds)
    return max(0.0, total_cost - available_funds)


def calculate_surplus(total_cost, available_funds):
    _nonnegative("total_cost", total_cost)
    _nonnegative("available_funds", available_funds)
    return max(0.0, available_funds - total_cost)


def calculate_coverage_percent(total_cost, available_funds):
    _nonnegative("total_cost", total_cost)
    _nonnegative("available_funds", available_funds)
    return (available_funds / total_cost * 100) if total_cost > 0 else 0.0


def calculate_stress_scenario(
    tuition, one_off, monthly_living, months,
    available_funds, monthly_cost_increase=0,
    cost_increase_percent=0, support_reduction=0
):
    _nonnegative("available_funds", available_funds)
    baseline = calculate_total_cost(tuition, one_off, monthly_living, months)
    _nonnegative("monthly_cost_increase", monthly_cost_increase)
    _nonnegative("cost_increase_percent", cost_increase_percent)
    _nonnegative("support_reduction", support_reduction)

    stressed_before_shock = calculate_total_cost(
        tuition, one_off, monthly_living + monthly_cost_increase, months
    )
    stressed_cost = stressed_before_shock * (1 + cost_increase_percent / 100)
    if not math.isfinite(stressed_cost):
        raise ValueError("stressed cost is too large")

    stressed_funds = max(0.0, available_funds - support_reduction)
    return {
        "baseline_cost": baseline,
        "stressed_cost": stressed_cost,
        "stressed_funds": stressed_funds,
        "funding_gap": calculate_funding_gap(stressed_cost, stressed_funds),
        "coverage_percent": calculate_coverage_percent(stressed_cost, stressed_funds),
    }


def estimate_conversion(destination_amount, home_currency_per_destination_unit, fee=0):
    _nonnegative("destination_amount", destination_amount)
    _nonnegative("fee", fee)
    _validate_number("home_currency_per_destination_unit",
                     home_currency_per_destination_unit)
    if home_currency_per_destination_unit <= 0:
        raise ValueError("exchange rate must be greater than zero")

    result = destination_amount * home_currency_per_destination_unit + fee
    if not math.isfinite(result):
        raise ValueError("conversion result is too large")
    return result
