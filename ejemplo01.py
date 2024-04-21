import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


st.title("Ejemplo 01 con Streamlit")

st.write("## Familia Romero González")

# After st.sidebar:
a = st.sidebar.radio('Choose:',[1,2])

col1, col2 = st.columns(2)
col1.write("### Maric")
col2.write("### RRR")

st.write("* Tefi")
st.write("* RRG")

anios=[1956, 1962, 1976, 1991]
df = pd.DataFrame(anios)
st.write(df)

fig, ax=plt.subplots()
ax.bar([1, 2, 3, 4],anios)
st.pyplot(fig)

st.bar_chart(df)

col1.write(df)
col2.bar_chart(df)
