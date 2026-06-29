from langchain_ollama import ChatOllama
from tools import read_pdf
from prompts import *

llm = ChatOllama(
    model="llama3.2:3b",
    temperature=0
)


def load_document(state):

    state["document"] = read_pdf(state["file_path"])

    return state


def summarize(state):

    prompt = SUMMARY_PROMPT.format(
        document=state["document"]
    )

    response = llm.invoke(prompt)

    state["summary"] = response.content

    return state


def analyze_risk(state):

    prompt = RISK_PROMPT.format(
        document=state["document"]
    )

    response = llm.invoke(prompt)

    state["risks"] = response.content

    return state


def compliance(state):

    prompt = COMPLIANCE_PROMPT.format(
        document=state["document"]
    )

    response = llm.invoke(prompt)

    state["compliance"] = response.content

    return state


def report(state):

    prompt = REPORT_PROMPT.format(
        summary=state["summary"],
        risks=state["risks"],
        compliance=state["compliance"],
    )

    response = llm.invoke(prompt)

    state["final_report"] = response.content

    return state