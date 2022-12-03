class Pedido():
    ids = set()
    totalTotal = 0
    def __init__(self, catalogo, pedido, id):
        self.catalogo = catalogo
        self.pedido = pedido
        self.id = id
        self.total = 0
        
        # aca habia que validar que no sea repetido el id de pedido
        
        if id in Pedido.ids:
            raise ValueError ("El ID de pedido ya existe")
        
        #tambien habia que validar que el articulo elegido en el pedido, se encuentre en el catalogo

        for articulo in pedido.keys():
            if articulo not in catalogo.keys(): #el .keys() puedo no ponerlo tambien, se puede obviar
                raise ValueError ("El pedido no se encuentra en el catalogo")

        # el precio total era un atributo de la clase Pedido

        Pedido.ids.add(id)
        Pedido.totalTotal += self.total


    def total(self):
        for articulo, cant in self.pedido.items():
            self.total += cant*self.catalogo[articulo]
    
    def calcularPromedio(self):
        # el len(Pedido.ids) es la longitud del set, o sea la cantidad de pedidos
        return Pedido.totalTotal/len(Pedido.pedido.ids)
