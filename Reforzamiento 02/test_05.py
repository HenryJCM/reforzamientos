"""
Crear una clase llamada Alumno que tenga como atributos el nombre,
edad y la nota final del alumno. Crear los métodos para inicializar sus
atributos, otro para imprimirlos y un método para mostrar un mensaje
con el resultado de la nota y si ha aprobado (mayor o igual a 11) o no el
alumno.Instanciar la clase por lo menos 3 veces (3 alumnos)
"""

class Alumno():
    nombre: str
    edad: int
    nota_final: float

    def __init__(self, nombre, edad, nota_final = 0):
        self.nombre = nombre
        self.edad = edad
        self.nota_final = nota_final

    def resultado(self):
        if self.nota_final >= 11:
            return "APROBADO"
        return "DESAPROBADO"

    def mostrarDatos(self):
        print("El alumno: {} de {} años, tiene una nota de {}. El alumno esta {}".format(self.nombre, self.edad, self.nota_final, self.resultado()))

alumno1 = Alumno("Juan", 20, 10)
alumno2 = Alumno("Luis", 21, 11)
alumno3 = Alumno("Maria", 21, 19)

alumno1.mostrarDatos()
alumno2.mostrarDatos()
alumno3.mostrarDatos()
