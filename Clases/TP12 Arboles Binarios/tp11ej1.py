'''Dado un árbol binario de búsqueda de números enteros, Implemente un método RECURSIVO que busque 
si un valor numérico dado está en el árbol binario de búsqueda'''

# escribir un metodo que determine si un determinado valor está en el arbol:

def buscarValor(node, dato):
    if dato == node.dato:
        return True
    elif dato < node.dato:
        if node.left == None:
            return False
        else:
            return buscarValor(node.left, dato)
    elif dato > node.dato:
        if node.right == None:
            return False
        else:
            return buscarValor(node.right, dato)

