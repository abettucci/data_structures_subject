### Ejercicio 8

''' Utilice funciones built-in del caso, para que genere una lista solo con los valores 
negativos de la lista dada

Ejemplo1:
lista=[1,2,-2,3,-3,-4,5]
listaNegativos=[-2,-2,-4]
'''
listaNegativos=[]
lista = [1,2,-2,3,-3,-3,-4,5]
for numero in lista:
    if numero<0 and numero not in listaNegativos:
        listaNegativos.append(numero)
print(lista)
print(listaNegativos)
print('Cantidad de negativos: ',sum(1 for number in lista if number < 0))
