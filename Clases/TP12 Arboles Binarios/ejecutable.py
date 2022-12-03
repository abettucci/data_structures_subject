import claseNodoArbol 
import claseArbol
from tp11ej1 import *

nodo1=claseNodoArbol.NodoArbol(10)
nodo2=claseNodoArbol.NodoArbol(100)
nodo3=claseNodoArbol.NodoArbol(8)
arbol1=claseArbol.arbol(nodo1)
arbol1.agregarnodo(nodo2)
arbol1.agregarnodo(nodo3)

print("Visualizar el arbol end preorder \n")
claseArbol.arbol.preorder(arbol1.root)
print("Visualizar el arbol end inorder \n")
claseArbol.arbol.inorder(arbol1.root)
print("Visualizar el arbol end postorder \n")
claseArbol.arbol.posorden(arbol1.root)
print('El numero 8 está en el arbol?',buscarValor(arbol1.root, 8))
print('El numero 5 está en el arbol?',buscarValor(arbol1.root, 5))