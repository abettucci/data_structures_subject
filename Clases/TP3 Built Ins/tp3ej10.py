### Ejercicio 10

''' Utilice funciones built-in del caso que, dada una lista de enteros arme dos listas 
distintas, una para los pares y una para los impares. Luego, ambas listas deben unirse en 
una lista final que posea primero losnúmeros pares y luego los impares

Ejemplo1:

lista=[1,2,2,3,3,4,5]
listaPar=[2,2,4]
listaImpar=[1,3,3,5]
listaUnion=[2,2,4,1,3,3,5]
'''
lista=[1,2,2,3,3,4,5]
listaPar=[]
listaImpar=[]

for i in range(len(lista)):
    if bool(lista[i]%2): #si es divisible por 2 es true
        listaPar.append(lista[i])
    else:
        listaImpar.append(lista[i])
print(listaPar)
print(listaImpar)
print('Lista Union = ',listaImpar+listaPar)
