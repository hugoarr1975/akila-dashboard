# -*- coding: utf-8 -*-
import io
import streamlit as st
import pandas as pd


def download_excel(df: pd.DataFrame):
    """
    Genera un archivo Excel con la información filtrada
    y muestra el botón de descarga.
    """

    output = io.BytesIO()

    with pd.ExcelWriter(output, engine="openpyxl") as writer:
        df.to_excel(
            writer,
            sheet_name="Apartamentos",
            index=False
        )

    output.seek(0)

    st.download_button(
        label="📥 Descargar Reporte en Excel",
        data=output,
        file_name="reporte_apartamentos.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        use_container_width=True
    )

