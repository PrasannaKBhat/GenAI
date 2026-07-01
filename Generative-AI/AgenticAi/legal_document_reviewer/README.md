# ⚖️ AI Legal Document Reviewer using LangGraph

An AI-powered Legal Document Reviewer built using **LangGraph**, **LangChain**, **Google Gemini**, and **Streamlit**.

The application analyzes legal contracts such as NDAs, Employment Agreements, Rental Agreements, and Service Agreements. It summarizes the document, identifies legal risks, verifies compliance, and generates a professional legal review report with **Human-in-the-Loop (HITL)** approval.

## Why LangGraph?

Unlike traditional LangChain chains, LangGraph models the application as a workflow of interconnected AI agents sharing a common state. This enables:

- Stateful execution
- Modular AI agents
- Human-in-the-Loop approval
- Memory & Checkpointing
- Scalable multi-agent workflows

---

# 🚀 Features

- 📄 Upload PDF legal documents
- 🤖 AI-powered legal contract analysis
- 📋 Executive Summary Generation
- ⚠️ Risk Analysis
- ✅ Compliance Verification
- 📑 Final Legal Review Report
- 👨 Human Approval before report generation
- 🔄 LangGraph Workflow
- 💾 Memory & Checkpointing
- 🛠 PDF Extraction Tool
- 🌐 Streamlit Web Interface

---

# 🏗 Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| LangGraph | Workflow Orchestration |
| LangChain | LLM Framework |
| Google Gemini 2.5 Flash | Large Language Model |
| Streamlit | User Interface |
| PyMuPDF | PDF Text Extraction |
| python-dotenv | Environment Variable Management |

---

# 📂 Project Structure

```text
legal-document-reviewer/
│
├── app.py
├── graph.py
├── nodes.py
├── state.py
├── prompts.py
├── tools.py
├── requirements.txt
├── README.md
└── .env
```

---

# 🏛 System Architecture

```text
                User
                  │
                  ▼
         Upload Legal PDF
                  │
                  ▼
          PDF Extraction Tool
                  │
                  ▼
          LangGraph Workflow
                  │
      ┌───────────┼────────────┐
      ▼           ▼            ▼
 Summary      Risk Agent   Compliance Agent
      │           │            │
      └───────────┼────────────┘
                  ▼
         Human Approval (HITL)
                  │
          Approve / Reject
                  │
                  ▼
        Final Report Generator
                  │
                  ▼
            Streamlit UI
```

---

# 🔄 LangGraph Workflow

```text
START
  │
  ▼
Load Document
  │
  ▼
Extract PDF Text
  │
  ▼
Summary Agent
  │
  ▼
Risk Analysis Agent
  │
  ▼
Compliance Agent
  │
  ▼
Human Approval
  │
  ▼
Report Generator
  │
  ▼
END
```

---

# 🤖 AI Agents

## 📋 Summary Agent

Responsibilities

- Read the legal document
- Generate an executive summary
- Highlight important clauses

---

## ⚠ Risk Analysis Agent

Identifies

- High Risk Clauses
- Medium Risk Clauses
- Low Risk Clauses

Examples

- Unlimited Liability
- Automatic Renewal
- Missing Termination Clause

---

## ✅ Compliance Agent

Checks whether the contract contains

- Confidentiality
- Payment Terms
- Governing Law
- Arbitration
- Force Majeure
- Data Privacy
- Termination Clause

---

## 📑 Report Agent

Generates

- Executive Summary
- Risk Analysis
- Compliance Report
- Recommendations

---

# 🛠 Tool Integration

The application uses a dedicated PDF extraction tool.

### Tool

```
read_pdf()
```

Responsibilities

- Read uploaded PDF
- Extract text using PyMuPDF
- Pass extracted text to LangGraph

---

# 🧠 LangGraph State

The application uses a shared state across all nodes.

Example

```text
Initial State

{
    file_path
}

↓

Load Document

{
    file_path,
    document
}

↓

Summary

{
    document,
    summary
}

↓

Risk Analysis

{
    summary,
    risks
}

↓

Compliance

{
    compliance
}

↓

Final Report

{
    final_report
}
```

Every node updates the same state object.

---

# 💾 Memory

The project uses **LangGraph MemorySaver**.

Benefits

- Maintains workflow state
- Enables checkpointing
- Preserves execution state during the workflow

---

# 🔖 Checkpointing

MemorySaver allows the workflow to resume from the last completed node.

Example

```text
Load Document

↓

Summary

↓

Risk Analysis

↓

Application Stops

↓

Restart

↓

Resume from Compliance
```

---

# 👨 Human-in-the-Loop (HITL)

Before generating the final legal report, the AI presents:

- Executive Summary
- Risk Analysis
- Compliance Review

The user must approve the AI analysis before the report is generated.

```text
AI Review Completed

Summary
Risk Analysis
Compliance

──────────────

Approve Report?

[Approve]

[Reject]
```

This ensures human oversight over AI-generated legal recommendations.

---

# 📄 Sample Output

## Executive Summary

This agreement defines the software development responsibilities between Company A and Company B.

---

## Risk Analysis

- Unlimited Liability
- Missing Confidentiality Clause
- Automatic Renewal

---

## Compliance

✔ Payment Terms

✔ Governing Law

❌ Force Majeure

❌ Arbitration

---

## Recommendations

- Add Confidentiality Clause
- Include Liability Limitation
- Add Arbitration Clause
- Define Termination Notice Period

---

# ⚙ Installation

## Clone Repository

```bash
git clone https://github.com/<your-username>/legal-document-reviewer.git
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Create .env

```text
GOOGLE_API_KEY=YOUR_API_KEY
```

---

## Run Application

```bash
streamlit run app.py
```

---

# 🎯 Evaluation Criteria Mapping

| Requirement | Status |
|------------|--------|
| LangGraph Workflow | ✅ |
| LLM Agents | ✅ |
| Tool Integration | ✅ |
| Memory | ✅ |
| Checkpointing | ✅ |
| Human-in-the-Loop | ✅ |
| End-to-End Application | ✅ |

---

# 🚀 Future Enhancements

- Retrieval-Augmented Generation (RAG)
- ChromaDB Integration
- Legal Clause Knowledge Base
- Multi-document Comparison
- PDF Report Export
- OCR Support
- Chat with Contract
- Multi-language Support

---

# 📸 Screenshots

Add screenshots of

- Upload Screen
- Review Screen
- Human Approval
- Final Report

---

# 👨‍💻 Author

**Prasanna Bhat**

Senior Android Engineer

AI • LangGraph • Android • Generative AI

---

# 📄 License

MIT License