import unittest
from app import Order, CustomerOrders, app
import json


class TestGetOrders(unittest.TestCase):

    def test_get_all_endpoint(self):
        test_client = app.test_client()
        test_client.post('/api/v1/orders', data=json.dumps(dict(
            order_number="order_number", order_description="order_description",
            order_price="order_price", size="size")), content_type='application/json')
        response = test_client.get('/api/v1/orders')
        self.assertEqual(len(json.loads(response.data)), 1)
