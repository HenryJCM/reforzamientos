"""
Escribir una clase en Python que contenga un método que convierta un
número entero en su cubo y contenga otro método que obtenga el
cuadrado de ese resultado. El valor inicial de resultado deberá estar
creado en el constructor. Considerar un método en la cual le pedirá al
usuario ingresar un valor numérico.
"""

class Potencia:
    numero = 0

    def __init__(self, numero = 0):
        self.numero = numero

    def cubo(self):
        return self.numero ** 3

    def cuadrado(self):
        return self.numero ** 2

    def ingresarNumero(self):
        self.numero = int(input("Ingrese un numero: "))


var_1 = Potencia(2)
var_2 = Potencia(3)

var_1.ingresarNumero()

print(var_1.cuadrado(), var_2.cuadrado())