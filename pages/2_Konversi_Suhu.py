import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title='Konversi Suhu', layout='wide')
st.title('Simulasi Konversi Suhu')
st.markdown('---')

# Input suhu dan satuan asal
col1, col2 = st.columns(2)
with col1:
    nilai = st.number_input('Masukkan nilai suhu', value=25.0)
with col2:
    satuan = st.selectbox('Pilih satuan asal suhu', ['Celsius', 'Fahrenheit', 'Kelvin', 'Reamur'])

# Konversi berdasarkan satuan asal
if satuan == 'Celsius':
    c = nilai
    f = c * 9/5 + 32
    k = c + 273.15
    r = c * 4/5
elif satuan == 'Fahrenheit':
    f = nilai
    c = (f - 32) * 5/9
    k = c + 273.15
    r = c * 4/5
elif satuan == 'Kelvin':
    k = nilai
    c = k - 273.15
    f = c * 9/5 + 32
    r = c * 4/5
else:  # Reamur
    r = nilai
    c = r * 5/4
    f = c * 9/5 + 32
    k = c + 273.15

# Tampilkan hasil konversi
st.markdown('---')
st.subheader('Hasil Konversi Suhu')
col3, col4 = st.columns(2)
with col3:
    st.success(f'Celsius: {c:.2f} °C')
    st.info(f'Kelvin: {k:.2f} K')
with col4:
    st.warning(f'Fahrenheit: {f:.2f} °F')
    st.info(f'Reamur: {r:.2f} °R')

# Grafik visualisasi suhu
st.markdown('---')
st.subheader('Grafik Perbandingan Suhu')
labels = ['Celsius', 'Fahrenheit', 'Kelvin', 'Reamur']
values = [c, f, k, r]
colors = ['blue', 'red', 'green', 'orange']
fig, ax = plt.subplots()
bars = ax.bar(labels, values, color=colors)
ax.set_ylabel('Suhu')
ax.set_title('Visualisasi Konversi Suhu')
for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2.0, yval + 1, f'{yval:.1f}', ha='center')
st.pyplot(fig)
