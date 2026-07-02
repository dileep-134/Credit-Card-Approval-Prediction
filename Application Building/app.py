from flask import Flask, render_template, request, jsonify
import numpy as np
import joblib
import os
import logging
from pathlib import Path

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load trained model and encoders
def load_model_and_encoders():
    """Load model and encoders with proper error handling"""
    try:
        # Use absolute path for model files
        model_dir = Path(__file__).parent.parent / "Model Building"
        
        model_path = model_dir / "model.pkl"
        encoders_path = model_dir / "encoders.pkl"
        
        if not model_path.exists():
            raise FileNotFoundError(f"Model file not found: {model_path}")
        if not encoders_path.exists():
            raise FileNotFoundError(f"Encoders file not found: {encoders_path}")
        
        model = joblib.load(model_path)
        encoders = joblib.load(encoders_path)
        
        logger.info("Model and encoders loaded successfully")
        return model, encoders
    
    except Exception as e:
        logger.error(f"Error loading model: {e}")
        raise

# Load model and encoders on startup
try:
    model, encoders = load_model_and_encoders()
except Exception as e:
    logger.error(f"Failed to load model on startup: {e}")
    model, encoders = None, None


def validate_input(data):
    """Validate and sanitize input data"""
    errors = []
    
    try:
        age = float(data.get("Age", 0))
        if age > 0 or age < -30000:
            errors.append("Age must be negative (days before birth)")
    except (ValueError, TypeError):
        errors.append("Age must be a valid number")
    
    try:
        income = float(data.get("Income", 0))
        if income < 0:
            errors.append("Income cannot be negative")
    except (ValueError, TypeError):
        errors.append("Income must be a valid number")
    
    try:
        employment_duration = float(data.get("Employment_Duration", 0))
    except (ValueError, TypeError):
        errors.append("Employment Duration must be a valid number")
    
    try:
        children = float(data.get("Children", 0))
        if children < 0:
            errors.append("Children count cannot be negative")
    except (ValueError, TypeError):
        errors.append("Children must be a valid number")
    
    try:
        family_members = float(data.get("Family_Members", 0))
        if family_members <= 0:
            errors.append("Family Members must be greater than 0")
    except (ValueError, TypeError):
        errors.append("Family Members must be a valid number")
    
    # Check for required fields
    required_fields = ["Gender", "Age", "Income", "Income_Type", 
                      "Employment_Duration", "Marital_Status", 
                      "Children", "Education", "Family_Members", "Occupation"]
    
    for field in required_fields:
        if not data.get(field):
            errors.append(f"{field} is required")
    
    return errors


@app.route("/")
def home():
    """Render home page"""
    return render_template("dileep.html")


@app.route("/predict", methods=["POST"])
def predict():
    """Handle credit card approval prediction"""
    try:
        # Validate model is loaded
        if model is None or encoders is None:
            return jsonify({
                "error": "Model is not available. Please contact administrator."
            }), 500
        
        # -------------------------
        # Validate Input Data
        # -------------------------
        validation_errors = validate_input(request.form)
        if validation_errors:
            return render_template(
                "result.html",
                prediction="❌ Invalid Input",
                confidence=0,
                error_message="; ".join(validation_errors)
            ), 400
        
        # -------------------------
        # Read Form Data
        # -------------------------
        gender = request.form.get("Gender").strip()
        age = float(request.form.get("Age"))
        income = float(request.form.get("Income"))
        income_type = request.form.get("Income_Type").strip()
        employment_duration = float(request.form.get("Employment_Duration"))
        marital_status = request.form.get("Marital_Status").strip()
        children = float(request.form.get("Children"))
        education = request.form.get("Education").strip()
        family_members = float(request.form.get("Family_Members"))
        occupation = request.form.get("Occupation").strip()
        
        # -------------------------
        # Encode categorical values
        # -------------------------
        try:
            gender = encoders["CODE_GENDER"].transform([gender])[0]
        except Exception as e:
            logger.error(f"Error encoding gender: {e}")
            return render_template(
                "result.html",
                prediction="❌ Invalid Gender Value",
                confidence=0,
                error_message="Invalid gender value provided"
            ), 400
        
        try:
            income_type = encoders["NAME_INCOME_TYPE"].transform([income_type])[0]
        except Exception as e:
            logger.error(f"Error encoding income type: {e}")
            return render_template(
                "result.html",
                prediction="❌ Invalid Income Type",
                confidence=0,
                error_message="Invalid income type value provided"
            ), 400
        
        try:
            marital_status = encoders["NAME_FAMILY_STATUS"].transform([marital_status])[0]
        except Exception as e:
            logger.error(f"Error encoding marital status: {e}")
            return render_template(
                "result.html",
                prediction="❌ Invalid Marital Status",
                confidence=0,
                error_message="Invalid marital status value provided"
            ), 400
        
        try:
            education = encoders["NAME_EDUCATION_TYPE"].transform([education])[0]
        except Exception as e:
            logger.error(f"Error encoding education: {e}")
            return render_template(
                "result.html",
                prediction="❌ Invalid Education Type",
                confidence=0,
                error_message="Invalid education type value provided"
            ), 400
        
        try:
            occupation = encoders["OCCUPATION_TYPE"].transform([occupation])[0]
        except Exception as e:
            logger.error(f"Error encoding occupation: {e}")
            return render_template(
                "result.html",
                prediction="❌ Invalid Occupation Type",
                confidence=0,
                error_message="Invalid occupation type value provided"
            ), 400
        
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
        
        logger.info(f"Prediction made - Result: {result}, Confidence: {confidence}%")
        
        return render_template(
            "result.html",
            prediction=result,
            confidence=confidence,
            error_message=None
        )
    
    except ValueError as e:
        logger.error(f"Value error: {e}")
        return render_template(
            "result.html",
            prediction="❌ Invalid Input",
            confidence=0,
            error_message="Invalid data format provided"
        ), 400
    
    except Exception as e:
        logger.error(f"Unexpected error: {e}", exc_info=True)
        return render_template(
            "result.html",
            prediction="❌ Prediction Error",
            confidence=0,
            error_message="An unexpected error occurred. Please try again."
        ), 500


@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return "Page not found", 404


@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    logger.error(f"Internal server error: {error}")
    return "Internal server error", 500


if __name__ == "__main__":
    # Use environment variable to control debug mode
    debug_mode = os.getenv("FLASK_DEBUG", "False").lower() == "true"
    app.run(debug=debug_mode, host="0.0.0.0", port=5000)
