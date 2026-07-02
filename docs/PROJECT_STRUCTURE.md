# Project Structure Guide

## Directory Organization

```
Credit-Card-Approval-Prediction/
├── data/                          # Data directory
│   ├── raw/                      # Raw datasets
│   │   ├── application_record.csv
│   │   └── credit_record.csv
│   └── processed/                # Processed/cleaned data
│       ├── application_processed.csv
│       └── credit_processed.csv
│
├── notebooks/                     # Jupyter notebooks (analysis & exploration)
│   ├── 01-data-collection.ipynb
│   ├── 02-data-preprocessing.ipynb
│   ├── 03-data-visualization.ipynb
│   └── 04-model-building.ipynb
│
├── models/                        # Serialized models
│   ├── model.pkl                 # Final trained model
│   └── encoders.pkl              # Categorical encoders
│
├── app/                           # Flask application
│   ├── __init__.py
│   ├── main.py                   # Main Flask app
│   ├── config.py                 # Configuration
│   └── utils.py                  # Utility functions
│
├── templates/                     # Flask HTML templates
│   ├── index.html                # Input form
│   └── result.html               # Prediction results
│
├── static/                        # Static files (CSS, JS, images)
│   └── style.css
│
├── docs/                          # Documentation
│   ├── PROJECT_STRUCTURE.md
│   ├── MODELS.md
│   └── API.md
│
├── requirements.txt              # Python dependencies
├── README.md                     # Project overview
└── .gitignore                    # Git ignore file
```

## Folder Descriptions

### data/
- **raw/**: Original, unmodified datasets
- **processed/**: Cleaned, preprocessed data ready for modeling

### notebooks/
Jupyter notebooks for exploration and analysis:
- 01-data-collection: Data overview and loading
- 02-data-preprocessing: Cleaning and transformation
- 03-data-visualization: Analysis and visualizations
- 04-model-building: Model training and evaluation

### models/
Serialized model files:
- `model.pkl`: Trained Random Forest classifier
- `encoders.pkl`: Fitted categorical encoders

### app/
Flask web application code:
- `main.py`: Core application with routes
- `config.py`: Environment configuration
- `utils.py`: Helper functions (optional)

### templates/ & static/
Web interface files:
- HTML templates for Flask
- CSS/JS for styling and interactivity

## File Naming Conventions

- **Notebooks**: `NN-description.ipynb` (e.g., `01-data-collection.ipynb`)
- **Python files**: `lowercase_with_underscores.py`
- **Directories**: `lowercase-with-hyphens` or `lowercase_with_underscores`
- **Data files**: `descriptive_name.csv` (e.g., `application_record.csv`)
- **Models**: `model_name.pkl` (e.g., `random_forest_model.pkl`)

## Best Practices

1. **Separate concerns**: Keep data, code, and models in different directories
2. **Version control**: Track models and major datasets separately
3. **Documentation**: Keep README files in each major folder
4. **Dependencies**: Maintain updated requirements.txt
5. **Configuration**: Use config files, not hardcoded paths
6. **Naming**: Use clear, descriptive names for all files and folders