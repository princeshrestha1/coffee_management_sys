import unittest
from testing.qry_testing import qry


class MyTestCase(unittest.TestCase):
    test = qry()

    def test_login(self):
        expected_result = self.test.login("anhex",'anhex')
        self.assertEqual(expected_result,1)

    def test_add_customers(self):
        expected_result = self.test.add_customer(9, "rihan", "rihanmail@123", 985689452)
        self.assertTrue(expected_result)

    def test_delete_order(self):
        actual_result = self.test.delete_order(2)
        expected = 1
        self.assertEqual(expected, actual_result)

    def test_show_products(self):
        result = self.test.show_products()
        actual_result = len(result)
        expected_result = 7
        self.assertTrue(expected_result, actual_result)

    def test_add_customer(self):
        expected_result = self.test.add_customer("kiara", 65,"mail@123", 985656482)
        self.assertFalse(expected_result)


    def test_show_product(self):
        result = self.test.show_products()
        actual_result = len(result)
        expected_result = 7
        self.assertTrue(expected_result, actual_result)










