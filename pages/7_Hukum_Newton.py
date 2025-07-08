import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title='Hukum Newton', layout='wide')
st.title('Simulasi Hukum Newton tentang Gerak')
st.markdown('---')

pilihan = st.radio('Pilih hukum:', ['Hukum Newton I', 'Hukum Newton II', 'Hukum Newton III'])

if pilihan == 'Hukum Newton I':
    st.subheader('Hukum Newton I')
    st.info('''Jika resultan gaya yang bekerja pada suatu benda sama dengan nol,
maka benda akan tetap diam atau bergerak lurus beraturan.''')
    st.image('https://upload.wikimedia.org/wikipedia/commons/thumb/3/3e/Newton%27s_First_Law.svg/640px-Newton%27s_First_Law.svg.png', width=400)
    st.markdown('Contoh: Buku yang diam di atas meja akan tetap diam jika tidak ada gaya luar.')

elif pilihan == 'Hukum Newton II':
    st.subheader('Hukum Newton II: F = m × a')
    hitung = st.selectbox('Pilih variabel yang ingin dihitung:', ['Gaya (F)', 'Massa (m)', 'Percepatan (a)'])
    if hitung == 'Gaya (F)':
        m = st.number_input('Massa (m) dalam kg', value=2.0)
        a = st.number_input('Percepatan (a) dalam m/s²', value=3.0)
        F = m * a
        st.success(f'F = {F:.2f} Newton')
    elif hitung == 'Massa (m)':
        F = st.number_input('Gaya (F) dalam N', value=10.0)
        a = st.number_input('Percepatan (a) dalam m/s²', value=2.0)
        m = F / a if a != 0 else 0
        st.success(f'm = {m:.2f} kg')
    else:
        F = st.number_input('Gaya (F) dalam N', value=15.0)
        m = st.number_input('Massa (m) dalam kg', value=5.0)
        a = F / m if m != 0 else 0
        st.success(f'a = {a:.2f} m/s²')

    # Visualisasi panah gaya
    st.markdown('---')
    st.subheader('Visualisasi Gaya pada Benda')
    fig, ax = plt.subplots()
    ax.arrow(0, 0, 1, 0, head_width=0.2, head_length=0.2, fc='blue', ec='blue')
    ax.text(1.1, 0, 'F', fontsize=12)
    ax.set_xlim(-1, 3)
    ax.set_ylim(-1, 1)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title('Gaya mendorong benda ke kanan')
    st.pyplot(fig)

else:
    st.subheader('Hukum Newton III')
    st.info('''Setiap aksi selalu ada reaksi yang sama besar dan berlawanan arah.''')
    st.image('https://upload.wikimedia.org/wikipedia/commons/thumb/f/f4/Newton%27s_cradle_animation_book_2.gif/320px-Newton%27s_cradle_animation_book_2.gif')
    st.markdown('Contoh: Ketika menekan dinding, dinding juga mendorong balik dengan gaya yang sama.')

st.markdown('---')
st.caption('Disusun untuk pembelajaran Fisika SMA oleh Andy Kurniawan, S.Si - SMA Negeri 1 Dolopo')
