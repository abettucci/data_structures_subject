### Ejercicio 6

''' Utilice funciones built-in del caso, para que a partir de dos listas de enteros 
se cree una lista que contenga la suma de los elementos de las listas de la siguiente 
manera: Lista1Elemento1+ Lista2Elemento1,Lista1Elemento2+Lista2Elemento2, etc. 
De no ser iguales los tamaños de ambas listas, manejarlo apropiadamente.

lista1=[1,2,3,4]
lista2=[2,3,4,5]
listaSuma=[3,5,7,9]
'''

lista1=[1,2,3,4]
lista2=[2,3,4,5]
listaSuma=[]

for i in range(len(lista1)):
    listaSuma.append(lista1[i] + lista2[i])
print(listaSuma)





