
from datetime import datetime


def build_report_text(
    currency,
    months,
    tuition,
    one_off,
    monthly_living,
    total_cost,
    available_funds,
    gap,
    surplus,
    coverage,
    monthly_increase,
    cost_shock,
    support_reduction,
    scenario,
    destination_amount,
    rate,
    fee,
    estimated_bdt,
):
    """Build a downloadable EduWallet AI financial planning report."""

    report_text = f"""
EDUWALLET AI
International Student Financial Readiness Report
Generated: {datetime.now().strftime("%Y-%m-%d %H:%M")}

IMPORTANT: This is an illustrative planning report, not financial,
immigration, or visa advice.

STUDY PLAN
Destination currency: {currency}
Budget duration: {int(months)} months
Tuition: {currency} {tuition:,.2f}
One-off setup costs: {currency} {one_off:,.2f}
Monthly living costs: {currency} {monthly_living:,.2f}

BASELINE FINANCIAL SUMMARY
Projected total cost: {currency} {total_cost:,.2f}
Available funds: {currency} {available_funds:,.2f}
Funding gap: {currency} {gap:,.2f}
Funds remaining after projected costs: {currency} {surplus:,.2f}
Cost coverage: {coverage:.1f}%

STRESS TEST
Extra monthly living cost: {currency} {monthly_increase:,.2f}
Additional cost shock: {cost_shock}%
Reduction in available funds: {currency} {support_reduction:,.2f}
Stressed total cost: {currency} {scenario['stressed_cost']:,.2f}
Stressed funding gap: {currency} {scenario['funding_gap']:,.2f}
Stressed coverage: {scenario['coverage_percent']:.1f}%

ILLUSTRATIVE CURRENCY CONVERSION
Destination amount: {currency} {destination_amount:,.2f}
User-entered rate: BDT {rate:,.2f} per {currency} 1
Illustrative fee: BDT {fee:,.2f}
Estimated total: BDT {estimated_bdt:,.2f}

LIMITATIONS
- Figures depend on the assumptions entered by the user.
- Exchange rates and fees are illustrative, not live quotes.
- No bank account is connected and no money is transferred.
- This report does not establish financial or visa eligibility.
"""

    return report_text
