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
 
    def delete_order(self, order_id):
        """
       create method to delete order of a given order_id
       """
        del self.orders[order_id]


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

    def delete(self, order_id):
        """
        create the delete method to pick order
        """
        self.abort_if_order_doesnt_exist(order_id)
        ORDER_MANAGER.delete_order(order_id)
        return '', status.HTTP_204_NO_CONTENT

API.add_resource(Order, '/API/v1/orders/<int:order_id>',
                 endpoint='Order_endpoint')

if __name__ == '__main__':
    APP.run(debug=True)
