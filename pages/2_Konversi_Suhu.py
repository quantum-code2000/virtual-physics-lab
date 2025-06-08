import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title='Konversi Suhu', layout='wide')
st.title('Simulasi Konversi Suhu')
st.markdown('---')
st.write('Masukkan suhu dalam salah satu satuan, dan lihat hasil konversi ke satuan lainnya:')

col1, col2 = st.columns(2)
with col1:
    suhu = st.number_input('Nilai suhu', value=25.0)
    satuan_asal = st.selectbox('Satuan asal suhu', ['Celsius', 'Fahrenheit', 'Kelvin', 'Reamur'])

with col2:
    if satuan_asal == 'Celsius':
        c = suhu
        f = c * 9/5 + 32
        k = c + 273.15
        r = c * 4/5
    elif satuan_asal == 'Fahrenheit':
        f = suhu
        c = (f - 32) * 5/9
        k = c + 273.15
        r = c * 4/5
    elif satuan_asal == 'Kelvin':
        k = suhu
        c = k - 273.15
        f = c * 9/5 + 32
        r = c * 4/5
    else:
        r = suhu
        c = r * 5/4
        f = c * 9/5 + 32
        k = c + 273.15

st.markdown('---')
st.subheader('Hasil Konversi')
col3, col4 = st.columns(2)
with col3:
    st.success(f'Celsius: {c:.2f} °C')
    st.success(f'Kelvin: {k:.2f} K')
with col4:
    st.info(f'Fahrenheit: {f:.2f} °F')
    st.info(f'Reamur: {r:.2f} °R')

st.markdown('---')
st.subheader('Grafik Visualisasi Suhu')
labels = ['Celsius', 'Fahrenheit', 'Kelvin', 'Reamur']
values = [c, f, k, r]
colors = ['blue', 'red', 'green', 'orange']
fig, ax = plt.subplots()
bars = ax.bar(labels, values, color=colors)
ax.set_ylabel('Suhu')
ax.set_title('Visualisasi Hasil Konversi Suhu')
st.pyplot(fig)
