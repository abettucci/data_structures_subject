class node():
    def __init__(self, data, next_node = None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_node):
        self.next_node = new_node

class LinkList(object):

    def __init__(self, head = None):
        self.head = head

    def add(self, data):
        new_node = node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def printlist(self):
        current_node = self.head
        while (current_node != None):
            print (current_node.get_data(), end = "->")
            current_node = current_node.get_next()
        print ()

def merge(L1, L2):

    temp = None

    if L1 is None:
        return L2

    if L2 is None:
        return L1
    if L1.data >= L2.data:
        temp = L1
        temp.next_node = merge(L1.next_node, L2)
    else:
        temp = L2
        temp.next_node = merge(L1, L2.next_node)

    return temp


def main():

    list1 = LinkList()
    list1.add(10)
    list1.add(20)
    list1.add(30)

    print("list2: ", end=" " )
    list1.printlist()

    list2 = LinkList()
    list2.add(11)
    list2.add(21)
    list2.add(51)
    print("list1: ", end=" " )
    list2.printlist()

    list3 = LinkList()

    list3.head = merge(list1.head, list2.head)
    print("merge link list: ", end=" " )
    list3.printlist()

if __name__ == "__main__":
    main()