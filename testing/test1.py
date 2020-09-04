import unittest
from testing.qry_testing import qry

class MyTestCase(unittest.TestCase):
    test=qry()

    def test_login(self):
        expected_result = self.test.login("anhex",'anhex')
        self.assertEqual(expected_result,1)


    # def test_add(self):
    #     expected_result = self.a.add_order()
    #     self.assertTrue(expected_result)
    #
    # def test_add1(self):
    #     expected_result = self.a.add_order("abc",123,458,514,"sgji")
    #     self.assertFalse(expected_result)
    #
    # def test_add_customer(self):
    #     expected_result = self.b.add_customer(123,"ilak","mail@123",9856)
    #     self.assertTrue(expected_result)
    #
    # def test_show_products(self):
    #     result = self.product.show_products()
    #     actual_result = len(result)
    #     expected_result = 6
    #     self.assertTrue(expected_result, actual_result)
    #
    # def test_search_customer(self):
    #     expected_result = self.search.search_id(1)
    #     self.assertTrue(expected_result)







