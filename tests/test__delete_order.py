"""
Module to test for the deletion of orders
"""
import json
import unittest
from app import app


class TestDeleteOrder(unittest.TestCase):
    """
    create a class to handle tests for the delete methods
    """

    def test_delete_existing_order(self):
        """
        Deleting already existing orders
        """
        order = json.dumps(dict(
            order_title="order_number", order_description="order_description",
            order_price="order_price", size="size"))

        test_client = app.test_client()
        test_client.post('/api/v1/orders', data=order,
                         content_type='application/json')
        response = test_client.delete('/api/v1/orders/0')
        self.assertEqual(json.loads(response.data)["message"], "order not found")

    def test_non_existing_order(self):
        """
        Test non existing order
        """
        test_client = app.test_client()
        response = test_client.delete('/api/v1/orders/3')
        self.assertEqual(json.loads(response.data)[
            "message"], "order not found")
