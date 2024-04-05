class Desconto:
    def __init__(self, valor: float, idade: int):
        self.valor = valor
        self.idade = idade
        self._desconto = 0

    '''
    Contrua uma função (em python) que realize o cálculo do desconto por dependente. A função

    recebe um valor, e a idade do dependente. A idade do dependente deve estar restrita ao inter-
    valo [0..24]. O valor mínimo da compra deve ser 250,00 reais. Para dependentes até 12 anos

    (inclusive) o desconto é de 15%. Entre 13 e 18 (inclusive) o desconto é de 12%. Dos 19 aos 21
    (inclusive) o desconto é de 5% e dos 22 aos 24 de 3%.
    '''
    

    # Verifica se o valor é elegível a desconto
    def _isElegivel(self):
        if self.idade >= 0 and self.idade <= 24 and self.valor >= 250:
            return True
        return False


    # Calcula o desconto válido
    def _calcularDesconto(self):
        if self.idade <= 12:
            self._desconto = 0.15
        
        elif self.idade <= 18:
            self._desconto = 0.12

        elif self.idade <= 21:
            self._desconto = 0.05

        elif self.idade <= 24:
            self._desconto = 0.03

    
    # Valida se o desconto 
    def _validarDesconto(self):
        if self._isElegivel():
            self._calcularDesconto()
            valor_com_desconto = self.valor * (1 - self.desconto)
            return valor_com_desconto