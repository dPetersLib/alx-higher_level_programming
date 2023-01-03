import unittest
from models.rectangle import Rectangle


class TestRectangleMethods(unittest.TestCase):
    def test_width_is_int(self):
        with self.assertRaises(TypeError):
            rec = Rectangle('5', 50)

    def test_correct_width(self):
        with self.assertRaises(ValueError):
            rec = Rectangle(-20, 40)
