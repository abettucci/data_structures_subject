
### IMPLEMETNO UNA PILA PORQUE DICE QUE LOS PLATOS RECIEN SALIDOS SE PRIORIZAN ANTES DE LOS QUE NO
### SE VINIERON A BUSCAR, POR LO QUE SEGUIRIA UN ORDEN TIPO LIFO (LAST IN FIRST OUT)

class Nodo():
    def __init__(self, dato=None, prox=None):
        self.dato = dato
        self.prox = prox
    def __str__(self) -> str:
        return str(self.dato)

class Pila():
    def __init__(self):
        self.headvalue = None
        self.len = 0
    def esVacia(self):
        if self.len == 0:
            return True
        else:
            return False
    def apilar(self, nodo: Nodo):
        nodo = Nodo(nodo)
        if (self.esVacia()):
            self.headvalue = nodo
        else:
            nodo.prox = self.headvalue
            self.headvalue = nodo
        self.len += 1
    def desapilar(self):
        if (self.esVacia()):
            print("No hay elementos para desapilar")
        else:
            nodo = self.headvalue
            self.headvalue = nodo.prox
            self.len -= 1
    def donarComidaExcedente(self,stock):
        for i in range(stock):
            Pila.desapilar(self)
    def __str__(self) -> str:
        nodo = self.headvalue
        cadena = ''
        if self.len == 0:
            return "0 pedidos"
        else:
            while (nodo != None):
                cadena += str(nodo.dato) + '\t'
                nodo = nodo.prox
            return cadena

### AL REGISTRAR UN PEDIDO, BAJA EL STOCK EN LA CANTIDAD PEDIDA Y SE APILA EN LA PILA DE PEDIDOS
def registrarPedido(stockComidas):
    producto = input('Ingrese la comida que quiere: ')
    cantidad = int(input('Ingrese la cantidad: '))
    i=0

    for i in range(cantidad): 
        pedidos.apilar(producto)
        stockComidas[producto] =  stockComidas[producto] - 1
        i -= 1
    return pedidos, stockComidas[producto]

### CREO EL MENU DEL DIA CON SU STOCK CORRESPONDIENTE CON UN DICCIONARIO

stockComidas = dict()
comidasDelDia = set()
i=0

cantidadDeComidas = int(input('Ingrese la cantidad de comidas que va a ofrecer en el dia: '))

for i in range(cantidadDeComidas):
    comidas = input('Ingrese nombre de la comida: ')
    comidasDelDia.add(comidas)

for comida in comidasDelDia:
    stock = int(input('Ingrese el stock del dia de la comida {}: '.format(comida)))
    stockComidas[comida] = stock

### REGISTRO LOS PEDIDOS DEL DIA

pedidos = Pila()
print('La pila tiene: ',pedidos)
registrarPedido(stockComidas)
print('La pila tiene los pedidos: ',pedidos)
print('El stock actual es de: \n')
for k,v in stockComidas.items():
    print(k,v)
print('\n')

#### AL FINAL DEL DIA SE HACE UN CLEAR DE LA PILA DE PEDIDOS PARA DONAR LA COMIDA
for stock in list(stockComidas.values()):
    Pila.donarComidaExcedente(pedidos, stock)

