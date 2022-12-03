import time
import numpy as np
import matplotlib.pyplot as pyplot
from datetime import datetime
from claseVentas import *
from utilitarios import *
import os

def imprimirPrimerasYUltimas2Filas():
    print('\n''---------- Primeras 2 filas -----------''\n')
    id=0
    while id < 2:
        print(list(Ventas.diccionarioVentas.values())[id])
        id+=1
    print('\n''---------- Ultimas 2 filas -----------''\n')
    id=len(Ventas.diccionarioVentas.keys())-2
    while id < len(Ventas.diccionarioVentas.keys()):
        print(list(Ventas.diccionarioVentas.values())[id])
        id+=1

def menu():
    #os.system("cls")
    opcionIngresada = input('''
        1. Cargar un listado de ventas desde un csv
        2. Cargar una venta manualmente, insertando los datos
        3. Determinar: Rating pago Ewallet > Rating pago otro medio?
        4. Calcular y discriminar '%' ingresos generados por hombres y por mujeres
        5. Determinar: Sucursal/es mejor/es calificada/s por los clientes
        6. Determinar: Existe sucursal/es / Gasto tot clientes "Member" < Gasto tot clientes no "Member"
        7. Graficar si exsite una corr. Rating Tipo Prod vs. Q Vtas Tipo Prod
        8. Graficar '%' de ingresos generados de compras hechas por hombres y por mujeres
        9. Imprimir todas las ventas posteriores a una determinada fecha y hora
        10. Imprimir todas las ventas anteriores a una determinada fecha y hora
        11. Imprimir todos los registros, del mas reciente al mas antiguo
        12. Imprimir todos los registros, del mas antiguo al mas reciente
        13. Finalizar

        Ingrese que accion desea realizar: ''')
    try:
        if opcionIngresada.isnumeric() == False or int(opcionIngresada) not in range(1,14):
            raise ValueError('Ingrese una valor numerico entre 1 y 13')
        else:
            return int(opcionIngresada)
    except ValueError as E:
        print(E)
        input('Presione enter para continuar: ')
        menu()
    #return int(opcionIngresada)

opcionIngresada = 0
corriendo = True

while corriendo == True:

    try: 
        opcionIngresada = int(input('''
        1. Cargar un listado de ventas desde un csv
        2. Cargar una venta manualmente, insertando los datos
        3. Determinar: Rating pago Ewallet > Rating pago otro medio?
        4. Calcular y discriminar '%' ingresos generados por hombres y por mujeres
        5. Determinar: Sucursal/es mejor/es calificada/s por los clientes
        6. Determinar: Existe sucursal/es / Gasto tot clientes "Member" < Gasto tot clientes no "Member"
        7. Graficar si exsite una corr. Rating Tipo Prod vs. Q Vtas Tipo Prod
        8. Graficar '%' de ingresos generados de compras hechas por hombres y por mujeres
        9. Imprimir todas las ventas posteriores a una determinada fecha y hora
        10. Imprimir todas las ventas anteriores a una determinada fecha y hora
        11. Imprimir todos los registros, del mas reciente al mas antiguo
        12. Imprimir todos los registros, del mas antiguo al mas reciente
        13. Finalizar

        Ingrese que accion desea realizar: '''))
    except ValueError:
        input("Por favor seleccione un valor valido.\n Precione Enter para continuar: ")

    if opcionIngresada == 1:
        start = time.process_time()
        cargarCSVaDiccionarioVentas()
        #imprimirPrimerasYUltimas2Filas()

        print('\n''Print del arbol inorden''\n')
        raiz = Ventas.arbolVentas.root
        claseArbol.arbol.inorder(raiz)
        print('\n')

        print("Tiempo de procesamiento: ","--- %s segundos ---" % (time.process_time() - start))       
        input("Presione Enter para continuar: ")

    elif opcionIngresada == 2:
        start = time.process_time()
        cargarVentaNueva()
        #imprimirPrimerasYUltimas2Filas()
        print("Tiempo de procesamiento: ","--- %s segundos ---" % (time.process_time() - start))
        input("Presione Enter para continuar: ")

    elif opcionIngresada  == 3:
        start = time.process_time()      
        comparacionRatingsMediosDePago()
        print("Tiempo de procesamiento: ","--- %s segundos ---" % (time.process_time() - start))
        input("Presione Enter para continuar: ")

    elif opcionIngresada  == 4:
        start = time.process_time()
        calcularPorcentajeIngresosHyM()
        print("Tiempo de procesamiento: ","--- %s segundos ---" % (time.process_time() - start))
        input("Presione Enter para continuar: ")

    elif opcionIngresada  == 5:
        start = time.process_time()
        calcularMejoresSucursales()
        print("Tiempo de procesamiento: ","--- %s segundos ---" % (time.process_time() - start))
        input("Presione Enter para continuar: ")

    elif opcionIngresada  == 6:
        start = time.process_time()
        gastoMemberVsOtros()
        print("Tiempo de procesamiento: ","--- %s segundos ---" % (time.process_time() - start))            
        input("Presione Enter para continuar: ")

    elif opcionIngresada  == 7:
        start = time.process_time()
        CorrelacionVentasVsRatingTipoProducto()
        print("Tiempo de procesamiento: ","--- %s segundos ---" % (time.process_time() - start))            
        input("Presione Enter para continuar: ")

    elif opcionIngresada  == 8:
        start = time.process_time()
        graficarIngresosHyM()
        print("Tiempo de procesamiento: ","--- %s segundos ---" % (time.process_time() - start))            
        input("Presione Enter para continuar: ")

    elif opcionIngresada  == 9:
        start = time.process_time()
        fecha1 = input('Ventas posteriores a la fecha : ')
        raiz = Ventas.arbolVentas.root
        claseArbol.arbol.filtrarRegistrosPosterioresAFecha(raiz,fecha1)
        print("Tiempo de procesamiento: ","--- %s segundos ---" % (time.process_time() - start))            
        input("Presione Enter para continuar: ")

    elif opcionIngresada  == 10:
        start = time.process_time()
        fecha1 = input('Ventas previas a la fecha : ')
        raiz = Ventas.arbolVentas.root
        claseArbol.arbol.filtrarRegistrosPreviosAFecha(raiz,fecha1)
        print("Tiempo de procesamiento: ","--- %s segundos ---" % (time.process_time() - start))            
        input("Presione Enter para continuar: ")

    elif opcionIngresada  == 11:
        start = time.process_time()
        raiz = Ventas.arbolVentas.root
        claseArbol.arbol.visualizarVentasDeRecienteAAntiguo(raiz)
        print("Tiempo de procesamiento: ","--- %s segundos ---" % (time.process_time() - start))            
        input("Presione Enter para continuar: ")

    elif opcionIngresada  == 12:
        start = time.process_time()
        raiz = Ventas.arbolVentas.root
        claseArbol.arbol.visualizarVentasDeAntiguoAReciente(raiz)
        print("Tiempo de procesamiento: ","--- %s segundos ---" % (time.process_time() - start))            
        input("Presione Enter para continuar: ")

    elif opcionIngresada == 13:
        corriendo = False
    else:
        print('\n Ingrese un numero valido \n')
        input('Ingrese una nueva accion: ')
        menu()

    
    