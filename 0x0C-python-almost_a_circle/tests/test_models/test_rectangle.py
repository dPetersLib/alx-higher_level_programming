import unittest
from models.rectangle import Rectangle


class TestRectangleMethods(unittest.TestCase):

    # Exceptions Test

    def test_width_is_int(self):
        with self.assertRaises(TypeError):
            rec = Rectangle('5', 50)

    def test_correct_width(self):
        with self.assertRaises(ValueError):
            rec = Rectangle(-20, 40)

    def test_height_is_int(self):
        with self.assertRaises(TypeError):
            rec = Rectangle(5, '2')

    def test_correct_height(self):
        with self.assertRaises(ValueError):
            rec = Rectangle(20, -5)

    def test_x_is_int(self):
        with self.assertRaises(TypeError):
            rec = Rectangle(5, 50, '4')

    def test_correct_x(self):
        with self.assertRaises(ValueError):
            rec = Rectangle(20, 40, -3)

    def test_y_is_int(self):
        with self.assertRaises(TypeError):
            rec = Rectangle(5, 50, 4, '23')

    def test_correct_y(self):
        with self.assertRaises(ValueError):
            rec = Rectangle(20, 40, 3, -23)

    # Area Tests

    def test_area(self):
        rec = Rectangle(2, 4)
        self.assertEqual(rec.area(), 8)
