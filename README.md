# 🏗️ Akila - Dashboard de Ventas

Dashboard interactivo para el seguimiento comercial del proyecto inmobiliario Akila. 
Construido con Python + Streamlit + Plotly.

## ¿Qué hace esta solución?

Este dashboard permite a la dirección de Akila visualizar en tiempo real:

- **📊 Estado General:** KPIs de unidades vendidas, disponibles, ingresos totales, precio promedio y variedad de producto.
- **📈 Ventas por Semana:** Evolución temporal de unidades vendidas y valor acumulado por semana.
- **🏠 Tipos de Apartamento Vendidos:** Tabla con unidades, % sobre ventas, valor total, precio y área promedio por tipo. Incluye gráfico de dona.
- **🏢 Disponibles vs Vendidos por Torre:** Inventario restante por tipo de apartamento y valor vendido por torre.
- **💰 Análisis Financiero:** Distribución de forma de pago (contado vs crédito).
- **📋 Inventario Detallado:** Tabla filtrable con todos los apartamentos, estados, fechas y montos.

## 🚀 ¿Cómo ejecutar?

### 1. Clonar el repositorio

```bash
git clone https://github.com/hugoarr1975/akila-dashboard.git
cd akila-dashboard

```bash
python -m venv venv

```bash
venv\Scripts\activate

```bash
pip install -r requirements.txt

```bash
streamlit run app.py
