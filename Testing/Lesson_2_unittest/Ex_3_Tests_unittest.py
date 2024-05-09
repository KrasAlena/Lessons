from Ex_3_unittest import Product, POSSystem
import unittest
'''
Write at least 3 tests for each of the methods for POSSystem
(Optional) think about the methods above. What made them difficult to test? 
What recommendations would you give to the developers who implemented 
add_to_cart and remove_from_cart methods? How would you change these methods 
so that they would be easier to test and use by other Python programmers?
'''
class TestProduct(unittest.TestCase):
    def test_product_creation(self):
        product = Product(1, 'Product 1', 150.5)
        self.assertEqual(product.product_id, 1)
        self.assertEqual(product.name, 'Product 1')
        self.assertEqual(product.price, 150.5)

    def setUp(self):
        self.product = Product(2, 'Product 2', 10.99)

    def test_product_id_type(self):
        self.assertIsInstance(self.product.product_id, int)

    def test_product_name_type(self):
        self.assertIsInstance(self.product.name, str)

    def test_product_price_type(self):
        self.assertIsInstance(self.product.price, float)

    def test_product_attributes(self):
        product = Product(3, 'Product 3', 5.0)
        self.assertTrue(hasattr(product, 'product_id'))
        self.assertTrue(hasattr(product, 'name'))
        self.assertTrue(hasattr(product, 'price'))

    def test_product_str_representation(self):
        product = Product(4, 'Product 4', 15.75)
        expected_output = "Product(product_id=4, name='Product 4', price=15.75)"
        self.assertEqual(str(product), expected_output)


class TestPOSSystem(unittest.TestCase):
    def setUp(self):
        self.pos_system = POSSystem()
        self.pos_system.add_product(1, 'Test product 1', 100.5)
        self.pos_system.add_product(2, 'Test product 2', 200.15)
        self.pos_system.add_product(3, 'Test product 3', 187.90)

    def test_get_all_products_3_products(self):
        expected_product_ids = [1, 2, 3]
        actual_products = self.pos_system.get_all_products()

        self.assertEqual(len(expected_product_ids), len(actual_products))

        for product_id in expected_product_ids:
            self.assertTrue(product_id in actual_products)

            self.assertIsInstance(actual_products[product_id], Product)

    def test_get_all_products_no_products(self):
        self.pos_system.products = {}
        actual_products = self.pos_system.get_all_products()

        self.assertEqual(len(actual_products), 0)

    def test_add_product(self):
        result = self.pos_system.add_product(4, 'Product 4', 100.0)
        self.assertIn(4, self.pos_system.products)


        self.assertEqual(result.product_id, 4)
        self.assertEqual(result.name, 'Product 4')
        self.assertEqual(result.price, 100.0)

    def test_add_product_with_sameID(self):
        result = self.pos_system.add_product(4, 'Product 4', 100.0)
        result2 = self.pos_system.add_product(4, 'Product 4', 100.0)
        self.assertIsNone(result2)




if __name__ == '__main__':
    unittest.main()