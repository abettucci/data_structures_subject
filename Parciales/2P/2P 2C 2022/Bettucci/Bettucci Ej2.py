'''
Generen un programa que construya un árbol binario a partir de su representación postfija 
guardada en un archivo y verifique que el árbol creado sea un árbol binario de búsqueda
'''

import csv

#patharchivo = input('Ingrese ruta del archivo: ')

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
class NodoArbol:
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

### CREO EL ARCHIVO CON EL EJEMPLO, ASUMO QUE EL ARCHIVO QUE SE RECIBE ES UN CSV
caracteres = []

with open('postfija.csv','w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow('((5+2)-9)*3')

### LEO EL ARCHIVO CON EL EJEMPLO Y GUARDO CADA NODO.DATO EN LA LISTA CARACTERES

with open('postfija.csv','r') as csvfile:
    reader = csv.reader(csvfile)
    for linea in reader:
        caracteres.append(linea)

expresion = ''.join(caracteres[0])

print(expresion)


