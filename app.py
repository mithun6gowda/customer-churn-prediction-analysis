from flask import Flask, render_template, request
import pickle
import json
import numpy as np
import os

app = Flask(__name__)

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model_path = os.path.join(BASE_DIR, "deployment", "model", "churn_prediction.pkl")
columns_path = os.path.join(BASE_DIR, "deployment", "model", "columns.json")

# Load model
with open(model_path, "rb") as f:
    model = pickle.load(f)

with open(columns_path, "r") as f:
    data_columns = json.load(f)["data_columns"]


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        input_data = {}

        # Handle numeric fields
        for col in data_columns:
            if col not in [
                "gender_female", "gender_male",
                "maritalstatus_divorced",
                "maritalstatus_married",
                "maritalstatus_single"
            ]:
                val = request.form.get(col)
                try:
                    input_data[col] = float(val)
                except:
                    input_data[col] = 0

        # Handle Gender
        gender = request.form.get("gender")
        input_data["gender_female"] = 1 if gender == "female" else 0
        input_data["gender_male"] = 1 if gender == "male" else 0

        # Handle Marital Status
        marital = request.form.get("maritalstatus")
        input_data["maritalstatus_divorced"] = 1 if marital == "divorced" else 0
        input_data["maritalstatus_married"] = 1 if marital == "married" else 0
        input_data["maritalstatus_single"] = 1 if marital == "single" else 0

        # Maintain order
        input_array = np.array([[input_data[col] for col in data_columns]])

        prediction = model.predict(input_array)[0]

        result = "Churn" if prediction == 1 else "Not Churn"

        return render_template("result.html", data={
            "prediction": result
        })

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)