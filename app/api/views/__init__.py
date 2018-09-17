from flask import Flask, render_template
from app.api.views.get_specific_order import fastfood_get_specific_order
from app.api.views.update_order import fastfood_update_order_status
from app.api.views.delete_order import fastfood_delete_order
from app.api.views.get_all_orders import fastfood_get_all_orders
from app.api.views.place_order import fastfood_place_order
import os

app = Flask(__name__)

app.register_blueprint(fastfood_get_specific_order)
app.register_blueprint(fastfood_get_all_orders)
app.register_blueprint(fastfood_place_order)
app.register_blueprint(fastfood_update_order_status)
app.register_blueprint(fastfood_delete_order)

app.config['SECRET_KEY'] = os.environ.get(
    'SECRET_KEY', 'Freedoms')
