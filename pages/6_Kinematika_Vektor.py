import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title='Kinematika Vektor', layout='wide')
st.title('Simulasi Kinematika Gerak dengan Analisis Vektor')
st.markdown('---')

# Input posisi awal dan akhir
st.subheader('Input Vektor Posisi')
x1 = st.number_input('Posisi awal x₁ (m)', value=0.0)
y1 = st.number_input('Posisi awal y₁ (m)', value=0.0)
x2 = st.number_input('Posisi akhir x₂ (m)', value=4.0)
y2 = st.number_input('Posisi akhir y₂ (m)', value=3.0)
dt = st.number_input('Selang waktu (Δt) dalam detik', value=2.0)

# Perhitungan vektor
dx = x2 - x1
dy = y2 - y1
dr = np.sqrt(dx**2 + dy**2)
vx = dx / dt
vy = dy / dt
v = np.sqrt(vx**2 + vy**2)
arah = np.degrees(np.arctan2(dy, dx))

st.markdown('---')
st.subheader('Hasil Perhitungan Vektor')
st.success(f'Vektor perpindahan Δr: ({dx:.2f}, {dy:.2f}) m')
st.success(f'Besarnya perpindahan: {dr:.2f} m')
st.info(f'Vektor kecepatan v: ({vx:.2f}, {vy:.2f}) m/s')
st.info(f'Kelajuan: {v:.2f} m/s')
st.warning(f'Arah gerak: {arah:.2f}° dari sumbu x positif')

# Visualisasi vektor
st.markdown('---')
st.subheader('Visualisasi Vektor')
fig, ax = plt.subplots()
ax.quiver(x1, y1, dx, dy, angles='xy', scale_units='xy', scale=1, color='red', label='Δr')
ax.quiver(x1, y1, vx, vy, angles='xy', scale_units='xy', scale=1, color='blue', label='v')
ax.plot([x1, x2], [y1, y2], 'ko--', label='Lintasan')
ax.set_xlim(min(x1, x2) - 1, max(x1, x2) + 2)
ax.set_ylim(min(y1, y2) - 1, max(y1, y2) + 2)
ax.set_xlabel('x (m)')
ax.set_ylabel('y (m)')
ax.set_title('Diagram Vektor Perpindahan dan Kecepatan')
ax.grid(True)
ax.set_aspect('equal')
ax.legend()
st.pyplot(fig)

st.markdown('---')
st.caption('Disusun untuk pembelajaran Fisika SMA oleh Andy Kurniawan, S.Si - SMA Negeri 1 Dolopo')
