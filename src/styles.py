import streamlit as st

def load_css():

    st.markdown("""

    <style>

    .main{

        background:#F7F9FC;

    }

    div[data-testid="metric-container"]{

        background:white;

        padding:18px;

        border-radius:12px;

        box-shadow:0 3px 10px rgba(0,0,0,.08);

    }

    h1{

        color:#0B5394;

    }

    </style>

    """,

    unsafe_allow_html=True)
