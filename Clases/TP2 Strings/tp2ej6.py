### Ejercicio 6
''' Realizar una funcion que, dada una cadena de caracteres, cuente la cantidad de
caracteres que se encuentran en la cadena'''

import string
frase = input("Ingrese frase: ")
listaLetras = []
listaRepeticiones = []
# def crearMatriz(filas, columnas):
#     lista=[None]*filas
#     for i in range(filas):
#         lista[i]=[None]*columnas
#     return lista

# lista = crearMatriz(len(frase), len(frase))

for i in range(len(frase)):
    if frase[i] in string.ascii_letters:
        if frase[i] not in listaLetras:
            print(str(frase[i]),'     ',frase.count(str(frase[i])),end='\n')
            listaLetras.append(frase[i])
    else:
        next

