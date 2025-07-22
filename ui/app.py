import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from model.rag_qa import answer_query

# --- Page configuration ---
st.set_page_config(
    page_title="📘 Bangla RAG QA System",
    page_icon="📘",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- Custom CSS ---
st.markdown("""
    <style>
    body {
        background-color: #f2f2f2;
    }

    .main {
        background-color: #ffffff;
        padding: 2rem;
        border-radius: 12px;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
    }

    .stTextArea textarea {
        font-size: 16px;
    }

    .stButton>button {
        background-color: #0a3d62;
        color: white;
        border-radius: 6px;
        padding: 0.5rem 1rem;
        font-weight: 500;
        font-size: 16px;
    }

    .stButton>button:hover {
        background-color: #074b8a;
    }

    .stSpinner > div > div {
        font-size: 16px;
        color: #0a3d62;
    }

    .answer-block {
        border-left: 4px solid #0a3d62;
        padding-left: 1rem;
        margin-top: 1rem;
        background-color: #f9f9f9;
        border-radius: 6px;
    }

    #MainMenu, footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# --- App Title ---
st.markdown("<h2 style='text-align:center; color:#0a3d62;'>📘 Bangla RAG QA System</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#666;'>Ask Bangla/English questions from your textbook and get accurate answers from your local model</p>", unsafe_allow_html=True)
st.markdown("<hr style='border:0.5px solid #ccc'/>", unsafe_allow_html=True)

# --- Input box ---
query = st.text_area("❓ Type your question", placeholder="e.g., অনুপমের ভাষায় আদর্শ মানুষ কে?", height=100)

# --- Answering Logic ---
if st.button("🔍 Get Answer"):
    if query.strip():
        with st.spinner("Thinking..."):
            answer = answer_query(query)
        st.markdown("### 💡 Answer")
        st.markdown(f"<div class='answer-block'>{answer}</div>", unsafe_allow_html=True)
    else:
        st.warning("Please enter a question before clicking Get Answer.")

# --- Footer ---
st.markdown("<hr/>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:gray;'>Made with ❤️ using Streamlit and Ollama | July 2025</p>", unsafe_allow_html=True)
