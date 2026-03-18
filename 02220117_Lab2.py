#Task_1
print("----- Task 1 Output -----")
class Node:
    def __init__(self, data):
        self.data = data      
        self.next = None      

class LinkedList:
    def __init__(self):
        self.head = None      
        self.tail = None      
        self.size = 0        

   
    def display_info(self):
        print("Current size:", self.size)
        print("Head:", self.head.data if self.head else None)



ll = LinkedList()
print("Created new LinkedList")
ll.display_info()


#Task_2
print("\n----- Task 2 Output -----")


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None



class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def append(self, element):
        new_node = Node(element)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1
        print("Appended", element, "to the list")

    def get(self, index):
        current = self.head
        for i in range(index):
            current = current.next
        return current.data

    def set(self, index, element):
        current = self.head
        for i in range(index):
            current = current.next
        current.data = element
        print("Set element at index", index, "to", element)

    def size(self):
        return self._size

    def prepend(self, element):
        new_node = Node(element)
        new_node.next = self.head
        self.head = new_node
        if self.tail is None:
            self.tail = new_node
        self._size += 1
        print("Prepend", element, "to the list")

    def print_list(self):
        current = self.head
        print("Print Linked list:[", end=" ")
        while current:
            print(current.data, end=" ")
            current = current.next
        print("]")



ll = LinkedList()

ll.append(5)

print("Element at index 0:", ll.get(0))

ll.set(0, 10)

print("Element at index 0:", ll.get(0))

print("Current size:", ll.size())

ll.prepend(10)

ll.print_list()