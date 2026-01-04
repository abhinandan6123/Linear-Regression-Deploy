from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open("linear_regression_model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

from flask import render_template

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()["data"]
    data = np.array(data).reshape(1, -1)
    scaled_data = scaler.transform(data)
    prediction = model.predict(scaled_data)
    return jsonify({"prediction": prediction[0]})

if __name__ == "__main__":
    app.run()
