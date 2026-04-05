import pandas as pd
import plotly.express as px
import streamlit as st

# ── Configuración de página ──────────────────────────────────────────────────
st.set_page_config(
    page_title="Análisis de Anuncios de Vehículos",
    page_icon="🚗",
    layout="wide",
)

# ── Cargar datos ─────────────────────────────────────────────────────────────
@st.cache_data
def load_data():
    df = pd.read_csv("vehicles_us.csv")
    return df

car_data = load_data()

# ── Encabezado principal ─────────────────────────────────────────────────────
st.header("🚗 Análisis de Anuncios de Venta de Vehículos en EE. UU.")
st.markdown(
    "Explora el conjunto de datos de anuncios de vehículos usados. "
    "Selecciona las casillas de verificación para generar visualizaciones interactivas."
)

# ── Métricas rápidas ─────────────────────────────────────────────────────────
col1, col2, col3 = st.columns(3)
col1.metric("Total de anuncios", f"{len(car_data):,}")
col2.metric("Precio promedio", f"${car_data['price'].mean():,.0f}")
col3.metric("Odómetro promedio", f"{car_data['odometer'].mean():,.0f} mi")

st.divider()

# ── Histograma ───────────────────────────────────────────────────────────────
st.subheader("Distribución de valores")

build_histogram = st.checkbox("📊 Mostrar histograma del odómetro")

if build_histogram:
    st.write("Distribución del odómetro en los anuncios de vehículos")
    fig_hist = px.histogram(
        car_data,
        x="odometer",
        nbins=50,
        title="Distribución del Odómetro (millas recorridas)",
        labels={"odometer": "Odómetro (millas)", "count": "Cantidad de vehículos"},
        color_discrete_sequence=["#1f77b4"],
    )
    fig_hist.update_layout(bargap=0.05)
    st.plotly_chart(fig_hist, use_container_width=True)

# ── Gráfico de dispersión ────────────────────────────────────────────────────
st.subheader("Relación entre variables")

build_scatter = st.checkbox("📈 Mostrar gráfico de dispersión: Precio vs Odómetro")

if build_scatter:
    st.write("Relación entre el precio de venta y el odómetro del vehículo")

    # Filtrar valores extremos para mejorar la visualización
    df_filtered = car_data[
        (car_data["price"] > 500) &
        (car_data["price"] < 100_000) &
        (car_data["odometer"] > 0) &
        (car_data["odometer"] < 400_000)
    ]

    fig_scatter = px.scatter(
        df_filtered,
        x="odometer",
        y="price",
        color="condition",
        title="Precio vs Odómetro por Condición del Vehículo",
        labels={
            "odometer": "Odómetro (millas)",
            "price": "Precio (USD)",
            "condition": "Condición",
        },
        opacity=0.5,
        hover_data=["model", "model_year", "fuel"],
    )
    st.plotly_chart(fig_scatter, use_container_width=True)

# ── Gráfico adicional ────────────────────────────────────────────────────────
st.subheader("Análisis por tipo de vehículo")

build_bar = st.checkbox("🏷️ Mostrar precio promedio por tipo de vehículo")

if build_bar:
    st.write("Precio promedio según el tipo de vehículo")
    avg_price = (
        car_data.groupby("type")["price"]
        .mean()
        .reset_index()
        .sort_values("price", ascending=False)
    )
    fig_bar = px.bar(
        avg_price,
        x="type",
        y="price",
        title="Precio Promedio por Tipo de Vehículo",
        labels={"type": "Tipo de Vehículo", "price": "Precio Promedio (USD)"},
        color="price",
        color_continuous_scale="Blues",
    )
    st.plotly_chart(fig_bar, use_container_width=True)

# ── Vista de datos ───────────────────────────────────────────────────────────
st.divider()
show_data = st.checkbox("🗂️ Mostrar tabla de datos crudos")
if show_data:
    st.dataframe(car_data.head(100), use_container_width=True)
