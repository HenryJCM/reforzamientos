numeros_impares = [i for i in range(1, 30) if i % 2 != 0]

numeros_impares.extend([1.0, 3.0, 5.0])

numeros_impares.insert(3, "cadena_en_posicion_3")

print("Lista con el string agregado:", numeros_impares)

del numeros_impares[3]

print("Lista después de eliminar el string:", numeros_impares)