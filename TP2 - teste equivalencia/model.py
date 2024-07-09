# modelo.py
class Triangulo:
    
    def __init__(self, a, b, c):
        if a > 0 and b > 0 and c > 0:
            self.a = a
            self.b = b
            self.c = c
        else:
            raise TypeError('Não é um triângulo válido')

    # Para formar um triângulo o valor de cada lado deve ser menor que a soma dos outros 2 lados.
    # ‘a’, ‘b’, e ‘c’ devem formam um triângulo, a função retorna true
    # se as medidas não formam um triângulo, a função retorna false
    # Utilize programação orientada a objetos.
    def validarForma(self):
        if (self.a < (self.b + self.c)):
            if (self.b < (self.a + self.c)):
                if (self.c < (self.a + self.b)):
                    return True

        return False   
    
    # Triângulo Equilátero: três lados iguais;
    def ehEquilatero(self):
        if self.validarForma():
            if (self.a == self.b and self.a == self.c):
                return True

        return False
    
    # Triângulo Isósceles: quaisquer dois lados iguais;
    def ehIsosceles(self):
        if self.validarForma():
            if ((self.a == self.b and self.a != self.c) or (self.a == self.c and self.a != self.b) or (self.b == self.c and self.a != self.b)):
                return True

        return False   

    # Triângulo Escaleno: três lados diferentes;
    def ehEscaleno(self):
        if self.validarForma():
            if (self.a != self.b and self.a != self.c and self.b != self.c):
                return True

        return False 