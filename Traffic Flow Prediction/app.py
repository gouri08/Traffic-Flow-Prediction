import streamlit as st
import numpy as np
import joblib
from datetime import datetime

# Load model and label encoder
model, le_target = joblib.load("traffic_rf_model.pkl")

# UI config
st.set_page_config(page_title="Traffic Predictor", layout="centered")
st.title("🚦 Traffic Flow Predictor")

st.markdown("Enter traffic details to predict:")
st.markdown("- 🔢 ML Prediction (Encoded)")
st.markdown("- 🏷️ ML Prediction (Label)")
st.markdown("- 📊 Rule-based Interpretation (based on vehicle count)")

# Input Form
with st.form("form"):
    col1, col2 = st.columns(2)
    with col1:
        car = st.number_input("Car Count", min_value=0, value=10)
        bike = st.number_input("Bike Count", min_value=0, value=5)
        bus = st.number_input("Bus Count", min_value=0, value=2)
        truck = st.number_input("Truck Count", min_value=0, value=1)

    with col2:
        day_name = st.selectbox("Day of Week", 
            ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])
        time_input = st.time_input("Time", value=datetime.strptime("08:00", "%H:%M").time())
        date_input = st.date_input("Date")

    submit = st.form_submit_button("🔮 Predict")

# Prediction
if submit:
    # Process input
    day_map = {
        "Monday": 0, "Tuesday": 1, "Wednesday": 2,
        "Thursday": 3, "Friday": 4, "Saturday": 5, "Sunday": 6
    }
    day_encoded = day_map[day_name]
    hour = time_input.hour
    total = car + bike + bus + truck
    month = date_input.month
    day = date_input.day

    input_data = np.array([[car, bike, bus, truck, total, hour, day_encoded, month, day]])

    # Predict
    encoded = model.predict(input_data)[0]
    label = le_target.inverse_transform([encoded])[0]

    # Rule-based logic
    if total <= 10:
        tag = "Low"
    elif total <= 50:
        tag = "Moderate"
    elif total <= 100:
        tag = "Normal"
    else:
        tag = "High"

    # Output
    st.success(f"🔢 Predicted Traffic Situation (encoded): {encoded}")
    st.success(f"🏷️ Predicted Traffic Situation: {label}")
    st.info(f"📊 Based on total vehicles ({total}): **{tag} traffic** (rule-based)")
