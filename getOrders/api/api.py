from flask import Flask
from flask_restful import abort, Api, fields, marshal_with, reqparse, Resource
import status


APP = Flask(__name__)
API = Api(APP)


class OrderManager():
    last_id = 0

    def __init__(self):
        self.orders = {}

    def get_order(self, id):
        return self.orders[id]


order_fields = {
    'id': fields.Integer,
    'uri': fields.Url('Order_endpoint'),
    'title': fields.String,
    'quantity': fields.String,
    'pieces': fields.Integer,
    'complete': fields.Boolean
}

Order_manager = OrderManager()


class Order(Resource):
    def abort_if_order_doesnt_exist(self, id):
        if id not in Order_manager.orders:
            abort(status.HTTP_404_NOT_FOUND,
                  error="order {0} doesn't exist".format(id))

    @marshal_with(order_fields)
    def get(self, id):
        self.abort_if_order_doesnt_exist(id)
        return Order_manager.get_order(id)


class OrderList(Resource):
    @marshal_with(order_fields)
    def get(self):
        return [v for v in Order_manager.orders.values()]


API.add_resource(OrderList, '/API/v1/orders/')

if __name__ == '__main__':
    APP.run(debug=True)
