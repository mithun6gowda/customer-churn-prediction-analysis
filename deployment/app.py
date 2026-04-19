import streamlit as st
import json
import numpy as np
import pickle

# Load model
import os
import json
import pickle

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model_path = os.path.join(BASE_DIR, "..", "churn_prediction.pkl")
columns_path = os.path.join(BASE_DIR, "..", "columns.json")

with open(model_path, "rb") as f:
    model = pickle.load(f)

with open(columns_path, "r") as f:
    data_columns = json.load(f)['data_columns']

st.title("My ML Model App")

st.write("Enter feature values:")

input_data = {}

for col in data_columns:
    input_data[col] = st.number_input(f"{col}", value=0.0)

# Convert input to array
input_array = np.array([list(input_data.values())])

if st.button("Predict"):
    prediction = model.predict(input_array)
    st.success(f"Prediction: {prediction[0]}")