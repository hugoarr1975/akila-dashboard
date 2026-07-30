from src.loader import load_data

from src.filters import sidebar_filters

from src.dashboard import render_dashboard

from src.styles import load_css

import streamlit as st

st.set_page_config(

    page_title="AKILA",

    layout="wide"

)

load_css()

df = load_data()

df = sidebar_filters(df)

render_dashboard(df)
