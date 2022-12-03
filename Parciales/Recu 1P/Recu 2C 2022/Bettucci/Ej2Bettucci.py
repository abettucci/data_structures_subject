'''
El sistema debe almacenar los productos pasados por el escáner, de cada producto se almacena lacantidad 
llevada, el precio, el nombre del producto y su código (único). El precio ya viene con losimpuestos incluido

El programa le debe permitir al empleado que maneja el sistema ver el valor total de cada venta,además mostrar 
el ticket con todo lo vendido incluyendo el precio final de la compra como se hace entodos los kioscos.

Adicionalmente en cualquier momento el vendedor puede visualizar el monto total que ha vendido hasta ese momento 
el kiosco
'''
from random import randint

class Producto():
    listaProductos = []

    def __init__(self,precio,SKU,nombre):
        self.precio = precio
        self.SKU = SKU #validar que sea único
        self.nombre = nombre #una descripcion amigable del producto
        Producto.listaProductos.append(self)

    def __str__(self):
        return 'El producto {} corresponde a {} y cuestan {} $/u'.format(self.SKU,self.nombre,self.precio)

class Orden():
    listaOrdenes = []
    
    def __init__(self,codigoDeOrden):
        self.codigoDeOrden = codigoDeOrden
        self.listaVentas = []
        self.SubtotalOrden = 0

        Orden.listaOrdenes.append(self)
    
    def __str__(self):
        Total = 0
        print('\n','Numero de orden: ',self.codigoDeOrden,'\n')
        print("{:<10} {:<13} {:<8} {:<8}".format('Producto', 'Cantidad', 'Precio','Total'))
        for ventas in self.listaVentas:
            print(ventas)
            self.SubtotalOrden += ventas.subtotal
        return "{:<10} {:<10}".format('Total', self.SubtotalOrden)

    def verVentasTotales():
        ventaDelDia = 0
        for orden in Orden.listaOrdenes:
            ventaDelDia += orden.SubtotalOrden
        return 'El total de ventas hasta el momento del dia es de ${}'.format(ventaDelDia)

class Venta():
    def __init__(self,producto,cantidad):
        self.cantidad = cantidad
        self.producto = producto
        self.subtotal = self.cantidad*self.producto.precio

    #Visualizar valor total de cada ticket
    def __str__(self):
        return '{:<10} {:<13} {:<8} {:<8}'.format(self.producto.nombre ,self.cantidad,self.producto.precio,self.subtotal)
        
########### MAIN ###############

### PRESENTO EL CATALOGO DE PRODUCTOS ###

producto1 = Producto(300,'ABC123','calzas')
producto2 = Producto(200,'ABC124','aretes')
producto3 = Producto(250,'AB125','pinta uñas')

print('Productos disponibles:')
print('\n')
for producto in Producto.listaProductos:
    print(producto)
print('\n')

### GENERO UNA ORDEN DE X PRODUCTOS ###

cantidadOrdenes = int(input('Cantidad de ordenes del dia: '))

for i in range(cantidadOrdenes):

    codigoOrden = randint(1,10000)
    orden = Orden(codigoOrden)

    cantidadDeProductosUnicos = int(input('Ingrese cuantos productos distintos lleva: '))

    for i in range(cantidadDeProductosUnicos):
        productoIngresado = input('Ingrese nombre del producto: ').lower().strip()
        for producto in Producto.listaProductos:
            if producto.nombre == productoIngresado:
                venta = Venta(producto,int(input('Ingrese cantidad que lleva: ')))
                orden.listaVentas.append(venta)
    print(orden)

print(Orden.verVentasTotales())


