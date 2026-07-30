import plotly.express as px

def sales_per_week(df):

    vendidos = df[df.estado=="Vendido"].copy()

    vendidos["Semana"] = vendidos["fecha_venta"].dt.to_period("W").astype(str)

    resumen = vendidos.groupby("Semana").size().reset_index(name="Ventas")

    fig = px.line(

        resumen,

        x="Semana",

        y="Ventas",

        markers=True,

        title="Ventas por semana"

    )

    return fig


def sales_by_type(df):

    vendidos = df[df.estado=="Vendido"]

    resumen = vendidos.groupby(

        "tipo_apartamento"

    ).size().reset_index(name="Cantidad")

    fig = px.bar(

        resumen,

        x="tipo_apartamento",

        y="Cantidad",

        color="Cantidad",

        title="Ventas por tipo"

    )

    return fig

def payment_method(df):

    vendidos = df[df.estado=="Vendido"]

    resumen = vendidos.groupby(

        "forma_pago"

    ).size().reset_index(name="Cantidad")

    fig = px.pie(

        resumen,

        names="forma_pago",

        values="Cantidad",

        hole=.45,

        title="Forma de pago"

    )

    return fig

def tower_sales(df):

    vendidos = df[df.estado=="Vendido"]

    resumen = vendidos.groupby(

        "torre"

    ).size().reset_index(name="Ventas")

    fig = px.bar(

        resumen,

        x="torre",

        y="Ventas",

        color="Ventas",

        title="Ventas por torre"

    )

    return fig


def average_price(df):

    vendidos = df[df.estado=="Vendido"]

    resumen = vendidos.groupby(

        "tipo_apartamento"

    )["precio_cop"].mean().reset_index()

    fig = px.bar(

        resumen,

        x="tipo_apartamento",

        y="precio_cop",

        color="precio_cop",

        title="Precio promedio"

    )

    return fig

