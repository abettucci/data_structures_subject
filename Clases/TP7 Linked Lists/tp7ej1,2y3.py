# Python3 program for insertion in a single linked
# list at a specified position
   
# A linked list Node
class Node:  
    def __init__(self, data):    
        self.data = data
        self.nextNode = None
   
# function to create and return a Node
def getNode(data):
  
    # allocating space
    newNode = Node(data)
    return newNode
  
# function to insert a Node at required position
def insertPos(headNode, position, data): 
    head = headNode
      
    # This condition to check whether the
    # position given is valid or not.
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
               newNode = getNode(data)
  
               # Making the new Node to point to
               # the old Node at the same position
               newNode.nextNode = headNode.nextNode
  
               # Replacing headNode with new Node
               # to the old Node to point to the new Node
               headNode.nextNode = newNode
               break
              
            headNode = headNode.nextNode
            if headNode == None:
                break            
        if position != 1:
              print("position out of range")        
    return head
       
# This function prints contents 
# of the linked list 
def printList(head):
    while (head != None):       
        print(' ' + str(head.data), end = '')
        head = head.nextNode;    
    print()

# This function adds a new node after a fiven reference node
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

# Driver Code
if __name__=='__main__':
      
    # Creating the list 3.5.8.10
    head = getNode(3)
    head.nextNode = getNode(5)
    head.nextNode.nextNode = getNode(8)
    head.nextNode.nextNode.nextNode = getNode(10)
    print("Linked list before insertion: ", end='')
    printList(head); 

    #inserting the data in the linked list
    data = int(input('New node value: '))
    position = int(input('Position to be inserted: '))
    head = insertPos(head, position, data);
    print("Linked list after insertion of {} at position {}: ".format(data,position), end = '')
    printList(head)
   
