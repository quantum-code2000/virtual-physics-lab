import streamlit as st

st.set_page_config(page_title='Momentum dan Impuls', layout='wide')
st.title('Simulasi Momentum dan Impuls')
st.markdown('---')

opsi = st.radio('Pilih jenis perhitungan:', ['Momentum (p = m × v)', 'Impuls (I = F × Δt)', 'Simulasi Tumbukan'])

# Momentum
if opsi == 'Momentum (p = m × v)':
    m = st.number_input('Massa (kg)', value=2.0)
    v = st.number_input('Kecepatan (m/s)', value=3.0)
    p = m * v
    st.success(f'Momentum: p = {p:.2f} kg·m/s')

# Impuls
elif opsi == 'Impuls (I = F × Δt)':
    F = st.number_input('Gaya (N)', value=10.0)
    dt = st.number_input('Lama gaya bekerja (s)', value=0.5)
    I = F * dt
    st.success(f'Impuls: I = {I:.2f} N·s')

# Simulasi tumbukan dua benda
else:
    st.markdown('### Input Sebelum Tumbukan')
    m1 = st.number_input('Massa benda 1 (kg)', value=1.0)
    v1 = st.number_input('Kecepatan awal benda 1 (m/s)', value=3.0)
    m2 = st.number_input('Massa benda 2 (kg)', value=1.0)
    v2 = st.number_input('Kecepatan awal benda 2 (m/s)', value=-2.0)
    e = st.slider('Koefisien restitusi (0 = tak lenting, 1 = lenting sempurna)', 0.0, 1.0, 1.0)

    v1_akhir = ((m1 - e * m2) * v1 + (1 + e) * m2 * v2) / (m1 + m2)
    v2_akhir = ((m2 - e * m1) * v2 + (1 + e) * m1 * v1) / (m1 + m2)

    st.markdown('### Hasil Setelah Tumbukan')
    st.success(f'Kecepatan akhir benda 1: {v1_akhir:.2f} m/s')
    st.success(f'Kecepatan akhir benda 2: {v2_akhir:.2f} m/s')

st.markdown('---')
st.caption('Disusun untuk pembelajaran Fisika SMA oleh Andy Kurniawan, S.Si - SMA Negeri 1 Dolopo')