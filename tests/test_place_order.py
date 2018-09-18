"""
Test module for placing orders
"""
import unittest
import json
import pytest
from app import app


class PlaceOrder(unittest.TestCase):
    """
    Class to handle the testing of the post order method
    """

    def test_all_post(self):
        """
        Test the post method
        """
        response = app.test_client().post(
            '/api/v1/orders',
            data=json.dumps(
                dict(
                    order_title="order_number",
                    order_description="order_description",
                    order_price="order_price",
                    size="size")),
            content_type='application/json')
        assert response.status_code == 406
