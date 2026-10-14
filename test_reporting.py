
from reporting import build_report_text


def test_report_contains_main_sections():
    report = build_report_text(
        currency="GBP",
        months=12,
        tuition=12000,
        one_off=1500,
        monthly_living=900,
        total_cost=24300,
        available_funds=20000,
        gap=4300,
        surplus=0,
        coverage=82.3,
        monthly_increase=100,
        cost_shock=10,
        support_reduction=1000,
        scenario={
            "stressed_cost": 27930,
            "funding_gap": 8930,
            "coverage_percent": 68.5,
        },
        destination_amount=24300,
        rate=150,
        fee=500,
        estimated_bdt=3645500,
    )

    assert "EDUWALLET AI" in report
    assert "STUDY PLAN" in report
    assert "BASELINE FINANCIAL SUMMARY" in report
    assert "STRESS TEST" in report
    assert "ILLUSTRATIVE CURRENCY CONVERSION" in report
    assert "LIMITATIONS" in report


def test_report_contains_expected_values():
    report = build_report_text(
        currency="GBP",
        months=12,
        tuition=12000,
        one_off=1500,
        monthly_living=900,
        total_cost=24300,
        available_funds=20000,
        gap=4300,
        surplus=0,
        coverage=82.3,
        monthly_increase=100,
        cost_shock=10,
        support_reduction=1000,
        scenario={
            "stressed_cost": 27930,
            "funding_gap": 8930,
            "coverage_percent": 68.5,
        },
        destination_amount=24300,
        rate=150,
        fee=500,
        estimated_bdt=3645500,
    )

    assert "GBP 12,000.00" in report
    assert "GBP 24,300.00" in report
    assert "GBP 4,300.00" in report
    assert "GBP 27,930.00" in report
    assert "BDT 3,645,500.00" in report
    assert "No bank account is connected" in report
