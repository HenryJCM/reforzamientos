"""
Crear una clase Persona con los siguientes requerimientos.
La clase tendrá como atributos el nombre, edad y sueldo de una persona.
Implementar los métodos necesarios para inicializar los atributos
(constructor), un método para mostrar los datos e indicar si la persona
es mayor de edad o no y otro método que bonificación que retornará el
20% adicional de su sueldo.
Instanciar por lo menos la clase con 2 diferentes personas.
"""

class Persona:
    nombre: str
    edad: int
    sueldo: float
    def __init__(self, nombre, edad, sueldo):
        self.nombre = nombre
        self.edad = edad
        self.sueldo = sueldo

    def mostrar_datos(self):
        print("El empleado {} tiene {} años. {}".format(self.nombre, self.edad, self.mayor_edad()))

    def bonificacion(self):
        return self.sueldo + self.sueldo * (20 / 100)

    def mostrar_bonificacion(self):
        print("Tiene un sueldo de: {}".format(self.bonificacion()))

    def mayor_edad(self):
        if self.edad >= 18:
            return "Es mayor de edad"
        return "NO es mayor de edad"

empleado1 = Persona("Juan", 30, 50)
empleado2 = Persona("Pablo", 17, 120)

empleado1.mostrar_datos()
empleado1.mostrar_bonificacion()
empleado2.mostrar_datos()
empleado2.mostrar_bonificacion()
