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

    def place_one_order_test(self):
        """
        Test placement of a single order
        """
        self.orders_list.place_order(self.order)
        self.assertEqual(len(self.orders_list.orders_list), 1)
        self.assertEqual(self.orders_list.orders_list[0].order_id, 0)

    def place_multiple_order_test(self):
        """
        test placement of multiple orders
        """
        self.orders_list.place_order(self.order)
        self.orders_list.place_order(self.order)
        self.orders_list.place_order(self.order)
        self.assertEqual(len(self.orders_list.orders_list), 3)
        self.assertEqual(self.orders_list.orders_list[2].order_id, 2)

    def get_orders_test(self):
        """
        test retrieving orders
        """
        self.orders_list.place_order(self.order)
        self.orders_list.place_order(self.order)
        self.orders_list.place_order(self.order)
        self.assertEqual(len(self.orders_list.get_orders()), 3)

    def get_one_order_test(self):
        """
        test get one order
        """
        self.orders_list.place_order(self.order)
        self.orders_list.place_order(self.order)
        self.assertEqual(self.orders_list.get_order(1), self.order)

    def get_non_existing_order_test(self):
        """
        test non existing order
        """
        self.orders_list.place_order(self.order)
        self.orders_list.place_order(self.order)
        self.assertEqual(self.orders_list.get_order(2),
                         "order does not exist")

    def delete_order_test(self):
        """
        Delete Order method test
        """
        self.orders_list.place_order(self.order)
        self.orders_list.place_order(self.order)
        self.assertEqual(self.orders_list.deletes_order(1), "deleted")
        self.assertEqual(len(self.orders_list.get_orders()), 1)

    def delete_non_existing_order_test(self):
        """
        test deletion of non existent order
        """
        self.orders_list.place_order(self.order)
        self.orders_list.place_order(self.order)
        self.assertEqual(self.orders_list.deletes_order(2),
                         "order not found. check the exixting orders first")
        self.assertEqual(len(self.orders_list.get_orders()), 2)

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
