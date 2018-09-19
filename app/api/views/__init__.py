"""
Module to handle innitialisation code of the modules
"""
import os
from flask import Flask, render_template
from app.api.views.place_order import FFF_POST

app = Flask(__name__)


app.register_blueprint(FFF_POST)

app.config['SECRET_KEY'] = os.environ.get(
    'SECRET_KEY', 'Freedoms')
