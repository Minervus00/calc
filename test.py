import unittest
from app import add


class TestAddition(unittest.TestCase):
    def test_deux_zero(self):
        self.assertEqual(add(1, 2), 3, "1 + 2 = 3")

    def test_decimaux(self):
        self.assertEqual(add(6.1, 4.7), 10.8)

    def test_negatifs(self):
        self.assertAlmostEqual(add(5, 0.1), 5.1)

    def test_entiers(self):
        self.assertEqual(add(5, 7), 12)


if __name__ == "__main__":
    unittest.main()
