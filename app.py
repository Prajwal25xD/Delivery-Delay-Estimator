import streamlit as st
import pandas as pd
import numpy as np
import pickle

# ================================
# LOAD MODEL + COLUMNS
# ================================
model = pickle.load(open("delivery_model.pkl", "rb"))
cols = pickle.load(open("columns.pkl", "rb"))

st.title("🚚 Delivery Delay Prediction System")

st.write("Predict whether an order will be delayed based on logistics data.")

# ================================
# USER INPUTS
# ================================

days_for_shipment = st.slider("Scheduled Shipping Days", 1, 10, 3)
order_item_quantity = st.slider("Order Quantity", 1, 10, 1)
sales = st.number_input("Sales Value", min_value=0.0, value=100.0)
discount_rate = st.slider("Discount Rate", 0.0, 1.0, 0.1)
weather_severity = st.slider("Weather Severity", 0, 5, 1)
precipitation = st.number_input("Precipitation", min_value=0.0, value=0.0)
windspeed = st.number_input("Max Wind Speed", min_value=0.0, value=5.0)

# Optional categorical (only if used in training)
shipping_mode = st.selectbox(
    "Shipping Mode",
    ["Standard Class", "Second Class", "First Class", "Same Day"]
)

# ================================
# CREATE INPUT DATAFRAME (MATCH TRAINING)
# ================================

# Initialize full dataframe with all columns
input_data = pd.DataFrame(columns=cols)
input_data.loc[0] = 0  # set all values = 0

# Fill numeric features (must match training column names EXACTLY)
if 'days_for_shipment_(scheduled)' in input_data.columns:
    input_data['days_for_shipment_(scheduled)'] = days_for_shipment

if 'order_item_quantity' in input_data.columns:
    input_data['order_item_quantity'] = order_item_quantity

if 'sales' in input_data.columns:
    input_data['sales'] = sales

if 'order_item_discount_rate' in input_data.columns:
    input_data['order_item_discount_rate'] = discount_rate

if 'weather_severity' in input_data.columns:
    input_data['weather_severity'] = weather_severity

if 'precipitation_sum' in input_data.columns:
    input_data['precipitation_sum'] = precipitation

if 'windspeed_max' in input_data.columns:
    input_data['windspeed_max'] = windspeed

# ================================
# HANDLE ONE-HOT ENCODED FEATURES
# ================================

# Example: shipping_mode_Standard Class
shipping_col = f"shipping_mode_{shipping_mode}"

if shipping_col in input_data.columns:
    input_data[shipping_col] = 1

# ================================
# PREDICTION
# ================================

if st.button("Predict"):
    prediction = model.predict(input_data)[0]
    prob = model.predict_proba(input_data)[0][1]

    st.subheader("📊 Prediction Result")

    if prediction == 1:
        st.error("⚠️ High Risk: Delivery will be DELAYED")
    else:
        st.success("✅ Delivery will be ON TIME")

    # Probability visualization
    st.progress(int(prob * 100))
    st.write(f"**Delay Probability:** {prob:.2%}")

    # Risk level
    if prob > 0.7:
        st.warning("🚨 Very High Delay Risk")
    elif prob > 0.4:
        st.info("⚠️ Moderate Risk")
    else:
        st.success("✅ Low Risk")