'''
Escribir un programa que genere un archivo csv, con la siguiente información

foto ejercicio tp10ej6 autores,libros,años

Con el archivo ya creado, verificando su existencia usando try - except, realice otro programa que le
pregunte al usuario si desea agregar una nueva línea de información y CUANTAS líneas nuevas serían las que
desea agregar y hágalo
'''

import sys
import os.path
import csv
from tp10ej6 import *
sys.path.append("C:/Users/agusb/Desktop/AGUS/AGUS ITBA/2C 2022/EDP/Clases/TP10 Dict")

dictionary = diccionario

### FUNCIONES ###
def crearCSV():
    with open('Books.csv','w', newline='') as csvfile:
        encabezados = dictionary.keys()
        writer = csv.DictWriter(csvfile, fieldnames=encabezados)
        writer.writeheader() 
        writer.writerow(dictionary)

def existe(patharchivo):
    file = open(patharchivo,'r')
    print('File exists')
    file.close()

def agregarLineas(lineas, csvfile):
    labels = ['Book','Author','Year']
    with open(csvfile, 'a') as file:
        for i in range(lineas):
            libro = input('Ingrese nombre del libro: ')
            autor = input('Ingrese autor del libro: ')
            año = input('Ingrese el año de publicacion: ')
            while año.isnumeric() == False:
                año = input('El año debe ser numerico: ')
            año = int(año)
            writer = csv.DictWriter(file, fieldnames= labels)
            writer.writerow({'Book': libro, 'Author': autor, 'Year': año})
            i += 1

### MAIN ###
crearCSV()
patharchivo = 'Books.csv'
try:
    existe(patharchivo)
    seguir = True
    while seguir == True:
        opcionAgregarLineas = input('Desea agregar lineas nuevas? (y/n) ')
        while opcionAgregarLineas.isnumeric() == True or opcionAgregarLineas not in ['y','n']:
            opcionAgregarLineas = input('Por favor ingresar y/n: ')
        if opcionAgregarLineas == 'y':
            lineas = input('Cuantos datos quiere agregar? ')
            while lineas.isnumeric() == False:
                lineas = input('La cantidad debe ser numerica: ')
            lineas = int(lineas)
            agregarLineas(lineas, patharchivo)

            with open(patharchivo, 'r') as file: #printeo el csv actualizado
                labels = ['Book','Author','Year']
                reader = csv.DictReader(file,fieldnames=labels)
                for linea in reader:
                    print(linea)
                    
        elif opcionAgregarLineas == 'n':
            seguir = False
except FileNotFoundError as e:
    e = 'File does not exists'
    print(e) 

