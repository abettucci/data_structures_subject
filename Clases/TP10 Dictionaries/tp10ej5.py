'''
Cree una función que permita almacenar la información del diccionario anterior en un archivo txt 
y posteriormente leerlo'''

from tp10ej4 import *

if __name__ == "__main__":
    diccionario = depurarComponentes("Verde-Azul, Amarillo, Amarillo, Azul")

def almacenarInfo(diccionario):    # no me funciona, capaz deberia convertir el set a diccionario?
    with open('file2.txt','w') as data:
        data.write(str(diccionario))

def leerInfo(file):
    data = open(file,'r')
    for lines in data.readlines():
        print(lines)

almacenarInfo(diccionario)
leerInfo('file2.txt')