# Credit Card Approval Prediction

A machine learning project that predicts credit card approval using various classification models with a Flask web application interface.

## 📋 Project Overview

This project analyzes credit card applications and predicts whether a card will be approved or rejected based on applicant information. It uses multiple machine learning models including Logistic Regression, Decision Trees, and Random Forests.

## 📁 Project Structure

```
Credit-Card-Approval-Prediction/
├── data collection/
│   ├── application_record.csv      # Applicant information dataset
│   └── credit_record.csv           # Credit history dataset
├── Data Pre-processing/
│   └── pre-processing.ipynb        # Data cleaning and preparation
├── Model Building/
│   ├── logistic_regression.ipynb   # Logistic Regression model
│   ├── decision_tree.ipynb         # Decision Tree model
│   ├── random_forest.ipynb         # Random Forest model
│   ├── model.pkl                   # Trained model (serialized)
│   └── encoders.pkl                # Category encoders (serialized)
├── Visualizing and analyzing the data/
│   └── Visualization.ipynb         # Data visualization and analysis
├── Application Building/
│   ├── app.py                      # Flask application
│   ├── templates/
│   │   ├── dileep.html             # Input form page
│   │   └── result.html             # Prediction result page
│   └── static/
│       └── style.css               # Stylesheet
├── Entity Relationship Diagram/    # Database schema diagrams
├── requirements.txt                # Python dependencies
└── README.md                       # This file
```


## 📊 Models Used

### 1. **Logistic Regression**
- Binary classification algorithm
- Fast and interpretable
- Good baseline model

### 2. **Decision Tree**
- Tree-based classifier
- Easy to visualize and understand
- Prone to overfitting

### 3. **Random Forest**
- Ensemble method combining multiple decision trees
- Reduces overfitting
- Best overall performance
- **Selected as the final model**

## 📈 Data Description

### Application Record Dataset
- **ID**: Unique customer identifier
- **CODE_GENDER**: Gender (M/F)
- **DAYS_BIRTH**: Age in days from birth (negative)
- **DAYS_EMPLOYED**: Employment duration in days (negative)
- **NAME_INCOME_TYPE**: Income category
- **NAME_EDUCATION_TYPE**: Education level
- **NAME_FAMILY_STATUS**: Marital status
- **NAME_HOUSING_TYPE**: Housing type
- **CNT_CHILDREN**: Number of children
- **CNT_FAM_MEMBERS**: Number of family members
- **OCCUPATION_TYPE**: Occupation category

### Credit Record Dataset
- **ID**: Customer identifier
- **MONTHS_BALANCE**: Month balance
- **STATUS**: Payment status (0-5, X, C)

## 🎯 Target Variable

**Approved**: Binary classification
- 0 = Credit Card Rejected (Good customer)
- 1 = Credit Card Approved (Bad customer)

## ✅ Input Validation

The Flask application includes comprehensive input validation:

- **Age**: Must be negative (days before birth) and between -30000 to 0
- **Income**: Must be non-negative
- **Children**: Must be non-negative
- **Family Members**: Must be greater than 0
- **All categorical fields**: Required and must match predefined options
- **Encoding validation**: Catches invalid categorical values

## 🔐 Error Handling

The application handles various error scenarios:

- Missing or invalid input data
- Model loading failures
- Invalid categorical values during encoding
- Database/file access errors
- Unexpected runtime errors

All errors are logged and displayed to users with clear messages.

## 📦 Dependencies

```
numpy           # Numerical computations
pandas          # Data manipulation
scikit-learn    # Machine learning
matplotlib      # Data visualization
seaborn         # Statistical visualization
jupyter         # Notebook environment
ipython         # Interactive shell
scipy           # Scientific computing
plotly          # Interactive plots
flask           # Web framework
joblib          # Model serialization
```

## 🛠️ Development Notes

### Model Training
- Train/test split: 80/20
- Stratified sampling: Used to maintain class distribution
- Encoding: Label encoding for categorical variables

### Feature Engineering
- Missing values filled with "Unknown"
- Categorical variables encoded using LabelEncoder
- No feature scaling required for tree-based models

### Class Imbalance
- Target variable is highly imbalanced (35,841 vs 616)
- Consider SMOTE or class weights for improved performance

## 📝 Usage Examples

### Run Jupyter Notebooks:
```bash
jupyter notebook
```

Then open:
- `Data Pre-processing/pre-processing.ipynb` - Data exploration
- `Model Building/logistic_regression.ipynb` - LR model
- `Model Building/decision_tree.ipynb` - DT model
- `Model Building/random_forest.ipynb` - RF model
- `Visualizing and analyzing the data/Visualization.ipynb` - Visualizations

## 🐛 Known Issues & Improvements

### Current Issues:
1. Class imbalance in target variable (98.3% class 0)
2. Limited feature engineering
3. No cross-validation in current implementation
4. Hard-coded model paths (assumes specific directory structure)

### Future Improvements:
1. Implement SMOTE for handling class imbalance
2. Add more feature engineering techniques
3. Use GridSearchCV/RandomizedSearchCV for hyperparameter tuning
4. Add cross-validation
5. Implement model explainability (SHAP values)
6. Add user authentication for Flask app
7. Deploy to production environment (Heroku, AWS, etc.)
8. Add API endpoints for programmatic access
9. Implement model versioning
10. Add A/B testing framework

## 🤝 Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.

## 📄 License

This project is open source and available under the MIT License.

## 👤 Author

## Authors

- **Baipothu Dileep** – Team Lead
- **Rajasri Kadali** – Member
- **Kodi Sahithi** – Member
- **Chempakayala Tharakesh** – Member
- **Anjali Vinukonda** – Member
## 📚 References

- [Scikit-learn Documentation](https://scikit-learn.org/)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Pandas Documentation](https://pandas.pydata.org/)
- [Credit Card Approval Dataset](https://www.kaggle.com/)

## 📞 Support

For questions or issues, please open a GitHub issue or contact the author directly.

---

**Last Updated**: July 2, 2026
**Version**: 1.0.0
