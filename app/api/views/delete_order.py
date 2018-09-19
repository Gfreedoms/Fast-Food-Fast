"""
Module to delete a given food item
"""
from flask import Blueprint, request
from app.api.models import FeedbackResponse
from app.api.views.customer_orders import customer_orders

FFF_DELETE = Blueprint('delete_order', __name__)


@FFF_DELETE.route('/api/v1/orders/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    """
    delete a given order given a specific id
    """
    if request.method == "DELETE":
        the_order = customer_orders.deletes_order(order_id)
        if the_order == "order does not exist":
            return FeedbackResponse.display(the_order, 404)
        return FeedbackResponse.display(the_order, 200)
