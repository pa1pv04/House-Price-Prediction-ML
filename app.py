from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load("model.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    features = [
        float(request.form["area"]),
        float(request.form["bedrooms"]),
        float(request.form["bathrooms"]),
        float(request.form["stories"]),
        float(request.form["mainroad"]),
        float(request.form["guestroom"]),
        float(request.form["basement"]),
        float(request.form["hotwaterheating"]),
        float(request.form["airconditioning"]),
        float(request.form["parking"]),
        float(request.form["prefarea"]),
        float(request.form["furnishingstatus"])
    ]

    prediction = model.predict([features])

    price = round(prediction[0], 2)

    return render_template(
        "index.html",
        prediction_text=f"Predicted House Price: ₹ {price}"
    )

if __name__ == "__main__":
    app.run(debug=True)