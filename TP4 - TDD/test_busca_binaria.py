import unittest
from buscarbinaria import busca_binaria

class TestBuscaBinaria(unittest.TestCase):
    def test_encontrado(self):
        arraytest = [1, 2, 3, 4, 5]
        self.assertTrue(busca_binaria(arraytest, 2))



    def test_nao_encontrado(self):
        arraytest = [1, 2, 3, 4, 5]
        self.assertFalse(busca_binaria(arraytest, 6))