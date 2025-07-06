import streamlit as st
import pandas as pd

st.set_page_config(page_title='Besaran dan Dimensi', layout='wide')
st.title('Simulasi Besaran Pokok, Turunan, dan Dimensi')
st.markdown('---')

st.subheader('Tabel Besaran Pokok')
data = {
    'Besaran Pokok': ['Panjang', 'Massa', 'Waktu', 'Arus Listrik', 'Suhu', 'Jumlah Zat', 'Intensitas Cahaya'],
    'Simbol': ['l', 'm', 't', 'I', 'T', 'n', 'Iv'],
    'Satuan SI': ['meter (m)', 'kilogram (kg)', 'sekon (s)', 'ampere (A)', 'kelvin (K)', 'mol (mol)', 'candela (cd)'],
    'Dimensi': ['[L]', '[M]', '[T]', '[I]', '[Θ]', '[N]', '[J]']
}
df = pd.DataFrame(data)
st.dataframe(df, use_container_width=True)

st.markdown('---')
st.subheader('Contoh Besaran Turunan dan Dimensi')
st.markdown('''
**Kecepatan (v) = s / t**  → Dimensi: [L][T^-1]  
**Percepatan (a) = v / t** → Dimensi: [L][T^-2]  
**Gaya (F) = m × a**       → Dimensi: [M][L][T^-2]  
**Usaha = F × s**          → Dimensi: [M][L²][T^-2]  
''')

st.markdown('---')
st.subheader('Kalkulator Dimensi Sederhana')
rumus = st.selectbox('Pilih rumus', ['F = m * a', 'a = v / t', 'v = s / t', 'Usaha = F * s'])
if rumus == 'F = m * a':
    st.info('Dimensi Gaya (F): [M][L][T^-2]')
elif rumus == 'a = v / t':
    st.info('Dimensi Percepatan (a): [L][T^-2]')
elif rumus == 'v = s / t':
    st.info('Dimensi Kecepatan (v): [L][T^-1]')
else:
    st.info('Dimensi Usaha: [M][L²][T^-2]')

st.markdown('---')
st.caption('Disusun untuk pembelajaran Fisika SMA oleh Pak Andy Kurniawan, S.Si - SMA Negeri 1 Dolopo')