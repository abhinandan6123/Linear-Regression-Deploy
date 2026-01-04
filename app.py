from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open("linear_regression_model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        bedrooms = float(request.form.get("bedrooms", 0))
        kitchens = float(request.form.get("kitchens", 0))
        bathrooms = float(request.form.get("bathrooms", 0))
        area = float(request.form.get("area", 0))
        furnished = 1 if request.form.get("furnished") == "yes" else 0
        location = float(request.form.get("location", 0))
        parking = float(request.form.get("parking", 0))

        features = np.array([
            bedrooms,
            kitchens,
            bathrooms,
            area / 1000,
            furnished,
            location,
            parking,
            0, 0, 0, 0, 0, 0
        ]).reshape(1, -1)

        prediction = model.predict(features)[0]

        return render_template(
            "index.html",
            prediction_text=f"Estimated House Price: ₹ {prediction * 100000:.2f}"
        )

    except Exception as e:
        return render_template(
            "index.html",
            prediction_text=f"Error occurred: {str(e)}"
        )


if __name__ == "__main__":
    app.run(debug=True)


