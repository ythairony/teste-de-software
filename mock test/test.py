# tests.py

import unittest
from unittest.mock import Mock
import modelo, datetime

class ServicoVeiculoTest(unittest.TestCase):

  def setUp(self):
    self.servico = modelo.ServicoVeiculo()
    self.servico.daoCompra = Mock()
    self.servico.daoVenda = Mock()

  def test_isEmPosseDaLoja_1(self):
    # teste: sem data de compra e venda
    
    #preparação  
    servico = modelo.ServicoVeiculo()
    servico.daoCompra = Mock()
    servico.daoVenda = Mock()
    
    #execução 
    placa = "NNX2015"
    servico.daoCompra.getUltimaData.return_value = None
    servico.daoVenda.getUltimaData.return_value = None
    em_posse = servico.isEmPosseDaLoja(placa)
    
    #avaliação
    self.assertFalse(em_posse)
    
  def test_isEmPosseDaLoja_2(self):
    # teste: com data de compra e sem data de venda
    placa = "NNX2015"
    self.servico.daoCompra.getUltimaData.return_value = datetime.datetime(2022, 10, 21)
    self.servico.daoVenda.getUltimaData.return_value = None
    em_posse = self.servico.isEmPosseDaLoja(placa)
    self.assertTrue(em_posse)
    
  def test_isEmPosseDaLoja_3(self):
    # teste: com data de compra e sem data de venda
    placa = "NNX2015"
    self.servico.daoCompra.getUltimaData.return_value = datetime.datetime(2022, 10, 21)
    self.servico.daoVenda.getUltimaData.return_value = datetime.datetime(2022, 10, 22)
    em_posse = self.servico.isEmPosseDaLoja(placa)
    self.assertFalse(em_posse)
     
  def test_isEmPosseDaLoja_4(self):
    # teste: com data de compra e sem data de venda
    placa = "NNX2015"
    self.servico.daoCompra.getUltimaData.return_value = datetime.datetime(2022, 10, 21)
    self.servico.daoVenda.getUltimaData.return_value = datetime.datetime(2021, 10, 22)
    em_posse = self.servico.isEmPosseDaLoja(placa)
    self.assertTrue(em_posse)    

if __name__ == '__main__':
  unittest.main()
