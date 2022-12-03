'''
Escriba un metodo que toma dos listas de enteros y las une en una sola lista de la sig manera:
lista1elemento1, lista2elemento1, lista1elemento2, lista2elemento2, etc. De no ser iguales los tamaños
de ambas listas, al final de la lista generada deben quedar los elementos de la lista mas larga.
'''

class Node:  
    def __init__(self, value):    
        self.value = value
        self.next = None

def getNode(value):
  
    # allocating space
    newNode = Node(value)
    return newNode

def printList(head):
    while (head != None):       
        print(' ' + str(head.value), end = '')
        head = head.next;    
    print()

def mergedAndSortedLists(head1, head2):
    if head1 is None:
        return head2
    if head2 is None:
        return head1

    # create dummy node to avoid additional checks in loop
    s = t = Node(0) 
    while not (head1 is None or head2 is None):
        if head1.value < head2.value:
            # remember current low-node
            c = head1
            # follow ->next
            head1 = head1.next
        else:
            # remember current low-node
            c = head2
            # follow ->next
            head2 = head2.next

        # only mutate the node AFTER we have followed ->next
        t.next = c          
        # and make sure we also advance the temp
        t = t.next

    t.next = head1 or head2

    # return tail of dummy node
    return s.next

# Creating the list A: 3.5.8.10
head1 = getNode(3)
head1.next = getNode(5)
head1.next.next = getNode(8)
head1.next.next.next = getNode(10)
print("Linked list A before merge: ", end='')
printList(head1); 

# Creating the list B: 1.2.3.4
head2 = getNode(1)
head2.next = getNode(2)
head2.next.next = getNode(3)
head2.next.next.next = getNode(4)
print("Linked list B: ", end='')
printList(head2); 

printList(mergedAndSortedLists(head1,head2))
