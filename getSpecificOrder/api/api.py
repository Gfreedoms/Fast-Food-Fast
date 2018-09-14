"""
Fast food fast
"""
from flask import Flask
from flask_restful import abort, Api, fields, marshal_with, reqparse, Resource
from models import OrderModel
import status


APP = Flask(__name__)
API = Api(APP)

"""
Create the order manager class
"""


class OrderManager():
    """
    Create the order manager class
    """
    last_order_id = 0

    """
    create constructor method for order manager
    """

    def __init__(self):
        """
        create constructor method for order manager
        """
        self.orders = {}

    def get_order(self, order_id):
        """
       create method to handle getting orders
       """
        return self.orders[order_id]


ORDER_FIELDS = {
    'order_id': fields.Integer,
    'uri': fields.Url('Order_endpoint'),
    'title': fields.String,
    'quantity': fields.String,
    'pieces': fields.Integer,
    'complete': fields.Boolean
}

ORDER_MANAGER = OrderManager()


class Order(Resource):
    """
    class to handle resource routing
    """

    def abort_if_order_doesnt_exist(self, order_id):
        """
        method to handle non existent routes
        """
        if order_id not in ORDER_MANAGER.orders:
            abort(status.HTTP_404_NOT_FOUND,
                  error="order {0} doesn't exist".format(order_id))

    @marshal_with(ORDER_FIELDS)
    def get(self, order_id):
        """
        method to retrieve orders
        """
        self.abort_if_order_doesnt_exist(order_id)
        return ORDER_MANAGER.get_order(order_id)

 
class OrderList(Resource):

    """
    Create the orderlist method that inherits from clas resource
    """
    @marshal_with(ORDER_FIELDS)
    def get(self):
        """
        Add the get method that returns an array order values
        """
        return [v for v in ORDER_MANAGER.orders.values()]


API.add_resource(OrderList, '/API/v1/orders/')
API.add_resource(Order, '/API/v1/orders/<int:order_id>',
                 endpoint='Order_endpoint')

if __name__ == '__main__':
    APP.run(debug=True)
