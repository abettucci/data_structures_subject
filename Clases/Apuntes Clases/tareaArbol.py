
class NodoArbol:
    def __init__(self,dato=None):
        self.dato=dato
        self.right=None
        self.left=None
    def agregarIzquierda(raiz,nodo):
        if raiz.left==None:
            raiz.left=nodo
        else:
            NodoArbol.agregarIzquierda(raiz.left,nodo)
    def agregarDerecha(raiz,nodo):
        if raiz.right==None:
            raiz.right=nodo
        else:
            NodoArbol.agregarIzquierda(raiz.right,nodo)

class Pila():
    def __init__(self):
        self.headvalue = None
        self.len = 0
    def esVacia(self):
        if self.len == 0:
            return True
        else:
            return False
    def apilar(self, nodo: NodoArbol):
        nodo = NodoArbol(nodo)
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

class BST:
    def __init__(self):
        self.root=None
    def insert(self,val):
        if(self.root == None):
            self.root = NodoArbol(val)
        else:
            self.root.insert(val)

class Arbol:
    def __init__(self,nodo=None):
        self.root=nodo
    def agregarnodoIzquierda(self,nodo):
            root=self.root
            NodoArbol.agregarIzquierda(root,nodo)
    def agregarnodoDerecha(self,nodo):
            root=self.root
            NodoArbol.agregarDerecha(root,nodo)
    def setearRaiz(self,nodo):
        if self.root == None:
            self.root = nodo
    def verHijoIzquierdo(nodo):
        if(nodo):
            Arbol.verHijoIzquierdo(nodo.left)
            print(nodo.dato)
    def verHijoDerecho(nodo):
        if(nodo):
            Arbol.verHijoDerecho(nodo.right)
            print(nodo.dato)

def calculo(Arbol):
    caracteres = ([*expresion])
    pila = Pila()    
    for caracter in caracteres:
        if caracter == '(':
            Arbol.agregarnodoIzquierda('')
            pila.apilar(NodoArbol)
            Arbol = Arbol.verHijoIzquierdo()
        elif caracteres in ['+', '-', '*', '/']:
            Arbol.setearRaiz(caracter)
            Arbol.agregarnodoDerecha('')
            pila.apilar(NodoArbol)
            Arbol = Arbol.verHijoDerecho()
        elif caracter == ')':
            Arbol = pila.pop()
        elif caracter not in ['+', '-', '*', '/', ')']:
            try:
                Arbol.setearRaiz(int(caracter))
                padre = pila.pop()
                Arbol = padre
            except ValueError:
                raise ValueError("token '{}' is not a valid integer".format(caracter))
    return Arbol

expresion = '((7+3)*/5-2))'

nodo1=NodoArbol('*')
nodo2=NodoArbol(2)
nodo3=NodoArbol('+')
nodo4=NodoArbol(7)
nodo5=NodoArbol(3)
arbol1=Arbol(nodo1)

resolucion = calculo(arbol1)
print(resolucion)




