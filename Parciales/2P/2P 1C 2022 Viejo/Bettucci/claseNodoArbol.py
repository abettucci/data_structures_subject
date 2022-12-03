from datetime import datetime
from claseVentas import *
from utilitarios import convertirFechayHoraANumero

class NodoArbol:
    #constructor
    def __init__(self,dato=None):
        self.dato=dato
        self.right=None
        self.left=None

    def agregarnodos(raiz,nodo):
        if float(convertirFechayHoraANumero(raiz.dato.date+' '+raiz.dato.time)) < float(convertirFechayHoraANumero(nodo.dato.date+' '+nodo.dato.time)):
            if raiz.right==None:
                raiz.right=nodo
            else:
                NodoArbol.agregarnodos(raiz.right,nodo)
        elif float(convertirFechayHoraANumero(raiz.dato.date+' '+raiz.dato.time)) > float(convertirFechayHoraANumero(nodo.dato.date+' '+nodo.dato.time)):
            if raiz.left==None:
                raiz.left=nodo
            else:
                NodoArbol.agregarnodos(raiz.left,nodo)