import streamlit as st
import pandas as pd
import joblib

model = joblib.load("decision_tree_model.pkl")
columns = joblib.load("model_columns.pkl")

st.set_page_config(
    page_title="Restaurant Rating Predictor",
    page_icon="🍽️",
    layout="centered"
)

st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #fdfbfb, #ebedee);
}

[data-testid="stHeader"] {
    background: rgba(0,0,0,0);
}

[data-testid="stVerticalBlock"] {
    background: linear-gradient(135deg, #fff1eb, #ace0f9);
    padding: 30px;
    border-radius: 20px;
}

.title {
    font-size: 45px;
    font-weight: 800;
    text-align: center;
    color: #ff3d00;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    color: #555;
    margin-bottom: 30px;
}

.rating {
    font-size: 40px;
    font-weight: 700;
    color: #2e7d32;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='title'>🍽️ Restaurant Rating Predictor</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>AI powered web app to predict restaurant ratings</div>", unsafe_allow_html=True)

votes = st.number_input("⭐ Total Votes", min_value=0)
cost = st.number_input("💰 Average Cost for Two", min_value=0)
price = st.slider("💳 Price Range", 1, 4)
delivery = st.selectbox("📦 Online Delivery", ["Yes", "No"])
booking = st.selectbox("🪑 Table Booking", ["Yes", "No"])

input_data = {
    "Votes": votes,
    "Average Cost for two": cost,
    "Price range": price,
    "Has Online delivery": 1 if delivery == "Yes" else 0,
    "Has Table booking": 1 if booking == "Yes" else 0
}

df = pd.DataFrame([input_data])

for col in columns:
    if col not in df.columns:
        df[col] = 0

df = df[columns]

if st.button("🔮 Predict Rating"):
    rating = model.predict(df)[0]
    st.markdown(f"<div class='rating'>⭐ {round(rating,2)} / 5</div>", unsafe_allow_html=True)
