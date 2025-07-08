import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(page_title='Elastisitas (Hukum Hooke)', layout='wide')
st.title('Simulasi Elastisitas - Hukum Hooke')
st.markdown('---')

st.subheader('Pilih variabel yang ingin dihitung')
hitung = st.selectbox('Hitung:', ['Gaya (F)', 'Konstanta Pegas (k)', 'Pertambahan Panjang (Δx)'])

# Default nilai
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

st.markdown('---')
st.subheader('Visualisasi Pegas Skala Realistis')

def draw_spring(ax, x, y0, length, color, label):
    y = np.linspace(y0, y0 + length, 120)
    zigzag = 0.05 * np.sin(15 * np.pi * (y - y0) / length)
    ax.plot(x + zigzag, y, color=color, linewidth=2, label=label)

y0 = 0.5
panjang_awal = 1.0
panjang_akhir = panjang_awal + dx

fig, ax = plt.subplots(figsize=(3, 6))
draw_spring(ax, 0.2, y0, panjang_awal, 'gray', 'Pegas awal')
draw_spring(ax, 0.5, y0, panjang_akhir, 'blue', 'Pegas sesudah')

# Tambah label dan garis skala
ax.annotate(f'{panjang_awal:.2f} m', (0.05, y0 + panjang_awal/2), fontsize=9)
ax.annotate(f'{dx:.2f} m', (0.6, y0 + panjang_awal + dx/2), fontsize=9, color='blue')
ax.annotate(f'{panjang_akhir:.2f} m', (0.55, y0 + panjang_akhir + 0.05), fontsize=9, color='blue')

ax.set_xlim(-0.2, 1.0)
ax.set_ylim(0, y0 + panjang_akhir + 0.6)
ax.axis('off')
ax.set_title('Perbandingan Panjang Pegas Sebelum dan Sesudah Diberi Gaya')
ax.legend(loc='upper right')
st.pyplot(fig)

st.markdown('---')
st.caption('Disusun untuk pembelajaran Fisika SMA oleh Andy Kurniawan, S.Si - SMA Negeri 1 Dolopo')
