import streamlit as st
import pandas as pd

from src.loader import load_data
from src.filters import sidebar_filters
from src.metrics import calculate_metrics
from src.charts import (
    plot_sales_week,
    plot_sales_type,
    plot_payment_method,
    plot_sales_tower,
    plot_price_type
)
from src.styles import load_css
from src.export import download_excel
from src.ai_summary import generate_summary

# --------------------------------------------------

st.set_page_config(
    page_title="AKILA Dashboard",
    page_icon="🏢",
    layout="wide"
)

load_css()

# --------------------------------------------------

df = load_data()

df = sidebar_filters(df)

metrics = calculate_metrics(df)

# --------------------------------------------------

st.title("🏢 Dashboard Comercial Proyecto AKILA")

st.caption("Transformación Digital e Inteligencia Artificial")

st.divider()

# --------------------------------------------------

c1,c2,c3,c4 = st.columns(4)

c1.metric(
    "Apartamentos Vendidos",
    metrics["vendidos"],
    metrics["delta_vendidos"]
)

c2.metric(
    "Disponibles",
    metrics["disponibles"]
)

c3.metric(
    "Valor Vendido",
    f"${metrics['valor_vendido']:,.0f}"
)

c4.metric(
    "% Proyecto Vendido",
    f"{metrics['avance']:.1f}%"
)

# --------------------------------------------------

c5,c6,c7,c8 = st.columns(4)

c5.metric(
    "Precio Promedio",
    f"${metrics['precio_promedio']:,.0f}"
)

c6.metric(
    "Precio Promedio m²",
    f"${metrics['precio_m2']:,.0f}"
)

c7.metric(
    "Tipos",
    metrics["tipos"]
)

c8.metric(
    "Valor Inventario",
    f"${metrics['inventario']:,.0f}"
)

st.divider()

# --------------------------------------------------

col1,col2 = st.columns(2)

with col1:

    st.plotly_chart(
        plot_sales_week(df),
        use_container_width=True
    )

with col2:

    st.plotly_chart(
        plot_sales_type(df),
        use_container_width=True
    )

# --------------------------------------------------

col3,col4 = st.columns(2)

with col3:

    st.plotly_chart(
        plot_payment_method(df),
        use_container_width=True
    )

with col4:

    st.plotly_chart(
        plot_sales_tower(df),
        use_container_width=True
    )

# --------------------------------------------------

st.plotly_chart(
    plot_price_type(df),
    use_container_width=True
)

# --------------------------------------------------

st.subheader("Resumen Ejecutivo")

summary = generate_summary(metrics)

st.info(summary)

# --------------------------------------------------

st.subheader("Detalle")

st.dataframe(
    df,
    use_container_width=True
)

# --------------------------------------------------

download_excel(df)

# --------------------------------------------------

st.caption("Proyecto desarrollado para AKILA")
