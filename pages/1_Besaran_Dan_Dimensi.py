import streamlit as st
import pandas as pd

st.set_page_config(page_title='Besaran dan Dimensi', layout='wide')
st.title('Simulasi Besaran Pokok, Turunan, dan Dimensi')
st.markdown('---')

# === TABEL BESARAN POKOK ===
st.subheader('Tabel Besaran Pokok')
data = {
    'Besaran Pokok': [
        'Panjang', 'Massa', 'Waktu', 'Arus Listrik',
        'Suhu', 'Jumlah Zat', 'Intensitas Cahaya'
    ],
    'Simbol': ['l', 'm', 't', 'I', 'T', 'n', 'Iv'],
    'Satuan SI': [
        'meter (m)', 'kilogram (kg)', 'sekon (s)',
        'ampere (A)', 'kelvin (K)', 'mol (mol)', 'candela (cd)'
    ],
    'Dimensi': ['[L]', '[M]', '[T]', '[I]', '[Θ]', '[N]', '[J]']
}
df = pd.DataFrame(data)
st.dataframe(df, use_container_width=True)

# === CONTOH BESARAN TURUNAN ===
st.markdown('---')
st.subheader('Contoh Besaran Turunan dan Dimensi')
st.markdown('''
**Kecepatan (v) = s / t**  → Dimensi: [L][T^-1]  
**Percepatan (a) = v / t** → Dimensi: [L][T^-2]  
**Gaya (F) = m × a**       → Dimensi: [M][L][T^-2]  
**Usaha = F × s**          → Dimensi: [M][L²][T^-2]  
**Momentum = m × v**       → Dimensi: [M][L][T^-1]  
**Tekanan = F / A**        → Dimensi: [M][L^-1][T^-2]  
**Daya = W / t**           → Dimensi: [M][L²][T^-3]  
**Hambatan = V / I**       → Dimensi: [M][L²][T^-3][I^-2]  
**Induktansi = W / I²**    → Dimensi: [M][L²][T^-2][I^-2]  
''')

# === KALKULATOR DIMENSI ===
st.markdown('---')
st.subheader('Kalkulator Dimensi Sederhana')

rumus = st.selectbox('Pilih rumus:', [
    'F = m * a',
    'a = v / t',
    'v = s / t',
    'Usaha = F * s',
    'Momentum = m * v',
    'Tekanan = F / A',
    'Daya = W / t',
    'Hambatan = V / I',
    'Induktansi = W / I^2'
])

dimensi_dict = {
    'F = m * a': '[M][L][T^-2]',
    'a = v / t': '[L][T^-2]',
    'v = s / t': '[L][T^-1]',
    'Usaha = F * s': '[M][L²][T^-2]',
    'Momentum = m * v': '[M][L][T^-1]',
    'Tekanan = F / A': '[M][L^-1][T^-2]',
    'Daya = W / t': '[M][L²][T^-3]',
    'Hambatan = V / I': '[M][L²][T^-3][I^-2]',
    'Induktansi = W / I^2': '[M][L²][T^-2][I^-2]'
}

st.info(f'Dimensi untuk {rumus} adalah: {dimensi_dict[rumus]}')

# === KREDIT ===
st.markdown('---')
st.caption('Disusun untuk pembelajaran Fisika SMA oleh Andy Kurniawan, S.Si - SMA Negeri 1 Dolopo')
