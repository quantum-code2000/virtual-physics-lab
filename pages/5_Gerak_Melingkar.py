import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(page_title='Gerak Melingkar', layout='wide')
st.title('Simulasi Gerak Melingkar')
st.markdown('---')

st.subheader('Input Variabel')
r = st.number_input('Jari-jari lintasan (r) dalam meter', value=2.0)
omega = st.number_input('Kecepatan sudut (ω) dalam rad/s', value=1.5)
t = st.number_input('Waktu (t) dalam detik', value=5.0)

# Perhitungan
theta = omega * t  # sudut tempuh (rad)
s = r * theta      # panjang lintasan (m)
v = r * omega      # kecepatan linear (m/s)
a = r * omega**2   # percepatan sentripetal (m/s^2)
T = 2 * np.pi / omega  # periode (s)
f = 1 / T               # frekuensi (Hz)

# Output
st.subheader('Hasil Perhitungan')
st.success(f'Sudut tempuh (θ): {theta:.2f} rad')
st.success(f'Panjang lintasan (s): {s:.2f} m')
st.info(f'Kecepatan linear (v): {v:.2f} m/s')
st.info(f'Percepatan sentripetal (a): {a:.2f} m/s²')
st.warning(f'Periode (T): {T:.2f} s')
st.warning(f'Frekuensi (f): {f:.2f} Hz')

# Visualisasi lintasan melingkar dan posisi
st.markdown('---')
st.subheader('Visualisasi Gerak Melingkar')
theta_vals = np.linspace(0, theta, 500)
x_vals = r * np.cos(theta_vals)
y_vals = r * np.sin(theta_vals)

fig, ax = plt.subplots()
ax.plot(x_vals, y_vals, label='Lintasan', color='blue')
ax.plot([0, x_vals[-1]], [0, y_vals[-1]], 'ro', label='Posisi Akhir')
circle = plt.Circle((0, 0), r, color='gray', linestyle='--', fill=False)
ax.add_patch(circle)
ax.set_aspect('equal')
ax.set_xlabel('x (m)')
ax.set_ylabel('y (m)')
ax.grid(True)
ax.set_title('Lintasan Gerak Melingkar')
ax.legend()
st.pyplot(fig)

st.markdown('---')
st.caption('Disusun untuk pembelajaran Fisika SMA oleh Andy Kurniawan, S.Si - SMA Negeri 1 Dolopo')
