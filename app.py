import streamlit as st
import numpy as np
import pickle

model = pickle.load(open('model.pkl','rb'))

st.title("🛢️ Crude Oil Price Prediction")

open_price = st.number_input("Open Price", value=80.0)
high_price = st.number_input("High Price", value=85.0)
low_price = st.number_input("Low Price", value=75.0)
volume = st.number_input("Volume", value=200000.0)

if st.button("Predict"):
    data = np.array([[open_price, high_price, low_price, volume]])
    pred = model.predict(data)
    st.success(f"Predicted Close Price: {pred[0]:.2f}")
