# -*- coding: utf-8 -*-
import streamlit as st
from src.loader import load_data
from src.filters import sidebar_filters
from src.dashboard import render_dashboard
from src.styles import load_css, page_header

st.set_page_config( page_title="AKILA Dashboard",
                    page_icon="🏢", layout="wide")
load_css()
page_header()
df = load_data()
df = sidebar_filters(df)
render_dashboard(df)
