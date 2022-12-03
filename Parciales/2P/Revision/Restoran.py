class Restaurante():
    stock = dict()
    Pedidos = Cola()
    PedidosListos = Pila()

    def agregarStock(producto,cantidad):
        Restaurante.stock.setdefault(producto)
        # hace "if producto not in stock -> prod[stock]=0, luego prod[stock] += cantidad"
    
    def cerrarRestaurante():
        #reincia el stock
        stock = dict()
    
    # los productos mas recientes son los que salen primero -> retiros = pila
    # los pedidos son registran en una cola en un cajero -> pedidos = cola

    # en teoria habria que hacer un diccionario de  k=producto , v=cantidad

    def pedir(producto,cantidad):
        #chequear que alcance el stock para suplir el pedido
        Pedidos.encolar(producto,encolar)

    def cocinar():
        pedido = Pedidos.desencolar()
        #(producto,cantidad) = Cola.desencolar()
        # luego de cocinar (desencolar), se apila lo cocinado
        PedidosListos.apilar(pedido)
    
    def retirar():
        PedidosListos.desapilar()
