#asumo una persona puede tener solo una cuenta bancaria

class Persona():
    conjuntoCuentas = set()
    conjuntoDNI = set()
    listaPersonas = []

    def __init__(self):
        self.nombreCompleto = input('Ingrese nombre y apellido del cliente: ')
        self.DNI = validarDNI(input('Ingrese el DNI del cliente: ')) #valores unicos
        self.genero = input('Ingrese sexo del cliente: ')
        self.CBU = validarCBU(input('Ingrese CBU del cliente: ')) #valores unicos
        self.listaTransacciones = []

        Persona.conjuntoCuentas.add(self.CBU)
        Persona.conjuntoDNI.add(self.DNI) 
        Persona.listaPersonas.append(self)

    def __str__(self):
        return "\nNombre y apellido: {}\n DNI: {}\n Genero: {}\n CBU: {}".format(self.nombreCompleto,self.DNI,self.genero,self.CBU)
    
    def visualizarDatosTitularCuenta(DNIinput):
       for persona in Persona.listaPersonas:
            for DNIinput in Persona.conjuntoDNI:
                if DNIinput == persona.DNI:
                    print(persona)

    def visualizarBalanceCuenta(DNIinput):
        return

    def visualizarTransaccionesDeCuenta(DNIinput):
        for persona in Persona.listaPersonas:
            for DNIinput in Persona.conjuntoDNI:
                if DNIinput == persona.DNI:
                    for tx in persona.listaTransacciones:
                        print(tx)


class Transaccion():

    def __init__(self,CBUcuenta,tipoTransaccion,monto):
        self.CBUcuenta = CBUcuenta  # CBU de la persona
        self.tipoTransaccion = tipoTransaccion #DEPOSITO O RETIRO
        self.monto = monto

        for persona in Persona.listaPersonas:
            for self.CBUcuenta in Persona.conjuntoCuentas:
                if self.CBUcuenta == persona.CBU:
                    persona.listaTransacciones.append(self)
        
    def __str__(self):
        return "Transaccion del tipo {} por {} pesos a la cuenta {}".format(self.tipoTransaccion,self.monto,self.CBUcuenta)
        

def validarCBU(CBU):
    while CBU in Persona.conjuntoCuentas:
        CBU = input('Ingrese un CBU no existente: ')
    return int(CBU)

def validarDNI(DNI):
    while DNI in Persona.conjuntoDNI or DNI.isnumeric() == False:
        DNI = input('Ingrese un DNI numerico y no repetido: ')
    return int(DNI)

def ingresoDNI():
    DNIinput = input('Ingrese DNI a consultar transacciones: ')
    while DNIinput.isnumeric() == False:
        DNIinput = input('Ingrese un DNI valido: ')
    return int(DNIinput)

def menu():
    opcionIngresada = input('''
        1. Realizar una transaccion
        2. Visualizar balance de la cuenta
        3. Visualizar datos del titular de cuenta
        4. Visualizar transacciones de la cuenta
        5. Salir

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

juan = Persona()

opcionIngresada = 0
corriendo = True
while corriendo == True:
    try: 
        opcionIngresada = int(input('''
        1. Realizar una transaccion
        2. Visualizar balance de la cuenta
        3. Visualizar datos del titular de cuenta
        4. Visualizar transacciones de la cuenta
        5. Salir

        Ingrese que accion desea realizar: '''))
    except ValueError:
        input("Por favor seleccione un valor valido.\n Precione Enter para continuar: ")

    if opcionIngresada == 1:
        CBU = input('Ingrese CBU al cual tranfiere: ')
        while CBU.isnumeric() == False:
            CBU = input('Por favor ingrese un valor numerico: ')
        CBU = int(CBU)
        tipoOperacion = input('Ingrese el tipo de operacion a realizar (retiro/deposito):  ').lower().strip()
        while tipoOperacion not in ['retiro','deposito']:
            tipoOperacion = input('Ingrese nuevamente una de las opciones (retiro/deposito): ')

        monto = input('Ingrese el monto de la transaccion: ')
        while monto.isnumeric() == False:
            monto = input('Ingrese un valor numerico: ')
        monto = float(monto)

        tx = Transaccion(CBU, tipoOperacion, monto)

        input("Presione Enter para continuar: ")

    elif opcionIngresada == 2:
        Persona.visualizarBalanceCuenta(ingresoDNI())
        input("Presione Enter para continuar: ")

    elif opcionIngresada == 3:
        Persona.visualizarDatosTitularCuenta(ingresoDNI())
        input("Presione Enter para continuar: ")

    elif opcionIngresada == 4:
        Persona.visualizarTransaccionesDeCuenta(ingresoDNI())
        input("Presione Enter para continuar: ")

    elif opcionIngresada == 5:
        corriendo = False
    else:
        print('\n Ingrese un numero valido \n')
        input('Ingrese una nueva accion: ')
        menu()

