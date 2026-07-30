import streamlit as st

def sidebar_filters(df):

    st.sidebar.title("Filtros")

    # ------------------------

    torre = st.sidebar.multiselect(

        "Torre",

        sorted(df["torre"].unique())

    )

    tipo = st.sidebar.multiselect(

        "Tipo apartamento",

        sorted(df["tipo_apartamento"].unique())

    )

    estado = st.sidebar.multiselect(

        "Estado",

        sorted(df["estado"].unique())

    )

    forma = st.sidebar.multiselect(

        "Forma pago",

        sorted(df["forma_pago"].unique())

    )

    # ------------------------

    if torre:

        df = df[
            df["torre"].isin(torre)
        ]

    if tipo:

        df = df[
            df["tipo_apartamento"].isin(tipo)
        ]

    if estado:

        df = df[
            df["estado"].isin(estado)
        ]

    if forma:

        df = df[
            df["forma_pago"].isin(forma)
        ]

    return df
