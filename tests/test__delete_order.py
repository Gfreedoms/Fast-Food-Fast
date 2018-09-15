import unittest
from app import Order, CustomerOrders, app
import json


class TestDeleteOrder(unittest.TestCase):

    def test_delete_existing_order(self):
        order = json.dumps(dict(
            order_title="order_number", order_description="order_description",
            order_price="order_price", size="size"))

        test_client = app.test_client()
        test_client.post('/api/v1/orders', data=order,
                         content_type='application/json')
        response = test_client.delete('/api/v1/orders/0')
        self.assertEqual(json.loads(response.data)[
                         "message"], "order not found")

    def test_non_existing_order(self):
        test_client = app.test_client()
        response = test_client.delete('/api/v1/orders/3')
        self.assertEqual(json.loads(response.data)[
            "message"], "order not found")
