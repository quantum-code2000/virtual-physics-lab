import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title='Hukum Newton II', layout='wide')
st.title('Simulasi Hukum Newton II (F = m × a)')
st.markdown('---')

st.write('Pilih variabel yang ingin dihitung, kemudian masukkan dua variabel lainnya:')
pilihan = st.selectbox('Saya ingin menghitung:', ['Gaya (F)', 'Massa (m)', 'Percepatan (a)'])

# Input dua variabel sesuai pilihan
if pilihan == 'Gaya (F)':
    m = st.number_input('Massa (kg)', value=1.0)
    a = st.number_input('Percepatan (m/s²)', value=1.0)
    F = m * a
    st.success(f'Gaya: {F:.2f} N')
elif pilihan == 'Massa (m)':
    F = st.number_input('Gaya (N)', value=1.0)
    a = st.number_input('Percepatan (m/s²)', value=1.0)
    if a != 0:
        m = F / a
        st.success(f'Massa: {m:.2f} kg')
    else:
        st.warning('Percepatan tidak boleh nol')
        m = 0
elif pilihan == 'Percepatan (a)':
    F = st.number_input('Gaya (N)', value=1.0)
    m = st.number_input('Massa (kg)', value=1.0)
    if m != 0:
        a = F / m
        st.success(f'Percepatan: {a:.2f} m/s²')
    else:
        st.warning('Massa tidak boleh nol')
        a = 0
else:
    F = m = a = 0

# Grafik batang
st.markdown('---')
st.subheader('Visualisasi Hukum Newton II')
labels = ['Gaya (N)', 'Massa (kg)', 'Percepatan (m/s²)']
values = [F, m, a]
colors = ['red', 'blue', 'green']
fig, ax = plt.subplots()
bars = ax.bar(labels, values, color=colors)
ax.set_ylim(0, max(values) * 1.2 if max(values) > 0 else 1)
for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2.0, yval + 0.05, f'{yval:.2f}', ha='center')
st.pyplot(fig)
