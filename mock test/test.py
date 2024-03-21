# tests.py

import datetime
import unittest
from unittest.mock import Mock

import modelo


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
    self.servico.daoCompra.getUltimaData.return_value = datetime.datetime(2022, 10 ,21)
    self.servico.daoVenda.getUltimaData.return_value = datetime.datetime(2021, 10, 22)
    em_posse = self.servico.isEmPosseDaLoja(placa)
    self.assertTrue(em_posse)

  
  # Aula de testes de MOCK prática
  def test_CompraFeitaComDataCompraNula(self):
    # compra realizado com carro sem registro de compra e venda
    placa = "ADS2O24"
    data_compra = datetime.datetime(2024, 3, 21)
    self.servico.daoCompra.getUltimaData.return_value = None

    foi_comprado = self.servico.compra(placa, data_compra)

    self.assertTrue(foi_comprado)


  def test_CompraNaoFeitaComDataCompra(self):
    # compra realizado com carro com registro de compra e sem registro de venda
    placa = "ADS2O24"
    data_compra = datetime.datetime(2024, 3, 21)
    self.servico.daoCompra.getUltimaData.return_value = datetime.datetime(2022, 10 ,21)
    self.servico.daoVenda.getUltimaData.return_value = None

    foi_comprado = self.servico.compra(placa, data_compra)

    self.assertFalse(foi_comprado)


  def test_CompraFeitaComDataCompraMenor(self):
    # compra realizado com carro com registro de compra menor que a venda
    placa = "ADS2O24"
    data_compra = datetime.date(2024, 3, 21)

    self.servico.daoCompra.getUltimaData.return_value = datetime.datetime(2022, 10 ,21)
    self.servico.daoVenda.getUltimaData.return_value = datetime.datetime(2022, 10, 31)

    foi_comprado = self.servico.compra(placa, data_compra)

    self.assertTrue(foi_comprado)


  def test_CompraNaoFeitaComDataCompraMaior(self):
    # compra realizado com carro com registro de compra e venda
    placa = "ADS2O24"
    data_compra = datetime.date(2024, 3, 21)

    self.servico.daoCompra.getUltimaData.return_value = datetime.datetime(2022, 10 ,31)
    self.servico.daoVenda.getUltimaData.return_value = datetime.datetime(2022, 10, 21)

    foi_comprado = self.servico.compra(placa, data_compra)

    self.assertFalse(foi_comprado)

if __name__ == '__main__':
  unittest.main()
