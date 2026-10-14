# EduWallet AI

International Student Financial Readiness Simulator

## Overview

EduWallet AI is a Streamlit prototype that helps international students estimate study costs, funding gaps, financial stress scenarios, and illustrative currency conversion.

## Features

- Study budget calculator
- Funding gap and cost coverage analysis
- Financial readiness insights
- Stress testing
- Illustrative currency conversion using a manually entered rate
- Downloadable financial report
- Automated tests

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
