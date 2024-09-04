cursos = ["Algoritmica", "Base de datos", "Computacion fisica", "Arquitectura empresarial", "Gestion del conocimiento", "Cálculo"]

cursos.append("Matematica discreta")
cursos.append("Sistemas inteligentes")
cursos.append("Redes")
cursos.append("Inteligencia artificial")
cursos.append("Inteligencia artificial")

cursos.remove("Algoritmica")
cursos.remove("Arquitectura empresarial")

contadores1 = dict((i, cursos.count(i)) for i in cursos)
print(contadores1)

cursos.reverse()
cursos.pop()
cursos.reverse()

contadores2 = dict((i, cursos.count(i)) for i in cursos)
print(contadores2)