cursos = ["Algoritmica", "Base de datos", "Computacion fisica", "Arquitectura empresarial", "Gestion del conocimiento", "Cálculo"]

cursos.append("Matematica discreta")
cursos.append("Sistemas inteligentes")
cursos.append("Redes")
cursos.append("Inteligencia artificial")

cursos.remove("Algoritmica")
cursos.remove("Arquitectura empresarial")

print("Mis cursos: ")
print(*cursos, sep = "\n")