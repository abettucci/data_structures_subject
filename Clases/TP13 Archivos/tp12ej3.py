'''
Usar el archivo del ejercicio 1 y a través de una función solicite al usuario que ingrese un año de inicio y un
año de final, y le muestre la información filtrada entre esos 2 años
'''

import sys
import os.path
from tp10ej6 import *
sys.path.append("C:/Users/agusb/Desktop/AGUS/AGUS ITBA/2C 2022/EDP/Clases/TP10 Dict")

fecha1 = int(input('Ingrese fecha de inicio: '))
fecha2 = int(input('Ingrese fecha final: '))

dictFiltrado = {}

def filtrarEntrePeriodos(fecha1,fecha2, diccionario):
    libros = []
    for i in range(len(diccionario.values())):
        if diccionario[i][2] in range(fecha1, fecha2):
            libros.append(diccionario[i][0])
    return libros

print(filtrarEntrePeriodos(fecha1,fecha2,diccionario))

