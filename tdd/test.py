import unittest

from fracao import Fracao

class FracaoTest(unittest.TestCase):
    def test_construtor_1(self):
        f = Fracao(2,3)
        self.assertEqual(2, f.numerador)
        self.assertEqual(3, f.denominador)


    def test_construtor_2(self):
        with self.assertRaises(ValueError):
            f = Fracao(2, 0)


    def test_construtor_3(self):
        f = Fracao(2, 4)
        self.assertEqual(1, f.numerador)
        self.assertEqual(2, f.denominador)

        

if __name__ == '__main__':
    unittest.main()