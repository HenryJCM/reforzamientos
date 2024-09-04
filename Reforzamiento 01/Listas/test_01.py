"""
Crear una lista de 6 objetos y mostrar en pantalla (ítems de cursos que lleves o hayas
llevado en la universidad) e Invierte y muestra en consola tu lista de cursos.
"""

cursos = ["Algoritmica", "Base de datos", "Computacion fisica", "Arquitectura empresarial", "Gestion del conocimiento", "Cálculo"]

print("Mis cursos: ")
print(*cursos, sep = "\n")

cursos.reverse()

print("\nMis cursos: ")
print(*cursos, sep = "\n")

