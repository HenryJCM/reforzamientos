"""
Realizar una clase que administre una agenda. Se debe almacenar enun
diccionario dentro de una lista para cada contacto el nombre, el
teléfono, email y DNI. Deberá tener los siguientes métodos:
Añadir contacto
Mostrar contactos
Buscar contacto (Por DNI)
"""

class Agenda:
    contactos = []

    def __init__(self, contactos):
        self.contactos = contactos

    def añadir_contacto(self, contacto):
        self.contactos.append(contacto)

    def mostrar_contactos(self):
        print(self.contactos)

    def buscar_contacto(self, dni):
        for contacto in self.contactos:
            if contacto["dni"] == dni:
                return contacto
        return ""

agenda = Agenda([])

agenda.añadir_contacto({"nombre": "Henry", "telefono": 89383731, "email": "henry@gmail.com", "dni": "123456789"})
agenda.añadir_contacto({"nombre": "Javier", "telefono": 131231, "email": "javier@gmail.com", "dni": "54444"})
agenda.añadir_contacto({"nombre": "Maria", "telefono": 897354, "email": "maria@gmail.com", "dni": "99988882323"})

agenda.mostrar_contactos()

contacto = agenda.buscar_contacto("99988882323")
print("Se encontro el contacto: ", contacto)