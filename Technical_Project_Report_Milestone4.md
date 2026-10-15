\# EduWallet AI — Technical Project Report



\*\*Project Category:\*\* Cross-border \& Student Finance Assistant  

\*\*Competition:\*\* 2026 Shenzhen International FinTech Competition  

\*\*Project Type:\*\* Financial planning prototype  

\*\*Version:\*\* Milestone 4 — Documentation Draft  

\*\*Development Environment:\*\* Python on Windows  

\*\*User Interface:\*\* Streamlit



\## 1. Executive Summary



EduWallet AI is a financial planning prototype designed to help international students estimate their study-related expenses, compare projected costs with available funds, identify potential funding gaps, and explore how unexpected expenses or reduced financial support could affect their plans.



The application provides an interactive dashboard, financial readiness insights, a stress-testing feature, an illustrative currency conversion calculator, and a downloadable financial report.



The project aims to make early-stage financial planning easier to understand. It is a decision-support prototype rather than a banking service, financial advisory service, or visa eligibility assessment system.



\## 2. Problem Statement



International students may need to manage several types of expenses before and during their studies abroad, including tuition fees, accommodation, food, transport, insurance, and initial setup costs.



Students may also face uncertainty from rising living costs, changes in exchange rates, unexpected expenses, or reductions in family support.



Without a structured budget, it can be difficult to determine whether available funds are sufficient for a planned period of study.



EduWallet AI addresses this problem by bringing basic expense estimation, funding-gap analysis, scenario testing, and report generation into one interface.



\## 3. Project Objectives



The main objectives are to:



1\. Estimate projected study costs using user-provided financial inputs.

2\. Compare projected costs with available funds.

3\. Calculate the funding gap, remaining funds, and cost coverage percentage.

4\. Test alternative financial scenarios involving increased expenses and reduced support.

5\. Estimate a currency conversion using a user-entered exchange rate and fee.

6\. Generate a downloadable report that summarises the entered assumptions and results.

7\. Demonstrate modular Python development and automated testing.



\## 4. Target Users



The intended users include:



\- Prospective international students planning their study budgets.

\- Current international students reviewing their living expenses.

\- Families and sponsors estimating the funds needed for education.

\- Education advisers who want to demonstrate basic budgeting scenarios.



The prototype is not intended to replace professional financial advice or official university and immigration requirements.



\## 5. System Overview



EduWallet AI is a local web application built with Python and Streamlit.



The user enters estimated costs, the duration of the budget, and available funds through the dashboard. The application passes the relevant values to calculation functions, displays the resulting financial indicators, and allows the user to download a report.



The application also allows the user to explore a stress scenario and enter an exchange rate for an illustrative conversion into Bangladeshi taka.



\### Main processing flow



1\. \*\*Input:\*\* The user enters study costs, budget duration, available funds, stress-test assumptions, and conversion details.

2\. \*\*Validation:\*\* Calculation functions check applicable numeric values and constraints.

3\. \*\*Calculation:\*\* The system estimates total costs, funding gaps, coverage, and scenario results.

4\. \*\*Presentation:\*\* Streamlit displays financial metrics and readiness insights.

5\. \*\*Reporting:\*\* The reporting module formats a downloadable text report.



\## 6. Technology Stack



| Technology | Purpose |

|---|---|

| Python | Application logic and calculations |

| Streamlit | Interactive web dashboard |

| Pytest | Automated testing |

| Python standard library | Numeric validation, report generation, and date/time formatting |

| Markdown | Project documentation |



\## 7. Software Architecture



The project separates the user interface, financial calculations, report generation, and automated tests.



\### 7.1 `app.py`



This file provides the Streamlit interface. It collects user inputs, calls the calculation functions, displays results and financial readiness insights, supports stress testing, provides the illustrative conversion interface, and offers report downloads.



\### 7.2 `finance\_logic.py`



This module contains calculation functions without depending on the Streamlit interface. It includes functions for total costs, funding gaps, surplus funds, cost coverage, stress scenarios, and illustrative currency conversion.



Separating calculations from the interface makes the logic easier to test and maintain.



\### 7.3 `reporting.py`



This module creates the downloadable financial planning report. It summarises the user's assumptions, baseline calculations, stress-test results, currency conversion inputs, and limitations.



\### 7.4 Automated tests



`test\_finance\_logic.py` checks financial calculation behaviour and input-validation cases.



`test\_reporting.py` checks report sections and expected values.



The tests are run using Pytest.



\## 8. Financial Calculation Methodology



The application uses the following formulas.



\### 8.1 Projected total cost



Projected total cost is calculated as:



\*\*Total Cost = Tuition + One-off Costs + (Monthly Living Costs × Number of Months)\*\*



This estimates the cost for the selected budget period.



\### 8.2 Funding gap



\*\*Funding Gap = max(0, Total Cost − Available Funds)\*\*



If available funds cover the projected cost, the funding gap is zero.



\### 8.3 Surplus funds



\*\*Surplus = max(0, Available Funds − Total Cost)\*\*



This estimates the amount remaining after projected costs, assuming the entered figures are accurate.



\### 8.4 Cost coverage



\*\*Coverage (%) = (Available Funds ÷ Total Cost) × 100\*\*



When total cost is zero, the application returns zero for this metric to avoid division by zero.



Coverage may exceed 100% when available funds are greater than projected costs.



\## 9. Stress Testing



The stress-testing feature allows users to examine how a less favourable financial situation could affect their budget.



The user can enter:



\- An additional monthly living-cost amount.

\- A percentage cost shock.

\- A reduction in available financial support.



The calculation first increases monthly living costs, recalculates the projected total, and then applies the percentage shock.



\*\*Stressed Cost = \[Tuition + One-off Costs + ((Monthly Living Costs + Extra Monthly Cost) × Months)] × (1 + Cost Shock ÷ 100)\*\*



Stressed funds are calculated as:



\*\*Stressed Funds = max(0, Available Funds − Support Reduction)\*\*



The application then calculates the stressed funding gap and coverage percentage.



These scenarios are illustrative assumptions, not predictions of future expenses or exchange-rate movements.



\## 10. Illustrative Currency Conversion



The application includes a conversion estimate that uses a destination-currency amount, a user-entered exchange rate, and an illustrative fee.



\*\*Estimated BDT Cost = Destination Amount × Exchange Rate + Fee\*\*



The rate represents the amount of BDT per one unit of the selected destination currency.



The application does not claim to provide live exchange rates, guaranteed bank rates, or exact remittance costs. Actual conversion costs may vary by provider, transaction method, and date.



## 11. Downloadable Financial Report

The `reporting.py` module generates a downloadable plain-text financial planning report using the inputs and calculated results supplied by the application.

The report includes:

- Report generation timestamp.
- Budget duration and destination currency.
- Tuition, one-off setup costs, and monthly living expenses.
- Projected total cost and available funds.
- Funding gap, remaining funds, and cost coverage percentage.
- Stress-test assumptions and resulting financial indicators.
- Illustrative currency conversion inputs, exchange rate, fee, and estimated total in Bangladeshi taka.
- Limitations and a financial-planning disclaimer.

The report-generation function formats the supplied values into a readable text summary. Its timestamp is generated using Python's local system time and does not explicitly specify a timezone.

The report is intended to help users review and retain their financial-planning assumptions. It is not an official financial statement, proof of funds, or assessment of financial or visa eligibility.



## 12. Validation and Error Handling

The financial calculation module includes input-validation checks designed to prevent common calculation errors.

- Numeric inputs must be real, finite numbers; Boolean values are rejected.
- Monetary inputs, cost increases, support reductions, and fees must be non-negative.
- The budget duration must be a positive integer.
- The exchange rate must be greater than zero.
- The stress-test and currency-conversion calculations check for non-finite results caused by excessively large values.

Invalid inputs raise `ValueError` exceptions in the calculation module. These checks improve the reliability of the calculations but do not guarantee that every possible numerical edge case or application failure is handled.

Further boundary testing and review would be required before real-world deployment.
The Streamlit interface constrains several inputs through its input widgets, while the calculation module performs additional validation. The current interface does not implement a general exception-handling layer for all calculation errors.


\## 13. Testing and Verification



Automated tests have been run using Pytest.



\*\*Latest recorded result during development: 21 tests passed.\*\*



The test suite covers calculation functions, invalid input cases, financial scenarios, currency conversion, and report content.



Manual checks have also been performed on the dashboard, including the displayed financial metrics, stress-test results, conversion estimate, and report download.



Execution evidence is maintained separately in the project's evidence folder.



The recorded result reflects the development state at the time of testing. Tests should be rerun against the final submission version.



\## 14. Security, Privacy, and Limitations



EduWallet AI is a prototype and has not undergone a formal security audit.



Its current scope does not include bank-account connections, payment processing, money transfers, or a live exchange-rate service.



The application uses figures entered by the user to perform calculations. Users should avoid entering unnecessary personal or confidential information.



The current prototype is not presented as a production service with a complete authentication, authorisation, deployment-security, or data-protection framework.



Key limitations include:



\- Results depend on the accuracy and completeness of user inputs.

\- Estimates may omit costs that are not entered.

\- Exchange rates and fees are manually supplied and illustrative.

\- Financial readiness insights are informational, not official eligibility decisions.

\- Automated tests do not prove the absence of software defects or security vulnerabilities.

\- Deployment to a public environment would require additional security and privacy review.



A separate security self-assessment document records the prototype's current controls, risks, and recommended improvements.



\## 15. Future Improvements



Potential future development includes:



1\. Optional budgets for different countries and currencies.

2\. Clearly sourced exchange-rate data, with the rate and retrieval time displayed.

3\. More detailed categories for accommodation, food, transport, insurance, and emergency expenses.

4\. Saving and comparing scenarios with explicit user consent and suitable privacy controls.

5\. More comprehensive automated tests, including boundary and numerical-overflow cases.

6\. Accessibility and usability improvements.

7\. Improved handling of errors and clearer explanations of assumptions.

8\. Security testing and a review of privacy requirements before public deployment.

9\. Additional report formats and a more polished presentation of financial insights.



Any future integrations involving personal data or external financial services would require appropriate security, consent, and data-handling controls.



\## 16. Conclusion



EduWallet AI demonstrates how a modular Python application can support international student financial planning through cost estimation, funding-gap analysis, stress testing, illustrative currency conversion, and downloadable reports.



Its value lies in making financial assumptions visible and helping users explore how different scenarios may affect their budgets.



The current version is a functional prototype for demonstration and evaluation. Further validation, testing, security review, and user feedback would be needed before it could be considered for production use.

## Additional Features: What-If Life Simulator and Survival Mode

The application includes two interactive financial-planning scenarios.

**What-If Life Simulator:** Users can change their assumed monthly living costs and add a one-off unexpected expense. The application calculates the alternative total cost, funding gap, remaining surplus, and cost coverage.

**Survival Mode:** Users can model higher monthly living costs, an emergency expense, and reduced available funds. The application calculates the resulting total cost, remaining funds, funding gap, surplus, and cost coverage.

**Interface design:** A dark navy-and-teal theme highlights key financial metrics and distinguishes the main dashboard from the sidebar.

**Limitations:** Scenario outputs are illustrative calculations based on user-entered assumptions, not predictions. These features do not verify financial eligibility or provide financial, immigration, or visa advice.

**Testing:** Python syntax compilation, automated tests, and manual browser checks should be recorded according to the actual results obtained. Automated tests of calculation and reporting logic are not an independent security audit.



\*\*Disclaimer:\*\* EduWallet AI provides illustrative estimates for planning and educational purposes only. It does not provide financial, legal, immigration, or visa advice and does not determine official financial eligibility.

