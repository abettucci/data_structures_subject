############ ENUNCIADO #################
'''
        1. Cargar un listado de ventas desde un csv
        2. Cargar una venta manualmente, insertando los datos
        3. Determinar si el pago con Ewallet mejora el rating de una venta en realcion con el resto de los medios de pago
        4. Calcular y discriminar el procentaje de los ingresos devenidos de compras hechas por hombres y por mujeres
        5. Determinar que cual de las sucursales es la mejor calificada por los clientes
        6. Determinar si existe alguna sucursal en la que los clientes de tipo "Member" hayan gastado, en total, menos que los no "Member"
        7. Demostrar graficamente si exsite una correlacion entre el rating de un tipo de producto y la cantidad de ventas que genera, es decir, si los tipos de producto asociados a ventas mejor calificadas venden mas
        8. Mostrar graficamente el porcentajo de los ingresos devenidos de compras hechas por hombres y por mujeres
        9. Imprimir todas las ventas posteriores a una determinada fecha y hora
        10. Imprimir todas las ventas anteriores a una determinada fecha y hora
        11. Imprimir todos los registros, del mas reciente al mas antiguo
        12. Imprimir todos los registros, del mas antiguo al mas reciente
        13. Finalizar
'''
############## CONSIDERACIONES #############
'''
1) ASUMIR LISTADO COMPLETO DE VENTAS PUEDE TENER MILLONES DE REGISTROS (O SEA DEBEMOS MANEJAR MILLONES DE FILAS EDE XLS)
2) VAMOS A PRIORIZAR VELOCIDAD ANTES QUE MEMORIA, ELEGIR ESTRUCTURAS ACORDE A ESTA PRIORIDAD!
3) HACER VALIDACIONES PARA EVITAR SALIDAS ABRUPTAS ---> MANEJO DE EXCEPCIONES
4) SI AL ELEGIR UNA OPCION DEL MENU TODAVIA NO HAY INFO PARA MOSTRAR, ENVIAR UN MENSAJE AL USUARIO Y SEGUIR CORRIENDO
5) USAR VARIABLES CON NOMBRES COHERENTES Y ENTENDIBLES, QUE SE LEAN SOLOS LOS CODIGOS. SEPARAR LOS MODULOS EN
FUNCIONES, ARCHIVOS, NO REPETIR CODIGOS, ARMAR CLASES, ETC.
6) EL CSV ES UNA LISTA DE PEDIDOS DE SUPERMERCADO CON 3 SUCURSALES. CADA VENTA TIENE UN ID DE CLIENTE ASOCIADO, EL CUAL ES UNICO!
'''
############### RESOLUCION ################
import time
import csv
import numpy as np
import matplotlib.pyplot as pyplot
from datetime import datetime
import claseNodoArbol 
import claseArbol

sales = {}
IDs = set()
#campos = tuple(["Invoice ID","Branch","City","Customer type","Gender","Product line","Unit price","Quantity","Tax 5%","Total","Date","Time","Payment","cogs","gross margin percentage","gross income","Rating"])
porcentajes = []

def cargasCSVaDiccionario():
    with open("supermarket_sales - Sheet1.csv",'r',newline='') as csvfile:
        campos = tuple(["Invoice ID","Branch","City","Customer type","Gender","Product line","Unit price","Quantity","Tax 5%","Total","Date","Time","Payment","cogs","gross margin percentage","gross income","Rating"])
        reader = csv.DictReader(csvfile,fieldnames=campos, delimiter=',')
        for linea in reader:
                sales[ linea['Invoice ID'] ] = {'Branch': linea['Branch'],'City': linea['City'],'Customer type': linea['Customer type'],'Gender':linea['Gender'],'Product line': linea['Product line'],'Unit price': linea['Unit price'],'Quantity': linea['Quantity'],'Tax 5%': linea['Tax 5%'],'Total': linea['Total'],'Date': linea['Date'],'Time': linea['Time'],'Payment': linea['Payment'],'cogs': linea['cogs'],'gross margin percentage': linea['gross margin percentage'],'gross income': linea['gross income'],'Rating': linea['Rating']}
                IDs.add(linea['Invoice ID'])

def cargarVentas(ID):
    sales[ID] = {}
    campos = tuple(["Invoice ID","Branch","City","Customer type","Gender","Product line","Unit price","Quantity","Tax 5%","Total","Date","Time","Payment","cogs","gross margin percentage","gross income","Rating"])
    for columnas in campos[1:]:
        value = input('Ingrese valor de ' + str(columnas)+ ': ')
        sales[ID][columnas] = value
    return sales[ID]

def verificarID(IDinput):
    IDnumeric = IDinput.split('-')
    if IDnumeric.isnumeric() == False:
        print('Error')
    elif len(IDnumeric[0]) != 3 or len(IDnumeric[1]) != 2 or len(IDnumeric[2]) !=4:
        print('Error')
    else:
        return IDnumeric

def comparacionRatingsMediosDePago():
    sumaRatingsEwallet = 0
    sumaRatingsCash = 0
    sumaRatingsCreditCard = 0
    countEwalletPymnt = 0
    countCashPymnt = 0
    countCreditCardPymnt = 0
    listaPromedios = []
    for ids in sales.keys(): # EWALLET
        if sales[ids]['Payment'] == 'Ewallet':
            sumaRatingsEwallet += float(sales[ids]['Rating'])
            countEwalletPymnt += 1
        elif sales[ids]['Payment'] == 'Cash': # CASH
            sumaRatingsCash += float(sales[ids]['Rating'])
            countCashPymnt += 1
        elif sales[ids]['Payment'] == 'Credit card': # CREDIT CARD
            sumaRatingsCreditCard += float(sales[ids]['Rating'])
            countCreditCardPymnt += 1
    listaPromedios.append(['Ewallet',float(sumaRatingsEwallet/countEwalletPymnt)])
    listaPromedios.append(['Cash',float(sumaRatingsCash/countCashPymnt)])
    listaPromedios.append(['Credit card',float(sumaRatingsCreditCard/countCreditCardPymnt)])
    print("El maximo rating en promedio es de {} y corresponde al metodo de pago {}".format(round(max(listaPromedios,key=lambda x: x[1])[1],4),max(listaPromedios,key=lambda x: x[1])[0]))

def calcularPorcentajeIngresosHyM():
    IngresosTotales = 0
    IngresosHombres = 0
    IngresosMujeres = 0
    percentIngresosHombres = 0
    percentIngresosMujeres = 0

    for ids in sales.keys():
        if sales[ids]['Gender'] == 'Female': #MUJERES
            IngresosMujeres += float(sales[ids]['Total'])
        elif sales[ids]['Gender'] == 'Male': #HOMBRES
            IngresosHombres += float(sales[ids]['Total'])
    IngresosTotales = IngresosMujeres + IngresosHombres
    percentIngresosHombres = IngresosMujeres/IngresosTotales
    percentIngresosMujeres = IngresosHombres/IngresosTotales
    porcentajes.append(percentIngresosHombres)
    porcentajes.append(percentIngresosMujeres)
    print('Porcentaje de ingresos generados por compras de hombres: ',"{:.0%}".format(percentIngresosHombres))
    print('Porcentaje de ingresos generados por compras de mujeres: ',"{:.0%}".format(percentIngresosMujeres))
    return porcentajes

def calcularMejoresSucursales():
    listaSucursales = [[],[],[]]
    listaPromediosSucursales = []
    for ids in sales.keys():
        if sales[ids]['Branch'] == 'A':
            print(sales[ids]['Rating'])

            listaSucursales[0].append(float(sales[ids]['Rating']))
        elif sales[ids]['Branch'] == 'B':
            print(sales[ids]['Rating'])

            listaSucursales[1].append(float(sales[ids]['Rating']))
        else:
            print(sales[ids]['Rating'])
            listaSucursales[2].append(float(sales[ids]['Rating']))
    PromedioA = round(sum(listaSucursales[0])/float(len(listaSucursales[0])),4)
    PromedioB = round(sum(listaSucursales[1])/float(len(listaSucursales[1])),4)
    PromedioC = round(sum(listaSucursales[2])/float(len(listaSucursales[2])),4)
    listaPromediosSucursales.append(['A',PromedioA])
    listaPromediosSucursales.append(['B',PromedioB])
    listaPromediosSucursales.append(['C',PromedioC])
    print("La sucursal con mayor rating de {}, es la sucursal {}".format(round(max(listaPromediosSucursales,key=lambda x: x[1])[1],4),max(listaPromediosSucursales,key=lambda x: x[1])[0]))

def gastoMemberVsOtros():
    x=0
    gastosSucursales = [[0,0],[0,0],[0,0]]
    for ids in sales.keys():
        if sales[ids]['Branch'] == 'A':
            if sales[ids]['Customer type'] == 'Member': #member
                gastosSucursales[0][0] += float(sales[ids]['Total']) #primera posicion = gasto total Member, segunda posicion = gasto total No Member
            else: #no member
                gastosSucursales[0][1] += float(sales[ids]['Total'])
        elif sales[ids]['Branch'] == 'B':
            if sales[ids]['Customer type'] == 'Member':
                gastosSucursales[1][0] += float(sales[ids]['Total'])
            else: 
                gastosSucursales[1][1] += float(sales[ids]['Total'])
        elif sales[ids]['Branch'] == 'C':
            if sales[ids]['Customer type'] == 'Member':
                gastosSucursales[2][0] += float(sales[ids]['Total'])
            else: 
                gastosSucursales[2][1] += float(sales[ids]['Total'])

    for sucursal in range(len(gastosSucursales)):
        if gastosSucursales[sucursal][0] < gastosSucursales[sucursal][1]:
            print("la sucursal {} tuvo mayores gastos de clientes no members que members".format(sucursal))
            x += 1
    if x==0:
        print('Ninguna sucursal presenta mayores ventas de no member vs member')

def CorrelacionVentasVsRatingTipoProducto():
    x=[]
    y=[]
    for ids in sales.keys():
        x.append(float(sales[ids]['Rating']))
        x.sort()
        y.append(float(sales[ids]['Quantity']))
        y.sort()
    pyplot.title("Correlacion entre Rating de Producto y Cantidad de Vtas del Producto")
    pyplot.xlabel('Rating del Producto')
    pyplot.ylabel('Cantidad de Ventas')
    pyplot.scatter(x,y)
    pyplot.show()

def graficarIngresosHyM():
    pyplot.title('Porcentaje de ingresos segmentado por hombres y mujeres',loc='center',color='black')
    print(porcentajes)
    pyplot.pie(porcentajes, labels=['Hombres','Mujeres'], autopct='%.2f%%')
    pyplot.show()
           
def filtrarRegistrosPrevioAFecha(nodo,fecha):
    if fecha == nodo.dato:
        return True
    elif fecha < nodo.dato: # previo a la fecha del nodo
        if nodo.left == None:
            return False
        else:
            print(nodo.dato)
            return filtrarRegistrosPrevioAFecha(nodo.left, fecha)

def leerPrimeras2Lineas():
    i=0
    while i < 2:
        print(list(sales.values())[i])
        i += 1

#def filtrarRegistrosPosterioresAFecha(fechaInicio):
#def visualizarVentasDeRecienteAAntiguo():
#def visualizarVentasDeAntiguoAReciente():

def menu():
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

    while opcionIngresada.isnumeric() == False or int(opcionIngresada) not in range(1,14):
        opcionIngresada = input('Ingrese una valor numerico entre 1 y 13: ')
    opcionIngresada = int(opcionIngresada)

    corriendo = True
    while corriendo == True:
        if opcionIngresada == 1:
            start = time.process_time()
            cargasCSVaDiccionario()
            print("Tiempo de procesamiento: ","--- %s segundos ---" % (time.process_time() - start))
            opcionIngresada = int(input('Ingrese una nueva accion: '))
            leerPrimeras2Lineas()

        elif opcionIngresada == 2:
            start = time.process_time()
            InvoiceID = input('Ingrese codigo de venta: ')
            IDnumeric = convertirIDaNumero(InvoiceID)
            while IDnumeric.isnumeric() == False or InvoiceID in IDs:
                InvoiceID =  input('Por favor ingrese un valor numerico y no repetido: ')
                IDnumeric = convertirIDaNumero(InvoiceID)
            IDnumeric = int(IDnumeric)
            cargarVentas(InvoiceID)
            print("Tiempo de procesamiento: ","--- %s segundos ---" % (time.process_time() - start))
            opcionIngresada = int(input('Ingrese una nueva accion: '))

        elif opcionIngresada == 3:
            start = time.process_time()      
            #haria un promedio del rating de aquellas ventas que fueron ewallet y un promedio para aquellas
            # ventas que fueron con cash o credit card y luego comparo entre esos 3 promedios cual fue el 
            # mas alto
            comparacionRatingsMediosDePago()
            print("Tiempo de procesamiento: ","--- %s segundos ---" % (time.process_time() - start))
            opcionIngresada = int(input('Ingrese una nueva accion: '))

        elif opcionIngresada == 4:
            start = time.process_time()
            calcularPorcentajeIngresosHyM()
            print("Tiempo de procesamiento: ","--- %s segundos ---" % (time.process_time() - start))
            opcionIngresada = int(input('Ingrese una nueva accion: '))

        elif opcionIngresada == 5:
            start = time.process_time()
            calcularMejoresSucursales()
            print("Tiempo de procesamiento: ","--- %s segundos ---" % (time.process_time() - start))
            opcionIngresada = int(input('Ingrese una nueva accion: '))

        elif opcionIngresada == 6:
            start = time.process_time()
            gastoMemberVsOtros()
            print("Tiempo de procesamiento: ","--- %s segundos ---" % (time.process_time() - start))            
            opcionIngresada = int(input('Ingrese una nueva accion: '))
        
        elif opcionIngresada == 7:
            start = time.process_time()
            CorrelacionVentasVsRatingTipoProducto()
            print("Tiempo de procesamiento: ","--- %s segundos ---" % (time.process_time() - start))            
            opcionIngresada = int(input('Ingrese una nueva accion: '))

        elif opcionIngresada == 8:
            start = time.process_time()
            graficarIngresosHyM()
            #correlacion()
            print("Tiempo de procesamiento: ","--- %s segundos ---" % (time.process_time() - start))            
            opcionIngresada = int(input('Ingrese una nueva accion: '))

        elif opcionIngresada == 9:
            start = time.process_time()
            date_format = "%m/%d/%Y"
            f1 = input('Ventas posteriores a la fecha: ')
            fecha1 = datetime.strptime(f1, date_format)
            filtrarRegistrosPosterioresAFecha(fecha1)
            print("Tiempo de procesamiento: ","--- %s segundos ---" % (time.process_time() - start))            
            opcionIngresada = int(input('Ingrese una nueva accion: '))

        elif opcionIngresada == 10:
            start = time.process_time()
            date_format = "%m/%d/%Y"
            f2 = input('Ventas previas a la fecha: ')
            fecha2 = datetime.strptime(f2, date_format)
            for ids in sales.keys():
                nodo1=claseNodoArbol.NodoArbol(sales[ids]['Date'])
                arbol1=claseArbol.arbol(nodo1)
                arbol1.agregarnodo(nodo1)
                break
            for ids in sales.keys():
                nodo=claseNodoArbol.NodoArbol(sales[ids]['Date'])
                #nodoFormateado = datetime.strptime(nodo.dato,"%m/%d/%Y")
                #nodo.dato = nodoFormateado
                arbol1.agregarnodo(nodo)
            claseArbol.arbol.preorder(arbol1.root)
            filtrarRegistrosPrevioAFecha(arbol1.root,fecha2)
            print("Tiempo de procesamiento: ","--- %s segundos ---" % (time.process_time() - start))            
            opcionIngresada = int(input('Ingrese una nueva accion: '))

        elif opcionIngresada == 11:
            start = time.process_time()
            #visualizarVentasDeRecienteAAntiguo()
            print("Tiempo de procesamiento: ","--- %s segundos ---" % (time.process_time() - start))            
            opcionIngresada = int(input('Ingrese una nueva accion: '))

        elif opcionIngresada == 12:
            start = time.process_time()
            #visualizarVentasDeAntiguoAReciente()
            print("Tiempo de procesamiento: ","--- %s segundos ---" % (time.process_time() - start))            
            opcionIngresada = int(input('Ingrese una nueva accion: '))

        elif opcionIngresada == 13:
            corriendo = False
        else:
            print('\n Ingrese un numero valido \n')
            opcionIngresada = int(input('Ingrese una nueva accion: '))

menu()