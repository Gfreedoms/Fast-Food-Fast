"""
Module to handle innitialisation code of the modules
"""
import os
from flask import Flask, render_template
from app.api.views.update_order import FFF_PUT

app = Flask(__name__)

app.register_blueprint(FFF_PUT)

app.config['SECRET_KEY'] = os.environ.get(
    'SECRET_KEY', 'Freedoms')
