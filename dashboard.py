import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

# Fungsi untuk membuat DataFrame ringkasan total pendapatan per kategori produk
def create_orders_items_product_df(df):
    sum_orders_items_product_df = orders_items_products_df.groupby(by="product_category_name").price.sum().sort_values(ascending=False).reset_index()
    return sum_orders_items_product_df

# Fungsi untuk membuat DataFrame ringkasan jumlah ulasan berdasarkan kelompok ulasan
def create_orders_reviews_orders_items_product_df(df):
    sum_orders_reviews_order_item_products_df = orders_reviews_order_item_products_df.groupby(by="review_group").review_id.nunique().reset_index()
    return sum_orders_reviews_order_item_products_df

# Membaca data dari file CSV
orders_items_products_df = pd.read_csv("items_product.csv")
orders_reviews_order_item_products_df= pd.read_csv("review_product.csv")

# Membuat DataFrame ringkasan untuk pendapatan per kategori produk
sum_orders_items_product_df = create_orders_items_product_df(orders_items_products_df)

# Membuat DataFrame ringkasan untuk jumlah ulasan per kelompok ulasan
sum_orders_reviews_order_item_products_df = create_orders_reviews_orders_items_product_df(orders_reviews_order_item_products_df)

# Menampilkan informasi profil di sidebar
st.sidebar.header("Profile Information")
st.sidebar.image("pp.jpg")  # Menampilkan gambar profil
st.sidebar.write("**Name:** M. Sohibbal")  # Menampilkan nama
st.sidebar.write("**University:** Universitas Riau")  # Menampilkan nama universitas

# Header utama untuk dashboard
st.header("E-Commerce Public Dashboard")

# Subheader untuk bagian pendapatan tertinggi dan terendah berdasarkan kategori produk
st.subheader("Highest and Lowest Income by Product Category")

# Membuat plot dengan dua kolom (untuk pendapatan tertinggi dan terendah)
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(18, 6))

# Warna untuk plot bar
colors = ["#72B3D4", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

# Membuat plot untuk kategori produk dengan pendapatan tertinggi
sns.barplot(x="price", y="product_category_name", data=sum_orders_items_product_df.sort_values(by="price", ascending=False).head(5), palette=colors, ax=ax[0])
ax[0].set_ylabel(None)  # Menghilangkan label sumbu y
ax[0].set_xlabel("Number of Sales", fontsize=14)  # Menambahkan label sumbu x
ax[0].set_title("Highest Income", loc="center", fontsize=16)  # Menambahkan judul plot
ax[0].tick_params(axis="y", labelsize=12)  # Mengatur ukuran label sumbu y
ax[0].margins(x=0.4)  # Mengatur margin sumbu x

# Membuat plot untuk kategori produk dengan pendapatan terendah
sns.barplot(x="price", y="product_category_name", data=sum_orders_items_product_df.sort_values(by="price", ascending=True).head(5), palette=colors, ax=ax[1])
ax[1].set_ylabel(None)  # Menghilangkan label sumbu y
ax[1].set_xlabel("Number of Sales", fontsize=14)  # Menambahkan label sumbu x
ax[1].invert_xaxis()  # Membalikkan sumbu x
ax[1].yaxis.set_label_position("right")  # Menempatkan label sumbu y di kanan
ax[1].yaxis.tick_right()  # Menempatkan tick sumbu y di kanan
ax[1].set_title("Lowest Income", loc="center", fontsize=16)  # Menambahkan judul plot
ax[1].tick_params(axis="y", labelsize=12)  # Mengatur ukuran label sumbu y
ax[1].margins(x=0.8)  # Mengatur margin sumbu x

# Menambahkan label pada setiap bar di kedua plot
for a in ax:
    for container in a.containers:
        a.bar_label(container, fmt="%.0f", fontsize=12, padding=3)

# Menampilkan plot pertama di Streamlit
st.pyplot(fig)

# Subheader untuk bagian jumlah ulasan pelanggan berdasarkan klasifikasi ulasan
st.subheader("Number of Customer Reviews by Review Classification")

# Membuat plot kedua untuk jumlah ulasan berdasarkan klasifikasi ulasan
fig2, ax2 = plt.subplots(figsize=(10, 5))

# Mengurutkan kelompok ulasan
sum_orders_reviews_order_item_products_df["review_group"] = pd.Categorical(sum_orders_reviews_order_item_products_df["review_group"], ["Good", "Average", "Bad"])

# Warna untuk plot bar kedua
colors_ = ["#72D460", "#D3D3D3", "#D3D3D3"]

# Membuat plot untuk jumlah ulasan berdasarkan klasifikasi ulasan
sns.barplot(
    y="review_id", 
    x="review_group",
    data=sum_orders_reviews_order_item_products_df.sort_values(by="review_group", ascending=False),
    palette=colors_,
    ax=ax2
)

# Mengatur label dan judul pada plot kedua
ax2.set_ylabel(None)  # Menghilangkan label sumbu y
ax2.set_xlabel(None)  # Menghilangkan label sumbu x
ax2.set_title("Number of Customer Reviews by Review Classification")  # Menambahkan judul plot
ax2.tick_params(axis="x", labelsize=12)  # Mengatur ukuran label sumbu x
ax2.margins(y=0.2)  # Mengatur margin sumbu y

# Menambahkan label pada setiap bar di plot kedua
for container in ax2.containers:
    ax2.bar_label(container, fmt="%.0f", padding=4)

# Menampilkan plot kedua di Streamlit
st.pyplot(fig2)