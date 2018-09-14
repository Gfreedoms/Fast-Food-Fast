from flask import Flask
from flask_restful import abort, Api, fields, marshal_with, reqparse, Resource, reqparse
from models import OrderModel
import status


APP = Flask(__name__)
API = Api(APP)


class OrderManager():
    last_id = 0

    def __init__(self):
        self.orders = {}

    def insert_order(self, order):
        self.__class__.last_id += 1
        order.id = self.__class__.last_id
        self.orders[self.__class__.last_id] = order

    def update_order(self, order):
        order.id = self.__class__.last_id
        self.orders[self.__class__.last_id] = order    

    def get_order(self, id):
        return self.orders[id]

    def delete_order(self, id):
        del self.orders[id]
    
    # def put_order(self, id):
    #    return self.orders[id]
   
    


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
      

    def delete(self, id):
        self.abort_if_order_doesnt_exist(id)
        Order_manager.delete_order(id)
        return '', status.HTTP_204_NO_CONTENT

 

    @marshal_with(order_fields)
    def put(self, id):
        self.abort_if_order_doesnt_exist(id)
        Order = Order_manager.get_order(id)
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
        Order_manager.update_order(order)
        return Order


class OrderList(Resource):
    @marshal_with(order_fields)
    def get(self):
        return [v for v in Order_manager.orders.values()]

    @marshal_with(order_fields)
    def post(self):
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
        Order_manager.insert_order(order)
        return order, status.HTTP_201_CREATED

      


API.add_resource(OrderList, '/API/v1/orders/')
API.add_resource(Order, '/API/v1/orders/<int:id>',
                 endpoint='Order_endpoint')

if __name__ == '__main__':
    APP.run(debug=True)
