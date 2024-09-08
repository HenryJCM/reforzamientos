"""
Crear una clase Persona que contenga dos atributos: nombre y edad.
Nombre y edad se ingresarán por teclado en el constructor.
Declarar una segunda clase llamada Empleado que herede de la clase
Persona y agregue un atributo sueldo y muestre si debe pagar impuestos
(10% de su sueldo) (si sueldo es superior a 4000 soles)
Instanciar la clase Empleado, mostrar el sueldo del empleado y cuánto
debe pagar de impuesto.
"""

class Persona:
    nombre: str
    edad: int

    def __init__(self):
        self.nombre = input('Ingrese el nombre de la persona: ')
        self.edad = int(input('Ingrese la edad de la persona: '))

class Empleado(Persona):
    sueldo: float

    def __init__(self):
        super().__init__()
        self.sueldo = int(input('Ingrese el sueldo del empleado: '))

    def cantidad_impuestos(self):
        return self.sueldo * (10 / 100)

    def impuesto(self):
        if self.sueldo > 4000:
            print("El empleado {} tiene un sueldo de {} debe pagar impuestos de: {}".format(self.nombre, self.sueldo, self.cantidad_impuestos()))
            return
        print("El empleado {} no debe pagar impuestos y tiene un sueldo de {}".format(self.nombre, self.sueldo))

empleado1 = Empleado()
empleado2 = Empleado()

empleado1.impuesto()
empleado2.impuesto()

