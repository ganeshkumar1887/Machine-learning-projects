import streamlit as st
import pandas as pd
import joblib

# Load model & columns
model = joblib.load("decision_tree_model.pkl")
columns = joblib.load("model_columns.pkl")

st.set_page_config(page_title="Restaurant Rating Predictor", layout="centered")

st.title("🍽️ Restaurant Rating Predictor")
st.write("Predict restaurant ratings using Machine Learning")

st.divider()

# User Inputs
votes = st.number_input("⭐ Votes", min_value=0, step=10)
avg_cost = st.number_input("💰 Average Cost for Two", min_value=0, step=100)
price_range = st.selectbox("💳 Price Range (1-4)", [1, 2, 3, 4])
online_delivery = st.selectbox("📦 Online Delivery", ["Yes", "No"])

online_delivery = 1 if online_delivery == "Yes" else 0

if st.button("🔮 Predict Rating"):
    input_df = pd.DataFrame(0, index=[0], columns=columns)

    input_df["Votes"] = votes
    input_df["Average Cost for two"] = avg_cost
    input_df["Price range"] = price_range
    input_df["Has Online delivery"] = online_delivery

    prediction = model.predict(input_df)[0]

    st.success(f"⭐ Predicted Restaurant Rating: {round(prediction, 2)}")
