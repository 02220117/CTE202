#array stack implementation by Tashi Eden dorji
class ArrayStack:
    def __init__(self, capacity=10):
        # Private array to store elements
        self._data = [None] * capacity
        
        # Variable to track the top of the stack
        self._top = -1
        
        # Capacity of stack
        self._capacity = capacity
        
        print(f"Created new ArrayStack with capacity: {capacity}")

    # Check if stack is empty
    def is_empty(self):
        return self._top == -1


# Example usage
stack = ArrayStack()
print("Stack is empty:", stack.is_empty())

#Task2
class ArrayStack:
    def __init__(self, capacity=10):
        self._data = [None] * capacity
        self._top = -1
        self._capacity = capacity
        print(f"Created new ArrayStack with capacity: {capacity}")

    # 1. Push element
    def push(self, element):
        if self._top == self._capacity - 1:
            print("Stack Overflow! Cannot push element.")
            return
        self._top += 1
        self._data[self._top] = element
        print(f"Pushed {element} to the stack")

    # 2. Pop element
    def pop(self):
        if self.is_empty():
            print("Stack Underflow! Cannot pop element.")
            return None
        element = self._data[self._top]
        self._top -= 1
        print(f"Popped element: {element}")
        return element

    # 3. Peek
    def peek(self):
        if self.is_empty():
            print("Stack is empty!")
            return None
        return self._data[self._top]

    # 4. Check if empty
    def is_empty(self):
        return self._top == -1

    # 5. Size of stack
    def size(self):
        return self._top + 1

    # 6. Display stack
    def display(self):
        if self.is_empty():
            print("Display stack: []")
        else:
            print("Display stack:", self._data[:self._top + 1])


# Example usage
stack = ArrayStack()

stack.push(10)
stack.display()

stack.push(20)
stack.display()

stack.push(30)
stack.display()

print("Top element:", stack.peek())

stack.pop()

print("Stack size:", stack.size())
stack.display()