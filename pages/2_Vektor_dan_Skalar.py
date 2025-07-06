import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title='Besaran Vektor dan Skalar', layout='wide')
st.title('Simulasi Besaran Vektor dan Skalar')
st.markdown('---')

# TABEL PERBANDINGAN
st.subheader('Perbandingan Besaran Skalar dan Vektor')
data = {
    'Jenis Besaran': ['Skalar', 'Skalar', 'Skalar', 'Vektor', 'Vektor', 'Vektor'],
    'Contoh': ['Massa', 'Suhu', 'Energi', 'Kecepatan', 'Percepatan', 'Gaya'],
    'Satuan': ['kg', 'K', 'J', 'm/s', 'm/s²', 'N']
}
df = pd.DataFrame(data)
st.dataframe(df, use_container_width=True)

# VISUALISASI ARAH VEKTOR
st.markdown('---')
st.subheader('Visualisasi Arah Vektor')
fig, ax = plt.subplots()
ax.quiver(0, 0, 2, 1, angles='xy', scale_units='xy', scale=1, color='r', label='Vektor A')
ax.quiver(0, 0, 1, 2, angles='xy', scale_units='xy', scale=1, color='b', label='Vektor B')
ax.set_xlim(0, 3)
ax.set_ylim(0, 3)
ax.set_aspect('equal')
ax.grid(True)
ax.legend()
ax.set_title('Contoh Dua Vektor')
st.pyplot(fig)

# PENJUMLAHAN VEKTOR
st.markdown('---')
st.subheader('Penjumlahan Dua Vektor (Metode Ekor-Kepala)')
ax1 = st.number_input('Vektor A - Komponen x', value=2.0)
ay1 = st.number_input('Vektor A - Komponen y', value=1.0)
bx1 = st.number_input('Vektor B - Komponen x', value=1.0)
by1 = st.number_input('Vektor B - Komponen y', value=2.0)

rx, ry = ax1 + bx1, ay1 + by1

fig2, ax2 = plt.subplots()
ax2.quiver(0, 0, ax1, ay1, angles='xy', scale_units='xy', scale=1, color='red', label='A')
ax2.quiver(ax1, ay1, bx1, by1, angles='xy', scale_units='xy', scale=1, color='blue', label='B')
ax2.quiver(0, 0, rx, ry, angles='xy', scale_units='xy', scale=1, color='green', label='Resultan')

ax2.set_xlim(0, max(rx, ax1 + bx1) + 1)
ax2.set_ylim(0, max(ry, ay1 + by1) + 1)
ax2.set_aspect('equal')
ax2.grid(True)
ax2.legend()
ax2.set_title('Penjumlahan Vektor A + B = Resultan')
st.pyplot(fig2)

# KREDIT
st.markdown('---')
st.caption('Disusun untuk pembelajaran Fisika SMA oleh Andy Kurniawan, S.Si - SMA Negeri 1 Dolopo')