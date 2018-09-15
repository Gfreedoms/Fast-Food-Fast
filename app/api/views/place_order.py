from flask import Blueprint, request, jsonify, json
from app.api.models import Order, CustomerOrders, FeedbackResponse
from app.api.views.customer_orders import customer_orders

fastfood_place_order = Blueprint('place_order', __name__)


@fastfood_place_order.route('/api/v1/orders', methods=['POST'])
def place_order():
    """
     method to create new order and apend to the existing list
    """
    if request.method == 'POST':
        data = request.get_json()
        if not data.get('order_number'):
            return FeedbackResponse.display("set order number please", 406)
        if not data.get('order_description'):
            return FeedbackResponse.display("set description please", 406)
        if not data.get('size'):
            return FeedbackResponse.display("set size please ", 406),
        if not data.get('order_price'):
            return FeedbackResponse.display("set price please", 406)        

        order_number = data.get('order_number')
        order_description = data.get('order_description')
        order_price = data.get('order_price')
        size = data.get('size')

        new_order = Order(order_number, order_description,
                          order_price, size)

        customer_orders.place_order(new_order)
        return FeedbackResponse.display("order number "+ order_number +" successfully placed", 200)
