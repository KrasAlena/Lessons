from Ex_5_unittest import Rectangle
import unittest


class TestRectangleMethods(unittest.TestCase):
    def test_set_width_positive_number(self):
        rectangle = Rectangle(4, 2)
        rectangle.set_width(5)
        self.assertEqual(rectangle.width, 5)

    def test_set_width_negative_number(self):
        rectangle = Rectangle(4, 2)
        rectangle.set_width(-4)
        self.assertEqual(rectangle.width, -4)

    def test_set_width_zero(self):
        rectangle = Rectangle(4, 2)
        rectangle.set_width(0)
        self.assertEqual(rectangle.width, 0)

    def test_set_width_float(self):
        rectangle = Rectangle(4, 2)
        rectangle.set_width(4.5)
        self.assertEqual(rectangle.width, 4.5)

    def test_set_width_string(self):
        rectangle = Rectangle(4, 2)
        with self.assertRaises(TypeError):
            rectangle.set_width('test')

    def test_set_width_no_value(self):
        rectangle = Rectangle(4, 2)
        with self.assertRaises(TypeError):
            rectangle.set_width()

    def test_set_height_positive_number(self):
        rectangle = Rectangle(4, 2)
        rectangle.set_height(5)
        self.assertEqual(rectangle.height, 5)

    def test_set_height_negative_number(self):
        rectangle = Rectangle(4, 2)
        rectangle.set_height(-2)
        self.assertEqual(rectangle.height, -2)

    def test_set_height_zero(self):
        rectangle = Rectangle(4, 2)
        rectangle.set_height(0)
        self.assertEqual(rectangle.height, 0)

    def test_set_height_float(self):
        rectangle = Rectangle(4, 2)
        rectangle.set_height(2.5)
        self.assertEqual(rectangle.height, 2.5)

    def test_set_height_string(self):
        rectangle = Rectangle(4, 2)
        with self.assertRaises(TypeError):
            rectangle.set_height('test')

    def test_set_height_no_value(self):
        rectangle = Rectangle(4, 2)
        with self.assertRaises(TypeError):
            rectangle.set_height()

    def test_set_height_same_value(self):
        rectangle = Rectangle(4, 2)
        rectangle.set_height(2)
        self.assertEqual(rectangle.height, 2)

    def test_get_area_numbers(self):
        rectangle = Rectangle(4, 2.5)
        self.assertEqual(rectangle.get_area(), 10.0)

    def test_get_area_strings(self):
        rectangle = Rectangle('test', 'test')
        with self.assertRaises(TypeError):
            rectangle.get_area()

    def test_get_area_string_and_number(self):
        rectangle = Rectangle('test', 2)
        with self.assertRaises(TypeError):
            rectangle.get_area()

    def test_get_area_no_values(self):
        rectangle = Rectangle()
        with self.assertRaises(TypeError):
            rectangle.get_area()


if __name__ == '__main__':
    unittest.main()