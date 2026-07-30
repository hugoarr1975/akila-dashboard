import streamlit as st

from src.loader import load_data
from src.metrics import calculate_metrics
from src.styles import load_css

from src.charts import *

st.set_page_config(

    page_title="AKILA Dashboard",

    layout="wide"

)

load_css()

df = load_data()

metricas = calculate_metrics(df)

st.title("🏢 Dashboard Comercial - Proyecto AKILA")

st.markdown("---")
