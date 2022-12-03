'''
Usar el archivo del ejercicio 1. 

Importe los datos del archivo Books.csv a una lista. 

Mostrar la lista al usuario. 

Pídales que seleccionen qué fila de la lista quieren eliminarlo y eliminarlo de la lista. 

Posteriormente preguntar al usuario qué datos quieren cambiar y permitirles cambiarlos.

Vuelva a escribir los datos en el archivo .csv original, sobrescribiendo en él los datos existentes con los
datos modificados.
'''

#from tp12ej2 import *
import csv

lista = []
indices = []

if __name__ == "__main__":
    with open('Books.csv','r',newline='') as csvfile:
        reader = csv.reader(csvfile,delimiter=',')
        i=0
        for linea in reader:
            if i==0:
                i+=1
                for elemento in linea:
                    indices.append(elemento)
                print(indices)
            else:
                print(*linea,sep=',')
            # for elemento in linea:
            #     print("{:40}".format(elemento))
            # lista.append(linea)

        #print("{:<40} {:<40} {:<8}".format('Book','Author','Year'))
        #for k,v in diccionario.items():
        #    v = book, author,year
        #print("{:<40} {:<40} {:<8}".format(book, author, year))
    
            #print(*linea, sep=',')
    # print(lista)
    # for elemento in lista:
    #     print(elemento)
    # print('\n')
    # filasAEliminar = int(input('Ingrese que fila quiere eliminar: '))
    # lista.pop(filasAEliminar)
    # for elemento in lista:
    #     print(elemento)