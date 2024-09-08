"""
Crear una clase llamada círculo que contenga radio en su constructory que
contenga un método área que devuelva el área de un círculo. Aplicar
excepciones en caso no se ingrese un dato tipo numérico.
Crear adicionalmente un método que devuelva el perímetro del círculo.Instanciar
la clase respectivamente para dos diferentes radios.
Habrá un método donde pedirá el radio del círculo.
Instanciar mínimo 2 veces la clase y mostrar resultados por consola.
"""
import math

class Circulo:
    radio: float

    def __init__(self, radio = 1):
        if not isinstance(radio, (int, float)):
            raise ValueError("El radio debe ser un número.")
        if radio <= 0:
            raise ValueError("El radio debe ser un número positivo.")
        self.radio = radio

    def area(self):
        return math.pi * (self.radio ** 2)

    def perimetro(self):
        return math.pi * self.radio * 2

    def ingresarRadio(self):
       self.radio = float(input("Ingrese el radio:"))


try:
    circulo = Circulo()
    circulo.ingresarRadio()
    print("El área del círculo 1 es: {}".format(circulo.area()))
    print("El perimetro del círculo 1 es: {}".format(circulo.perimetro()))
except ValueError as e:
    print(e)

try:
    circulo = Circulo()
    circulo.ingresarRadio()
    print("El área del círculo 2 es: {}".format(circulo.area()))
    print("El perimetro del círculo 2 es: {}".format(circulo.perimetro()))
except ValueError as e:
    print(e)

try:
    circulo_invalido = Circulo("no-numérico")
except ValueError as e:
    print("Error: {}".format(e))