from flask import Flask, render_template, request
import numpy as np
import joblib
import os

app = Flask(__name__)

# Load trained model and encoders
model_dir = os.path.join(os.path.dirname(__file__), "..", "Model Building")
model = joblib.load(os.path.join(model_dir, "model.pkl"))
encoders = joblib.load(os.path.join(model_dir, "encoders.pkl"))

@app.route("/")
def home():
    return render_template("dileep.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:

        # -------------------------
        # Read Form Data
        # -------------------------

        gender = request.form.get("Gender")
        age = float(request.form.get("Age"))
        income = float(request.form.get("Income"))
        income_type = request.form.get("Income_Type")
        employment_duration = float(request.form.get("Employment_Duration"))
        marital_status = request.form.get("Marital_Status")
        children = float(request.form.get("Children"))
        education = request.form.get("Education")
        family_members = float(request.form.get("Family_Members"))
        occupation = request.form.get("Occupation")

        # -------------------------
        # Encode categorical values
        # -------------------------

        gender = encoders["CODE_GENDER"].transform([gender])[0]

        income_type = encoders["NAME_INCOME_TYPE"].transform(
            [income_type]
        )[0]

        marital_status = encoders["NAME_FAMILY_STATUS"].transform(
            [marital_status]
        )[0]

        education = encoders["NAME_EDUCATION_TYPE"].transform(
            [education]
        )[0]

        occupation = encoders["OCCUPATION_TYPE"].transform(
            [occupation]
        )[0]

        # -------------------------
        # Create Feature Array
        # -------------------------

        features = np.array([[
            gender,
            age,
            income,
            income_type,
            employment_duration,
            marital_status,
            children,
            education,
            family_members,
            occupation
        ]])

        # -------------------------
        # Prediction
        # -------------------------

        prediction = model.predict(features)[0]

        probability = model.predict_proba(features)[0]
        confidence = round(max(probability) * 100, 2)

        if prediction == 1:
            result = "✅ Credit Card Approved"
        else:
            result = "❌ Credit Card Rejected"

        return render_template(
            "result.html",
            prediction=result,
            confidence=confidence
        )

    except Exception as e:
        return f"Error: {e}"


if __name__ == "__main__":
    app.run(debug=True)
