from flask import Blueprint, request, jsonify, json
from app.api.models import Order, CustomerOrders, FeedbackResponse
from app.api.views.customer_orders import customer_orders

fastfood_get_specific_order = Blueprint('get_specific_order', __name__)


@fastfood_get_specific_order.route('/api/v1/orders/<int:order_id>', methods=['GET'])
def get_specific_order(order_id):
    """
    gets user order by id
    """
    if request.method == "GET":
        the_order = customer_orders.get_order(order_id)
        if the_order == "order does not exist":
            return FeedbackResponse.display(the_order, 404)
        else:
            return jsonify(customer_orders.get_order(order_id).toJSON()), 200
