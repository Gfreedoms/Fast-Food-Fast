"""
Module to test the methods that handle orders
"""
import unittest
from app import app, Order, CustomerOrders


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

    def test_order_inst(self):
        """
        test order instance
        """
        self.assertIsInstance(self.order, Order)

    def test_list_inst(self):
        """
        testlist instance
        """
        self.assertIsInstance(self.orders_list, CustomerOrders)

    def test_place_one_order(self):
        """
        Test placement of a single order
        """
        self.orders_list.place_order(self.order)
        self.assertEqual(len(self.orders_list.orders_list), 1)
        self.assertEqual(self.orders_list.orders_list[0].order_id, 0)

    def test_place_multiple_orders(self):
        """
        test placement of multiple orders
        """
        self.orders_list.place_order(self.order)
        self.orders_list.place_order(self.order)
        self.orders_list.place_order(self.order)
        self.assertEqual(len(self.orders_list.orders_list), 3)
        self.assertEqual(self.orders_list.orders_list[2].order_id, 2)

    def test_get_orders(self):
        """
        test retrieving orders
        """
        self.orders_list.place_order(self.order)
        self.orders_list.place_order(self.order)
        self.orders_list.place_order(self.order)
        self.assertEqual(len(self.orders_list.get_orders()), 3)

    def test_get_one_order(self):
        """
        test get one order
        """
        self.orders_list.place_order(self.order)
        self.orders_list.place_order(self.order)
        self.assertEqual(self.orders_list.get_order(1), self.order)

    def test_get_non_existing_order(self):
        """
        test non existing order
        """
        self.orders_list.place_order(self.order)
        self.orders_list.place_order(self.order)
        self.assertEqual(self.orders_list.get_order(2),
                         "order does not exist")

    def test_delete_order(self):
        """
        Delete Order method test
        """
        self.orders_list.place_order(self.order)
        self.orders_list.place_order(self.order)
        self.assertEqual(self.orders_list.deletes_order(1), "Order successfully trashed")
        self.assertEqual(len(self.orders_list.get_orders()), 1)

    def test_delete_non_existing_order(self):
        """
        test deletion of non existent order
        """
        self.orders_list.place_order(self.order)
        self.orders_list.place_order(self.order)
        self.assertEqual(self.orders_list.deletes_order(2),
                         "order not found")
        self.assertEqual(len(self.orders_list.get_orders()), 2)

    def test_order_update(self):
        """
        Test Order update
        """
        self.orders_list.place_order(self.order)
        self.orders_list.place_order(self.order)
        self.assertEqual(self.orders_list.change_status(
            1, "pending"), "status changed to pending")
        self.assertEqual(self.orders_list.get_order(1).complete, "pending")

    def test_non_existing_order(self):
        """
        Test update of a non existing order
        """
        self.orders_list.place_order(self.order)
        self.orders_list.place_order(self.order)
        self.assertEqual(self.orders_list.change_status(
            2, "pending"), "order not found")
