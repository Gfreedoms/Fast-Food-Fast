import unittest
from app import Order, CustomerOrders


class TestOrders(unittest.TestCase):
    def setUp(self):
        self.order = Order("order_number", "order_description",
                           "order_price", "size")
        self.orders_list = CustomerOrders()

    def teardown(self):
        pass

    def order_instance_test(self):
        self.assertIsInstance(self.order, Order)

    # def test_invalid_order_instance(self):
    #     with self.assertRaises(TypeError):
    #         Order("order_number", "order_description",
    #               "order_price", "size")

    def list_instance_test(self):
        self.assertIsInstance(self.orders_list, CustomerOrders)

    def place_single_order_test(self):
        self.orders_list.place_order(self.order)
        self.assertEqual(len(self.orders_list.orders_list), 1)
        self.assertEqual(self.orders_list.orders_list[0].order_id, 0)

    def place_many_order_test(self):
        self.orders_list.place_order(self.order)
        self.orders_list.place_order(self.order)
        self.orders_list.place_order(self.order)
        self.assertEqual(len(self.orders_list.orders_list), 3)
        self.assertEqual(self.orders_list.orders_list[2].order_id, 2)

    def getting_orders_test(self):
        self.orders_list.place_order(self.order)
        self.orders_list.place_order(self.order)
        self.orders_list.place_order(self.order)
        self.assertEqual(len(self.orders_list.get_orders()), 3)

    def getting_single_order_test(self):
        self.orders_list.place_order(self.order)
        self.orders_list.place_order(self.order)
        self.assertEqual(self.orders_list.get_order(1), self.order)

    def getting_non_existing_order_test(self):
        self.orders_list.place_order(self.order)
        self.orders_list.place_order(self.order)
        self.assertEqual(self.orders_list.get_order(2),
                         "order does not exist")

    def deleting_order_test(self):
        self.orders_list.place_order(self.order)
        self.orders_list.place_order(self.order)
        self.assertEqual(self.orders_list.deletes_order(1), "deleted")
        self.assertEqual(len(self.orders_list.get_orders()), 1)

    def deleting_non_existing_order_test(self):
        self.orders_list.place_order(self.order)
        self.orders_list.place_order(self.order)
        self.assertEqual(self.orders_list.deletes_order(2),
                         "order not found. check the exixting orders first")
        self.assertEqual(len(self.orders_list.get_orders()), 2)

    def order_update_test(self):
        self.orders_list.place_order(self.order)
        self.orders_list.place_order(self.order)
        self.assertEqual(self.orders_list.change_status(
            1, "pending"), "status changed to pending")
        self.assertEqual(self.orders_list.get_order(1).order_status, "pending")

    def non_existing_order_test(self):
        self.orders_list.place_order(self.order)
        self.orders_list.place_order(self.order)
        self.assertEqual(self.orders_list.change_status(
            2, "pending"), "order not found")
