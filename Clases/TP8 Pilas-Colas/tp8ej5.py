'''Escriba un método en la clase pila que transfiere los datos de una a la otra, se debe mantener el ordende 
ellas'''

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

    def __str__(self) -> str:
        nodo = self.headvalue
        cadena = ''
        if self.len == 0:
            return "Lista vacia"
        else:
            while (nodo != None):
                cadena += str(nodo.dato) + '\t'
                nodo = nodo.prox
            return cadena

    def longitud(self):
        return self.len

    def transferir(self, pila2):
        pila2 = Pila()
        for i in range(self.longitud()):
            print('Pila1: ',self)
            print('Pila2: ',pila2)
            pila2.apilar(self.desapilar())
            print('Pila1: ',self)
            print('Pila2: ',pila2)
        return pila2
        
if __name__ == "__main__":
    pila = Pila()
    pila.apilar(8)
    pila.apilar(88)
    pila.apilar(881)
    pila.desapilar()
    #print('Pila: ',pila)
    #print('Longitud: ',pila.longitud())
    #print('Pila vacia? ',pila.esVacia())
    pila2 = Pila()
    pila.transferir(pila2)
    print('Pila inicial: ',pila)
    print('Pila2 :',pila2)