"""
RAGFlow AI Platform.

Streamlit frontend for interacting with the RAGFlow AI Platform.
"""

import requests
import streamlit as st


API_URL = "http://127.0.0.1:8000/api/v1/ask"


st.set_page_config(
    page_title="RAGFlow AI Platform",
    page_icon="🔎",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ============================================================
# Main Page
# ============================================================

st.title("RAGFlow AI Platform")

st.write(
    "Ask questions about your documents using "
    "Retrieval-Augmented Generation (RAG)."
)


# ============================================================
# Sidebar
# ============================================================

with st.sidebar:

    st.header("Platform Information")

    st.markdown(
        """
        **Application**

        RAGFlow AI Platform

        **Version**

        Sprint 04

        **Backend**

        FastAPI

        **Vector Database**

        FAISS

        **Embedding Model**

        all-mpnet-base-v2

        **LLM**

        DeepSeek-R1
        """
    )


# ============================================================
# User Input
# ============================================================

st.divider()

st.subheader("Ask a Question")

question = st.text_area(
    label="Question",
    placeholder="Example: What is the American Community Survey?",
    height=120,
)

submit_button = st.button(
    "Submit",
    type="primary",
)


# ============================================================
# Generate Response
# ============================================================

if submit_button:

    if not question.strip():

        st.warning("Please enter a question.")

    else:

        with st.spinner("Generating response..."):

            try:

                response = requests.post(
                    API_URL,
                    json={
                        "question": question,
                    },
                    timeout=120,
                )

                if response.status_code == 200:

                    result = response.json()

                    st.success(
                        "Response generated successfully."
                    )

                    st.divider()

                    st.subheader("Answer")

                    st.write(result["answer"])

                else:

                    st.error(
                        f"Backend returned HTTP "
                        f"{response.status_code}"
                    )

            except requests.exceptions.ConnectionError:

                st.error(
                    "Unable to connect to the FastAPI backend."
                )

            except requests.exceptions.Timeout:

                st.error(
                    "The request timed out."
                )

            except Exception as error:

                st.exception(error)