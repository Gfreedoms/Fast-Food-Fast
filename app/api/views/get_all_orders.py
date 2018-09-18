"""
Module to  retrieve orders
"""
from flask import Blueprint, request, jsonify
from app.api.views.customer_orders import customer_orders

FFF_GET = Blueprint('get_all_orders', __name__)


@FFF_GET.route('/api/v1/orders', methods=['GET'])
def get_all_orders():
    """
    gets all the placed orders
    """
    if request.method == "GET":
        all_orders = []
        for key in range(len(customer_orders.get_orders())):
            all_orders.append(customer_orders.get_orders()[key].toJSON())

        return jsonify(all_orders), 200
