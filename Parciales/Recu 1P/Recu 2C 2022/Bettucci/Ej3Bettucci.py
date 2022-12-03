import matplotlib.pyplot as plt

# Si la ruta es nacional es camioneta y si la ruta es internacional es camion?

class Vehiculo():
    
    listaVehiculosNacionales = []
    listaVehiculosInternacionales = []

    # Constructor de vehiculos
    def __init__(self,patente,carga,tipoRuta):
        self.patente = patente
        self.carga = carga
        self.tipoRuta = tipoRuta
        #Validaciones -> (tipoRuta.lower() in ['internacionl','nacional'])
        
        if self.tipoRuta.lower() == 'nacional':
            Vehiculo.listaVehiculosNacionales.append(self) #agrego el vehiculo a la lista de vehiculos cuando lo creo
        else:
            if self.tipoRuta.lower() == 'internacional':
                Vehiculo.listaVehiculosInternacionales.append(self)

    # Visualizar el vehiculo
    def __str__(self):
        return 'Vehiculo con patente {}, carga transportada de {} ton y viajes por ruta {}'.format(self.patente,self.carga,self.tipoRuta)

class Empleados():

    listaEmpleados = []
    #Constructor de objetos empleado
    def __init__(self,nombre, apellido ,DNI,puesto):
        self.nombre = nombre
        self.apellido = apellido
        self.DNI = DNI
        self.puesto = puesto

        #Validaciones (DNI no repetido, etc)
        Empleados.listaEmpleados.append(self)

#Considero que el piloto y copiloto son una extension de la clase empleado de la empresa de transporte
class Piloto(Empleados):
    def __init__(self, nombre, apellido, DNI, puesto, tipoLicencia):
        super().__init__(nombre, apellido, DNI, puesto)
        self.tipoLicencia = tipoLicencia

    def __str__(self):
        return 'El empleado {} {} de DNI {}, ocupa el puesto de {} y posee {} licencias'.format(self.nombre,self.apellido,self.DNI,self.puesto,self.tipoLicencia)

class Copiloto(Empleados):
    def __init__(self, nombre, apellido, DNI, puesto):
        super().__init__(nombre, apellido, DNI, puesto)

    def __str__(self):
        return 'El empleado {} {} de DNI {}, ocupa el puesto de {}'.format(self.nombre,self.apellido,self.DNI,self.puesto)
    
    def entregarPedidos():
        return None

def conocerCantVehiculosPorRuta(ruta):
    while ruta.lower().strip() not in ['nacional','internacional']:
        ruta = input('Ingrese una ruta valida entre Nacional o Internacional: ')
    if ruta == 'nacional':
        print('La cantidad de vehiculos que poseen ruta nacional son: ',len(Vehiculo.listaVehiculosNacionales))
    else:
        print('La cantidad de vehiculos que poseen ruta internacional son: ',len(Vehiculo.listaVehiculosInternacionales))

def visualizarVehiculosConMasDeXToneladas(limiteInferior):  

    vehiculosConCargaMayorALimite = []

    for vehiculos in Vehiculo.listaVehiculosInternacionales:
        if vehiculos.carga > limiteInferior:
           vehiculosConCargaMayorALimite.append(vehiculos)

    for vehiculos in Vehiculo.listaVehiculosNacionales:
        if vehiculos.carga > limiteInferior:
            vehiculosConCargaMayorALimite.append(vehiculos)        
    
    plt.title(label="Cantidad de vehiculos con carga mayor a {} toneladas".format(limiteInferior), fontsize=15, color='black')
    plt.xlabel('Carga')
    plt.ylabel('Cantidad de vehiculos')
    plt.bar(limiteInferior, len(vehiculosConCargaMayorALimite), color='green', width=0.5)
    plt.show()
    
def visualizarVehiculosConMenosDeXToneladas(limiteSuperior):
    vehiculosConCargaMenorALimite = []

    # print('Vehiculos con ruta Internacional con carga mayor a {} toneladas'.format(limite))
    for vehiculos in Vehiculo.listaVehiculosInternacionales:
        if vehiculos.carga < limiteSuperior:
           vehiculosConCargaMenorALimite.append(vehiculos)

    for vehiculos in Vehiculo.listaVehiculosNacionales:
        if vehiculos.carga < limiteSuperior:
            vehiculosConCargaMenorALimite.append(vehiculos)        
    
    plt.title(label="Cantidad de vehiculos con carga menor a {} toneladas".format(limiteSuperior), fontsize=15, color='black')
    plt.xlabel('Carga')
    plt.ylabel('Cantidad de vehiculos')
    plt.bar(limiteSuperior, len(vehiculosConCargaMenorALimite), color='green', width=0.5)
    plt.show()

vehiculo = Vehiculo('ac541ur',11,'nacional')
vehiculo2 = Vehiculo('ac652as',12,'internacional')
vehiculo3 = Vehiculo('acd123',6,'nacional')
piloto = Piloto('agustin','bettucci',40635013,'conductor',3) #3 licencias posee

#print(piloto)
# visualizarVehiculosConMasDeXToneladas(10)
# visualizarVehiculosConMenosDeXToneladas(10)
##conocerCantVehiculosPorRuta('internacional')
#conocerCantVehiculosPorRuta('nacional')
#conocerCantVehiculosPorRuta('interacional')