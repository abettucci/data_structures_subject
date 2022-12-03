#from tp5ej1Clase import *

#listaEmpresas = []
listaCamiones1 = []

class Camion():
    def __init__(self, patente, carga, marca, año):
        self.patente = patente
        self.carga = carga
        self.marca = marca
        self.año= año
    def __eq__(self, otro):
        return self.carga==otro.carga and self.año==otro.año and self.patente==otro.patente
    def __str__(self):
        return('El camion de patente {}, marca {} y año {}, carga {} toneladas mensuales'.format(self.patente,
        self.marca,self.año,self.carga))

class Empresa():
    def __init__(self,nombreEmp,CUIT,cantCamiones,listaCamiones):
        self.nombreEmp = nombreEmp
        self.CUIT = CUIT
        self.cantCamiones = cantCamiones
        self.listaCamiones = []
    def __str__(self):
        return('La empresa se llama {}, el CUIT es {}, tiene {} camiones, los cuales son: '.format(self.nombreEmp,self.CUIT,self.cantCamiones,self.listaCamiones))

#class Sistema(Empresa):
#    def __init__(self, nombreEmp,CUIT,cantCamiones,listaCamiones):
#        super().__init__(self,nombreEmp,CUIT,cantCamiones,listaCamiones)
    

empresa1= Empresa(input('Ingrese nombre empresa: '),int(input('Ingrese CUIT: ')),
int(input('Ingrese cantidad de camiones que posee: ')),[])

#sistema1 = Sistema(empresa1)

# camion1 = Camion(input('Ingrese patente: '),input('Ingrese capacidad camion: '),input('Ingrese marca del camion: '),
# input('Ingrese año del camion: '))
# sistemaEmpresa.listaCamiones.append()

corriendo = True

while corriendo == True:
    opcionMenu = int(input('''
    1. Actualizar informacion de la empresa
    2. Visualizar informacion de la empresa
    3. Ingresar un nuevo camion en la empresa
    4. Visualizar cantidad de camiones de la empresa
    5. Visualizar la informacion de la carga total transportada
    6. Salir

    Elija una opcion: '''))
    if opcionMenu == 1:
        opcionActualizar = int(input('''
        
        1. Modificar nombre de la empresa
        2. Modificar CUIT de la empresa

    Elija una opcion: '''))
        if opcionActualizar == 1:
            empresaInput = input('Ingrese nombre de la empresa: ')
#            for empresas in sistemaEmpresa.listaEmp:
            if empresaInput == empresa1.nombreEmp:
                    empresa1.nombreEmp = input('Ingrese nuevo nombre de la empresa: ')
            else: print('La empresa no existe') 
        elif opcionActualizar == 2:
            if empresaInput == empresa1.nombreEmp:
                empresa1.CUIT = int(input('Ingrese nuevo CUIT de la empresa: '))
            else: print('La empresa no existe')
    elif opcionMenu == 2:
        empresaInput = input('Ingrese nombre de la empresa a visualizar: ')
        if empresaInput == empresa1.nombreEmp:
            print(empresa1.nombreEmp)
   
    elif opcionMenu == 3:
        empresaInput = input('Ingrese nombre de la empresa: ')
        n=int(input('Ingrese cantidad de camiones nuevos: '))>0
        if empresaInput == empresa1.nombreEmp:
            while n>0:
                empresa1.listaCamiones.append(Camion(input('Ingrese patente: '),input('Ingrese capacidad camion: '),input('Ingrese marca del camion: '),
                input('Ingrese año del camion: ')))
                n-=1
        else:
            print('La empresa no existe')

    elif opcionMenu == 4:
        empresaInput = input('Ingrese nombre de la empresa: ')
        if empresaInput == empresa1.nombreEmp:
            print('La empresa ',empresa1.nombreEmp,' posee ',len(empresa1.listaCamiones),' camiones')
            for camiones in empresa1.listaCamiones:
                print(camiones)
    elif opcionMenu == 5:
        empresaInput = input('Ingrese nombre de la empresa: ')
        if empresaInput == empresa1.nombreEmp:
            print('La carga total transportada: ',lambda empresa1: camiones in empresa1.listaCamiones, sum(camiones.carga))

    elif opcionMenu == 6:
        corriendo = False

