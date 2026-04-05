#  Análisis de Anuncios de Venta de Vehículos en EE. UU.

## Descripción del proyecto

Esta aplicación web interactiva permite explorar y visualizar un conjunto de datos de anuncios de venta de vehículos usados en los Estados Unidos. El objetivo es identificar patrones en el mercado de coches de segunda mano, como la relación entre el precio y el odómetro, la distribución de precios por tipo de vehículo o el tiempo promedio que un anuncio permanece activo.

## Funcionalidades de la aplicación

- **Métricas rápidas**: resumen del total de anuncios, precio promedio y odómetro promedio.
- **Histograma del odómetro**: visualización de la distribución de millas recorridas entre los vehículos listados.
- **Gráfico de dispersión**: relación entre el precio de venta y el odómetro, segmentado por condición del vehículo.
- **Precio promedio por tipo**: gráfico de barras que compara el precio promedio entre distintos tipos de vehículo (SUV, pickup, sedan, etc.).
- **Vista de datos**: tabla interactiva con los primeros 100 registros del dataset.

## Tecnologías utilizadas

- [Python 3](https://www.python.org/)
- [Streamlit](https://streamlit.io/) – framework para la aplicación web
- [Pandas](https://pandas.pydata.org/) – manipulación de datos
- [Plotly Express](https://plotly.com/python/plotly-express/) – visualizaciones interactivas

## Estructura del proyecto

```
.
├── README.md
├── app.py
├── vehicles_us.csv
├── requirements.txt
└── notebooks
    └── EDA.ipynb
```

## Cómo ejecutar la aplicación localmente

1. Clona el repositorio:
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd <NOMBRE_DEL_REPOSITORIO>
   ```

2. Crea y activa un entorno virtual:
   ```bash
   python -m venv vehicles_env
   source vehicles_env/bin/activate   # macOS/Linux
   vehicles_env\Scripts\activate      # Windows
   ```

3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

4. Ejecuta la aplicación:
   ```bash
   streamlit run app.py
   ```

5. Abre tu navegador en `http://localhost:8501`

## Despliegue

La aplicación está desplegada en [Render](https://render.com) y es accesible de forma pública en:

```
https://<APP_NAME>.onrender.com
```
