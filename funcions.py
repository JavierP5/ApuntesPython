import math

def NumeroNegativo (Exception):
    def __str__(self):
        return "Existe un número negativo"


def promedio (lista):
    suma = 0.0
    elementos = 0
    for numero in lista:
        if numero <0:
            raise NumeroNegativo()
        else:

            suma = suma + numero
            elementos = elementos + 1
    return suma/elementos

try:
    print (promedio([2,2,2,-2,2,2,2,2]))
except
    

