# -*- coding: utf-8 -*-
#from datetime import datetime
import pandas as pd


def currency(value):
    """
    Formatea valores monetarios en formato cop.
    Ejemplo:
    174741800000 -> $174.741.800.000
    """

    if pd.isna(value):
        return "$0"

    return f"${value:,.0f}".replace(",", ".")


def percent(value, decimals=1):
    """
    Formatea porcentajes.
    Ejemplo:
    59.34 -> 59.3 %
    """

    if pd.isna(value):
        return "0 %"

    return f"{value:.{decimals}f} %"


def format_number(value):
    """
    Formatea números enteros.
    Ejemplo:
    15432 -> 15.432
    """

    if pd.isna(value):
        return "0"

    return f"{value:,.0f}".replace(",", ".")


def safe_division(numerator, denominator):
    """
    Evita división por cero.
    """

    if denominator == 0:
        return 0

    return numerator / denominator


def date_format(date):
    """
    Convierte fechas al formato cop.
    """

    if pd.isna(date):
        return ""

    if isinstance(date, str):
        date = pd.to_datetime(date)

    return date.strftime("%d/%m/%Y")