class Compress:
    def __init__(self):
        pass

    def compress(self,text):
        index = 1
        split = text.split(sep=' ')
        split_2 = []
        diccionario2 = {}
        for word in split:
            if word not in split_2:
                split_2.append(word)
        for value in split_2:
            diccionario2[value] = index
            index += 1
        
        lista = []
        for word in split:
            if word in diccionario2:
                lista.append(diccionario2[word])

        return lista,diccionario2
        

    def uncompress(self,lista,diccionario):
        list = lista
        diccionario = diccionario
        texto = ''
        palabras = ['index']
        for k in diccionario:
            palabras.append(k)
        for i in list:
            texto += f'{palabras[i]} '
        texto = texto[:-1]
        return texto
        