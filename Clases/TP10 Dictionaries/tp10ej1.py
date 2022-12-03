'''
Utilizando la información de las ventas de las diferentes zonas de influencia de cada uno los vendedores de la empresa “Si se puede”, usted debe realizar un programa que permita realizar las siguientes tareas:
1. Crear un diccionario que permita manejar la información de las ventas en cada zona de cada vendedor.
2. Preguntar al usuario si desea modificar alguna información existente en la data, de ser así pedir nombre del vendedor, la zona de influencia y el valor de la venta a modificar.
3. Visualizar las ventas totales de la empresa
4. Visualizar la zona de mayores ventas.
'''
nombres = ['Nicolas','Daniela','Maria','Francisco']
valores = [[3528,2400,1200,8200],[3824,6786,5598,3612],[8008,4653,8425,1000],[5833,6356,2548,1386]]

import numpy as np

dictVendedores= {}

def crearDiccionario():
    i=0
    #N = int(input('Ingrese cantidad de vendedores: '))
    while i < len(range(4)):
        nombre = nombres[i]
        while nombre == '' or nombre in dictVendedores.keys():
            nombre = input('Ingrese un nombre valido y no repetido: ')
        norte = valores[i][0]      
        sur = valores[i][1]
        este = valores[i][2]
        oeste = valores[i][3]
        dictVendedores[nombre] = [norte,sur,este,oeste]
        i += 1
    print("{:<8} {:<8} {:<8} {:<8}".format('\n''Norte','Sur','Este','Oeste'))
    for k, v in dictVendedores.items():
        norte,sur,este,oeste = v
        print("{:<8} {:<8} {:<8} {:<8}".format(norte, sur, este, oeste))
    return dictVendedores

def modificarVentas(dictVendedores):
    vendedor = input('Ingrese nombre del vendedor a cambiar: ')
    for vendedores in dictVendedores.keys():
        if vendedor == vendedores:
            norte = int(input('Ingrese nuevo valor de ventas en zona norte: '))
            sur = int(input('Ingrese nuevo valor de ventas en zona sur: '))
            este = int(input('Ingrese nuevo valor de ventas en zona este: '))
            oeste = int(input('Ingrese nuevo valor de ventas en zona oeste: '))
            dictVendedores2 = dictVendedores
            #dictVendedores2.update({norte,sur,este,oeste})
            dictVendedores2[vendedor] = [norte,sur,este,oeste]
            print("{:<8} {:<8} {:<8} {:<8}".format('\n''Norte','Sur','Este','Oeste'))
            for k, v in dictVendedores2.items():
                norte,sur,este,oeste = v
                print("{:<8} {:<8} {:<8} {:<8}".format(norte, sur, este, oeste))
            return dictVendedores2

def mostrarVentasTot(dictVendedores2):
    #creé dictVendedores2 porque no me estaba tomando el dictionario modificado, me esta tomando solo el original que creé en la opcion 1
    suma = 0
    #suma = sum(dictVendedores.values()) #no me funciona porque tengo un elemento que es el nombre del vendedor con nombres 'agus' y 'mati'
    #print(suma)
    for k, v in dictVendedores2.items():
        norte,sur,este,oeste = v
        suma += norte + sur + norte + oeste
    print('\n''Suma de todos: ',suma,'\n')   

def mostrarZonaMayoresVentas(dictVendedores): #mostrar la zona de mayores ventas, sumo las columnas y armos lista de zonas y busco el max ahi
    zonas = [[],[],[],[]]
    for k, v in dictVendedores.items():
        norte,sur,este,oeste = v
        zonas[0].append(norte)
        zonas[1].append(sur)
        zonas[2].append(este)
        zonas[3].append(oeste)
        dicSumaValores = dict()
        dicSumaValores['Norte'] = sum(zonas[0])
        dicSumaValores['Sur'] = sum(zonas[1])
        dicSumaValores['Este'] = sum(zonas[2])
        dicSumaValores['Oeste'] = sum(zonas[3])
    print ('Las ventas maximas fueron de: {}, correspondientes a la zona {}'.format(max(dicSumaValores.values()),max(dicSumaValores, key=dicSumaValores.get)))

def menu():
    opcionIngresada = int(input('''
        1. Crear diccionario
        2. Modificar datos de ventas
        3. Mostrar ventas totales
        4. Mostrar zona de mayores ventas
        5. Finalizar
        Ingrese que accion desea realizar: '''))
    corriendo = True
    while corriendo == True:
        if opcionIngresada == 1:
            crearDiccionario()
            opcionIngresada = int(input('Ingrese una nueva accion: '))

        elif opcionIngresada == 2:
            modificarVentas(dictVendedores)
            opcionIngresada = int(input('Ingrese una nueva accion: '))

        elif opcionIngresada == 3:
            mostrarVentasTot(dictVendedores)
            opcionIngresada = int(input('Ingrese una nueva accion: '))

        elif opcionIngresada == 4:
            mostrarZonaMayoresVentas(dictVendedores)
            opcionIngresada = int(input('Ingrese una nueva accion: '))
        elif opcionIngresada == 5:
            corriendo = False
        else:
            print('\n Ingrese un numero valido \n')
            opcionIngresada = int(input('Ingrese una nueva accion: '))

menu()

# dictVendedores= {}

# def crearDiccionario():
#     i=0
#     while i <2:
#         nombre = input('Ingrese nombre del vendedor: ') 
#         while nombre == '' or nombre in dictVendedores.values():
#             nombre = input('Ingrese un nombre valido y no repetido: ')
#         norte = int(input('Ingrese ventas en zona Norte: '))
#         sur = int(input('Ingrese ventas en zona Sur: '))
#         este = int(input('Ingrese ventas en zona Este: '))
#         oeste = int(input('Ingrese ventas en zona Oeste: ')) 
#         dictVendedores[i] = [nombre,norte,sur,este,oeste]
#         i += 1
#     print("{:<15} {:<8} {:<8} {:<8} {:<8}".format('\n''Nombre','Norte','Sur','Este','Oeste'))
#     for k, v in dictVendedores.items():
#         nombre,norte,sur,este,oeste = v
#         print("{:<15} {:<8} {:<8} {:<8} {:<8}".format(nombre, norte, sur, este, oeste))
#     print(dictVendedores.values())
#     print(dictVendedores.keys())
#     print(dictVendedores)
#     return dictVendedores

# def modificarVentas(dictVendedores):
#     vendedor = int(input('Ingrese ID del vendedor a cambiar: '))
#     if vendedor == 0:
#         norte = int(input('Ingrese nuevo valor de ventas en zona norte: '))
#         sur = int(input('Ingrese nuevo valor de ventas en zona sur: '))
#         este = int(input('Ingrese nuevo valor de ventas en zona este: '))
#         oeste = int(input('Ingrese nuevo valor de ventas en zona oeste: '))
#         nombre = 'agus' #probe solo con el primer vendedor
#         dictVendedores2 = dictVendedores
#         dictVendedores2.update({0:[nombre,norte,sur,este,oeste]})
#         print("{:<15} {:<8} {:<8} {:<8} {:<8}".format('\n''Nombre','Norte','Sur','Este','Oeste'))
#         for k, v in dictVendedores2.items():
#             nombre,norte,sur,este,oeste = v
#             print("{:<15} {:<8} {:<8} {:<8} {:<8}".format(nombre, norte, sur, este, oeste))
#         return dictVendedores2

# def mostrarVentasTot(dictVendedores2):
#     #creé dictVendedores2 porque no me estaba tomando el dictionario modificado, me esta tomando solo el original que creé en la opcion 1
#     suma = 0
#     #suma = sum(dictVendedores.values()) #no me funciona porque tengo un elemento que es el nombre del vendedor con nombres 'agus' y 'mati'
#     #print(suma)
#     for k, v in dictVendedores2.items():
#         nombre,norte,sur,este,oeste = v
#         suma += norte + sur + norte + oeste
#     print('\n''Suma de todos: ',suma,'\n')   

# def menu():
#     opcionIngresada = int(input('''
#         1. Crear diccionario
#         2. Modificar datos de ventas
#         3. Mostrar ventas totales
#         4. Mostrar zona de mayores ventas
#         5. Finalizar
#         Ingrese que accion desea realizar: '''))
#     corriendo = True
#     while corriendo == True:
#         if opcionIngresada == 1:
#             dic = crearDiccionario()
#         elif opcionIngresada == 2:
#             modificarVentas(dictVendedores)
#             pass
#         elif opcionIngresada == 3:
#             mostrarVentasTot(dictVendedores)
#             pass
#         elif opcionIngresada == 4:
#             #mostrarHotspot()
#             pass
#         elif opcionIngresada == 5:
#             corriendo = False
#             break
#         else:
#             print('\n Ingrese un numero valido \n')
#         opcionIngresada = int(input('Ingrese una nueva accion: '))

# menu()