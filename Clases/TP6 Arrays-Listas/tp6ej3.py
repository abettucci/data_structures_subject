'''
Diseña una función que, dado un vector de números enteros, visualice el vector que la suma de sus elementos 
sea la mayor

Ejemplo 1
Array= np.array([ [1,2,3], [4,5,6], [10,11,12], [7,8,9]])
visualizara:
[10,11,12]
'''

from operator import index
import random
import array as arr
import numpy as np

Array= np.array([ [1,2,3], [4,5,6], [10,11,12], [7,8,9]])

def vectorMaximo(Array):
    listaDeSumas = []
    for i in range(len(Array)):
        listaDeSumas.append(sum(Array[i])) #obtengo la  suma de todos los elementos de cada vector en el array
    #print(listaDeSumas)
    maximaSuma = max(listaDeSumas)
    #print(maximaSuma)#obtengo que suma de valores es el mas grande y luego uso la posicion en la listaDeSumas para entrar con index
    posicionMaximo = listaDeSumas.index(maximaSuma)
    #print(posicionMaximo)
    return Array[posicionMaximo]#en el Array y traerme el vector que genera el maximo

print(vectorMaximo(Array))


