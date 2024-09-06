departamentos = {
    'Lima': 1,
    'Cusco': 2,
    'Arequipa': 3,
    'Piura': 4,
    'La Libertad': 5,
    'Ica': 6
}

print("Original:", departamentos)

del departamentos['Cusco']

departamento_borrado = 'Cusco'
if departamento_borrado not in departamentos:
    print(f"El departamento '{departamento_borrado}' ya no existe en el diccionario.")
else:
    print(f"El departamento '{departamento_borrado}' todavía existe en el diccionario.")

print("Actualizado:", departamentos)