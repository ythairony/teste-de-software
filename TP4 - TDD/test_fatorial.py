import unittest
from fatorial import factorial

class TestFatorial(unittest.TestCase):
    def test_factorial_positivo(self):
        n = factorial(self)
        self.assertEqual(6, n)
        pass

    def test_factorial_zero(self):
        n = factorial(self)
        self.assertEqual(1, n)

    def test_factorial_negativo(self):
        with self.assertRaises(ValueError):
            n = 0
            t = factorial(n)


if __name__ == '__main__':
    unittest.main()