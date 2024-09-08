"""
Crear una clase en python que contenga un método que revierta una
cadena de palabras.
Input: "Hola Pythonista, seguimos adelante"
Output: "adelante seguimos Pythonista Hola"
"""

class Reversor:
    def reverse(self, cadena):
        return " ".join(cadena.split()[::-1])



obj_1 = Reversor()
cadena1 = input("Ingrese la primera cadena de palabras: ")
print(obj_1.reverse(cadena1))
cadena2 = input("Ingrese la segunda cadena de palabras: ")
print(obj_1.reverse(cadena2))
