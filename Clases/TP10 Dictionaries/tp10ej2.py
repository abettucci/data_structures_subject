'''
Realizar una función que dada una lista de palabras y un diccionario que contiene cuantos puntos 
vale cada letra, devolver la palabra cuyo puntaje sea máximo. El puntaje total, se calcula sumando 
los puntajes de cada una de las letras que la componen (de manera similar a la del juego Scrabble'’).
Las letras que no están en el diccionario otorgan 1 punto cada una. Las letras que sí están en el 
diccionario otorgan el valor indicado en el diccionario
'''

puntajes = {'a': 2, 'n': 3, 'f': 5, 'z': 5}
listaPalabras = ['cono','mazazo','fanzine','fhan','marsupial']
puntosPalabras = {}

def contarPuntos(listaPalabras):
    for palabras in listaPalabras:
        suma = 0
        for letra in palabras:
            if letra not in puntajes.keys():
                suma += 1
            else:
                suma += puntajes[letra]
        puntosPalabras[palabras] = suma
    for k,v in puntosPalabras.items():
        print(k,v)
    return puntosPalabras

maximo = max(contarPuntos(listaPalabras).values())
k = list(puntosPalabras.keys())
v = list(puntosPalabras.values())

print('La palabra {} tiene el maximo puntaje de {}'.format(k[v.index(max(v))],maximo))


