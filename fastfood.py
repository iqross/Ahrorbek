import streamlit as st
import pandas as pd
import joblib

# Modelni yuklash
model = joblib.load('fastfood.pkl')

# Streamlit interfeysini yaratish
st.title("Fastfood Narxini Aniqlash")

# Foydalanuvchi uchun forma
st.header("Ma'lumotlarni kiriting:")

mahsulot = st.selectbox(
    "Mahsulot nomini tanlang:",
    ["Shawarma", "Gamburger", "Cheeseburger", "Lavash (oddiy)", "Lavash (maxsus)", 
     "Pizza", "Tovuq qanotlari", "Hot-dog", "Kartoshka fri", "Nuggets", "Doner", 
     "Milkshake", "Gazlangan ichimliklar"]
)

shahar = st.selectbox(
    "Shaharni tanlang:",
    ["Toshkent", "Samarqand", "Farg'ona", "Buxoro", "Andijon", "Namangan", "Urganch", "Qo'qon"]
)

restoran_turi = st.selectbox(
    "Restoran turini tanlang:",
    ["Mahalliy", "Xalqaro"]
)

hajm = st.selectbox(
    "Mahsulot hajmini tanlang:",
    ["Kichik", "O'rta", "Katta"]
)

# Bashorat qilish tugmasi
if st.button("Narxni Bashorat Qiling"):
    # Test ma'lumotlarini yaratish
    test_data = pd.DataFrame({
        "Mahsulot nomi": [mahsulot],
        "Shahar": [shahar],
        "Restoran turi": [restoran_turi],
        "Mahsulot hajmi": [hajm]
    })
    
    # Model yordamida bashorat
    prediction = model.predict(test_data)
    
    # Natijani chiqarish
    st.subheader("Bashorat qilingan narx:")
    st.write(f"{prediction[0]:,.0f} so'm")
