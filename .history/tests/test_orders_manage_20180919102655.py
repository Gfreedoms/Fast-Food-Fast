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
    def order_update_test(self):
        """
        Test Order update
        """
        self.orders_list.place_order(self.order)
        self.orders_list.place_order(self.order)
        self.assertEqual(self.orders_list.change_status(
            1, "pending"), "status changed to pending")
        self.assertEqual(self.orders_list.get_order(1).order_status, "pending")

    def non_existing_order_test(self):
        """
        Test update of a non existing order
        """
        self.orders_list.place_order(self.order)
        self.orders_list.place_order(self.order)
        self.assertEqual(self.orders_list.change_status(
            2, "pending"), "order not found")
