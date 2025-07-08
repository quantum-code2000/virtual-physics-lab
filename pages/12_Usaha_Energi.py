import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(page_title='Usaha dan Energi', layout='wide')
st.title('Simulasi Usaha dan Energi')
st.markdown('---')

pilihan = st.radio('Pilih jenis perhitungan:', ['Usaha (W)', 'Energi Potensial (Ep)', 'Energi Kinetik (Ek)'])

if pilihan == 'Usaha (W)':
    F = st.number_input('Gaya (F) dalam N', value=10.0)
    s = st.number_input('Jarak perpindahan (s) dalam m', value=5.0)
    theta = st.number_input('Sudut antara gaya dan arah gerak (θ) dalam derajat', value=0.0)
    W = F * s * np.cos(np.radians(theta))
    st.success(f'Usaha: W = {W:.2f} Joule')

    fig, ax = plt.subplots()
    ax.arrow(0, 0, s, 0, head_width=1, head_length=0.5, fc='green', ec='green')
    ax.arrow(0, 0, F * np.cos(np.radians(theta))/2, F * np.sin(np.radians(theta))/2, 
             head_width=1, head_length=0.5, fc='blue', ec='blue')
    ax.text(s/2, 1.5, 's', color='green')
    ax.text(F * np.cos(np.radians(theta))/2, F * np.sin(np.radians(theta))/2 + 0.5, 'F', color='blue')
    ax.set_xlim(-1, max(6, s + 2))
    ax.set_ylim(-1, 5)
    ax.set_aspect('equal')
    ax.set_title('Visualisasi Usaha')
    ax.axis('off')
    st.pyplot(fig)

elif pilihan == 'Energi Potensial (Ep)':
    m = st.number_input('Massa (m) dalam kg', value=2.0)
    g = st.number_input('Percepatan gravitasi (g) dalam m/s²', value=9.8)
    h = st.number_input('Ketinggian (h) dalam meter', value=10.0)
    Ep = m * g * h
    st.success(f'Energi Potensial: Ep = {Ep:.2f} Joule')
    st.image('assets/energi_potensial.png', width=400)

else:
    m = st.number_input('Massa (m) dalam kg', value=1.5)
    v = st.number_input('Kecepatan (v) dalam m/s', value=4.0)
    Ek = 0.5 * m * v**2
    st.success(f'Energi Kinetik: Ek = {Ek:.2f} Joule')
    st.image('assets/energi_kinetik.png', width=400)

st.markdown('---')
st.caption('Disusun untuk pembelajaran Fisika SMA oleh Andy Kurniawan, S.Si - SMA Negeri 1 Dolopo')