lista = [100, 34, 24, 230, 1, 345]
cursos = ["Algoritmica", "Base de datos", "Computacion fisica", "Arquitectura empresarial", "Gestion del conocimiento", "Cálculo"]

lista.sort()

print(lista)

cursos.sort(key=len)

print(cursos)

lista.sort(reverse=True)

print(lista)

print(sorted(cursos))
print(sorted(cursos, reverse=True))

