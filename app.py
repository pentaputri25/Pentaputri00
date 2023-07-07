import streamlit as st
from PIL import Image

# section header
NAMA = "Penta Putri Nunik Yuniarti"
DESKRIPSI = "Programer Kesehatan"
RESUME = "Sebagai progamer dalam lingkup pengkodingan data riwayat pasien dalam skala puskesmas ataupun rumah sakit"
EMAIL = "pentaputri33@gmail.com"
SOCIAL_MEDIA = {
	'WhatsApp' : 'https://wa.me/+6288227224214',
	'Instagram' : 'https://instagram.com/pentaaaputri_?igshid=OGQ5ZDc2ODk2ZA==',
}

# sec
st.header(':wave: BIOGRAPHY')
st.title(NAMA)
image = Image.open('foto.jpg')
st.image(image, width=230)
st.subheader(DESKRIPSI)
st.write(EMAIL)
st.info(RESUME)

#####
st.subheader('Biodata Diri')
col1, col2 = st.columns(2)
with col1:
	st.write('Nama')
	st.write('Tempat, Tanggal Lahir')
	st.write('Jenis Kelamin')
	st.write('Agama')
	st.write('Alamat')

with col2:
	st.write(': Penta Putri NUnik Yuniarti')
	st.write(': Grobogan, 25 Juni 2003')
	st.write(': Perempuan')
	st.write(': Kristen')
	st.write(': Jl.Trengguli 3 No 29')
#

st.subheader('Pendidikan')
col1, col2 = st.columns(2)
with col1:
	st.write('2009-2010')
	st.write('2010-2016')
	st.write('2016-2019')
	st.write('2019-2022')
	st.write('2022-2025')

with col2:
	st.write (': TK Kristen Purwodadi')
	st.write(': SD Kristen Purwodadi')
	st.write(': SMP 1 Purwodadi')
	st.write(': SMK Theresiana SEmarang')
	st.write(': Universitas Nasional Karangturi')
#

st.subheader("Kemampuan")
st.info('''
- Mengerti MS Word Ms Excel
- Mengelola Data Rekam Medis
''')

st.subheader("Pengalaman Kerja")
st.info('Januari 2023-Juli 2023 Di Rumah Sakit Tulip')

st.write('#')
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
	st.write(f"[{platform}]({link})")
