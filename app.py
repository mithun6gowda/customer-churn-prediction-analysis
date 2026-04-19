from flask import Flask, render_template, request
import pickle
import json
import numpy as np
import os

app = Flask(__name__)

# Load model
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model_path = os.path.join(BASE_DIR, "model", "churn_prediction.pkl")
columns_path = os.path.join(BASE_DIR, "model", "columns.json")

with open(model_path, "rb") as f:
    model = pickle.load(f)

with open(columns_path, "r") as f:
    data_columns = json.load(f)["data_columns"]


@app.route("/", methods=["GET", "POST"])
def index_page():
    if request.method == "POST":
        input_data = {}

        for col in data_columns:
            val = request.form.get(col)

            # Convert to float safely
            try:
                input_data[col] = float(val)
            except:
                input_data[col] = 0

        # Maintain correct order
        input_array = np.array([[input_data[col] for col in data_columns]])

        prediction = model.predict(input_array)[0]

        result = "Churn" if prediction == 1 else "Not Churn"

        return render_template("result.html", data={
            "prediction": result
        })

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)