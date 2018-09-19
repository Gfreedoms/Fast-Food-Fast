"""
nodule to handle order update 
"""
from flask import Blueprint, request
from app.api.models import FeedbackResponse
from app.api.views.customer_orders import customer_orders

FFF_PUT = Blueprint('update_order_status', __name__)


@FFF_PUT.route('/api/v1/orders/<int:order_id>', methods=['PUT'])
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
