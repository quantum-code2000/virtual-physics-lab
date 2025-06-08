import streamlit as st
from PIL import Image

st.set_page_config(page_title="Virtual Physics Lab", layout="wide")

# Header
col1, col2 = st.columns([1, 8])
with col1:
    st.image("assets/logosmando2d.png", width=80)
with col2:
    st.title("Virtual Physics Lab")
    st.caption("Dikembangkan oleh Andy Kurniawan, S.Si — SMA Negeri 1 Dolopo")

# Konten Beranda
st.markdown("""
## Selamat datang di Virtual Physics Lab

Silakan gunakan sidebar di kiri untuk mengakses simulasi:
- GLBB
- Konversi Suhu
- Hukum Newton II

Akan terus dikembangkan untuk mencakup semua hukum fisika SMA.
""")
