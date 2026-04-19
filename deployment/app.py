import streamlit as st
import json
import numpy as np
import pickle

# Load model
with open("churn_prediction.pkl", "rb") as f:
    model = pickle.load(f)

# Load columns
with open("columns.json", "r") as f:
    data_columns = json.load(f)['data_columns']

st.title("My ML Model App")

st.write("Enter feature values:")

# Collect inputs dynamically
input_data = {}

for col in data_columns:
    input_data[col] = st.number_input(f"{col}", value=0.0)

# Convert input to array
input_array = np.array([list(input_data.values())])

if st.button("Predict"):
    prediction = model.predict(input_array)
    st.success(f"Prediction: {prediction[0]}")