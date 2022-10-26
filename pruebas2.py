lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 17, 24, 25, 26, 14]
diccionario = {'TDD': 1, 'o': 2, 'Test-Driven': 3, 'Development': 4, '(desarrollo': 5, 'dirigido': 6, 'por': 7, 'tests)': 8, 'es': 9, 'una': 10, 'práctica': 11, 'de': 12, 'programación': 13, 'que': 14, 'consiste': 15, 'en': 16, 'escribir': 17, 'primero': 18, 'las': 19, 'pruebas': 20, '(generalmente': 21, 'unitarias),': 22, 'después': 23, 'el': 24, 'código': 25, 'fuente': 26, "tuki": 27}

texto = ''

palabras = ['index']

for k in diccionario:
    palabras.append(k)

print(palabras[1])



for i in lista:
    texto += f'{palabras[i]} '
    

print(texto)