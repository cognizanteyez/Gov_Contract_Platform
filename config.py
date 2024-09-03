import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SAM_API_KEY = 'RMVjBP7PVIAAmGcCHWmvkAR6P6HvvXy7GPYB9ZfA'  # Your API key here
