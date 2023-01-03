import unittest
from models.base import Base


class TestBaseMethods(unittest.TestCase):
    def test_default_id(self):
        base = Base()
        self.assertEqual(base.id, 1)

    def test_users_id(self):
        base = Base(24)
        self.assertEqual(base.id, 24)
