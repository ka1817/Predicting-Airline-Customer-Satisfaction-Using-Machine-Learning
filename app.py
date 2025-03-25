import streamlit as st
import pandas as pd
import requests

API_URL = "http://backend:4000/predict"

st.set_page_config(page_title="Airline Customer Satisfaction", layout="centered")
st.title("✈️ Airline Customer Satisfaction Predictor")
st.markdown("Enter customer details to predict satisfaction level.")

st.sidebar.header("User Input Features")

def user_input_features():
    Gender = st.sidebar.selectbox("Gender", ["Male", "Female"])
    Customer_Type = st.sidebar.selectbox("Customer Type", ["Loyal", "Disloyal"])
    Age = st.sidebar.slider("Age", 10, 80, 30)
    Type_of_Travel = st.sidebar.selectbox("Type of Travel", ["Business travel", "Personal Travel"], index=0)
    Class = st.sidebar.selectbox("Class", ["Business", "Eco", "Eco Plus"], index=0)
    Flight_Distance = st.sidebar.slider("Flight Distance", 100, 5000, 1000)
    Delay_Category = st.sidebar.selectbox("Delay Category", ["No Delay", "Short Delay", "Moderate Delay", "Long Delay"], index=0)
    Service_Quality = st.sidebar.selectbox("Service Quality", ["Excellent", "Good", "Average", "Poor"], index=1)
    
    data = {
        "Gender": Gender,
        "Customer_Type": Customer_Type,
        "Age": Age,
        "Type_of_Travel": Type_of_Travel,
        "Class": Class,
        "Flight_Distance": Flight_Distance,
        "Delay_Category": Delay_Category,
        "Service_Quality": Service_Quality,
    }
    return data

data = user_input_features()


if st.button("Predict Satisfaction"):
    response = requests.post(API_URL, json=data)
    if response.status_code == 200:
        result = response.json()["prediction"]
        st.subheader("Prediction Result")
        if result == 'satisfied':
            st.success("😊 The customer is **Satisfied**!")
        else:
            st.error("😟 The customer is **Neutral or Dissatisfied**.")
    else:
        st.error("⚠️ Error: Unable to get prediction. Check FastAPI server.")
    
st.subheader("User Input Features")
st.write(pd.DataFrame([data]))