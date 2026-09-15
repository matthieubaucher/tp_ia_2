import unittest

from fibonacci import Fibonacci


class TestFibonacci(unittest.TestCase):
    def setUp(self):
        self.fibonacci = Fibonacci()

    def test_fibbo_zero(self):
        self.assertEqual(self.fibonacci.fibbo(0), 0)

    def test_fibbo_one(self):
        self.assertEqual(self.fibonacci.fibbo(1), 1)

    def test_fibbo_known_value(self):
        self.assertEqual(self.fibonacci.fibbo(10), 55)

    def test_fibbo_negative_value(self):
        with self.assertRaises(ValueError):
            self.fibonacci.fibbo(-1)


if __name__ == "__main__":
    unittest.main()
