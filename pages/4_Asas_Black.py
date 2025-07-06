import streamlit as st
import matplotlib.pyplot as plt

kalor_jenis_dict = {
    'Air': 4186,
    'Aluminium': 900,
    'Tembaga': 385,
    'Besi': 450,
    'Timah': 130
}

st.set_page_config(page_title='Simulasi Asas Black', layout='wide')
st.title('Simulasi Asas Black: Kalor Dilepas = Kalor Diterima')
st.markdown('---')
st.subheader('Input Data Zat 1 (Panas)')
massa1 = st.number_input('Massa zat 1 (kg)', value=1.0)
suhu1 = st.number_input('Suhu awal zat 1 (°C)', value=80.0)
zat1 = st.selectbox('Jenis zat 1', list(kalor_jenis_dict.keys()), key='zat1')
c1 = kalor_jenis_dict[zat1]

st.markdown('---')
st.subheader('Input Data Zat 2 (Dingin)')
massa2 = st.number_input('Massa zat 2 (kg)', value=1.0)
suhu2 = st.number_input('Suhu awal zat 2 (°C)', value=30.0)
zat2 = st.selectbox('Jenis zat 2', list(kalor_jenis_dict.keys()), key='zat2')
c2 = kalor_jenis_dict[zat2]

st.markdown('---')
if massa1 > 0 and massa2 > 0 and suhu1 != suhu2:
    T_akhir = (massa1 * c1 * suhu1 + massa2 * c2 * suhu2) / (massa1 * c1 + massa2 * c2)
    st.success(f'Suhu akhir pencampuran: {T_akhir:.2f} °C')
    st.subheader('Visualisasi Suhu')
    labels = ['Zat 1 (awal)', 'Zat 2 (awal)', 'Suhu Akhir']
    values = [suhu1, suhu2, T_akhir]
    colors = ['red', 'blue', 'green']
    fig, ax = plt.subplots()
    bars = ax.bar(labels, values, color=colors)
    ax.set_ylabel('Suhu (°C)')
    ax.set_title('Perbandingan Suhu Zat')
    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2.0, yval + 1, f'{yval:.1f}', ha='center')
    st.pyplot(fig)
else:
    st.info('Masukkan massa dan suhu yang valid untuk kedua zat.')
