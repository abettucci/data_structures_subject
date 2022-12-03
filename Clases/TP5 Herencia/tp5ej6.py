import csv

class Aparato():
    def __init__(self,voltaje,precio):
        self.voltaje = voltaje
        self.precio = precio
    def calculoDescuento(aparatoVendido): #asumo que el descuento depende del aparato que se compre
        if isinstance(aparatoVendido,Televisor):
            return '15%'
        elif isinstance(aparatoVendido,EquipoDeMusica):
            return '10%'

class Televisor(Aparato): #el televisor es un aparato porque tiene voltaje y precio
    def __init__(self,voltaje,precio,tamaño):
        super().__init__(voltaje,precio)
        self.tamaño = tamaño
    def __str__(self): #imprimirTV
        return 'Televisor de {} pulgadas'.format(self.tamaño)

class EquipoDeMusica(Aparato): #el equipo de musica es un aparato porque tiene voltaje y precio
    def __init__(self,voltaje,precio,cantidadCD):
        super().__init__(voltaje,precio)
        self.cantidadCD = cantidadCD
    def __str__(self): #imprimirEquipo
        return 'El equipo de musica de {} Volts y {} CDs, cuesta ${}'.format(self.voltaje,self.precio,self.cantidadCD)

class Factura():
    listaFacturas = []

    def __init__(self, nroFact, aparatoVendido, descuento: float):
        self.nroFact = nroFact
        self.aparatoVendido = aparatoVendido
        self.descuento = descuento
        Factura.listaFacturas.append(self)

    def capturarDatos():
        with open('aparatosElectronicos.csv','r', newline='') as csvfile:
            for venta in csvfile:
                datos_ventas = venta.split(',')    
                if datos_ventas[5] == 'televisor':
                    aparato = Televisor(datos_ventas[1],datos_ventas[2],datos_ventas[3]) #el 1 es Voltaje, el 2 es precio, el 3 es tamaño o cantidad de CD es aparato
                elif datos_ventas[5] == 'equipo':
                    aparato = EquipoDeMusica(datos_ventas[1],datos_ventas[2],datos_ventas[3])
                Factura(datos_ventas[0],aparato,datos_ventas[4]) #el 0 es nro factura y el 4 es descuento, el 5 lo agregue para reconocer que aparato es

    def __str__(self): #imprimirDatos
        if isinstance(self.aparatoVendido,Televisor):
            return "{:<20} {:<30} {:<9}".format(self.nroFact,'Televisor de {} pulgadas'.format(self.aparatoVendido.tamaño),self.descuento)
        elif isinstance(self.aparatoVendido,EquipoDeMusica):
            return "{:<20} {:<30} {:<9}".format(self.nroFact,'Equipo de {} CDs'.format(self.aparatoVendido.cantidadCD),self.descuento)

    def imprimirFacturas():
        print("{:<20} {:<30} {:<9}".format('Numero de factura','Aparato Vendido','Descuento'))
        for facturas in Factura.listaFacturas:
            print(facturas)

def crearArchivo(): #Creo el csvfile
    with open('aparatosElectronicos.csv','w', newline='') as csvfile:
        csvfile.write('1' + ',' + '50' + ',' + '1000' + ',' + '30' + ',' + '15%' + ',' + 'televisor') #creo el televisor
        csvfile.write('2' + ',' + '50' + ',' + '350' + ',' + '10' + ',' + '10%' + ',' + 'equipo') #creo el equipo

if __name__ == "__main__":

    crearArchivo()
    Factura.capturarDatos()
    print('\n')
    Factura.imprimirFacturas()
    print('\n')