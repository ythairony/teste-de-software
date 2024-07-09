import math


class Fracao:
    def __init__(self, numerador, denominador):
        if denominador == 0:
            raise ValueError('Denominador deve ser diferente de zero')

        # Reduzindo numerador e denominador 
        self._numerador = numerador // math.gcd(numerador, denominador)
        self._denominador = denominador // math.gcd(numerador, denominador)



    def somar(self, f):
        if self.denominador == f.denominador:
            return Fracao(self.numerador + f.numerador, self.denominador)
        else: 
            novo_numerador = self.numerador * f.denominador + f.numerador * self.denominador
            novo_denominador = self.denominador * f.denominador
            return Fracao(novo_numerador, novo_denominador)
        

    def subtrair(self, f):
        if self.denominador == f.denominador:
            return Fracao(self.numerador - f.numerador, self.denominador)
        else: 
            novo_numerador = self.numerador * f.denominador - f.numerador * self.denominador
            novo_denominador = self.denominador * f.denominador
            return Fracao(novo_numerador, novo_denominador)


    def multiplicar(self, f):
        novo_num = self.numerador * f.numerador
        novo_dem = self.denominador * f.denominador
        return Fracao(novo_num, novo_dem)
    

    def dividir(self, f):
        novo_num = self.numerador * f.denominador
        novo_dem = self.denominador * f.numerador
        return Fracao(novo_num, novo_dem)



    @property
    def numerador(self):
        return self._numerador

    @property
    def denominador(self):
        return self._denominador