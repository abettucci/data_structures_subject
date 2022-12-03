'''
tp10ej6) Escribir un programa que genere un archivo txt, con la siguiente información: (ver foto)
Con el archivo ya creado, realice otro programa que le pregunte al usuario si desea agregar una nueva 
línea de información y CUANTAS líneas nuevas serían las que desea agregar y hágalo

tp2ej2) Escribir un programa que genere un archivo csv, con la siguiente información

foto del ejercicio tp10ej6: autores,libros,años

Con el archivo ya creado, verificando su existencia usando try - except, realice otro programa que le
pregunte al usuario si desea agregar una nueva línea de información y CUANTAS líneas nuevas serían las que
desea agregar y hágalo
'''

import json
import csv

diccionario= {}

autores = ['Harper Lee','Stephen Hawking','F. Scott Fitzgerald','Oliver Sacks','Jane Austen']
libros = ['To Kill a Mockingbird','A Brief History of Time','The Great Gatsby','The Man Who Mistook His Wife for a Hat','Pride and Prejudice']
años = [1960,1988,1922,1985,1813]

def crearDiccionario():
    i=0
    print("{:<40} {:<40} {:<8}".format('Book','Author','Year'))
    while i < len(autores):
        book = libros[i]
        while book == '' or book in diccionario.keys():
            book = input('Ingrese nombre del libro valido y no repetido: ')
        author = autores[i]     
        year = años[i]
        diccionario[i] = {'Book':book,'Author':author,'Year': year}
        i += 1   
        for k,v in diccionario.items():
            v = book, author,year
        print("{:<40} {:<40} {:<8}".format(book, author, year))
    
    with open('tp10ej6.txt','w') as txtfile:
        txtfile.write(str(diccionario))

def appendearInfo():
    with open('tp10ej6.txt','w') as txtfile:
        lineas = int(input('Ingrese la cantidad de lineas a agregar: '))
        for i in range(lineas):   
            i = len(diccionario.keys())  
            book = input('Ingrese nombre del libro: ')
            nombre = input('Ingrese nombre del autor: ')
            año = input('Ingrese año de publicacion: ')
            diccionario[i+1] = {'Book':book,'Author':nombre,'Year': año}
            i += 1
        txtfile.write(str(diccionario))
    return diccionario 
    
def leer():
    with open('tp10ej6.txt','r',newline='') as txtfile:
        print(txtfile.readlines())

crearDiccionario()
appendearInfo()
leer()
