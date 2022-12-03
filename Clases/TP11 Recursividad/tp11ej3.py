'''
Escribir un método recursivo, que calcule la suma de los elementos de una lista secuencial (enlazada)
'''
import math

class Sum:
	tsum = None

class Node:
	def __init__(self,data):
		self.data = data
		self.next = None

def push(head, data):
	if not head:
		return Node(data)
	new_node = Node(data)
	new_node.next = head
	head = new_node
	return head

def sumOfNode(head, S):
	# if head = NULL
	if not head:
		return
	# recursively sum the remaining nodes
	sumOfNode(head.next, S)
	# accumulate sum
	S.tsum += head.data

# utility function to find
# the sum of nodes
def sumOfNodesUtil(head):
	S = Sum()
	S.tsum = 0
	# find the sum of nodes
	sumOfNode(head, S)
	# required sum
	return S.tsum

# Driver Code
if __name__=='__main__':
	head = None
	# create linked list 7->6->8->4->1
	head = push(head, 7)
	head = push(head, 6)
	head = push(head, 8)
	head = push(head, 4)
	head = push(head, 1)
	print("Sum of Nodes = {}" .
		format(sumOfNodesUtil(head)))

