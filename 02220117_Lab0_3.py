#Task_3
print("----- Task 3 Output -----")
# Node class
class Node:
    def __init__(self, data):
        self.data = data     
        self.next = None      



class LinkedStack:
    def __init__(self):
        self.top = None       
        self.size = 0         # number of elements in stack
        print("Created new LinkedStack")

    # Check if stack is empty
    def is_empty(self):
        return self.size == 0



stack = LinkedStack()
print("Stack is empty:", stack.is_empty())

#Task_4
print("----- Task 4 Output -----")
# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# LinkedStack class
class LinkedStack:
    def __init__(self):
        self.top = None
        self._size = 0
        print("Created new LinkedStack")

    # 1. Push operation
    def push(self, element):
        new_node = Node(element)
        new_node.next = self.top
        self.top = new_node
        self._size += 1
        print(f"Pushed {element} to the stack")

    # 2. Pop operation
    def pop(self):
        if self.is_empty():
            print("Stack Underflow")
            return None
        popped = self.top.data
        self.top = self.top.next
        self._size -= 1
        print(f"Popped element: {popped}")
        return popped

    # 3. Peek operation
    def peek(self):
        if self.is_empty():
            return None
        return self.top.data

    # 4. Check if empty
    def is_empty(self):
        return self.top is None

    # 5. Size of stack
    def size(self):
        return self._size

    # 6. Display stack
    def display(self):
        current = self.top
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        if elements:
            print("Current stack:", " -> ".join(elements), "-> null")
        else:
            print("Stack is empty")
        
# Example usage
stack = LinkedStack()

stack.push(10)
stack.display()

stack.push(20)
stack.display()

stack.push(30)
stack.display()

print("Top element:", stack.peek())

stack.pop()
stack.display()

print("Stack size:", stack.size())