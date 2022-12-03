'''
Realizar una función que determine si dos vectores son iguales. Dos vectores son iguales si y solo si: los elementos 
de uno de los vectores son igual al cuadrado de los elementos del otro vector, sin importar el orden de los elementos.
Basicamente tiene que aparecer el valor elevado al cuadrado de cada uno de los elementos de una lista en la otra lista,
sin importar el orden.

Ejemplo 1
vectores =(‘i’, [121, 144, 19, 161, 19, 144, 19, 11])
vector = (‘i’,[121, 14641, 20736, 361, 25921, 361, 20736, 361])
visualizara: Los dos vectores son iguales

'''
import array as arr
import numpy as np

vectores = arr.array('i', [121, 144, 19, 161, 19, 144, 19, 11])
vector = arr.array('i',[121, 14641, 20736, 361, 25921, 361, 20736, 361])

def vectoresIguales(vectores,vector):
    i=0
    iguales = True
    while iguales == True:
        for i in range(len(vector)):
            if vectores[i]**2 not in vector:
                iguales = False
                return 'Los dos vectores no son iguales'
        return 'Los dos vectores son iguales'

print(vectoresIguales(vectores,vector))




