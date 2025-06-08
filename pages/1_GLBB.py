import streamlit as st

st.title('Simulasi GLBB')
st.write('Masukkan percepatan (a) dan waktu (t):')
a = st.number_input('Percepatan (m/s²)', value=2.0)
t = st.number_input('Waktu (s)', value=3.0)
v = a * t
s = 0.5 * a * t ** 2
st.success(f'Kecepatan akhir: {v} m/s')
st.success(f'Jarak tempuh: {s} meter')