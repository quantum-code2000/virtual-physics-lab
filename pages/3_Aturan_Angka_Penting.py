import streamlit as st
import re

st.set_page_config(page_title='Aturan Angka Penting', layout='wide')
st.title('Aturan Angka Penting - Versi Revisi')
st.markdown('---')

def highlight_significant_figures(number_str):
    number_str = number_str.strip()
    if 'e' in number_str.lower():
        parts = number_str.split('e')
        base = parts[0]
        exponent = 'e' + parts[1]
    else:
        base = number_str
        exponent = ''
    digits_only = base.replace('.', '')
    stripped = digits_only.lstrip('0')
    sig_digits = len(stripped)
    highlighted = ''
    digit_index = 0
    for ch in base:
        if ch.isdigit():
            if digit_index >= len(digits_only) - sig_digits:
                highlighted += f'<span style="color:green;font-weight:bold">{ch}</span>'
            else:
                highlighted += f'<span style="color:gray">{ch}</span>'
            digit_index += 1
        else:
            highlighted += ch
    return f'{highlighted}{exponent}', sig_digits

st.subheader('Tampilkan Angka Penting dalam Sebuah Bilangan')
user_input = st.text_input('Masukkan angka:', value='0.005600')
if user_input:
    try:
        rendered, count = highlight_significant_figures(user_input)
        st.markdown(f'Jumlah angka penting: <b>{count}</b>', unsafe_allow_html=True)
        st.markdown(f'Visualisasi: {rendered}', unsafe_allow_html=True)
    except:
        st.error('Masukkan angka valid.')

st.markdown('---')
st.subheader('Simulasi Operasi Hitung (AP)')
num1 = st.text_input('Angka pertama', '3.45')
num2 = st.text_input('Angka kedua', '2.1')
op = st.selectbox('Pilih operasi', ['Penjumlahan', 'Pengurangan', 'Perkalian', 'Pembagian'])

def count_decimal_places(s):
    if '.' in s:
        return len(s.split('.')[-1].rstrip('0'))
    return 0

try:
    val1 = float(num1)
    val2 = float(num2)
    if op == 'Penjumlahan':
        result = val1 + val2
        decimals = min(count_decimal_places(num1), count_decimal_places(num2))
        format_str = f'{{:.{decimals}f}}'
    elif op == 'Pengurangan':
        result = val1 - val2
        decimals = min(count_decimal_places(num1), count_decimal_places(num2))
        format_str = f'{{:.{decimals}f}}'
    elif op == 'Perkalian':
        result = val1 * val2
        ap = min(len(re.sub(r'[^0-9]', '', num1.lstrip('0'))), len(re.sub(r'[^0-9]', '', num2.lstrip('0'))))
        format_str = f'{{:.{ap - 1}g}}'
    else:
        result = val1 / val2
        ap = min(len(re.sub(r'[^0-9]', '', num1.lstrip('0'))), len(re.sub(r'[^0-9]', '', num2.lstrip('0'))))
        format_str = f'{{:.{ap - 1}g}}'
    formatted_result = format_str.format(result)
    st.markdown(f'Hasil: <b>{formatted_result}</b>', unsafe_allow_html=True)
    visual, sig = highlight_significant_figures(formatted_result)
    st.markdown(f'Angka penting dalam hasil: {visual} ({sig} AP)', unsafe_allow_html=True)
except:
    st.warning('Input tidak valid')

st.markdown('---')
st.caption('Disusun untuk pembelajaran Fisika SMA oleh Pak Andy Kurniawan, S.Si - SMA Negeri 1 Dolopo')
