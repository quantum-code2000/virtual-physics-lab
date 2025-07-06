import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(page_title='Simulasi GLBB', layout='wide')
st.title('Simulasi Gerak Lurus Berubah Beraturan (GLBB)')
st.markdown('---')
st.write('Masukkan parameter di bawah ini untuk melihat hasil simulasi:')

col1, col2 = st.columns(2)
with col1:
    v0 = st.number_input('Kecepatan awal (v₀) dalam m/s', value=0.0)
    a = st.number_input('Percepatan (a) dalam m/s²', value=2.0)
with col2:
    t = st.number_input('Waktu (t) dalam detik', value=5.0)
    satuan = st.selectbox('Tampilkan waktu dalam', ['detik'])

v = v0 + a * t
s = v0 * t + 0.5 * a * t**2

st.markdown('---')
st.subheader('Hasil Perhitungan')
st.success(f'Kecepatan akhir: {v:.2f} m/s')
st.success(f'Jarak tempuh: {s:.2f} meter')

st.markdown('---')
st.subheader('Grafik Simulasi')
time = np.linspace(0, t, num=100)
velocity = v0 + a * time
position = v0 * time + 0.5 * a * time**2

tab1, tab2 = st.tabs(['Grafik Kecepatan vs Waktu', 'Grafik Jarak vs Waktu'])
with tab1:
    fig1, ax1 = plt.subplots()
    ax1.plot(time, velocity, color='blue', label='v(t)')
    ax1.set_xlabel('Waktu (s)')
    ax1.set_ylabel('Kecepatan (m/s)')
    ax1.set_title('Grafik Kecepatan vs Waktu')
    ax1.grid(True)
    st.pyplot(fig1)
with tab2:
    fig2, ax2 = plt.subplots()
    ax2.plot(time, position, color='green', label='s(t)')
    ax2.set_xlabel('Waktu (s)')
    ax2.set_ylabel('Jarak (m)')
    ax2.set_title('Grafik Jarak vs Waktu')
    ax2.grid(True)
    st.pyplot(fig2)
