'''Escriba un método en la clase cola que invierte el orden de los elementos de la cola'''
class Nodo():
    def __init__(self, dato):
        self.dato = dato
        self.prox = None
 
class Cola():
    def __init__(self):
        self.inicio = self.final = None
        self.size = 0
        
    def esVacia(self):
        return self.inicio == None

    def encolar(self, nodo):
        temp = Nodo(nodo)
        if self.final == None:
            self.inicio = self.final = temp
            return
        self.final.prox = temp
        self.final = temp
        self.size += 1

    def desencolar(self):
        if self.esVacia():
            return
        temp = self.inicio
        self.inicio = temp.prox
        if(self.inicio == None):
            self.final = None
        self.size -= 1

    def visualizar(self):
        while (self.inicio != None):       
            print(str(self.inicio.dato), end = ' ')
            self.inicio = self.inicio.prox;    
        print()  

    def longitud(self):
        return self.size

    def invertir(self):
        colaAux = Cola()
        for i in range(self.longitud()):
            colaAux.encolar(self.desencolar())
        return colaAux

if __name__ == "__main__":
    cola = Cola()
    cola.encolar(9)
    cola.encolar(27)
    cola.desencolar()
    cola.encolar(32)
    cola.encolar(85)
    print(cola.esVacia())
    print(cola.visualizar())
    print(cola.longitud())
    print(cola.invertir())