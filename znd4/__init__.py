"""Zane Dufour's personal website project.
This is where we set up our application...
although maybe we should be doing that somewhere else.
"""
# pylint: disable=invalid-name,wrong-import-position
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from znd4 import routes, models
