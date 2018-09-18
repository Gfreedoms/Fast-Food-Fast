"""
Module to handle innitialisation code of the modules
"""
import os
from flask import Flask, render_template
from app.api.views.get_specific_order import FFF_GET_SPECIFIC
from app.api.views.update_order import FFF_PUT
from app.api.views.delete_order import FFF_DELETE
from app.api.views.get_all_orders import FFF_GET
from app.api.views.place_order import FFF_POST

app = Flask(__name__)

app.register_blueprint(FFF_GET_SPECIFIC)
app.register_blueprint(FFF_GET)
app.register_blueprint(FFF_POST)
app.register_blueprint(FFF_PUT)
app.register_blueprint(FFF_DELETE)

app.config['SECRET_KEY'] = os.environ.get(
    'SECRET_KEY', 'Freedoms')
