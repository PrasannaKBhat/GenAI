import streamlit as st
import tempfile

from graph import graph

st.title("⚖️ Legal Document Reviewer")

uploaded = st.file_uploader(
    "Upload PDF",
    type=["pdf"]
)

if uploaded:

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".pdf"
    ) as tmp:

        tmp.write(uploaded.read())

        path = tmp.name

    if st.button("Review Document"):
        with st.spinner("🔍 Reviewing legal document... Please wait..."):
            result = graph.invoke(
            {
                "file_path": path
            },
            config={
                "configurable": {
                    "thread_id": "legal-review"
                }
            }
        )
        st.success("✅ Review Completed!")

        st.subheader("Summary")

        st.write(result["summary"])

        st.subheader("Risk Analysis")

        st.write(result["risks"])

        st.subheader("Compliance")

        st.write(result["compliance"])

        st.subheader("Final Report")

        st.write(result["final_report"])