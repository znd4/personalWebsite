"""Zane Dufour's personal website project.
This is where we set up our application...
although maybe we should be doing that somewhere else.
"""
# pylint: disable=invalid-name,wrong-import-position
from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

from znd4 import routes
