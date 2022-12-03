''''
Diseña una función que le llega como parámetro de entrada un vector con los precios de un producto y 
muestre por pantalla el menor y el mayor de los precios.

EJ 1:
precios=(‘i’,[ 50, 75, 46, 22, 80, 65, 8])
visualizara: Precio máximo:80 Precio mínimo=8
'''

import array as arr

vector = arr.array("i",[50,75,46,22,80,65,8]) #uso el tipo de dato 'i' porque son numeros enteros que le paso
print('Precio maximo: ',max(vector),' Precio minimo: ',min(vector))


