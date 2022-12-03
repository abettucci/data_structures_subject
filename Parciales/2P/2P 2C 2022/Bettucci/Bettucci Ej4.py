class Pedido():
    conjuntoPedidos = set()
    conjuntoIDs = set()

    def __init__(self,ID,catalogo,pedido):
        self.ID = ID
        self.catalogo = catalogo
        self.pedido = pedido
        self.montoTotal = Pedido.precioTotal(self)
        Pedido.conjuntoPedidos.add(self)

    def __str__(self):
        return "Pedido numero {} con productos: {} y monto total {}".format(self.ID,verProductos(self),self.montoTotal)

    def precioTotal(pedido):
        sumaPrecio = 0
        for producto in pedido.pedido.keys():
            if producto in list(pedido.pedido.keys()):
                sumaPrecio += pedido.catalogo[producto]*pedido.pedido[producto]
        return sumaPrecio

    def calcularPrecioPromedio():
        sumaPrecios = 0
        cantidadPedidos = 0
        for pedido in Pedido.conjuntoPedidos:
            sumaPrecios += pedido.montoTotal
            cantidadPedidos += 1
        return 'El precio promedio total es: {}'.format(sumaPrecios/cantidadPedidos)

def verProductos(pedido):
    for k,v in pedido.pedido.items():
        return(k,v)

pedidos = dict()

### CREO EL PEDIDO
ID = 1
if not Pedido.conjuntoPedidos:
    ID = 1
else:
    ID += 1

### CATALOGO DE PRUEBA
catalogo = {'Pan':50, 'Queso':100}

cantidadProductos = input('Ingrese cantidad de productos diferentes a ordenar: ')
while cantidadProductos.isnumeric() == False:
    cantidadProductos = input('Ingrese un valor numerico: ')

for i in range(int(cantidadProductos)):
    producto = input('Ingrese nombre del producto: ').capitalize()
    cantidad = input('Ingrese unidades a comprar del producto: ')
    while cantidad.isnumeric() == False:
        cantidad = input('Ingrese un valor numerico: ')
    pedidos[producto] = int(cantidad)

Pedido(ID, catalogo, pedidos)
print(Pedido.calcularPrecioPromedio())
