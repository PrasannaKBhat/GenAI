# ⚖️ Legal Document Reviewer using LangGraph

An AI-powered Legal Document Reviewer built using **LangGraph**, **LangChain**, **Ollama**, and **Streamlit**.

The application analyzes legal contracts such as NDAs, Employment Agreements, Rental Agreements, and Service Contracts. It summarizes the document, identifies legal risks, checks compliance, and generates a professional review report.

---

## 🚀 Features

* 📄 Upload PDF legal documents
* 🤖 AI-powered contract review
* 📋 Executive summary generation
* ⚠️ Risk analysis (High, Medium, Low)
* ✅ Compliance checking
* 📑 Final legal review report
* 🧠 LangGraph workflow
* 💾 Memory & Checkpointing
* 👨‍⚖️ Human-in-the-Loop (HITL)
* 🛠️ Tool Calling
* 🌐 100% Open Source (Runs locally)

---

## 🛠 Tech Stack

| Technology | Purpose                |
| ---------- | ---------------------- |
| Python     | Programming Language   |
| LangGraph  | Workflow Orchestration |
| LangChain  | LLM Framework          |
| Ollama     | Local LLM Runtime      |
| Qwen2.5:7B | Open Source LLM        |
| Streamlit  | Web UI                 |
| PyMuPDF    | PDF Reader             |

---

## 📂 Project Structure

```text
legal-document-reviewer/
│
├── app.py
├── graph.py
├── nodes.py
├── prompts.py
├── state.py
├── tools.py
├── requirements.txt
├── sample.pdf
└── README.md
```

---

## 🏗️ Architecture

```text
             Upload PDF
                  │
                  ▼
           PDF Reader Tool
                  │
                  ▼
          LangGraph Workflow
                  │
      ┌───────────┼────────────┐
      │           │            │
      ▼           ▼            ▼
 Summary      Risk Agent   Compliance Agent
      │           │            │
      └───────────┼────────────┘
                  ▼
        Human-in-the-Loop
                  │
                  ▼
       Final Report Generator
                  │
                  ▼
             Streamlit UI
```

---

## 🔄 LangGraph Workflow

```text
START
   │
Load PDF
   │
Summary Agent
   │
Risk Analysis Agent
   │
Compliance Agent
   │
Human Approval
   │
Generate Report
   │
END
```

---

## 🤖 AI Agents

### 1. Summary Agent

* Reads the contract
* Generates an executive summary

### 2. Risk Analysis Agent

Identifies:

* High Risk Clauses
* Medium Risk Clauses
* Low Risk Clauses

### 3. Compliance Agent

Checks for:

* Confidentiality
* Governing Law
* Termination
* Payment Terms
* Force Majeure
* Arbitration
* Data Privacy

### 4. Report Agent

Creates the final legal review report.

---

## 🛠 Tool Calling

The application uses a PDF Reader Tool built with **PyMuPDF**.

Responsibilities:

* Read uploaded PDF
* Extract text
* Pass content to AI agents

---

## 🧠 Memory

Uses **LangGraph MemorySaver**.

Benefits:

* Remembers previous conversation
* Supports follow-up questions
* Stores workflow state

Example:

```
User:
Explain Clause 5

AI:
Provides explanation without reprocessing the PDF.
```

---

## 💾 Checkpointing

Uses LangGraph Checkpointing.

If the application stops unexpectedly:

```
Summary Completed
↓

Risk Analysis Completed
↓

Application Stops
↓

Resume from Compliance Step
```

No need to start from the beginning.

---

## 👨‍⚖️ Human-in-the-Loop (HITL)

Before generating the final report:

```
AI:
Found 3 High Risk Clauses.

Approve Report?

[Approve]
[Review Again]
```

This allows human validation before the final report is created.

---

## 📊 Sample Output

### Summary

This agreement defines the terms between ABC Pvt Ltd and XYZ Technologies regarding software development services.

### Risks

* Unlimited Liability
* Automatic Renewal
* Missing Termination Notice

### Missing Clauses

* Force Majeure
* Confidentiality
* Arbitration

### Recommendation

* Add confidentiality clause.
* Add liability limitation.
* Include dispute resolution clause.

---

## ⚙️ Installation

Clone the repository

```bash
git clone <repository-url>
```

Install dependencies

```bash
pip install -r requirements.txt
```

Install Ollama

https://ollama.com/download

Pull the model

```bash
ollama pull qwen2.5:7b
```

Start Ollama

```bash
ollama serve
```

Run the application

```bash
streamlit run app.py
```

---

## 🎯 Future Improvements

* RAG using ChromaDB
* Legal knowledge base
* Multi-document comparison
* Clause highlighting
* PDF report export
* OCR support
* Voice interaction
* Multi-language support

---

## 📸 Screenshots

Add screenshots here after running the application.

---

## 👨‍💻 Author

**Prasanna Bhat**

Senior Android Engineer | AI & LangGraph Enthusiast

---

## 📄 License

MIT License
