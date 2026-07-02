# Credit Card Approval Prediction

A machine learning project that predicts credit card approval using various classification models with a Flask web application interface.

## 📋 Project Overview

This project analyzes credit card applications and predicts whether a card will be approved or rejected based on applicant information. It uses multiple machine learning models including Logistic Regression, Decision Trees, and Random Forest with the Random Forest model selected for production deployment.

## 🆕 Updated Project Structure

```
Credit-Card-Approval-Prediction/
├── data/
│   ├── raw/                              # Original datasets
│   │   ├── application_record.csv
│   │   └── credit_record.csv
│   └── processed/                        # Processed datasets
├── notebooks/                            # Jupyter analysis notebooks
│   ├── 01-data-collection.ipynb
│   ├── 02-data-preprocessing.ipynb
│   ├── 03-data-visualization.ipynb
│   └── 04-model-building.ipynb
├── models/                               # Trained models
│   ├── model.pkl
│   └── encoders.pkl
├── app/                                  # Flask application
│   ├── main.py
│   └── config.py
├── templates/                            # HTML templates
│   ├── index.html
│   └── result.html
├── static/                               # CSS/JS files
│   └── style.css
├── docs/                                 # Documentation
│   └── PROJECT_STRUCTURE.md
├── requirements.txt
└── README.md
```

**Key improvements:**
- ✅ Fixed typo: `data coluction` → `data/raw/` and `data/processed/`
- ✅ Standardized folder naming (lowercase with hyphens)
- ✅ Separated data, code, and models
- ✅ Better documentation structure
- ✅ Added `.gitignore` and configuration files

## 🔧 Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Setup Instructions

1. **Clone the repository:**
```bash
git clone https://github.com/dileep-134/Credit-Card-Approval-Prediction.git
cd Credit-Card-Approval-Prediction
```

2. **Create a virtual environment:**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

## 🚀 Running the Application

### Start the Flask Server:
```bash
python app/main.py
```

The application will be available at `http://localhost:5000`

### Using the Web Interface:
1. Navigate to `http://localhost:5000` in your browser
2. Fill in the applicant details
3. Click "Predict" to get the approval prediction with confidence score

## 📊 Models Used

### Random Forest (Selected)
- Ensemble method combining multiple decision trees
- Best overall performance (98.09% accuracy)
- Robust to overfitting

### Also Included
- **Logistic Regression**: Fast baseline model
- **Decision Tree**: Interpretable tree-based model

## 📈 Data Description

### Application Record Dataset
- Customer demographics and financial information
- 438,557 records with 18 features

### Credit Record Dataset
- Payment history and credit status
- Used to create target variable

## ✅ Input Validation

Comprehensive validation for:
- Age, Income, Employment Duration, etc.
- Categorical fields validation
- Error logging and user-friendly messages

## 📦 Dependencies

See `requirements.txt` for the complete list including:
- numpy, pandas, scikit-learn
- flask, joblib
- matplotlib, seaborn, plotly

## 🛠️ Development

### Running Notebooks:
```bash
jupyter notebook
```

Then open notebooks in the `notebooks/` directory

## 📚 Documentation

See `docs/PROJECT_STRUCTURE.md` for detailed folder organization and best practices.

## 🐛 Known Issues & Future Improvements

- Class imbalance in target variable (98.3% vs 1.7%)
- Potential for SMOTE implementation
- Cross-validation planned for next version
- Model explainability (SHAP) to be added

## 👤 Author

**Dileep B** - [@dileep-134](https://github.com/dileep-134)

## 📄 License

MIT License - Open source and available for use
