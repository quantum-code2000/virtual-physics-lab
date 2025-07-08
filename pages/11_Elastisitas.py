import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(page_title='Elastisitas (Hukum Hooke)', layout='wide')
st.title('Simulasi Elastisitas - Hukum Hooke')
st.markdown('---')

st.subheader('Pilih variabel yang ingin dihitung')
hitung = st.selectbox('Hitung:', ['Gaya (F)', 'Konstanta Pegas (k)', 'Pertambahan Panjang (Δx)'])

# Variabel default
k, dx, F = 100.0, 0.05, 5.0

if hitung == 'Gaya (F)':
    k = st.number_input('Konstanta pegas (k) dalam N/m', value=100.0)
    dx = st.number_input('Pertambahan panjang (Δx) dalam meter', value=0.05)
    F = k * dx
    st.success(f'Gaya tarik F = {F:.2f} N')
elif hitung == 'Konstanta Pegas (k)':
    F = st.number_input('Gaya tarik (F) dalam N', value=10.0)
    dx = st.number_input('Pertambahan panjang (Δx) dalam meter', value=0.02)
    k = F / dx if dx != 0 else 0
    st.success(f'Konstanta pegas k = {k:.2f} N/m')
else:
    F = st.number_input('Gaya tarik (F) dalam N', value=15.0)
    k = st.number_input('Konstanta pegas (k) dalam N/m', value=300.0)
    dx = F / k if k != 0 else 0
    st.success(f'Pertambahan panjang Δx = {dx:.4f} m')

# Visualisasi pegas zig-zag
st.markdown('---')
st.subheader('Visualisasi Pegas Sebelum dan Sesudah Diberi Gaya')
def draw_spring(ax, x_center, y_start, y_end, color='blue', label='Pegas', turns=6):
    length = y_end - y_start
    y = np.linspace(y_start, y_end, 100)
    x = x_center + 0.05 * np.sin(2 * np.pi * turns * (y - y_start) / length)
    ax.plot(x, y, color=color, linewidth=2, label=label)

fig, ax = plt.subplots(figsize=(2, 5))
draw_spring(ax, x_center=0.2, y_start=0.2, y_end=1.5, color='gray', label='Pegas awal')
draw_spring(ax, x_center=0.5, y_start=0.2, y_end=1.5 + dx*10, color='blue', label='Pegas sesudah')
ax.set_xlim(-0.2, 0.8)
ax.set_ylim(0, 2.5)
ax.set_title('Pegas sebelum dan sesudah diberi gaya')
ax.axis('off')
ax.legend(loc='upper right')
st.pyplot(fig)

st.markdown('---')
st.caption('Disusun untuk pembelajaran Fisika SMA oleh Andy Kurniawan, S.Si - SMA Negeri 1 Dolopo')
