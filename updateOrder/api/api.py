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

    def update_order(self, order):
        """
       create method to update an existing order
       """
        order.order_id = self.__class__.last_order_id
        self.orders[self.__class__.last_order_id] = order


    def put_order(self, order_id):
        """
        update a given order
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
    def put(self, order_id):
        """
        create method to update orders
        """
        self.abort_if_order_doesnt_exist(order_id)
        parser = reqparse.RequestParser()
        parser.add_argument('title', type=str)
        parser.add_argument('pieces', type=int)
        parser.add_argument('quantity', type=str)
        args = parser.parse_args()
        order = OrderModel(
            title=args['title'],
            pieces=args['pieces'],
            quantity=args['quantity']
        )
        ORDER_MANAGER.update_order(order)
        return ORDER_MANAGER.put_order(order_id)


API.add_resource(Order, '/API/v1/orders/<int:order_id>',
                 endpoint='Order_endpoint')

if __name__ == '__main__':
    APP.run(debug=True)
