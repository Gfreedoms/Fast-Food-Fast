from flask import Blueprint, request, jsonify, json
from app.api.models import Order, CustomerOrders, FeedbackResponse
from app.api.views.customer_orders import customer_orders

fastfood_delete_order = Blueprint('delete_order', __name__)


@fastfood_delete_order.route('/api/v1/orders/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    """
    deletes order
    """
    if request.method == "DELETE":
        the_order = customer_orders.deletes_order(order_id)
        if the_order == "order does not exist":
            return FeedbackResponse.display(the_order, 404)
        else:
            return FeedbackResponse.display(the_order, 200)
