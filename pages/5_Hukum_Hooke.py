import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title='Hukum Hooke', layout='wide')
st.title('Simulasi Hukum Hooke (F = k × Δx)')
st.markdown('---')
st.write('Pilih variabel yang ingin dihitung, lalu masukkan dua variabel lainnya:')
pilihan = st.selectbox('Hitung:', ['Gaya (F)', 'Konstanta Pegas (k)', 'Pertambahan Panjang (Δx)'])

if pilihan == 'Gaya (F)':
    k = st.number_input('Konstanta pegas k (N/m)', value=100.0)
    dx = st.number_input('Pertambahan panjang Δx (m)', value=0.05)
    F = k * dx
    st.success(f'Gaya: {F:.2f} N')
elif pilihan == 'Konstanta Pegas (k)':
    F = st.number_input('Gaya F (N)', value=10.0)
    dx = st.number_input('Pertambahan panjang Δx (m)', value=0.05)
    if dx != 0:
        k = F / dx
        st.success(f'Konstanta Pegas: {k:.2f} N/m')
    else:
        k = 0
        st.warning('Δx tidak boleh nol.')
elif pilihan == 'Pertambahan Panjang (Δx)':
    F = st.number_input('Gaya F (N)', value=10.0)
    k = st.number_input('Konstanta pegas k (N/m)', value=100.0)
    if k != 0:
        dx = F / k
        st.success(f'Pertambahan panjang: {dx:.3f} m')
    else:
        dx = 0
        st.warning('Konstanta pegas tidak boleh nol.')
else:
    F = k = dx = 0

st.markdown('---')
st.subheader('Visualisasi Nilai Variabel')
labels = ['Gaya (F)', 'Konstanta (k)', 'Δx']
values = [F, k, dx]
colors = ['red', 'blue', 'green']
fig, ax = plt.subplots()
bars = ax.bar(labels, values, color=colors)
ax.set_ylabel('Nilai')
ax.set_title('Hubungan F = k × Δx')
for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2.0, yval + 0.02, f'{yval:.2f}', ha='center')
st.pyplot(fig)