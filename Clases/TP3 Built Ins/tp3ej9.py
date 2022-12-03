### Ejercicio 9

''' Utilice funciones built-in del caso, para que dadas dos listas de enteros las una en 
una sola lista de la siguiente manera: Lista1Elemento1, Lista2Elemento1, Lista1Elemento2, 
Lista2Elemento2, etc. De no seriguales los tamaños de ambas listas, manejarlo apropiadamente.

Ejemplo1:
lista1=[1,2,3,4]
lista2=[2,3,4,5]
listaUnion=[1,2,2,3,3,4,4,5]

Ejemplo2:

lista1=[1,2,3]
lista2=[2,3,4,5]
listaUnion=[1,2,2,3,3,4,5]
'''
lista1=[1,2,3,4]
lista2=[2,3,4,5]
print(lista1,'\t',lista2,'\t',lista1+lista2,sorted(lista1+lista2))
