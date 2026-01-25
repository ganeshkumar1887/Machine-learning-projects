import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics.pairwise import cosine_similarity

st.set_page_config(page_title="Restaurant Recommendation System", layout="centered")

@st.cache_data
def load_data():
    return pd.read_csv("Dataset .csv")

df = load_data()

df = df.dropna(subset=['Cuisines', 'Aggregate rating', 'Price range'])
df['Votes'].fillna(df['Votes'].median(), inplace=True)

le = LabelEncoder()
df['Cuisines_encoded'] = le.fit_transform(df['Cuisines'])
df['Online_delivery_encoded'] = df['Has Online delivery'].map({'Yes': 1, 'No': 0})

features = df[['Cuisines_encoded', 'Price range', 'Aggregate rating', 'Online_delivery_encoded']]

st.title("🍽️ Restaurant Recommendation System")
st.write("Content-Based Filtering using User Preferences")
st.divider()

cuisine = st.selectbox("🍕 Select Preferred Cuisine", sorted(df['Cuisines'].unique()))

price_range = st.selectbox(
    "💰 Select Price Range",
    options=[1, 2, 3, 4],
    format_func=lambda x: {1: "Low", 2: "Medium", 3: "High", 4: "Very High"}[x]
)

min_rating = st.slider("⭐ Minimum Rating", 0.0, 5.0, 4.0, 0.1)

online_delivery = st.radio("🚚 Online Delivery Required?", ["Yes", "No"])
online_delivery = 1 if online_delivery == "Yes" else 0

top_n = st.slider("🔢 Number of Recommendations", 1, 10, 5)

def recommend_restaurants():
    cuisine_encoded = le.transform([cuisine])[0]
    user_vector = np.array([[cuisine_encoded, price_range, min_rating, online_delivery]])
    similarity_scores = cosine_similarity(user_vector, features)
    df['Similarity'] = similarity_scores[0]
    filtered_df = df[
        (df['Aggregate rating'] >= min_rating) &
        (df['Online_delivery_encoded'] == online_delivery)
    ]
    recommendations = filtered_df.sort_values(by='Similarity', ascending=False).head(top_n)
    return recommendations[['Restaurant Name', 'Cuisines', 'Aggregate rating', 'Price range', 'Has Online delivery']]

if st.button("🔍 Recommend Restaurants"):
    result = recommend_restaurants()
    if result.empty:
        st.warning("⚠️ No restaurants found for selected preferences.")
    else:
        st.success("✅ Top Recommended Restaurants")
        st.dataframe(result, use_container_width=True)
