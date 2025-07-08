import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(page_title='Gerak Lurus (GLB & GLBB)', layout='wide')
st.title('Simulasi Gerak Lurus: GLB & GLBB')
st.markdown('---')

jenis = st.radio('Pilih jenis gerak:', ['Gerak Lurus Beraturan (GLB)', 'Gerak Lurus Berubah Beraturan (GLBB)'])
if jenis == 'Gerak Lurus Beraturan (GLB)':
    st.subheader('Rumus GLB: s = v × t')
    v = st.number_input('Kecepatan (v) m/s', value=10.0)
    t = st.number_input('Waktu (t) s', value=5.0)
    s = v * t
    st.success(f'Jarak tempuh: {s:.2f} meter')
    st.subheader('Grafik GLB')
    t_vals = np.linspace(0, t, 100)
    s_vals = v * t_vals
    fig, ax = plt.subplots()
    ax.plot(t_vals, s_vals, label='s = v × t', color='blue')
    ax.set_xlabel('Waktu (s)')
    ax.set_ylabel('Jarak (m)')
    ax.set_title('Grafik Jarak vs Waktu (GLB)')
    ax.grid(True)
    st.pyplot(fig)
else:
    st.subheader('Rumus GLBB: s = v₀t + ½at², v = v₀ + at')
    v0 = st.number_input('Kecepatan awal (v₀) m/s', value=0.0)
    a = st.number_input('Percepatan (a) m/s²', value=2.0)
    t = st.number_input('Waktu (t) s', value=5.0)
    s = v0 * t + 0.5 * a * t ** 2
    v = v0 + a * t
    st.success(f'Jarak tempuh: {s:.2f} meter')
    st.info(f'Kecepatan akhir: {v:.2f} m/s')
    st.subheader('Grafik GLBB')
    t_vals = np.linspace(0, t, 100)
    s_vals = v0 * t_vals + 0.5 * a * t_vals**2
    v_vals = v0 + a * t_vals

    tab1, tab2 = st.tabs(['Jarak vs Waktu', 'Kecepatan vs Waktu'])
    with tab1:
        fig1, ax1 = plt.subplots()
        ax1.plot(t_vals, s_vals, color='green')
        ax1.set_xlabel('Waktu (s)')
        ax1.set_ylabel('Jarak (m)')
        ax1.set_title('Grafik Jarak vs Waktu (GLBB)')
        ax1.grid(True)
        st.pyplot(fig1)
    with tab2:
        fig2, ax2 = plt.subplots()
        ax2.plot(t_vals, v_vals, color='orange')
        ax2.set_xlabel('Waktu (s)')
        ax2.set_ylabel('Kecepatan (m/s)')
        ax2.set_title('Grafik Kecepatan vs Waktu (GLBB)')
        ax2.grid(True)
        st.pyplot(fig2)

st.markdown('---')
st.caption('Disusun untuk pembelajaran Fisika SMA oleh Pak Andy Kurniawan, S.Si - SMA Negeri 1 Dolopo')
