import streamlit as st
import json
import numpy as np
import pickle
import os

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, "model", "churn_prediction.pkl")
columns_path = os.path.join(BASE_DIR, "model", "columns.json")

# Load
with open(model_path, "rb") as f:
    model = pickle.load(f)

with open(columns_path, "r") as f:
    data_columns = json.load(f)['data_columns']

st.title("📊 Customer Churn Prediction App")

st.write("Enter feature values:")

input_data = {}

for col in data_columns:
    input_data[col] = st.number_input(f"{col}", value=0.0)

# Correct ordering
input_array = np.array([[input_data[col] for col in data_columns]])

if st.button("Predict"):
    prediction = model.predict(input_array)

    if prediction[0] == 1:
        st.error("⚠️ Customer is likely to churn")
    else:
        st.success("✅ Customer will stay")