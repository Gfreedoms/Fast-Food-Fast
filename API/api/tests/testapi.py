""" api.py"""
import unittest
import os
import json

class FastFoodFast(unittest.TestCase):

    # def setUp(self):
    #     self.APP = APP.test_client()

    # def test_get_all(self):
    #     response = self.app.get(BASE_URL)
    #     data = json.loads(response.get_data())
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(len(data['items']), 3)

    # def test_get_one(self):
    #     response = self.app.get(BASE_URL)
    #     data = json.loads(response.get_data())
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(data['items'][0]['name'], 'laptop')

    # def test_item_not_exist(self):
    #     response = self.app.get(BAD_ITEM_URL)
    #     self.assertEqual(response.status_code, 404)



"""Make the tests conveniently executable"""
if __name__ == "__main__":
    unittest.main()