

def verificarNumero(Numero):
    while Numero.isnumeric() == False:
        Numero = input('Se debe ingresar un numero: ').strip()
    return int(Numero)

class Camion():
    def __init__(self,CUIT):
        self.patente= input('Ingrese patente del camion: ')
        self.carga = int(input('Ingrese carga del camion: '))
        self.marca= input('Ingrese marca del camion: ')
        self.año= int(input('Ingrese año del camion: '))
        self.empresaDueña = CUIT
    def __eq__(self, otro):
        return self.carga==otro.carga and self.año==otro.año and self.patente==otro.patente
    def __str__(self):
        return('El camion de patente {}, marca {} y año {}, carga {} toneladas mensuales'.format(self.patente,
        self.marca,self.año,self.carga))

class Empresa():
    listaEmpresas = []
    i=0
    def __init__(self):
        self.nombre = input('Ingrese nombre: ')
        self.CUIT = int(input('Ingrese el CUIT: '))
        self.listaCamiones = []
        self.cantCamiones = int(input('Ingrese cantidad de camiones que posee: '))

        for i in range(self.cantCamiones):
            camion = Camion(self.CUIT)
            self.listaCamiones.append(camion)
        
        # for empresa in Empresa.listaEmpresas:
        #     if self.CUIT not in empresa.CUIT:
        Empresa.listaEmpresas.append(self)

    def __str__(self):
        return('La empresa se llama {}, el CUIT es {} y tiene {} camiones'.format(self.nombre,self.CUIT,len(self.listaCamiones)))
        
def menuInicial():
    opcionIngresada = input('''
    1. Actualizar info de la empresa
    2. Visualizar info de la empresa
    3. Ingresar nuevo camion
    4. Visualizar camiones
    5. Visualizar carga total de todos los camiones
    6. Crear empresa
    7. Salir
    Ingrese que accion desea realizar: ''')
    return opcionIngresada

def menuModificarDatos():
    opcionIngresada = input('''
    1. Modificar nombre de la empresa
    2. Modificar CUIT de la empresa
    3. Salir de modificacion de datos
    Ingrese que accion desea realizar: ''')
    return opcionIngresada
    

#Valido que se ingrese un numero
opcionIngresada = verificarNumero(menuInicial())

while opcionIngresada != 7: #Salir

    if opcionIngresada == 1: #Actualizar info de la empresa
        opcionIngresada = verificarNumero(menuModificarDatos())
        
        while opcionIngresada != 3: #Salir
            if opcionIngresada == 1: #Modificar nombre de la empresa
                empresaIngresada = int(input('Ingrese el CUIT de la empresa: ')) #uso el cuit como id unico
                for empresa in Empresa.listaEmpresas:
                    if empresa.CUIT == empresaIngresada:
                        empresa.nombre = input('Ingrese nuevo nombre de la empresa: ')
                        print('Cambios realizados:')
                        print(empresa)

            elif opcionIngresada == 2: #Modificar CUIT de la empresa
                empresaIngresada = int(input('Ingrese el CUIT de la empresa: ')) #uso el cuit como id unico
                for empresa in Empresa.listaEmpresas:
                    if empresa.CUIT == empresaIngresada:
                        empresa.CUIT = int(input('Ingrese nuevo CUIT de la empresa: '))
                        print('Cambios realizados:')
                        print(empresa)

            input('Presione cualquier letra si desea realizar otra accion ')
            opcionIngresada = verificarNumero(menuModificarDatos())

    elif opcionIngresada == 2: #Visualizar info de la empresa
        empresaIngresada = int(input('Ingrese el CUIT de la empresa: ')) #uso el cuit como id unico
        for empresa in Empresa.listaEmpresas:
            if empresa.CUIT == empresaIngresada:
                print(empresa)
        
    elif opcionIngresada == 3: #Ingresar nuevo camion
        empresaIngresada = int(input('Ingrese el CUIT de la empresa: ')) #uso el cuit como id unico
        for empresa in Empresa.listaEmpresas:
            if empresa.CUIT == empresaIngresada:
                camion = Camion(empresa.CUIT)
                empresa.listaCamiones.append(camion)

    elif opcionIngresada == 4: #Visualizar camiones
        empresaIngresada = int(input('Ingrese el CUIT de la empresa: ')) #uso el cuit como id unico
        for empresa in Empresa.listaEmpresas:
            if empresa.CUIT == empresaIngresada:
                print('La empresa {} posee los siguientes camiones:'.format(empresa.nombre))
                print('\n')
                for camiones in empresa.listaCamiones:
                    print(camiones)

    elif opcionIngresada == 5: #Visualizar carga total de todos los camiones
        empresaIngresada = int(input('Ingrese el CUIT de la empresa: ')) #uso el cuit como id unico
        for empresa in Empresa.listaEmpresas:
            if empresa.CUIT == empresaIngresada:
                cargaTotalTransportada = 0
                for camiones in empresa.listaCamiones:
                    cargaTotalTransportada += camiones.carga
        print('La carga total transportada en kgs es de: ',cargaTotalTransportada)

    elif opcionIngresada == 6: #Crear empresa
        Empresa()

    input('Presione cualquier letra si desea realizar otra accion ')
    opcionIngresada = verificarNumero(menuInicial())
