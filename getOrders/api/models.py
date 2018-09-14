class OrderModel:
    def __init__(self, title, quantity, pieces):
        self.order_id = 0
        self.title = title
        self.quantity = quantity
        self.pieces = pieces
        self.compltete = False
        