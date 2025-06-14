import pandas as pd
import plotly.express as px
import streamlit as st


df = pd.read_csv('vehicles_us_clean.csv')

st.header('Información de la base de datos sobre los autos') # Titulo de la aplicacion
st.dataframe(df) # Se muestra el df en la aplicacion

#st.write('Tipos de vehiculos')
# Como hacer una tabla interactiva entre los tipos de vehiculo



st.write('Histograma por año del carro')
hist_button = st.button('Crear un histograma')
if hist_button:
     fig = px.histogram(df, x="model_year")
     st.plotly_chart(fig, use_container_width=True) #duda es correcto este codigo, que hace?



st.write('Relación precio/odómetro')
price_button = st.button('Crear gráfico precio/marca')
if price_button:
     st.scatter(df, x='odometer', y='price')
     st.plotly_chart(fig, use_container_width=True) # duda es correcto este codigo, que hace?



