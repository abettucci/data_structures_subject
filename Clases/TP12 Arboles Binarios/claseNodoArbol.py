class NodoArbol:
    #constructor
    def __init__(self,dato=None):
        self.dato=dato
        self.right=None
        self.left=None

    def agregarnodos(raiz,nodo):
        if raiz.dato<nodo.dato:
            if raiz.right==None:
                raiz.right=nodo
            else:
                NodoArbol.agregarnodos(raiz.right,nodo)
        elif raiz.dato>nodo.dato:
            if raiz.left==None:
                raiz.left=nodo
            else:
                NodoArbol.agregarnodos(raiz.left,nodo)
    def calculoAltura(self, altura):
        if self.left == None and self.right == None:
            return altura
        else:
            alturaIzq = altura
            if self.left != None:
                alturaIzq = self.left.calculoAltura(altura + 1)
            
            alturaDer = altura
            if self.right != None:
                alturaDer = self.right.calculoAltura(altura + 1)
            
            return max(alturaIzq,alturaDer)