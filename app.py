from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open("linear_regression_model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    bedrooms = float(request.form["bedrooms"])
    kitchens = float(request.form["kitchens"])
    bathrooms = float(request.form["bathrooms"])
    area = float(request.form["area"])
    furnished = 1 if request.form["furnished"] == "yes" else 0
    location = float(request.form["location"])
    parking = float(request.form["parking"])

    # Convert inputs into numeric array (8 features)
    features = np.array([[bedrooms, kitchens, bathrooms,
                           area / 1000,
                           furnished, location,
                           parking, 1.0]])

    scaled_data = scaler.transform(features)
    prediction = model.predict(scaled_data)[0]

    return render_template(
        "index.html",
        prediction_text=f"Estimated House Price: ₹ {prediction * 100000:.2f}"
    )

if __name__ == "__main__":
    app.run(debug=True)

