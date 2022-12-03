### Ejercicio 12

''' Utilice funciones built-in del caso que, dada una lista de números enteros genere una 
nueva lista en la cual los números menores de 9000 se les haya sumado 3000

Ejemplo1:
lst1=[1000, 500, 600, 700, 5000, 90000, 17500]
listaFinal=[4000, 3500, 3600, 3700, 8000, 90000, 17500]
'''
lst1=[1000, 500, 600, 700, 5000, 90000, 17500]
listaFinal = []

for i in range(len(lst1)):
    if lst1[i]<9000:
        lst1[i] += 3000
    listaFinal.append(lst1[i])
print(listaFinal)
