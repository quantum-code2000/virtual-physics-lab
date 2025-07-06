import streamlit as st
import matplotlib.pyplot as plt
import math

st.set_page_config(page_title='Aturan Angka Penting', layout='wide')
st.title('Simulasi Aturan Angka Penting dalam Fisika')
st.markdown('---')

st.subheader('Penjelasan Aturan Angka Penting')
st.markdown('''
**1. Semua angka bukan nol adalah angka penting**
**2. Nol di antara angka bukan nol adalah angka penting**
**3. Nol di depan angka bukan nol tidak dianggap penting**
**4. Nol di belakang angka desimal adalah angka penting**
**5. Hasil operasi harus disesuaikan dengan angka penting terkecil**
''')

st.markdown('---')
st.subheader('Hitung Jumlah Angka Penting')
user_input = st.text_input('Masukkan angka:', value='0.005600')

def count_significant_figures(number_str):
    if '.' in number_str:
        number_str = number_str.strip('0')
        if '.' in number_str:
            return len(number_str.replace('.', '').lstrip('0'))
    return len(number_str.strip('0').replace('.', ''))

try:
    count = count_significant_figures(user_input)
    st.success(f'Jumlah angka penting: {count}')
except:
    st.error('Masukkan angka valid.')

st.markdown('---')
st.subheader('Visualisasi Angka Penting')
fig, ax = plt.subplots()
ax.bar(['Angka Penting'], [count], color='green')
ax.set_ylim(0, max(count + 1, 5))
ax.set_ylabel('Jumlah')
ax.set_title('Grafik Jumlah Angka Penting')
st.pyplot(fig)

st.markdown('---')
st.subheader('Simulasi Operasi Hitung dengan Angka Penting')
num1 = st.text_input('Angka pertama:', '3.45')
num2 = st.text_input('Angka kedua:', '2.1')
operasi = st.selectbox('Pilih operasi:', ['Perkalian', 'Pembagian'])

def sig_fig(val):
    return count_significant_figures(val)

try:
    v1 = float(num1)
    v2 = float(num2)
    if operasi == 'Perkalian':
        hasil = v1 * v2
    else:
        hasil = v1 / v2
    min_sig = min(sig_fig(num1), sig_fig(num2))
    format_str = f'{{:.{min_sig - 1}g}}'
    st.success(f'Hasil sesuai aturan angka penting: {format_str.format(hasil)}')
except:
    st.warning('Masukkan angka valid.')

st.markdown('---')
st.caption('Disusun untuk pembelajaran Fisika SMA oleh Andy Kurniawan, S.Si - SMA Negeri 1 Dolopo')
