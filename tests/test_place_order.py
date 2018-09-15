import unittest
from app import Order, CustomerOrders, app
import json
import pytest

def test_all_post():
    response = app.test_client().post('/api/v1/orders', data=json.dumps(dict(
        order_title="order_number", order_description="order_description",
        order_price="order_price", size="size")), content_type='application/json')
    assert response.status_code == 406
