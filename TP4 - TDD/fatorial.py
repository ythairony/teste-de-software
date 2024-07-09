import math

def factorial(n):
    if n == 0:
        return 1

    elif n > 0:
        return math.factorial(n)

    else:
        raise ValueError('Não existe fatorial de número negativo.')
    

