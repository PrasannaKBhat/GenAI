SUMMARY_PROMPT = """
You are a legal expert.

Summarize the following contract.

Contract:

{document}
"""

RISK_PROMPT = """
You are a legal risk analyst.

Find

High Risks

Medium Risks

Low Risks

Document

{document}
"""

COMPLIANCE_PROMPT = """
Check whether these clauses exist.

- Confidentiality

- Termination

- Payment Terms

- Governing Law

- Force Majeure

Return missing clauses.

Document

{document}
"""

REPORT_PROMPT = """
Generate a professional legal report.

Summary

{summary}

Risks

{risks}

Compliance

{compliance}
"""