'''Realizar un programa que permita mantener actualizada la información de los diferentes hoteles que forman 
parte de la cadena de hoteles “Estructuras y nada más”. De cada Hotel se deben mantener actualizados los 
atributos nombre(string),idHotel (int), zona(string), y precio (int).

Las zonas donde podrán estar los hoteles son: "playa", "montaña" o "rural". 

El precio por noche supondremos que es un dato en euros que podrá tomar valores entre 40 y 150.

Los id de los hoteles son únicos e irrepetibles, para el almacenamiento de los hoteles deberá usar un conjunto.

El programa realizará las siguientes tareas:

1. Carga de Data
2. Visualización de los hoteles que tiene la cadena de hoteles
3. Dada una zona por el usuario mostrar los hoteles disponibles y el precio por noche'''

zonas = ['playa','montaña','rural']
conjuntoHoteles = set()
ids = set()

class Hotel():
    def __init__(self,nombre,idHotel,zona,precio):
        self.nombre = nombre
        self.idHotel = idHotel
        self.zona = zona
        self.precio = precio
    def __str__(self):
        return ('El hotel {} tiene el ID {}, esta ubicado en zona {} y cuesta {} pesos la noche').format(self.nombre, self.idHotel,self.zona,self.precio)
    
def cargarHotel():
    nombreHotel = input('Ingrese nombre del hotel: ')
    idhotel = input('Ingrese el id del hotel: ')

    while idhotel.isnumeric() == False:
        idhotel=input('Ingrese un id numerico: ')
    idhotel=int(idhotel)
    while idhotel in ids:
        idhotel = input('Ingrese un id no repetido: ')

    zona = input("Ingrese zona ubicada del hotel: ")
    
    while zona not in zonas:
        zona=input('Ingrese zona ubicada del hotel valida: ')
    
    precio = input('Ingrese precio por noche del hotel: ')

    while precio.isnumeric() == False:
        precio=input('Ingrese un precio numerico: ')
    precio=int(precio)

    while precio > 150 or precio < 40:
        precio=input('Ingrese precio por noche del hotel entre 40 y 150: ')
        while precio.isnumeric() == False:
            precio=input('Ingrese un precio numerico: ')
        precio=int(precio)

    hotel = Hotel (nombreHotel,idhotel,zona,precio)
    ids.add(idhotel)
    conjuntoHoteles.add(hotel)
    return hotel

def mostrarHotelesyPrecios(zonaInput):
    listaHoteles = set()
    for hoteles in conjuntoHoteles:
        if hoteles.zona == zonaInput:
            listaHoteles.add(hoteles)
    if len(listaHoteles) != 0:
        print('Hoteles en la zona',zonaInput)
        for hoteles in listaHoteles:
            print('\n','Hotel: ',hoteles.nombre, '\t','Precio: ', hoteles.precio)

def menu():
    opcionIngresada = input('''
        1. Cargar data del hotel
        2. Visualizar hoteles
        3. Mostrar hoteles disponibles y precios por zona
        4. Finalizar
        Ingrese que accion desea realizar: ''')
    corriendo = True
    while corriendo == True:
        while opcionIngresada.isnumeric() == False:
            print("\nIngrese un numero\n")
            opcionIngresada = input('Ingresar una opcion nuevamente: ')   
        opcionIngresada = int(opcionIngresada)
        if opcionIngresada == 1:
            cargarHotel()
            opcionIngresada=input('Ingrese una nueva accion: ')
        elif opcionIngresada == 2:
            visualizarHoteles()
            opcionIngresada=input('Ingrese una nueva accion: ')
        elif opcionIngresada == 3:
            zonaInput = input('Ingrese la zona buscado: ')
            mostrarHotelesyPrecios(zonaInput)
            opcionIngresada=input('Ingrese una nueva accion: ')
        elif opcionIngresada == 4:
            corriendo = False
        else:
            print('\n Ingrese un numero valido \n')
 
def visualizarHoteles():
    for hoteles in conjuntoHoteles:
        print(hoteles)

menu()
