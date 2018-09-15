from flask import Blueprint, request, jsonify, json
from app.api.models import Order, CustomerOrders, FeedbackResponse
from app.api.views.customer_orders import customer_orders

fastfood_update_order_status = Blueprint('update_order_status', __name__)


@fastfood_update_order_status.route('/api/v1/orders/<int:order_id>', methods=['PUT'])
def update_order_status(order_id):
    """updates order status
    """
    if request.method == "PUT":
        data = request.get_json()
        if not data.get('complete'):
            return FeedbackResponse.display("status changed to complete", 406)

        complete = data.get('complete')
        status = customer_orders.change_status(order_id, complete)
        if status == "order does not exist":
            return FeedbackResponse.display(status, 404)
        else:
            return FeedbackResponse.display(status, 200)
