from claseNodoArbol import *
from utilitarios import convertirFechayHoraANumero

class arbol:
    def __init__(self,nodo=None):
        self.root=nodo
    
    # Mostrar el arbol en preorden
    def preorder(nodo):
        if nodo:
            print(nodo.dato)
            arbol.preorder(nodo.left)
            arbol.preorder(nodo.right)
    
    # Mostrar el arbol en inorden
    def inorder(nodo):
        if(nodo):
            arbol.inorder(nodo.left)
            print(nodo.dato)
            arbol.inorder(nodo.right)

    # Mostrar el arbol en postorden
    def posorden(nodo):
        if nodo:
            arbol.posorden(nodo.left)
            arbol.posorden(nodo.right)
            print(nodo.dato)

    # agregar al arbol
    def agregarnodo(self,nodo):
        if self.root==None:
            root=nodo
        else:
            root=self.root
            NodoArbol.agregarnodos(root,nodo)

    # imprimir los nodos que tengan un dato mayor al dato del nodo Fecha
    def filtrarRegistrosPosterioresAFecha(nodo,fecha): #el primer nodo que le paso por parametro es la raiz
        if (nodo):
            arbol.filtrarRegistrosPosterioresAFecha(nodo.left,fecha)
            if int(convertirFechayHoraANumero(nodo.dato.date+' '+nodo.dato.time)) > int(convertirFechayHoraANumero(fecha)):
                print("La venta {} con fecha {} es posterior a la fecha dato {}".format(nodo.dato.invoiceID,nodo.dato.date,fecha))
            arbol.filtrarRegistrosPosterioresAFecha(nodo.right, fecha)

    # imprimir los nodos que tengan un dato menor al dato del nodo Fecha
    def filtrarRegistrosPreviosAFecha(nodo,fecha): #el primer nodo que le paso por parametro es la raiz
        if (nodo):
            arbol.filtrarRegistrosPreviosAFecha(nodo.left,fecha)
            if int(convertirFechayHoraANumero(nodo.dato.date+' '+nodo.dato.time)) < int(convertirFechayHoraANumero(fecha)):                
                print("La venta {} con fecha {} es previa la fecha dato {}".format(nodo.dato.invoiceID,nodo.dato.date,fecha))
            arbol.filtrarRegistrosPreviosAFecha(nodo.right, fecha)

    def visualizarVentasDeRecienteAAntiguo(nodo):
        if (nodo):
            arbol.visualizarVentasDeRecienteAAntiguo(nodo.left)
            print("La fecha {} corresponde con la venta {}".format(nodo.dato.date,nodo.dato.invoiceID))
            arbol.visualizarVentasDeRecienteAAntiguo(nodo.right)
        
    def visualizarVentasDeAntiguoAReciente(nodo):
        if (nodo):
            arbol.visualizarVentasDeRecienteAAntiguo(nodo.right)
            print("La fecha {} corresponde con la venta {}".format(nodo.dato.date,nodo.dato.invoiceID))
            arbol.visualizarVentasDeRecienteAAntiguo(nodo.left)
        