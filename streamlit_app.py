import streamlit as st
import pandas as pd


df = pd.read_excel ("Sampah.xlsx")

ds = pd.read_csv ("Tahun.csv")
st.title("Kajian terhadap Penanganan Sampah di Indonesia")

st.markdown("""<span style="word-wrap:break-word;">Indonesia termasuk ke dalam 10 negara dengan jumlah penduduk terbanyak di dunia. Banyaknya penduduk yang tinggal di sebuah negara tentunya akan menumpulkan sejumlah persoalan, diantaranya adalah produksi sampah dan pengolahannya Kementerian Lingkungan Hidup dan Kehutanan (KLHK) menyampaikan bahwa produksi sampah nasional mencapai 175.000 ton per hari. Rata-rata satu orang penduduk Indonesia menyumbang sampah sebanyak 0.7kg per hari. Jika dikalkulasi dalam skala tahunan, Indonesia menghasilkan sampah sebanyak 64juta ton! Jumlah yang sangat besar, dan bukan jumlah yang patut dibanggakan.</span>""", unsafe_allow_html=True)

st.bar_chart(ds)
st.markdown("""<span style="word-wrap:break-word;">Berdasarkan data dari Kementerian Lingkungan Hidup dan Kehutanan (KLHK) mencatat, Indonesia menghasilkan sampah sebanyak 21,88 juta ton pada tahun 2021. Jumlah itu menurun dibandingkan tahun lalu sebanyak 33% yaitu 32,82 juta ton tahun 2020
.</span>""", unsafe_allow_html=True)

st.markdown('<div style="text-align: center;">Jumlah Timbulan Sampah Indonesia Tahun 2021</div>', unsafe_allow_html=True)

st.dataframe(df)
dt = pd.read_csv ("sampah123.csv")

st.markdown('<div style="text-align: center;">Jumlah Timbulan Sampah di Indonesia Perprovinsi Tahun 2021</div>', unsafe_allow_html=True)

st.bar_chart(dt)

st.markdown("""<span style="word-wrap:break-word;">Berdasarkan wilayahnya, Jawa Tengah menjadi provinsi dengan sampah terbesar di Indonesia pada 2021, yakni 3,65 juta ton. Posisinya disusul oleh Jawa Timur dengan sampah sebanyak 2,64 juta ton. DKI Jakarta berada di posisi ketiga lantaran menyumbang 2,59 juta ton sampah. Kemudian, sampah yang dihasilkan di Jawa Barat sebanyak 2,11 juta ton..</span>""", unsafe_allow_html=True)
