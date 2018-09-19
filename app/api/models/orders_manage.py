import datetime


class Order:
    """
    creates order to innitialise attributes
    """

    def __init__(self, order_number, order_description, order_price, size):
        self.order_number = order_number
        self.order_description = order_description
        self.order_price = order_price
        self.size = size
        self.created_at = datetime.datetime.now().timestamp()
        self.complete = False
        self.order_id = ''

    def toJSON(self):
        return {"order_id": self.order_id, "order_number": self.order_number,
                "order_description": self.order_description, "order_price": self.order_price,
                "size": self.size, "created_at": self.created_at,
                "complete": self.complete
                }


class CustomerOrders:
    def __init__(self):
        self.orders_list = []

    def place_order(self, new_order: Order):
        """
        assigns id to new order and adds it to orders list
        """

        if len(self.orders_list) >= 0:
            new_order.order_id = len(self.orders_list)
        else:
            new_order.order_id = 0
        self.orders_list.append(new_order)

   