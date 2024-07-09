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


    # TESTE ADIÇÃO
    def test_adicao(self):
        f1 = Fracao(3, 5)
        f2 = Fracao(1, 5)
        res = f1.somar(f2)
        self.assertEqual(4, res.numerador)
        self.assertEqual(5, res.denominador)
        

    # TESTE SUBTRAÇÃO
    def test_subtracao(self):
        f1 = Fracao(3, 5)
        f2 = Fracao(1, 5)
        res = f1.subtrair(f2)
        self.assertEqual(2, res.numerador)
        self.assertEqual(5, res.denominador)


    # TESTE MULTIPLICAÇÃO
    def test_multiplicacao(self):
        f1 = Fracao(3, 5)
        f2 = Fracao(1, 5)
        res = f1.multiplicar(f2)
        self.assertEqual(3, res.numerador)
        self.assertEqual(25, res.denominador)
        

    # TESTE DIVISÃO 
    def test_divisao(self):
        f1 = Fracao(3, 5)
        f2 = Fracao(1, 5)
        res = f1.dividir(f2)
        self.assertEqual(3, res.numerador)
        self.assertEqual(1, res.denominador)

if __name__ == '__main__':
    unittest.main()