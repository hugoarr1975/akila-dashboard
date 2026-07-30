import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


COLOR_AKILA = "#0B5394"
COLOR_GREEN = "#2E8B57"
COLOR_RED = "#C0392B"


# ==========================================================
# VENTAS POR SEMANA
# ==========================================================

def plot_sales_week(df):

    vendidos = df[df["estado"] == "Vendido"].copy()

    if vendidos.empty:
        return go.Figure()

    ventas = (
        vendidos
        .groupby("Semana")
        .agg(
            Cantidad=("apartamento", "count"),
            Valor=("precio_cop", "sum")
        )
        .reset_index()
    )

    fig = px.line(
        ventas,
        x="Semana",
        y="Cantidad",
        markers=True,
        text="Cantidad",
        title="Ventas por Semana"
    )

    fig.update_traces(
        line=dict(width=4),
        marker=dict(size=10)
    )

    fig.update_layout(
        template="plotly_white",
        height=420,
        title_x=.02
    )

    return fig


# ==========================================================
# VENTAS POR TIPO
# ==========================================================

def plot_sales_type(df):

    vendidos = df[df["estado"] == "Vendido"]

    resumen = (
        vendidos
        .groupby("tipo_apartamento")
        .size()
        .reset_index(name="Cantidad")
        .sort_values("Cantidad")
    )

    fig = px.bar(
        resumen,
        x="Cantidad",
        y="tipo_apartamento",
        orientation="h",
        color="Cantidad",
        title="Tipos de Apartamentos Vendidos"
    )

    fig.update_layout(
        template="plotly_white",
        height=420
    )

    return fig


# ==========================================================
# PARTICIPACIÓN
# ==========================================================

def plot_sales_share(df):

    vendidos = df[df["estado"] == "Vendido"]

    resumen = (
        vendidos
        .groupby("tipo_apartamento")
        .size()
        .reset_index(name="Cantidad")
    )

    fig = px.pie(
        resumen,
        values="Cantidad",
        names="tipo_apartamento",
        hole=.55,
        title="Participación por Tipo"
    )

    fig.update_layout(height=420)

    return fig


# ==========================================================
# FORMA DE PAGO
# ==========================================================

def plot_payment_method(df):

    vendidos = df[df["estado"] == "Vendido"]

    resumen = (
        vendidos
        .groupby("forma_pago")
        .size()
        .reset_index(name="Cantidad")
    )

    fig = px.pie(
        resumen,
        names="forma_pago",
        values="Cantidad",
        hole=.45,
        title="Forma de Pago"
    )

    fig.update_layout(height=420)

    return fig


# ==========================================================
# TORRES
# ==========================================================

def plot_sales_tower(df):

    vendidos = df[df["estado"] == "Vendido"]

    resumen = (
        vendidos
        .groupby("torre")
        .size()
        .reset_index(name="Ventas")
    )

    fig = px.bar(
        resumen,
        x="torre",
        y="Ventas",
        color="Ventas",
        title="Ventas por Torre"
    )

    fig.update_layout(
        template="plotly_white",
        height=420
    )

    return fig


# ==========================================================
# INVENTARIO
# ==========================================================

def plot_inventory(df):

    disponibles = df[df["estado"] == "Disponible"]

    resumen = (
        disponibles
        .groupby("torre")
        .size()
        .reset_index(name="Disponibles")
    )

    fig = px.bar(
        resumen,
        x="torre",
        y="Disponibles",
        color="Disponibles",
        title="Inventario Disponible"
    )

    fig.update_layout(height=420)

    return fig


# ==========================================================
# PRECIO PROMEDIO
# ==========================================================

def plot_price_type(df):

    vendidos = df[df["estado"] == "Vendido"]

    resumen = (
        vendidos
        .groupby("tipo_apartamento")["precio_cop"]
        .mean()
        .reset_index()
    )

    fig = px.bar(
        resumen,
        x="tipo_apartamento",
        y="precio_cop",
        color="precio_cop",
        title="Precio Promedio por Tipo"
    )

    fig.update_layout(
        template="plotly_white",
        height=420
    )

    return fig


# ==========================================================
# PRECIO POR M²
# ==========================================================

def plot_price_m2(df):

    vendidos = df[df["estado"] == "Vendido"].copy()

    vendidos["precio_m2"] = (
        vendidos["precio_cop"] /
        vendidos["area_m2"]
    )

    resumen = (
        vendidos
        .groupby("tipo_apartamento")["precio_m2"]
        .mean()
        .reset_index()
    )

    fig = px.bar(
        resumen,
        x="tipo_apartamento",
        y="precio_m2",
        color="precio_m2",
        title="Precio Promedio por m²"
    )

    fig.update_layout(height=420)

    return fig


# ==========================================================
# HEATMAP
# ==========================================================

def plot_heatmap(df):

    vendidos = df[df["estado"] == "Vendido"]

    tabla = pd.pivot_table(
        vendidos,
        values="apartamento",
        index="piso",
        columns="torre",
        aggfunc="count",
        fill_value=0
    )

    fig = px.imshow(
        tabla,
        aspect="auto",
        text_auto=True,
        title="Mapa de Calor de Ventas"
    )

    fig.update_layout(height=500)

    return fig
