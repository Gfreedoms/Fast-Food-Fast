"""
Module to test the retrieving order module
"""
import json
import unittest
from app import app



class TestGetOrders(unittest.TestCase):
    """
    Class to handle the tests for retrieval of both existing and non exiting orders
    """
    def test_get_all_ordes(self):
        """
        test the endpoint for retrieving all the orders
        """
        test_client = app.test_client()
        test_client.post('/api/v1/orders', data=json.dumps(dict(
            order_number="order_number", order_description="order_description",
            order_price="order_price", size="size")), content_type='application/json')
        response = test_client.get('/api/v1/orders')
        self.assertEqual(len(json.loads(response.data)), 1)
