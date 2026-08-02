# -*- coding: utf-8 -*-
import pandas as pd

def calculate_metrics(df):

    vendidos = df[df["estado"] == "Vendido"]

    disponibles = df[df["estado"] == "Disponible"]

    # ------------------------

    total = len(df)

    vendidos_total = len(vendidos)

    disponibles_total = len(disponibles)

    avance = 0

    if total > 0:

        avance = vendidos_total / total * 100

    # ------------------------

    valor_vendido = vendidos["precio_cop"].sum()

    inventario = disponibles["precio_cop"].sum()

    # ------------------------

    precio_promedio = vendidos["precio_cop"].mean()

    if pd.isna(precio_promedio):

        precio_promedio = 0

    # ------------------------

    precio_m2 = (vendidos["precio_cop"].sum() / vendidos["area_m2"].sum())

    if pd.isna(precio_m2):

        precio_m2 = 0

    # ------------------------

    tipos = df["tipo_apartamento"].nunique()

    # ------------------------
    # Delta semanal
    # ------------------------

    if len(vendidos) > 0:

        semanal = (vendidos.groupby("Semana").size().reset_index(name="Ventas"))

        if len(semanal) >= 2:

            actual = semanal.iloc[-1]["Ventas"]

            anterior = semanal.iloc[-2]["Ventas"]

            if anterior > 0:

                delta = ((actual-anterior) / anterior) * 100

            else:

                delta = 0

        else:

            delta = 0

    else:

        delta = 0

    return {

        "vendidos": vendidos_total,

        "disponibles": disponibles_total,

        "valor_vendido": valor_vendido,

        "inventario": inventario,

        "precio_promedio": precio_promedio,

        "precio_m2": precio_m2,

        "tipos": tipos,

        "avance": avance,

        "delta_vendidos": f"{delta:.1f}%"

    }
