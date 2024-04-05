import unittest

from lojao_do_desconto import Desconto

class DescontoTest(unittest.TestCase):
    # Idade e valor válido
    def test_IdadeEValorValido(self):
        compra = Desconto(250, 0)
        self.assertTrue(compra._isElegivel())
        
        compra = Desconto(251, 1)
        self.assertTrue(compra._isElegivel())

        compra = Desconto(251, 23)
        self.assertTrue(compra._isElegivel())

        compra = Desconto(251, 24)
        self.assertTrue(compra._isElegivel())


    # Idade e valor inválido
    def test_IdadeEValorInvalido(self):
        compra = Desconto(249, -1)
        self.assertFalse(compra._isElegivel())

        compra = Desconto(249, 25)
        self.assertFalse(compra._isElegivel())


    # Idade válida e valor inválido
    def test_IdadeValidaValorInvalido(self):
        compra = Desconto(249, 0)
        self.assertFalse(compra._isElegivel())

        compra = Desconto(249, 1)
        self.assertFalse(compra._isElegivel())
        
        compra = Desconto(249, 23)
        self.assertFalse(compra._isElegivel())

        compra = Desconto(249, 24)
        self.assertFalse(compra._isElegivel())


    # Idade inválida e valor válido
    def test_IdadeInvalidaValorValido(self):
        compra = Desconto(250, -1)
        self.assertFalse(compra._isElegivel())

        compra = Desconto(251, -1)
        self.assertFalse(compra._isElegivel())

        compra = Desconto(250, 25)
        self.assertFalse(compra._isElegivel())

        compra = Desconto(251, 25)
        self.assertFalse(compra._isElegivel())


    def test_CalcularDescontoIdadeMenorQue12Anos(self):
        compra = Desconto(250, 0)
        self.assertTrue(compra._calcularDesconto())



if __name__ == "__main__":
    unittest.main()