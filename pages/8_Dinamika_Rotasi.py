import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title='Dinamika Rotasi', layout='wide')
st.title('Simulasi Dinamika Rotasi')
st.markdown('---')

st.subheader('Input Variabel')
hitung = st.selectbox('Pilih variabel yang ingin dihitung:', ['Torsi (τ)', 'Momen Inersia (I)', 'Percepatan Sudut (α)'])

if hitung == 'Torsi (τ)':
    I = st.number_input('Momen Inersia (I) kg·m²', value=2.0)
    alpha = st.number_input('Percepatan Sudut (α) rad/s²', value=3.0)
    tau = I * alpha
    st.success(f'Torsi τ = {tau:.2f} N·m')
elif hitung == 'Momen Inersia (I)':
    tau = st.number_input('Torsi (τ) N·m', value=10.0)
    alpha = st.number_input('Percepatan Sudut (α) rad/s²', value=2.0)
    I = tau / alpha if alpha != 0 else 0
    st.success(f'Momen Inersia I = {I:.2f} kg·m²')
else:
    tau = st.number_input('Torsi (τ) N·m', value=15.0)
    I = st.number_input('Momen Inersia (I) kg·m²', value=5.0)
    alpha = tau / I if I != 0 else 0
    st.success(f'Percepatan Sudut α = {alpha:.2f} rad/s²')

st.markdown('---')
st.subheader('Visualisasi Roda dan Torsi')
fig, ax = plt.subplots()
circle = plt.Circle((0, 0), 1, fill=False, color='gray', linestyle='--')
ax.add_artist(circle)
ax.arrow(0, 0, 0.7, 0, head_width=0.1, head_length=0.1, fc='blue', ec='blue')
ax.text(0.8, 0.1, 'τ', fontsize=12, color='blue')
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_aspect('equal')
ax.set_title('Torsi sebagai gaya rotasi pada roda')
ax.axis('off')
st.pyplot(fig)

st.markdown('---')
st.caption('Disusun untuk pembelajaran Fisika SMA oleh Andy Kurniawan, S.Si - SMA Negeri 1 Dolopo')
