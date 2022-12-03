'''
Escribir un programa que genere un archivo txt, con la siguiente información: (ver foto)
Con el archivo ya creado, realice otro programa que le pregunte al usuario si desea agregar una nueva 
línea de información y CUANTAS líneas nuevas serían las que desea agregar y hágalo
'''
import json

diccionario= {}

autores = ['Harper Lee','Stephen Hawking','F. Scott Fitzgerald','Oliver Sacks','Jane Austen']
libros = ['To Kill a Mockingbird','A Brief History of Time','The Great Gatsby','The Man Who Mistook His Wife for a Hat','Pride and Prejudice']
años = [1960,1988,1922,1985,1813]

def crearDiccionario():
    i=0
    while i < len(autores):
        book = libros[i]
        while book == '' or book in diccionario.keys():
            book = input('Ingrese nombre del libro valido y no repetido: ')
        author = autores[i]     
        year = años[i]
        diccionario[i] = [book, author, year]
        i += 1
    print("{:<15} {:<15} {:<8}".format('\n''Book''\t''\t''\t''\t','Author''\t''\t','Year'))
    for k, v in diccionario.items():
        book, author, year = v
        print("{:<15} {:<15} {:<8}".format(book, author, year))
    
    with open('file.txt','w') as data:
        data.write(str(diccionario))

def agregarInfo():
    lineas = int(input('Ingrese la cantidad de lineas a agregar: '))
    for i in range(lineas):
        libros.append(input('Ingrese nombre del libro: '))
        autores.append(input('Ingrese nombre del autor: '))
        años.append(int(input('Ingrese año de publicacion: ')))
    crearDiccionario() #hago un overwrite digamos

crearDiccionario()
agregarInfo()