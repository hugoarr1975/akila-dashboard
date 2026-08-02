# -*- coding: utf-8 -*-
import streamlit as st

from src.utils import currency, percent
from src.metrics import calculate_metrics
from src.charts import (
    plot_sales_week,
    plot_sales_type,
    plot_sales_share,
    plot_payment_method,
    plot_sales_tower,
    plot_inventory,
    plot_price_type,
    plot_price_m2,
    plot_heatmap,
)

from src.export import download_excel
from src.ai_summary import generate_summary
from src.styles import section


def render_dashboard(df):
    """
    Construye todo el dashboard.
    """

    metrics = calculate_metrics(df)

    # =====================================================
    # KPIs
    # =====================================================

    section("📊 Indicadores Principales")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "Apartamentos Vendidos",
            metrics["vendidos"], #metrics["delta_vendidos"],
        )

    with c2:
        st.metric(
            "Disponibles",
            metrics["disponibles"],
        )

    with c3:
        st.metric(
            "Valor Vendido",
            currency(metrics["valor_vendido"]),
        )

    with c4:
        st.metric(
            "% Proyecto Vendido",
            percent(metrics["avance"]),
        )

    c5, c6, c7, c8 = st.columns(4)

    with c5:
        st.metric(
            "Precio Promedio",
            currency(metrics["precio_promedio"]),
        )

    with c6:
        st.metric(
            "Precio promedio m²",
            currency(metrics["precio_m2"]),
        )

    with c7:
        st.metric(
            "Tipos de apartamento",
            metrics["tipos"],
        )

    with c8:
        st.metric(
            "Inventario",
            currency(metrics["inventario"]),
        )

    st.divider()

    # =====================================================
    # GRÁFICOS
    # =====================================================

    section("📈 Análisis Comercial")

    col1, col2 = st.columns(2)

    with col1:
        st.plotly_chart(
            plot_sales_week(df),
            use_container_width=True,
        )

    with col2:
        st.plotly_chart(
            plot_sales_type(df),
            use_container_width=True,
        )

    col3, col4 = st.columns(2)

    with col3:
        st.plotly_chart(
            plot_payment_method(df),
            use_container_width=True,
        )

    with col4:
        st.plotly_chart(
            plot_sales_tower(df),
            use_container_width=True,
        )

    col5, col6 = st.columns(2)

    with col5:
        st.plotly_chart(
            plot_inventory(df),
            use_container_width=True,
        )

    with col6:
        st.plotly_chart(
            plot_sales_share(df),
            use_container_width=True,
        )

    st.plotly_chart(
        plot_price_type(df),
        use_container_width=True,
    )

    st.plotly_chart(
        plot_price_m2(df),
        use_container_width=True,
    )

    st.plotly_chart(
        plot_heatmap(df),
        use_container_width=True,
    )

    st.divider()

    # =====================================================
    # TABLA
    # =====================================================

    section("📋 Detalle de Apartamentos")

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True,
    )

    st.divider()

    # =====================================================
    # RESUMEN EJECUTIVO
    # =====================================================

    section("🤖 Resumen Ejecutivo")

    st.info(
        generate_summary(metrics)
    )

    st.divider()

    # =====================================================
    # EXPORTAR
    # =====================================================

    section("📥 Exportar Información")

    download_excel(df)