### PLATAFORMA MASIVA DE LIBROS ###

### IMPLEMENTACION LISTA ENLAZADA ###

class Node:
    # Constructor para inicializar un nuevo nodo
    def __init__(self, data):
        self.data = data
        self.next = None
 
    def getNode(value):
        # allocating space
        newNode = Node(value)
        return newNode

class LinkedList:
    # Funcion para inicializar el puntero
    def __init__(self):
        self.head = None
        self.len = 0
 
    # Funcion para insertar un nodo al principio de la lista
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
        self.len += 1
 
    # Dada una referencia al puntero de la lista y un valor, eliminar la primer ocurrencia del valor de la lista enlazada
    def deleteNode(self, key):
        # Store head node
        temp = self.head
        # If head node itself holds the key to be deleted
        if (temp is not None):
            if (temp.data == key):
                self.head = temp.next
                temp = None
                return
        # Search for the key to be deleted, keep track of the previous node as we need to change 'prev.next'
        while(temp is not None):
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        # if key was not present in linked list
        if(temp == None):
            return
        # Unlink the node from linked list
        prev.next = temp.next
        temp = None
        self.len -= 1

    # Funcion para imprimir la lista enlazada
    def printList(self):
        temp = self.head
        if self.len == 0:
            print('La lista es vacia')
        else:
            while(temp):
                print (temp.data)
                temp = temp.next
    
    def printCalificacionesMayorA(self,calificacion):
        temp = self.head
        if self.len == 0:
            print('La lista es vacia')
        else:
            if (temp.data.calificacionPromedio > calificacion):
                print (temp.data)
                temp = temp.next

    # Funcion para agregar un nodo despues de una determinado nodo pasado como parametro
    def insertAfter(self, prev_node, new_data):
 
    # 1. Check if the given prev_node exists
        if prev_node is None:
            print('The given previous node must in LinkedList.')
            return
    
        # 2. Create new node &
        # 3. Put in the data
        new_node = Node(new_data)
    
        # 4. Make next of new Node as next of prev_node
        new_node.next = prev_node.next
    
        # 5. make next of prev_node as new_node
        prev_node.next = new_node

    # Funcion para agregar un nodo en una posicion determinada de la lista enlazada
    def insertPos(headNode, position, data): 
        head = headNode
        # This condition to check whether the position given is valid or not.
        if (position < 1):        
            print("Invalid position!")
        if position == 1:
            newNode = Node(data)
            newNode.nextNode = headNode
            head = newNode   
        else:
            # Keep looping until the position is zero
            while (position != 0):           
                position -= 1
                if (position == 1):
                    # adding Node at required position
                    newNode = Node.getNode(data)
                    # Making the new Node to point to the old Node at the same position
                    newNode.nextNode = headNode.nextNode
                    # Replacing headNode with new Node to the old Node to point to the new Node
                    headNode.nextNode = newNode
                    break  
                headNode = headNode.nextNode
                if headNode == None:
                    break            
            if position != 1:
                print("position out of range")        
        return head  

### IMPLEMENTACION CLASE LIBRO ###
class Libro():
    listaLibros = []
    listaCalificaciones = []

    def __init__ (self,titulo,autor,ISBN):
        self.titulo = titulo
        self.autor = autor
        self.ISBN = ISBN
        self.listaReseñas = []
        self.listaCalificaciones = []
        self.calificacionPromedio = 0
        #AGREGAR VALIDACIONES
        Libro.listaLibros.append(self)
        Libro.listaCalificaciones.append(self)
        llist.push(self)

    def agregarReseña(libroInput,reseña,calificacion):
        for libro in Libro.listaLibros:
            if libroInput == libro.titulo:
                libro.listaReseñas.append(reseña)
                libro.listaCalificaciones.append(calificacion)
                libro.calificacionPromedio = float(sum(libro.listaCalificaciones)/len(libro.listaCalificaciones))

    def __str__(self):
        return 'El libro "{}" del autor {}, tiene el codigo {} y una calificacion promedio de {} con {} reseñas'.format(self.titulo,self.autor,self.ISBN,self.calificacionPromedio,len(self.listaReseñas))

class User(): #puedo sacar una cant de reseñas de cada usuario si lo creo como una clase
    def __init__(self,nombre):
        self.nombre = nombre
        self.reseñas = []
        self.calificaciones = []

    def reseñar(self):
        libro = input('Ingresar libro a dejar reseña: ')
        reseña = input('Ingrese su reseña (texto): ')
        self.reseñas.append(reseña)
        calificacion = int(input('Ingrese calificacion del libro (nota): '))
        self.calificaciones.append(calificacion)
        Libro.agregarReseña(libro,reseña,calificacion)

def verLibrosDisponibles():
    for libro in Libro.listaCalificaciones:
        print(libro)

def verLibrosConCalificacionMayorA(calificacion):
    # Libro.listaCalificaciones.sort(key=lambda x: x.calificacionPromedio,reverse=True)

    LinkedList.printCalificacionesMayorA(llist,calificacion)
    
    # for libro in Libro.listaLibros:
    #     if libro.calificacionPromedio < calificacion: 
    #         llist.deleteNode(libro)
    # print('\n')
    # print('Lista filtrada:')
    # llist.printList()

    # print('\n')
    # print('Libro con calificacion mayor a', calificacion, ':')
    # print('\n')
    # for libro in Libro.listaCalificaciones:
    #     if libro.calificacionPromedio >= calificacion:
    #         print(libro)

def verTopLibros():
    Libro.listaCalificaciones.sort(key=lambda x: x.calificacionPromedio,reverse=True)
    for libro in Libro.listaCalificaciones:
        print(libro)

#### MAIN ####

llist = LinkedList()

print('\n''Libros disponibles: ''\n')
libro1 = Libro('Libro1','Martin V.',1234)
libro2 = Libro('Libro2','Warren Buffet',1235)

verLibrosDisponibles()

print('\n')

agustin = User('agustin')
#Validar si el libro existe en la DB
cantidadReseñas = int(input('Cantidad de reseñas: '))
i=0
for i in range(cantidadReseñas):
    User.reseñar(agustin)

#Veo que se hayan aplicado los cambios con la carga de reseñas
verLibrosDisponibles()

print('\n')
calificacionInput = float(input('Ver libros con calificacion promedio mayor a: '))
verLibrosConCalificacionMayorA(calificacionInput)

#verTopLibros()