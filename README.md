# EduWallet AI

International Student Financial Readiness Simulator

## Overview

EduWallet AI is a Streamlit prototype that helps international students estimate study costs, funding gaps, financial stress scenarios, and illustrative currency conversion.

## Key Features

- **Study Budget Calculator:** Estimates tuition, setup expenses, and living costs over a selected study period.
- **Funding Gap Analysis:** Compares projected expenses with available funds and estimates cost coverage.
- **Premium Dashboard Interface:** Uses a navy-and-teal visual design with clearly presented financial metrics.
- **What-If Life Simulator:** Lets users change monthly living costs and add unexpected expenses to compare alternative budgets.
- **Survival Mode:** Simulates higher living costs, emergency expenses, and reduced available funds to examine potential financial shortfalls.
- **Financial Readiness Insights:** Summarises baseline budget coverage and results under selected stress-test assumptions.
- **Stress Testing:** Models increased living costs, additional cost shocks, and reduced financial support.
- **Illustrative Currency Conversion:** Estimates a BDT amount using a manually entered exchange rate and transfer fee; it is not a live exchange quote.
- **Downloadable Financial Report:** Generates a text report containing the user's entered assumptions and calculated results.
- **Automated Tests:** Tests financial calculation and report-generation logic.

## Important Limitations

EduWallet AI is a competition prototype for illustrative financial planning. It does not connect to banks, execute payments, retrieve live exchange rates, verify funding, or determine admission, visa, or immigration eligibility. What-If Life Simulator and Survival Mode results depend on user-entered assumptions and are not predictions. The prototype does not implement user authentication or persistent personal profiles.

The application is not financial, immigration, or visa advice.

## Technology

- Python
- Streamlit
- Pytest

## Installation

1. Clone or download this repository.
2. Open a terminal in the project directory.
3. Create and activate a Python virtual environment if desired.
4. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Run the Application

```bash
streamlit run app.py
```

## Run Tests

```bash
python -m pytest -v
```
## Calculation Approach

- Total cost = tuition + one-off expenses + monthly living expenses multiplied by duration.
- Funding gap = projected costs minus available funds, with a minimum of zero.
- Cost coverage = available funds divided by projected costs, multiplied by 100. Coverage is zero when projected costs are zero.
- Stress testing models selected expense increases and reductions in available funds.
- Currency conversion uses a manually entered exchange rate and fee; it is not a live quote.

## Testing

The latest recorded local test run completed successfully, with **21 tests passed**.

The automated tests cover the financial calculation logic and financial report generation. Run the test suite again after code changes to verify the current version.

This result demonstrates functional testing; it is not an independent security audit.

## Security

This is a demonstration prototype, not a production financial service. It does not connect to bank accounts, execute payments, transfer money, or provide live exchange rates. It does not currently implement authenticated accounts or enforced role-based permissions. Estimates depend on user inputs and assumptions. Downloaded reports should be handled carefully.

## Limitations

- Currency exchange rates are illustrative user-provided inputs and are not retrieved from a live exchange-rate service.
- Financial projections depend on the assumptions and figures entered by the user.
- The prototype does not provide bank integration, payments, user authentication, or role-based access control.
- The application is a financial-planning aid, not professional financial advice or an official assessment of visa eligibility.

Users should verify tuition fees, living costs, exchange rates, and other financial requirements with the relevant institutions before making decisions.

## Disclaimer

EduWallet AI provides illustrative educational budgeting calculations. It is not financial, investment, immigration, or visa advice. Users should independently verify costs and official requirements.
