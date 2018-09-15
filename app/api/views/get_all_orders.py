from flask import Blueprint, request, jsonify, json
from app.api.models import Order, CustomerOrders
from app.api.views.customer_orders import customer_orders

fastfood_get_all_orders = Blueprint('get_all_orders', __name__)


@fastfood_get_all_orders.route('/api/v1/orders', methods=['GET'])
def get_all_orders():
    """
    gets all the placed orders
    """
    if request.method == "GET":
        all_orders = []
        for key in range(len(customer_orders.get_orders())):
            all_orders.append(customer_orders.get_orders()[key].toJSON())

        return jsonify(all_orders), 200
