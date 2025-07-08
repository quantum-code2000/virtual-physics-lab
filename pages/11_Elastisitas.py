import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title='Elastisitas (Hukum Hooke)', layout='wide')
st.title('Simulasi Elastisitas - Hukum Hooke')
st.markdown('---')

st.subheader('Pilih variabel yang ingin dihitung')
hitung = st.selectbox('Hitung:', ['Gaya (F)', 'Konstanta Pegas (k)', 'Pertambahan Panjang (Δx)'])

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

# Visualisasi pegas
st.markdown('---')
st.subheader('Visualisasi Pegas')
fig, ax = plt.subplots(figsize=(6, 2))
pegas_awal = [0, 0.5]
pegas_akhir = [0, 0.5 + (dx if 'dx' in locals() else 0.05)]
ax.plot([0, 1], pegas_awal, 'gray', lw=8, label='Pegas sebelum')
ax.plot([0, 1], pegas_akhir, 'blue', lw=8, label='Pegas sesudah')
ax.set_xlim(-0.5, 1.5)
ax.set_ylim(0, 1.5)
ax.set_title('Pegas memanjang akibat gaya')
ax.axis('off')
ax.legend()
st.pyplot(fig)

st.markdown('---')
st.caption('Disusun untuk pembelajaran Fisika SMA oleh Andy Kurniawan, S.Si - SMA Negeri 1 Dolopo')
