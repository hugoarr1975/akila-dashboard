# -*- coding: utf-8 -*-
import pandas as pd
import streamlit as st


@st.cache_data
def load_data():

    df = pd.read_csv(
        "data/apartamentos_akila.csv"
    )

    # ------------------------
    # Fechas
    # ------------------------

    df["fecha_venta"] = pd.to_datetime(
        df["fecha_venta"],
        errors="coerce"
    )

    df["fecha_entrega"] = pd.to_datetime(
        df["fecha_entrega"],
        errors="coerce"
    )
    
    df["semana"] = df["fecha_venta"].dt.isocalendar().week
    

    # ------------------------
    # Valores nulos
    # ------------------------

    columnas_texto = [
        "estado",
        "forma_pago",
        "tipo_apartamento",
        "torre"
    ]

    for c in columnas_texto:
        df[c] = df[c].fillna("No aplica")

    columnas_numero = [
        "precio_cop",
        "area_m2",
        "monto_credito_cop",
        "monto_contado_cop",
        "porcentaje_credito"
    ]

    for c in columnas_numero:
        df[c] = df[c].fillna(0)

    # ------------------------
    # Eliminar duplicados
    # ------------------------

    df = df.drop_duplicates()

    # ------------------------
    # Columnas auxiliares
    # ------------------------

    df["Semana"] = (
        df["fecha_venta"]
        .dt.to_period("W")
        .astype(str)
    )

    df["Mes"] = (
        df["fecha_venta"]
        .dt.strftime("%Y-%m")
    )

    df["Año"] = (
        df["fecha_venta"]
        .dt.year
    )

    return df
