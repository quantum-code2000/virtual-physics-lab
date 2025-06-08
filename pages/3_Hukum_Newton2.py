import streamlit as st

st.title('Simulasi Hukum Newton II')
massa = st.number_input('Massa benda (kg)', value=1.0)
gaya = st.number_input('Gaya total (N)', value=10.0)
if massa > 0:
    percepatan = gaya / massa
    st.success(f'Percepatan: {percepatan:.2f} m/s²')
else:
    st.warning('Massa harus lebih dari 0!')