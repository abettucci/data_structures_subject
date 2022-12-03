'''
Diseña una función que, mueva todos los ceros (0) que aparezcan en un vector al final de este.
Ejemplo 1
vector= (‘i’,[3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1])
visualizara:
vector final= [3, 4, 6, 2, 6, 7, 6, 9, 10, 7, 4, 4, 5, 3, 2, 9, 7, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
'''
import numpy as np
import array as arr

vector = arr.array('i',[3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1])

# print(len(vector))

# def moverCeros(vector):
#     i=0
#     for i in range(len(vector)):
#         if vector[i] == 0:
#             vectorFinal = vector.extend(vector[i])
#             vectorFinal = vector.pop(i)
#     return vectorFinal    

# print(moverCeros(vector))

#otra forma de hacerlo es ir creando una lista nueva 


def moveZeros(vector):
    i=0
    j=0
    listaNueva = []
    listaNueva2 = []
    for i in range(len(vector)):
        if vector[i]!=0:
            listaNueva.append(vector[i])
    listaNueva2 = listaNueva
    print(listaNueva2)

    for j in range(len(vector)):
        if vector[j] == 0:
            listaNueva2.append(vector[j])
    return listaNueva2

print(moveZeros(vector))