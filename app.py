import pandas as pd
import plotly.express as px
import streamlit as st


df = pd.read_csv('vehicles_us_clean.csv')

st.header('Información de la base de datos sobre los autos') # Titulo de la aplicacion
st.dataframe(df) # Se muestra el df en la aplicacion

#st.write('Tipos de vehiculos')
# Como hacer una tabla interactiva entre los tipos de vehiculo



st.write('Histograma vehicular relacionado con el año')
hist_button = st.button('Crear un histograma')
if hist_button:
     fig_hist = px.histogram(df, x="model_year")
     st.plotly_chart(fig_hist, use_container_width=True) #Se crea un histograma con forme al año
     




st.write('Relación Precio/Odómetro')
price_button = st.button('Crear gráfico precio/marca')
if price_button:
    fig_dis = px.scatter_chart(df, x='odometer', y='price')
    px.plotly_chart(fig_dis, use_container_width=True) # Se crea un gráfico de dispersion entre el precio y el kilometraje



