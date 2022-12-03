class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val
    def insert(self,val):
        if(val>self.val):
            if(self.right == None):
                self.right=Node(val)
            else:
                self.right.insert(val)
        elif val < self.val:
            if(self.left == None):
                self.left=Node(val)
            else:
                self.left.insert(val)

class BST:
    def __init__(self):
        self.root=None
    def insert(self,val):
        if(self.root == None): #root = raiz
            self.root = Node(val)
        else:
            self.root.insert(val)
    def buscarMinimo(self):
        if self.root != None:
            return buscarMinimo(self.root)

   
     #yo le pido el minimo al arbol, no al nodo
    
#bst es solo para soportar el arbol vacio y guardar un root vacio en algun lado

def insert2(node,val): #ver si se soluciona con @classmethod
        if node == None:
            return Node(val)
        elif val < node.val:
            node.left = insert2(node.left,val)
        elif val > node.val:
            node.right = insert2(node.right,val)
        return node

#si la variable esta gris oscuro es porque nunca la use, ahi puede que deba usar classmethod
#si la funcion la dejo fuera de la clase es un metodo de instancia

#cuando encuentro un lugar vacio, creo un nuevo nodo
# si no hay un lugar vacio no puedo insertarlo. Entonces pregunto si el valor de la izquierda es < a mi valor, voy a la derecha
# si no pondo el return node no termino de crear las lineas que unen los distinto nodos, o sea las ramas. Una funcion sin return devuelve None y no tendria ramas

#encontrar el valor mas chico de un arbol binario de busqueda
# si encuentro un nodo que no tiene nada a la izquierda entonces es el nodo con el valor mas chico
# siempre voy mirando a la izquierda:

def buscarMinimo(node): #el node que uso de parametro debe ser la raiz
    if node.left == None:
        return node.val
    else: #el else podia sacarlo y dejar el buscarMinimo(node.left) sin indentar
        return buscarMinimo(node.left) #el return este es esencial

#en el arbol se recorre la cantidad de niveles mientras que en una lista enlazada tengo que comparar todos los nodos
#por ejemplo para buscar en 30 niveles tardaria 30 iteraciones mientras que en listas enlazadads tardaria 2^31-1

# los sets son mas utiles para ver si un elemento existe en un conjunto

#TAREA:

'''
Escribir un algoritmo que dado un string que representa una serie de operaciones matematicas me devuelva la respuesta
O sea convertir la expresion en un arbol y luego resolverlo.
'''






