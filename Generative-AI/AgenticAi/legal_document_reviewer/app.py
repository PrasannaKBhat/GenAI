import streamlit as st
import tempfile

from graph import graph
from nodes import report

st.set_page_config(
    page_title="Legal Document Reviewer",
    page_icon="⚖️",
    layout="wide"
)

st.title("⚖️ AI Legal Document Reviewer")

# -----------------------------
# Session State Initialization
# -----------------------------

if "pdf_path" not in st.session_state:
    st.session_state.pdf_path = None

if "review_done" not in st.session_state:
    st.session_state.review_done = False

if "review_result" not in st.session_state:
    st.session_state.review_result = None

if "report_generated" not in st.session_state:
    st.session_state.report_generated = False


# -----------------------------
# Upload PDF
# -----------------------------

uploaded = st.file_uploader(
    "Upload Legal PDF",
    type=["pdf"]
)

if uploaded is not None:

    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(uploaded.read())
        st.session_state.pdf_path = tmp.name

# -----------------------------
# Review Button
# -----------------------------

if st.session_state.pdf_path:

    if st.button("🔍 Review Document"):

        with st.spinner("Reviewing legal document..."):

            result = graph.invoke(
                {
                    "file_path": st.session_state.pdf_path
                },
                config={
                    "configurable": {
                        "thread_id": "legal-review"
                    }
                }
            )

        st.session_state.review_result = result
        st.session_state.review_done = True
        st.session_state.report_generated = False

# -----------------------------
# Display Review
# -----------------------------

if st.session_state.review_done:

    result = st.session_state.review_result

    st.success("✅ Review Completed")

    st.subheader("📋 Executive Summary")
    st.write(result["summary"])

    st.subheader("⚠ Risk Analysis")
    st.write(result["risks"])

    st.subheader("✅ Compliance Check")
    st.write(result["compliance"])

    st.divider()

    st.subheader("👨 Human Approval")

    col1, col2 = st.columns(2)

    with col1:

        if st.button("✅ Approve Report"):

            with st.spinner("Generating Final Report..."):

                report_result = report(st.session_state.review_result)

                st.session_state.review_result = report_result
                st.session_state.report_generated = True

            st.rerun()

    with col2:

        if st.button("❌ Reject Report"):

            st.error("Report generation rejected by user.")

# -----------------------------
# Final Report
# -----------------------------

if st.session_state.report_generated:

    st.divider()

    st.subheader("📑 Final Legal Report")

    st.write(
        st.session_state.review_result["final_report"]
    )