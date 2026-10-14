
import streamlit as st
from reporting import build_report_text
from finance_logic import (
    calculate_total_cost,
    calculate_funding_gap,
    calculate_coverage_percent,
    calculate_stress_scenario,
    estimate_conversion,
)

st.set_page_config(
    page_title="EduWallet AI",
    page_icon="🎓",
    layout="wide",
)

st.title("🎓 EduWallet AI")
st.subheader("International Student Financial Readiness Simulator")
st.caption(
    "Competition prototype • Illustrative planning only • "
    "No live financial integrations"
)

# --------------------------------------------------
# 1. STUDY PLAN INPUTS
# --------------------------------------------------

with st.sidebar:
    st.header("Study plan")

    currency = st.selectbox(
        "Destination currency",
        ["GBP", "USD", "EUR"],
    )

    tuition = st.number_input(
        f"Tuition in {currency}",
        min_value=0.0,
        value=15000.0,
        step=500.0,
    )

    one_off = st.number_input(
        f"One-off setup costs in {currency}",
        min_value=0.0,
        value=1500.0,
        step=100.0,
    )

    monthly_living = st.number_input(
        f"Monthly living costs in {currency}",
        min_value=0.0,
        value=900.0,
        step=50.0,
    )

    months = st.number_input(
        "Months to budget",
        min_value=1,
        max_value=60,
        value=12,
        step=1,
    )

    available_funds = st.number_input(
        f"Available funds in {currency}",
        min_value=0.0,
        value=20000.0,
        step=500.0,
    )

    st.divider()
    st.caption("Exchange estimate (editable demo rate)")

    rate = st.number_input(
        f"BDT per 1 {currency}",
        min_value=0.01,
        value={"GBP": 150.0, "USD": 122.0, "EUR": 133.0}[currency],
        step=1.0,
    )

    fee = st.number_input(
        "Illustrative transfer fee (BDT)",
        min_value=0.0,
        value=500.0,
        step=100.0,
    )

# --------------------------------------------------
# 2. BASELINE FINANCIAL CALCULATIONS
# --------------------------------------------------

total_cost = calculate_total_cost(
    tuition,
    one_off,
    monthly_living,
    int(months),
)

gap = calculate_funding_gap(total_cost, available_funds)

coverage = calculate_coverage_percent(
    total_cost,
    available_funds,
)

surplus = max(0.0, available_funds - total_cost)

c1, c2, c3 = st.columns(3)

c1.metric(
    "Projected total cost",
    f"{currency} {total_cost:,.2f}",
)

c2.metric(
    "Funding gap",
    f"{currency} {gap:,.2f}",
)

c3.metric(
    "Cost coverage",
    f"{coverage:.1f}%",
)

if gap > 0:
    st.warning(
        f"Your plan currently has a projected funding gap of "
        f"{currency} {gap:,.2f}."
    )
else:
    st.success(
        f"Your entered funds cover the estimated costs, with "
        f"{currency} {surplus:,.2f} remaining."
    )

# --------------------------------------------------
# 3. STRESS TEST
# --------------------------------------------------

st.divider()
st.header("Stress test")

st.write(
    "Explore how the plan changes if living costs rise, "
    "total costs receive a shock, or available support falls."
)

left, middle, right = st.columns(3)

with left:
    monthly_increase = st.slider(
        f"Extra monthly living cost ({currency})",
        min_value=0,
        max_value=1000,
        value=100,
        step=50,
    )

with middle:
    cost_shock = st.slider(
        "Additional cost shock (%)",
        min_value=0,
        max_value=30,
        value=5,
        step=1,
    )

with right:
    support_reduction = st.slider(
        f"Reduction in available funds ({currency})",
        min_value=0,
        max_value=int(max(available_funds, 10000)),
        value=min(1000, int(max(available_funds, 10000))),
        step=500,
    )

scenario = calculate_stress_scenario(
    tuition,
    one_off,
    monthly_living,
    int(months),
    available_funds,
    monthly_cost_increase=monthly_increase,
    cost_increase_percent=cost_shock,
    support_reduction=support_reduction,
)

s1, s2, s3 = st.columns(3)

s1.metric(
    "Stressed total cost",
    f"{currency} {scenario['stressed_cost']:,.2f}",
    delta=(
        f"{scenario['stressed_cost'] - total_cost:,.2f} "
        "vs baseline"
    ),
    delta_color="inverse",
)

s2.metric(
    "Stressed funding gap",
    f"{currency} {scenario['funding_gap']:,.2f}",
)

s3.metric(
    "Stressed coverage",
    f"{scenario['coverage_percent']:.1f}%",
)

# --------------------------------------------------
# 4. FINANCIAL READINESS INSIGHTS
# --------------------------------------------------

st.divider()
st.header("Financial Readiness Insights")

st.caption(
    "Budget-planning indicators based only on your entered figures. "
    "These do not determine admission, visa, or financial eligibility."
)

insight_left, insight_right = st.columns(2)

with insight_left:
    if gap == 0:
        st.success("Baseline budget: Covered")
        st.write(
            f"Your entered funds cover the projected costs, with "
            f"{currency} {surplus:,.2f} remaining."
        )
    else:
        st.warning("Baseline budget: Funding needed")
        st.write(
            f"You need approximately {currency} {gap:,.2f} more "
            "to cover the projected costs."
        )

with insight_right:
    if scenario["funding_gap"] == 0:
        st.success("Stress test: Covered")
        st.write(
            "Your entered funds still cover the costs under "
            "the selected stress-test assumptions."
        )
    else:
        st.warning("Stress test: Funding risk")
        st.write(
            f"Under the selected assumptions, the projected "
            f"funding gap is {currency} "
            f"{scenario['funding_gap']:,.2f}."
        )

# --------------------------------------------------
# 5. ILLUSTRATIVE BDT CONVERSION
# --------------------------------------------------

st.divider()
st.header("Illustrative BDT conversion")

st.write(
    "This uses your manually entered exchange rate and fee; "
    "it is not a live quote."
)

destination_amount = st.number_input(
    f"Amount to convert from {currency}",
    min_value=0.0,
    value=1000.0,
    step=100.0,
)

estimated_bdt = estimate_conversion(
    destination_amount,
    rate,
    fee,
)

st.metric(
    "Estimated total in BDT",
    f"৳ {estimated_bdt:,.2f}",
)

st.caption(
    f"Formula: ({destination_amount:,.2f} {currency} × "
    f"৳{rate:,.2f}) + ৳{fee:,.2f} fee"
)

# --------------------------------------------------
# 6. ASSUMPTIONS, SECURITY AND LIMITATIONS
# --------------------------------------------------

with st.expander("Assumptions, security and limitations"):
    st.markdown("""
    - All amounts and exchange rates are user-entered demo assumptions.
    - No bank accounts, payment rails, passports, or identity documents
      are connected.
    - No real money moves through this prototype.
    - Inputs are processed for the current calculation; no account
      login or personal profile storage is implemented.
    - The prototype is not financial, immigration, or visa advice.
    - Before real deployment, add authenticated access, server-side
      validation, data minimisation, logging controls, dependency
      scanning, and a privacy review.
    """)

# --------------------------------------------------
# 7. DOWNLOAD FINANCIAL REPORT
# --------------------------------------------------

st.divider()
st.header("Download your financial report")

report_text = build_report_text(
    currency=currency,
    months=months,
    tuition=tuition,
    one_off=one_off,
    monthly_living=monthly_living,
    total_cost=total_cost,
    available_funds=available_funds,
    gap=gap,
    surplus=surplus,
    coverage=coverage,
    monthly_increase=monthly_increase,
    cost_shock=cost_shock,
    support_reduction=support_reduction,
    scenario=scenario,
    destination_amount=destination_amount,
    rate=rate,
    fee=fee,
    estimated_bdt=estimated_bdt,
)

st.download_button(
    label="Download financial report (.txt)",
    data=report_text,
    file_name="EduWallet_AI_Financial_Report.txt",
    mime="text/plain",
)
