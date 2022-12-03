'''Implemente un método RECURSIVO que calcule la altura de un árbol binario de búsqueda'''

#deberiamos ver la cantidad de niveles que tiene el arbol recorriendo cada rama


import claseNodoArbol 
import claseArbol

nodo1=claseNodoArbol.NodoArbol(10)
nodo2=claseNodoArbol.NodoArbol(100)
nodo3=claseNodoArbol.NodoArbol(8)
nodo4=claseNodoArbol.NodoArbol(7)
arbol1=claseArbol.arbol(nodo1)
arbol1.agregarnodo(nodo2)
arbol1.agregarnodo(nodo3)
arbol1.agregarnodo(nodo4)
print('La altura del arbol es {}'.format(claseNodoArbol.NodoArbol.calculoAltura(nodo1,0)))