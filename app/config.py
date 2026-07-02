import os
from pathlib import Path

# Get the project root directory
BASE_DIR = Path(__file__).parent.parent

# Model and data paths
MODELS_DIR = BASE_DIR / "models"
DATA_DIR = BASE_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

# Flask configuration
class Config:
    """Base configuration"""
    FLASK_ENV = os.getenv("FLASK_ENV", "development")
    DEBUG = FLASK_ENV == "development"
    TESTING = False

class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True

class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False