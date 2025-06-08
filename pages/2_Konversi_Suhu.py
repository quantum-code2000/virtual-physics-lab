import streamlit as st

st.title('Konversi Suhu')
suhu_c = st.number_input('Suhu dalam Celcius (°C)', value=25.0)
suhu_f = suhu_c * 9/5 + 32
suhu_k = suhu_c + 273.15
suhu_r = suhu_c * 4/5
st.write(f'Fahrenheit: {suhu_f:.2f} °F')
st.write(f'Kelvin: {suhu_k:.2f} K')
st.write(f'Reamur: {suhu_r:.2f} °R')