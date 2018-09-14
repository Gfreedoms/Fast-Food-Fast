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

    def insert_order(self, order):
        """
        insert order and update order_id automatically
        """
        self.__class__.last_order_id += 1
        order.order_id = self.__class__.last_order_id
        self.orders[self.__class__.last_order_id] = order

    def update_order(self, order):
        """
       create method to update an existing order
       """
        order.order_id = self.__class__.last_order_id
        self.orders[self.__class__.last_order_id] = order

    def get_order(self, order_id):
        """
       create method to handle getting orders
       """
        return self.orders[order_id]

    def delete_order(self, order_id):
        """
       create method to delete order of a given order_id
       """
        del self.orders[order_id]

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
    def get(self, order_id):
        """
        method to retrieve orders
        """
        self.abort_if_order_doesnt_exist(order_id)
        return ORDER_MANAGER.get_order(order_id)

    def delete(self, order_id):
        """
        create the delete method to pick order
        """
        self.abort_if_order_doesnt_exist(order_id)
        ORDER_MANAGER.delete_order(order_id)
        return '', status.HTTP_204_NO_CONTENT

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

    @marshal_with(ORDER_FIELDS)
    def post(self):
        """
        Add the post method to add new items
        """
        parser = reqparse.RequestParser()
        parser.add_argument('title', type=str, required=True,
                            help='title cannot be blank!')
        parser.add_argument('pieces', type=int, required=True,
                            help='Pieces cannot be blank!')
        parser.add_argument('quantity', type=str, required=True,
                            help='quantity can not be blank!')

        args = parser.parse_args()
        order = OrderModel(
            title=args['title'],
            pieces=args['pieces'],
            quantity=args['quantity']
        )
        ORDER_MANAGER.insert_order(order)
        return order, status.HTTP_201_CREATED


API.add_resource(OrderList, '/API/v1/orders/')
API.add_resource(Order, '/API/v1/orders/<int:order_id>',
                 endpoint='Order_endpoint')

if __name__ == '__main__':
    APP.run(debug=True)
