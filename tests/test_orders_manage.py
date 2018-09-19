"""
Module to test the methods that handle orders
"""
import unittest
from app import Order, CustomerOrders


class TestOrders(unittest.TestCase):
    """
    Class to handle testing of all the methods that handle orders
    """
    def setUp(self):
        """
        Test setup
        """
        self.order = Order("order_number", "order_description",
                           "order_price", "size")
        self.orders_list = CustomerOrders()

    def teardown(self):
        """
        Waiting for the db migrations to fullfill this
        """
        pass

    def order_inst_test(self):
        """
        test order instance
        """
        self.assertIsInstance(self.order, Order)

    def list_inst_test(self):
        """
        testlist instance
        """
        self.assertIsInstance(self.orders_list, CustomerOrders)

    
    def get_one_order_test(self):
        """
        test get one order
        """
        self.orders_list.place_order(self.order)
        self.orders_list.place_order(self.order)
        self.assertEqual(self.orders_list.get_order(1), self.order)

