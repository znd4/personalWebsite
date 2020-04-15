import os
from pathlib import Path

basedir = Path(__file__).resolve().parent


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY") or "you-will-never-guess"
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL") or "sqlite:///" + (
        basedir / "app.db"
    )
