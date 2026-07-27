import streamlit as st
import pandas as pd
import pickle

# Load Model
model = pickle.load(open("house_price_model.pkl", "rb"))

st.set_page_config(page_title="House Price Prediction", page_icon="🏠")

st.title("🏠 House Price Prediction System")

st.write("Enter the house details below to predict the estimated price.")

square_feet = st.number_input("Square Feet", min_value=500, max_value=10000, value=1500)

bedrooms = st.number_input("Bedrooms", min_value=1, max_value=10, value=3)

bathrooms = st.number_input("Bathrooms", min_value=1, max_value=10, value=2)

year_built = st.number_input("Year Built", min_value=1900, max_value=2026, value=2015)

neighborhood = st.selectbox(
    "Neighborhood",
    ["Rural", "Suburb", "Urban"]
)

suburb = 1 if neighborhood == "Suburb" else 0
urban = 1 if neighborhood == "Urban" else 0

input_data = pd.DataFrame({
    "SquareFeet": [square_feet],
    "Bedrooms": [bedrooms],
    "Bathrooms": [bathrooms],
    "YearBuilt": [year_built],
    "Neighborhood_Suburb": [suburb],
    "Neighborhood_Urban": [urban]
})

if st.button("Predict Price"):

    prediction = model.predict(input_data)

    st.success(f"Estimated House Price: ${prediction[0]:,.2f}")