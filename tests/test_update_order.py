import unittest
from app import Order, CustomerOrders, app
import json


class TestUpdateOrderStatus(unittest.TestCase):

    def test_sending_empty_order_status(self):
        test_client = app.test_client()
        response = test_client.put('/api/v1/orders/0', data=json.dumps(dict(
            order_status="")), content_type='application/json')

        self.assertEqual(json.loads(response.data)[
                         "message"], "status changed to complete")

    def test_updating_non_existing_order(self):
        test_client = app.test_client()
        response = test_client.put('/api/v1/orders/20', data=json.dumps(dict(
            order_status="complete")), content_type='application/json')

        self.assertEqual(json.loads(response.data)[
                         "message"], "status changed to complete")

    def test_updating_existing_order(self):
        test_client = app.test_client()
        response = test_client.put('/api/v1/orders/0', data=json.dumps(dict(
            order_status="complete")), content_type='application/json')

        self.assertEqual(json.loads(response.data)[
                         "message"], "status changed to complete")
