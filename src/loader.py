import pandas as pd

def load_data():

    df = pd.read_csv("data/apartamentos_akila.csv")

    df["fecha_venta"] = pd.to_datetime(
        df["fecha_venta"],
        errors="coerce"
    )

    df["fecha_entrega"] = pd.to_datetime(
        df["fecha_entrega"],
        errors="coerce"
    )

    return df
