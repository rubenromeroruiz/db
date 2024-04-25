import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# Título del dashboard
st.title('Ejemplo de Dashboard con Streamlit')

# Datos de ejemplo
np.random.seed(0)
dates = pd.date_range('20220101', periods=100)
data = pd.DataFrame(np.random.randn(100, 3), index=dates, columns=['A', 'B', 'C'])

# Gráfico de líneas con matplotlib
st.subheader('Gráfico de Líneas (Matplotlib)')
st.line_chart(data)

# Gráfico interactivo de dispersión con plotly
st.subheader('Gráfico de Dispersión Interactivo (Plotly)')
fig = px.scatter(x=[0, 1, 2, 3, 4, 5, 6, 7], y=[0, 1, 4, 9, 16, 25, 36, 42])
st.plotly_chart(fig)

# Agregar sección para mostrar datos tabulares
st.subheader('Datos Tabulares')
st.write(data)

# Agregar controles interactivos (por ejemplo, slider)
st.sidebar.title('Configuración')
selected_variable = st.sidebar.selectbox('Selecciona una variable:', ('A', 'B', 'C'))

# Gráfico de barras interactivo basado en la selección
st.subheader('Gráfico de Barras Interactivo')
fig_bar = px.histogram(data, x=selected_variable)
st.plotly_chart(fig_bar)

# Agregar un mapa de calor con matplotlib
st.subheader('Mapa de Calor (Matplotlib)')
plt.figure(figsize=(8, 6))
plt.imshow(data.corr(), cmap='viridis', interpolation='nearest')
plt.colorbar()
plt.title('Matriz de Correlación')
st.pyplot(plt)

# Agregar un widget de texto para comentarios
st.subheader('Comentarios')
comment = st.text_area('Escribe tus comentarios aquí...', height=100)
st.write('Comentario guardado:', comment)
