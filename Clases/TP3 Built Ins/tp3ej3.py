### Ejercicio 3

''' Realizar una función anónima que tenga como parámetro z y regrese si z es par. 
Realice el llamado de lafunción anónima correctamente y visualice la respuesta obtenida

Ejemplo 1:
z=2
visualizara: 2 es par
'''

from random import randint


esPar = lambda z: z%2 == 0 #se fija si la division es entera o hay resto. Si hay resto entonces no es par pq no es divisible por 2
for i in range(10):
    print('Es par el numero ',i,' ? ',esPar(i))
