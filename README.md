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

Run these commands from the project folder on Windows:

```bat
cd /d D:\EduWallet_AI_Milestone3
.venv_m3\Scripts\activate
python -m pip install -r requirements.txt
python -m pip install pytest
```

## Run the Application

```bat
python -m streamlit run app.py
```

## Run Tests

```bat
python -m pytest -v
```

The last confirmed test run passed 21 tests. Rerun the tests before submission.

## Calculation Approach

- Total cost = tuition + one-off expenses + monthly living expenses multiplied by duration.
- Funding gap = projected costs minus available funds, with a minimum of zero.
- Cost coverage = available funds divided by projected costs, multiplied by 100. Coverage is zero when projected costs are zero.
- Stress testing models selected expense increases and reductions in available funds.
- Currency conversion uses a manually entered exchange rate and fee; it is not a live quote.

## Security and Limitations

This is a demonstration prototype, not a production financial service. It does not connect to bank accounts, execute payments, transfer money, or provide live exchange rates. It does not currently implement authenticated accounts or enforced role-based permissions. Estimates depend on user inputs and assumptions. Downloaded reports should be handled carefully.

## Disclaimer

EduWallet AI provides illustrative educational budgeting calculations. It is not financial, investment, immigration, or visa advice. Users should independently verify costs and official requirements.