import pandas as pd

def calculate_metrics(df):

    vendidos = df[df["estado"] == "Vendido"]

    disponibles = df[df["estado"] == "Disponible"]

    return {

        "total":

            len(df),

        "vendidos":

            len(vendidos),

        "disponibles":

            len(disponibles),

        "valor_vendido":

            vendidos["precio_cop"].sum(),

        "valor_disponible":

            disponibles["precio_cop"].sum(),

        "precio_promedio":

            vendidos["precio_cop"].mean(),

        "tipos":

            df["tipo_apartamento"].nunique(),

        "avance":

            len(vendidos) / len(df) * 100

    }
