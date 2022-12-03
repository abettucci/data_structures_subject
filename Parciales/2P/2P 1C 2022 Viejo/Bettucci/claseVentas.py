import claseArbol
import claseNodoArbol
import csv
from utilitarios import verificarFormatoID
from utilitarios import convertirFechayHoraANumero
import matplotlib.pyplot as pyplot
from datetime import datetime

porcentajes = []
listaDeVentas = []

class Ventas():
    conjuntoVentas = set()
    diccionarioVentas = dict()
    conjuntoIDs = set()
    arbolVentas = None

    #me guardo solo los campos del csv necesarios para los calculos en los atributos
    # no le pongo str() al resto de los atirbutos pq ya vienen como str del csv
    def __init__(self, invoiceID, branch, customerType, gender, productLine, quantity,total,date,time,payment, rating):
        self.invoiceID = invoiceID
        self.branch = branch
        self.customerType = customerType
        self.gender = gender
        self.productLine = productLine
        self.quantity = quantity
        self.total = total
        self.date= date #chequearFormatoFecha
        self.time = time #chequearFormatoHora
        self.payment = payment
        if float(rating) > 10:
            raise ValueError("No se puede poner un puntaje mas alto que 10")  
        elif float(rating) < 0:
            raise ValueError("No se puede poner un puntaje menor a 0")
        self.rating = float(rating)

        if self.invoiceID not in Ventas.conjuntoIDs: #Verifico que si agrego un objeto con un ID igual a otro no voy a estar sobreescribiendo el diccionario
            Ventas.conjuntoIDs.add(self.invoiceID)
            Ventas.diccionarioVentas[self.invoiceID] = {'Invoice ID':self.invoiceID,'Branch':self.branch,'Customer type':self.customerType,'Gender':self.gender,'Product line':self.productLine,'Quantity':self.quantity,'Total':self.total,'Date':self.date,'Time':self.time,'Payment':self.payment,'Rating':self.rating} #agrego el objeto ventas al diccionario de ventas
        Ventas.conjuntoVentas.add(self) #agrego el objeto ventas al conjunto de ventas
        listaDeVentas.append(self) #agrego el objeto ventas a la lista secuencial de ventas

        nodo = claseNodoArbol.NodoArbol(self)
        if Ventas.arbolVentas == None:
            Ventas.arbolVentas=claseArbol.arbol(nodo)
        else:
            Ventas.arbolVentas.agregarnodo(nodo)

    def __str__(self):
        return str((self.invoiceID, self.branch, self.customerType, self.gender, self.productLine, self.quantity, self.total, self.date, self.time, self.payment, self.rating))

def cargarCSVaDiccionarioVentas():
    try:
        with open("supermarket_sales - Sheet1.csv",'r',newline='') as csvfile:
            reader = csv.DictReader(csvfile,delimiter=',')
            for linea in reader:
                InvoiceID=linea['Invoice ID']
                Branch = linea['Branch']
                CustomerType = linea['Customer type']
                Gender = linea['Gender']
                ProductLine = linea['Product line']
                Quantity = linea['Quantity']
                Total = linea['Total']
                Date = linea['Date']
                Time = linea['Time']
                Payment = linea['Payment']
                rating = linea['Rating']
                Ventas(InvoiceID,Branch,CustomerType,Gender,ProductLine,Quantity,Total,Date,Time,Payment,rating)
    except FileNotFoundError:
        print("No se ha encontrado el archivo")
        return
        
def verificarIDnoRepetido(ID):
    if ID in Ventas.conjuntoIDs: #aca tengo que ver lista de IDs, no lista de objetos. Uso IDinput porque ventas.invoiceID no esta formateado, viene como string tipo "xxx-xx-xxxx"
        IDnuevo = input('Ingrese un codigo no repetido: ')
        verificarIDnoRepetido(IDnuevo)

def cargarVentaNueva():
    InvoiceID = input('Ingrese codigo de venta: ')
    verificarFormatoID(InvoiceID)
    verificarIDnoRepetido(InvoiceID)
    branch = input('Ingrese sucursal de la venta: ')
    customerType = input('Ingrese tipo de cliente: ')
    while customerType not in ['Member','Normal']:
        customerType = input('Ingrese tipo de cliente: ')
    gender = input('Ingrese genero: ')
    productLine = input('Ingrese tipo de producto: ')
    quantity = input('Ingrese cantidad: ')
    total = input('Ingrese total: ')
    date = input('Ingrese fecha: ')
    time = input('Ingrese hora: ')
    payment = input('Ingrese pago: ')
    rating = input('Ingrese rating: ')
    Ventas(InvoiceID, branch,customerType,gender,productLine,quantity,total,date,time,payment,rating)  

def comparacionRatingsMediosDePago():
    sumaRatingsEwallet = 0
    sumaRatingsCash = 0
    sumaRatingsCreditCard = 0
    countEwalletPymnt = 0
    countCashPymnt = 0
    countCreditCardPymnt = 0
    listaPromedios = []
    for ids in Ventas.diccionarioVentas.keys(): # EWALLET
        if Ventas.diccionarioVentas[ids]['Payment'] == 'Ewallet':
            sumaRatingsEwallet += float(Ventas.diccionarioVentas[ids]['Rating'])
            countEwalletPymnt += 1
        elif Ventas.diccionarioVentas[ids]['Payment'] == 'Cash': # CASH
            sumaRatingsCash += float(Ventas.diccionarioVentas[ids]['Rating'])
            countCashPymnt += 1
        elif Ventas.diccionarioVentas[ids]['Payment'] == 'Credit card': # CREDIT CARD
            sumaRatingsCreditCard += float(Ventas.diccionarioVentas[ids]['Rating'])
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

    for ids in Ventas.diccionarioVentas.keys():
        if Ventas.diccionarioVentas[ids]['Gender'] == 'Female': #MUJERES
            IngresosMujeres += float(Ventas.diccionarioVentas[ids]['Total'])
        elif Ventas.diccionarioVentas[ids]['Gender'] == 'Male': #HOMBRES
            IngresosHombres += float(Ventas.diccionarioVentas[ids]['Total'])
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
    for ids in Ventas.diccionarioVentas.keys():
        if Ventas.diccionarioVentas[ids]['Branch'] == 'A':
            listaSucursales[0].append(float(Ventas.diccionarioVentas[ids]['Rating']))
        elif Ventas.diccionarioVentas[ids]['Branch'] == 'B':
            listaSucursales[1].append(float(Ventas.diccionarioVentas[ids]['Rating']))
        else:
            listaSucursales[2].append(float(Ventas.diccionarioVentas[ids]['Rating']))
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
    for ids in Ventas.diccionarioVentas.keys():
        if Ventas.diccionarioVentas[ids]['Branch'] == 'A':
            if Ventas.diccionarioVentas[ids]['Customer type'] == 'Member': #member
                gastosSucursales[0][0] += float(Ventas.diccionarioVentas[ids]['Total']) #primera posicion = gasto total Member, segunda posicion = gasto total No Member
            else: #no member
                gastosSucursales[0][1] += float(Ventas.diccionarioVentas[ids]['Total'])
        elif Ventas.diccionarioVentas[ids]['Branch'] == 'B':
            if Ventas.diccionarioVentas[ids]['Customer type'] == 'Member':
                gastosSucursales[1][0] += float(Ventas.diccionarioVentas[ids]['Total'])
            else: 
                gastosSucursales[1][1] += float(Ventas.diccionarioVentas[ids]['Total'])
        elif Ventas.diccionarioVentas[ids]['Branch'] == 'C':
            if Ventas.diccionarioVentas[ids]['Customer type'] == 'Member':
                gastosSucursales[2][0] += float(Ventas.diccionarioVentas[ids]['Total'])
            else: 
                gastosSucursales[2][1] += float(Ventas.diccionarioVentas[ids]['Total'])

    for sucursal in range(len(gastosSucursales)):
        if gastosSucursales[sucursal][0] < gastosSucursales[sucursal][1]:
            print("la sucursal {} tuvo mayores gastos de clientes no members que members".format(sucursal))
            x += 1
    if x==0:
        print('Ninguna sucursal presenta mayores ventas de no member vs member')

def CorrelacionVentasVsRatingTipoProducto():
    x=[]
    y=[]
    for ids in Ventas.diccionarioVentas.keys():
        x.append(float(Ventas.diccionarioVentas[ids]['Rating']))
        x.sort()
        y.append(float(Ventas.diccionarioVentas[ids]['Quantity']))
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