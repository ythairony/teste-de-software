import math

class Fracao:
    def __init__(self, numerador, denominador):
        if denominador == 0:
            raise ValueError('Denominador deve ser diferente de zero')

        # Reduzindo numerador e denominador 
        self._numerador = numerador / math.gcd(numerador, denominador)
        self._denominador = denominador / math.gcd(numerador, denominador)

    @property
    def numerador(self):
        return self._numerador

    @property
    def denominador(self):
        return self._denominador