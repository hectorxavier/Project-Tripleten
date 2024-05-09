import streamlit as st
import pandas as pd
import plotly.express as pt

df_data =  pd.read_csv('vehicles_us.csv')
st.header('Aplicación Tripleten - Sprint 5')
hist_button = st.button('Construir Histograma')
disp_button = st.button('Construir Gráfico de Dispersión')

if hist_button:
    st.write('Creación de un histograma para el conjunto de datos')
    fig = pt.histogram(df_data, x = 'odometer')
    st.plotly_chart(fig, use_container_width=True)

if disp_button:
    st.write('Creación de un gráfico de dispersión')
    fig = pt.scatter(df_data, x = 'odometer')
    st.plotly_chart(fig, use_container_width=True)