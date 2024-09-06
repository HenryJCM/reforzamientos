from bisect import insort

numeros = [None] * 10

for i in range(10):
    numeros[i] = float(input(f"Ingresa un número para la posición {i + 1}: "))

print(numeros)

suma_numeros = sum(numeros)

media_numeros = suma_numeros / len(numeros)

print(f"La suma de los números es: {suma_numeros}")
print(f"La media de los números es: {media_numeros}")

