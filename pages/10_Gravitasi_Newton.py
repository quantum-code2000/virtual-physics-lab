import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title='Hukum Gravitasi Newton', layout='wide')
st.title('Simulasi Hukum Gravitasi Newton')
st.markdown('---')

G = 6.674 * 10**-11  # konstanta gravitasi
st.markdown(f'**Konstanta Gravitasi (G): {G:.3e} N·m²/kg²**')

m1 = st.number_input('Massa benda pertama (m₁) dalam kg', value=5.97e24)
m2 = st.number_input('Massa benda kedua (m₂) dalam kg', value=7.35e22)
r = st.number_input('Jarak antara kedua benda (r) dalam meter', value=3.84e8)

F = G * m1 * m2 / r**2 if r != 0 else 0
st.success(f'Gaya Gravitasi (F): {F:.2e} Newton')

st.markdown('---')
st.subheader('Visualisasi Gaya Gravitasi antara Dua Benda')
fig, ax = plt.subplots(figsize=(6, 2))
ax.plot(0, 0, 'o', markersize=20, label='m₁')
ax.plot(r, 0, 'o', markersize=15, label='m₂')
ax.annotate('', xy=(r * 0.25, 0), xytext=(0.5, 0), arrowprops=dict(arrowstyle='<-', color='blue'))
ax.annotate('', xy=(r * 0.75, 0), xytext=(r - 0.5, 0), arrowprops=dict(arrowstyle='->', color='blue'))
ax.text(0, 0.2, 'm₁', ha='center')
ax.text(r, 0.2, 'm₂', ha='center')
ax.set_xlim(-r * 0.2, r * 1.2)
ax.set_ylim(-1, 1)
ax.axis('off')
ax.set_title('Dua benda saling tarik menarik dengan gaya gravitasi')
st.pyplot(fig)

st.markdown('---')
st.caption('Disusun untuk pembelajaran Fisika SMA oleh Andy Kurniawan, S.Si - SMA Negeri 1 Dolopo')
