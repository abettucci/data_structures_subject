'''Implemente la clase Cola. En esta implementación el constructor de la clase es una lista. Los métodos de 
la clase Cola a implementar son: 
1) encolar
2) desencolar
3) esVacia
4) visualizar Cola
5) longitud'''

class Cola():
    def __init__(self):
        self.cola = []
    def encolar(self, valor):
        self.cola.append(valor)
    def esVacia(self):
        return self.cola == [] #devuelve un True si la cola no tiene elementos y es igual a lista vacia (==[])
    def longitud(self):
        return len(self.cola)
    def desencolar(self):
        return self.cola.pop()
    def visualizar(self):
        listaAux = []
        for i in range(len(self.cola)):
            listaAux.append(self.cola[i])
        return listaAux
    def invertir(self):
        colaAux = []
        for i in range(len(self.cola)):
            colaAux.append(self.cola.pop())
        return colaAux
    
if __name__ == "__main__":
    cola = Cola()
    invertida = []
    cola.encolar(9)
    cola.encolar(27)
    print(cola.visualizar())
    print(cola.esVacia())
    print(cola.longitud)
    print(cola.invertir())






