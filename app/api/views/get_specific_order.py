"""
Module to retrieve a specific order given a certain id
"""
from flask import Blueprint, request, jsonify
from app.api.models import FeedbackResponse
from app.api.views.customer_orders import customer_orders

FFF_GET_SPECIFIC = Blueprint('get_specific_order', __name__)


@FFF_GET_SPECIFIC.route('/api/v1/orders/<int:order_id>', methods=['GET'])
def get_specific_order(order_id):
    """
    gets user order by id
    """
    if request.method == "GET":
        the_order = customer_orders.get_order(order_id)
        if the_order == "order does not exist":
            return FeedbackResponse.display(the_order, 404)
        return jsonify(customer_orders.get_order(order_id).toJSON()), 200
