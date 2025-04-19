import pandas as pd
import plotly.express as px
import streamlit as st

# Crear un encabezado para la aplicación
st.header('Análisis de datos de vehículos')

# Leer el archivo de datos
car_data = pd.read_csv('vehicles_us.csv')

# Botón para construir un histograma
hist_button = st.button('Construir histograma')

# Acción al presionar el botón del histograma
if hist_button:
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    # Crear un histograma con la columna "odometer"
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)  # Mostrar el histograma

# Botón para construir un gráfico de dispersión
scatter_button = st.button('Construir gráfico de dispersión')

# Acción al presionar el botón del gráfico de dispersión
if scatter_button:
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    fig = px.scatter(car_data, x="odometer", y="price", color="condition",
                     title="Relación entre el kilometraje y el precio")  # Crear gráfico de dispersión
    st.plotly_chart(fig, use_container_width=True)  # Mostrar el gráfico
