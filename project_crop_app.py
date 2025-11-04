#Abhishek Palase
import streamlit as st
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# 🌾 sample dataset
data = pd.DataFrame({
    'SoilType': ['Loamy', 'Sandy', 'Clay', 'Sandy', 'Loamy', 'Clay', 'Sandy', 'Loamy', 'Clay', 'Loamy'],
    'Rainfall': [200, 120, 300, 100, 250, 320, 130, 220, 310, 210],
    'Temperature': [25, 32, 22, 35, 28, 24, 34, 27, 23, 26],
    'pH': [6.5, 7.2, 5.8, 7.5, 6.8, 5.6, 7.3, 6.4, 5.9, 6.6],
    'Crop': ['Rice', 'Wheat', 'Sugarcane', 'Bajra', 'Maize', 'Paddy', 'Jowar', 'Barley', 'Cotton', 'Rice']
})

# 🌱 encode soil type
data['SoilType'] = data['SoilType'].map({'Loamy':0, 'Sandy':1, 'Clay':2})

# split into features & labels
x = data[['SoilType', 'Rainfall', 'Temperature', 'pH']]
y = data['Crop']

# train model
model = DecisionTreeClassifier()
model.fit(x, y)

# 🌾 app UI
st.title("🌾 Crop Recommendation System")
st.write("### Predict the best crop based on soil, rainfall, temperature, and pH.")

soil = st.selectbox("🌍 Soil Type", ['Loamy', 'Sandy', 'Clay'])
rain = st.slider("🌧️ Rainfall (mm)", 50, 400, 200)
temp = st.slider("🌡️ Temperature (°C)", 10, 45, 28)
ph = st.slider("⚗️ pH Value", 4.0, 9.0, 6.5)

if st.button("🌿 Predict Suitable Crop"):
    s = {'Loamy':0, 'Sandy':1, 'Clay':2}[soil]
    pred = model.predict([[s, rain, temp, ph]])[0]
    st.success(f"🌱 Recommended Crop: **{pred}**")
    st.info("Based on the given conditions, this crop is most suitable for optimal yield and sustainability.")

if st.button("🔁 Reset Fields"):
    st.experimental_rerun()
