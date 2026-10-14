\# EduWallet AI — Security Self-Assessment



\*\*Project:\*\* EduWallet AI — International Student Financial Readiness Simulator

\*\*Competition:\*\* 2026 Shenzhen International FinTech Competition

\*\*Assessment type:\*\* Prototype-level self-assessment

\*\*Status:\*\* Draft for technical review



\## 1. System Overview



EduWallet AI is a Python and Streamlit prototype that calculates estimated study costs, funding gaps, cost coverage, financial stress scenarios, and illustrative currency conversions.



The prototype is designed for educational budgeting. It does not execute financial transactions or connect to financial institutions.



\## 2. Data Handling and Permission Model



\- Users enter financial planning figures through the Streamlit interface.

\- The application uses these inputs to calculate estimates and generate a downloadable text report.

\- The current prototype does not implement user accounts, authentication, persistent personal-profile storage, or application-level role-based access control.

\- There are no implemented permission tiers because the prototype does not have a multi-user account or authorisation system.

\- The report is generated from the current calculation inputs and can be downloaded by the user.

\- The prototype does not request passports or identity documents, and users should avoid entering sensitive information that is unnecessary for budgeting.



The absence of an account system does not establish that every deployment environment retains no data. Hosting, runtime, access-log, and platform-retention behaviour should be reviewed separately before public deployment.



\## 3. Financial Safety Controls



The calculation module validates inputs such as negative amounts, invalid budget durations, non-finite numeric values, and invalid exchange rates.



Automated tests cover the calculation logic, selected invalid inputs, and report generation.



These controls reduce certain input-related risks but do not establish that the application is secure against every possible attack or misuse.



\## 4. External Integrations and Transactions



The prototype currently has:



\- No bank-account integrations

\- No payment processing

\- No money transfers

\- No live exchange-rate API

\- No passport or identity-document processing

\- No implemented user authentication



Exchange rates and fees are manually entered assumptions. They must not be presented as verified live market quotes.



\## 5. Identified Risks and Limitations



\### Financial accuracy



Incorrect tuition, living-cost, exchange-rate, or funding inputs can produce misleading results.



\*\*Mitigation:\*\* Clearly label outputs as estimates and encourage users to verify figures with official sources.



\### Input validation



The calculation module includes validation, but additional testing of unusual inputs, arithmetic overflow, and interface boundaries remains appropriate.



\*\*Mitigation:\*\* Maintain automated tests and review calculations before future releases.



\### Dependency vulnerabilities



Third-party packages may contain security vulnerabilities.



\*\*Mitigation:\*\* Review dependencies, keep packages updated, and run dependency vulnerability checks before deployment.



\### Privacy and data exposure



The prototype has no account system or persistent personal-profile storage. However, the security and retention behavior of the runtime environment, hosting platform, and any future integrations must be assessed separately.



\*\*Mitigation:\*\* Minimise collected data, avoid sensitive inputs, review hosting settings, and document data retention before public deployment.



\### Unauthorised access



The local prototype does not implement application-level user authentication.



\*\*Mitigation:\*\* If publicly deployed, assess access controls, HTTPS, platform configuration, and abuse protections appropriate to the hosting environment.



\### Financial and immigration misunderstanding



Users may incorrectly interpret a budget indicator as confirmation of visa eligibility or financial sufficiency.



\*\*Mitigation:\*\* Display clear disclaimers stating that the application does not determine admission, visa approval, or official financial eligibility.



\*\*Permission-tier status:\*\* No permission tiers or role-based access controls are currently implemented. The application is a single-interface budgeting prototype without user accounts. If multi-user access is introduced in the future, authentication, authorisation, and permission enforcement must be designed and tested before deployment.



\## 6. Recommended Pre-Deployment Actions



Before production or public deployment:



1\. Review all dependencies for known vulnerabilities.

2\. Test invalid, extreme, and boundary input values.

3\. Review data processing, logging, hosting, and retention behavior.

4\. Configure appropriate access controls and HTTPS where applicable.

5\. Avoid storing sensitive personal or financial information unnecessarily.

6\. Review report content for misleading or unsupported claims.

7\. Retest the complete application after changes.

8\. Document remaining limitations and unresolved risks.



\## 7. Current Verification Evidence



The latest recorded development test run reported 21 automated tests passing. Manual checks also confirmed the dashboard, financial readiness insights, stress-test results, illustrative currency conversion, and downloadable financial report.



These results represent the recorded development state and should not be treated as confirmation that the final submission version has been retested. The full test suite should be rerun after final code changes, and the resulting output should be retained as execution evidence.



These checks are functional verification activities, not a penetration test, independent security audit, or guarantee of production security.



\## 8. Overall Assessment



EduWallet AI has a limited prototype attack surface because it does not implement payment processing, bank integrations, or user accounts. Its main current risks relate to input handling, dependency management, privacy assumptions, deployment configuration, and users misinterpreting illustrative financial results.



The application should remain a demonstration prototype until the recommended security, privacy, testing, and deployment reviews have been completed.



\## 9. Disclaimer



This self-assessment is a development document, not an independent security certification. It records the prototype's intended boundaries and known limitations based on the current implementation.

