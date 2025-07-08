import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title='Kesetimbangan Benda Tegar', layout='wide')
st.title('Simulasi Kesetimbangan Benda Tegar')
st.markdown('---')

# Input gaya-gaya
st.subheader('Input Gaya dan Posisi terhadap Titik Tumpu')
F1 = st.number_input('Gaya 1 (N)', value=10.0)
d1 = st.number_input('Jarak Gaya 1 dari titik tumpu (m)', value=2.0)
arah1 = st.selectbox('Arah Gaya 1', ['searah jarum jam', 'berlawanan jarum jam'])

F2 = st.number_input('Gaya 2 (N)', value=15.0)
d2 = st.number_input('Jarak Gaya 2 dari titik tumpu (m)', value=1.33)
arah2 = st.selectbox('Arah Gaya 2', ['searah jarum jam', 'berlawanan jarum jam'])

# Hitung momen gaya (torsi)
tau1 = F1 * d1 * (-1 if arah1 == 'searah jarum jam' else 1)
tau2 = F2 * d2 * (-1 if arah2 == 'searah jarum jam' else 1)
total_torsi = tau1 + tau2

st.markdown('---')
st.subheader('Hasil Analisis')
st.write(f'Momen Gaya 1 (τ₁): {tau1:.2f} N·m')
st.write(f'Momen Gaya 2 (τ₂): {tau2:.2f} N·m')
st.write(f'Total Momen (τ₁ + τ₂): {total_torsi:.2f} N·m')

if abs(total_torsi) < 1e-5:
    st.success('✅ Sistem dalam keadaan SEIMBANG (∑τ = 0)')
else:
    st.error('❌ Sistem TIDAK SEIMBANG (∑τ ≠ 0)')

# Visualisasi
st.markdown('---')
st.subheader('Visualisasi Tuas dan Gaya')
fig, ax = plt.subplots(figsize=(8,2))
ax.hlines(0, -3, 3, colors='gray', linestyles='solid', linewidth=5)
ax.plot(0, 0, 'ko', markersize=10)  # titik tumpu

x1 = -d1 if arah1 == 'searah jarum jam' else d1
x2 = -d2 if arah2 == 'searah jarum jam' else d2
ax.arrow(x1, 0.2, 0, 0.8, head_width=0.1, head_length=0.1, color='blue')
ax.arrow(x2, -0.2, 0, -0.8, head_width=0.1, head_length=0.1, color='red')
ax.text(x1, 1.1, 'F1', ha='center')
ax.text(x2, -1.3, 'F2', ha='center')
ax.set_xlim(-3, 3)
ax.set_ylim(-2, 2)
ax.axis('off')
st.pyplot(fig)

st.markdown('---')
st.caption('Disusun untuk pembelajaran Fisika SMA oleh Andy Kurniawan, S.Si - SMA Negeri 1 Dolopo')
