"""
Module to handle innitialisation code of the modules
"""
import os
from flask import Flask, render_template
from app.api.views.get_specific_order import FFF_GET_SPECIFIC

app = Flask(__name__)

app.register_blueprint(FFF_GET_SPECIFIC)

app.config['SECRET_KEY'] = os.environ.get(
    'SECRET_KEY', 'Freedoms')
