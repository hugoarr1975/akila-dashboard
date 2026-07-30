import streamlit as st

def load_css():
    """
    Carga los estilos CSS personalizados para el Dashboard AKILA.
    """

    st.markdown(
        """
<style>

/* ===========================================================
   FONDO GENERAL
=========================================================== */

.stApp{
    background-color:#F5F7FA;
}


/* ===========================================================
   TITULO
=========================================================== */

h1{
    color:#0B5394;
    font-weight:700;
}

h2,h3{
    color:#0B5394;
}


/* ===========================================================
   SIDEBAR
=========================================================== */

section[data-testid="stSidebar"]{
    background:#0B5394;
}

section[data-testid="stSidebar"] *{
    color:white;
}


/* ===========================================================
   KPI
=========================================================== */

div[data-testid="metric-container"]{

    background:white;

    border-radius:15px;

    padding:18px;

    border:1px solid #E5E7EB;

    box-shadow:0px 3px 10px rgba(0,0,0,.08);

    transition:.3s;
}


div[data-testid="metric-container"]:hover{

    transform:translateY(-3px);

    box-shadow:0px 10px 25px rgba(0,0,0,.12);

}


div[data-testid="metric-container"] label{

    color:#0B5394;

    font-weight:600;

    font-size:15px;

}


div[data-testid="metric-container"] div{

    font-size:26px;

}


/* ===========================================================
   BOTONES
=========================================================== */

.stButton>button{

    background:#0B5394;

    color:white;

    border:none;

    border-radius:8px;

    font-weight:bold;

    height:45px;

}

.stButton>button:hover{

    background:#1976D2;

    color:white;

}


/* ===========================================================
   DOWNLOAD BUTTON
=========================================================== */

.stDownloadButton>button{

    background:#2E8B57;

    color:white;

    border:none;

    border-radius:8px;

    font-weight:bold;

}

.stDownloadButton>button:hover{

    background:#3CB371;

}


/* ===========================================================
   DATAFRAME
=========================================================== */

div[data-testid="stDataFrame"]{

    border-radius:12px;

    border:1px solid #EAEAEA;

    background:white;

}


/* ===========================================================
   INFO BOX
=========================================================== */

div[data-testid="stAlert"]{

    border-radius:12px;

}


/* ===========================================================
   EXPANDER
=========================================================== */

details{

    background:white;

    border-radius:12px;

    padding:8px;

}


/* ===========================================================
   PLOTLY
=========================================================== */

.js-plotly-plot{

    border-radius:12px;

}


/* ===========================================================
   TABS
=========================================================== */

button[data-baseweb="tab"]{

    font-size:15px;

    font-weight:600;

}


/* ===========================================================
   SCROLLBAR
=========================================================== */

::-webkit-scrollbar{

    width:10px;

}

::-webkit-scrollbar-track{

    background:#ECECEC;

}

::-webkit-scrollbar-thumb{

    background:#0B5394;

    border-radius:20px;

}


/* ===========================================================
   FOOTER
=========================================================== */

footer{

    visibility:hidden;

}

header{

    visibility:hidden;

}


/* ===========================================================
   SEPARADORES
=========================================================== */

hr{

    margin-top:20px;

    margin-bottom:20px;

}


/* ===========================================================
   TITULOS DE GRAFICOS
=========================================================== */

.plot-container .gtitle{

    font-weight:bold !important;

    font-size:18px !important;

}


/* ===========================================================
   RESPONSIVE
=========================================================== */

@media (max-width:768px){

    div[data-testid="metric-container"]{

        padding:10px;

    }

}

</style>
""",
        unsafe_allow_html=True,
    )


def page_header():
    """
    Encabezado principal del dashboard.
    """

    st.markdown(
        """
        <div style="
            background: linear-gradient(90deg,#0B5394,#1976D2);
            padding:18px;
            border-radius:15px;
            margin-bottom:20px;
        ">
            <h1 style="
                color:white;
                text-align:center;
                margin:0;
            ">
            🏢 Dashboard Comercial Proyecto AKILA
            </h1>

            <p style="
                color:white;
                text-align:center;
                margin-top:10px;
                font-size:18px;
            ">
            Transformación Digital • Analítica • Inteligencia Artificial
            </p>

        </div>
        """,
        unsafe_allow_html=True,
    )


def section(title):
    """
    Crea un encabezado para cada sección.
    """

    st.markdown(
        f"""
        <h3 style="
            color:#0B5394;
            margin-top:30px;
            margin-bottom:15px;
        ">
        {title}
        </h3>
        """,
        unsafe_allow_html=True,
    )


def success_box(texto):

    st.markdown(
        f"""
        <div style="
            background:#E8F5E9;
            border-left:6px solid #2E8B57;
            padding:15px;
            border-radius:8px;
            margin-bottom:15px;
        ">

        {texto}

        </div>
        """,
        unsafe_allow_html=True,
    )


def warning_box(texto):

    st.markdown(
        f"""
        <div style="
            background:#FFF8E1;
            border-left:6px solid #F9A825;
            padding:15px;
            border-radius:8px;
            margin-bottom:15px;
        ">

        {texto}

        </div>
        """,
        unsafe_allow_html=True,
    )


def error_box(texto):

    st.markdown(
        f"""
        <div style="
            background:#FDECEA;
            border-left:6px solid #C62828;
            padding:15px;
            border-radius:8px;
            margin-bottom:15px;
        ">

        {texto}

        </div>
        """,
        unsafe_allow_html=True,
    )
