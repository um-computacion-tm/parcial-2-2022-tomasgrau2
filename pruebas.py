
# Con esta práctica se consigue, entre otras cosas, un código más robusto, más seguro, más mantenible y una mayor rapidez en el desarrollo.
# En este post voy a centrarme solamente en cómo TDD afecta al diseño de software, si queréis más información, hay una introducción bastante buena en la Wikipedia y Carlos Blé tiene disponible online un libro muy completo. Además, en esta infografía os contamos en qué consiste TDD, en qué principios se basa (SOLID) y cuáles son sus ventajas y desventajas. Y, si quieres profundizar aún más, te recomendamos que le eches un vistazo a TDD, una metodología para gobernarlos a todos y Molecule: desarrollo TDD en Ansible.  "

# split = text.split(sep=' ')
# # print(split)


# split_2 = []

# for word in split:
#     if word not in split_2:
#         split_2.append(word)

# # print(split_2)

# diccionario2 = {}

# diccionario = dict(enumerate(set(split)))

# index = 1
# for value in split_2:
#     diccionario2[value] = index
#     index += 1
# # print(diccionario2)


# lista = []
# for word in split:
#     if word in diccionario2:
#         lista.append(diccionario2[word])

# print(diccionario2)
# print(lista)



texto = 'a. '

texto = texto[:-1]
print(texto)