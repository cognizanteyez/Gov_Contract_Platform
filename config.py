import os


class Config:
    """Runtime configuration supplied through environment variables."""

    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or "sqlite:///app.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SAM_API_KEY = os.environ.get("SAM_API_KEY")
