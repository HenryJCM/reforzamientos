"""
Crear una clase que contenga dos métodos, uno que pida ingresar un
nombre y apellido, un método para pedir su edad y otro método que lo
imprima ambos resultados, pero estarán contenidos en un diccionario.
Comprobar ambos métodos instanciado la clase respectivamente.
Considerar en el constructor los valores necesarios.
"""

class Persona:
    datos: dict

    def __init__(self):
        self.datos = {}

    def ingresarNombreyApellido(self):
        self.datos["nombre"] = input("Ingrese su nombre: ")
        self.datos["apellido"] = input("Ingrese su apellido: ")

    def ingresarEdad(self):
        self.datos["edad"] = input("Ingrese su edad: ")

    def mostrarDados(self):
        print("{} {} tiene {} años.".format(self.datos["nombre"], self.datos["apellido"], self.datos["edad"]))

persona = Persona()
persona.ingresarNombreyApellido()
persona.ingresarEdad()
persona.mostrarDados()

