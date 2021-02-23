from dotenv import load_dotenv
from pathlib import Path
import os

env_path = Path('../')
load_dotenv(env_path)

class Config:
    TESTING = os.getenv('TESTING')
    FLASK_DEBUG = os.getenv('FLASK_DEBUG')
    FLASK_ENV = os.getenv('FLASK_ENV')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    SERVER = os.getenv('SERVER')
    PORT = os.getenv('PORT')
    MONGO_URI = os.getenv('DB_CONNECTION_URL')
