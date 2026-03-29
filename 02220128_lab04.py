class ArrayQueue:
    def __init__(self, capacity=10):
        # Private array to store elements
        self._data = [None] * capacity
        
        # Front and rear indices
        self._front = 0
        self._rear = 0
        
        # Number of elements in queue
        self._size = 0
        
        print(f"Created new Queue with capacity: {capacity}")

    def is_empty(self):
        return self._size == 0


# Example usage
q = ArrayQueue()

print("Queue is empty:", q.is_empty())

#Task2
class ArrayQueue:
    def __init__(self, capacity=10):
        self._data = [None] * capacity
        self._front = 0
        self._rear = 0
        self._size = 0
        self._capacity = capacity
        
        print(f"Created new Queue with capacity: {capacity}")

    def is_empty(self):
        return self._size == 0

    # 1. Enqueue
    def enqueue(self, element):
        if self._size == self._capacity:
            print("Queue is full!")
            return
        
        self._data[self._rear] = element
        self._rear = (self._rear + 1) % self._capacity
        self._size += 1
        
        print(f"Enqueued {element} to the queue")

    # 2. Dequeue
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty!")
            return None
        
        element = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % self._capacity
        self._size -= 1
        
        print(f"Dequeued element: {element}")
        return element

    # 3. Peek
    def peek(self):
        if self.is_empty():
            print("Queue is empty!")
            return None
        
        return self._data[self._front]

    # 4. Size
    def size(self):
        return self._size

    # 5. Display
    def display(self):
        elements = []
        index = self._front
        
        for _ in range(self._size):
            elements.append(self._data[index])
            index = (index + 1) % self._capacity
        
        print(f"Display queue:{elements}")


# Example usage
q = ArrayQueue()

q.enqueue(10)
q.display()

q.enqueue(20)
q.display()

q.enqueue(30)
q.display()

print("Front element:", q.peek())

q.dequeue()

print("Current queue:", end=" ")
q.display()

print("Queue size:", q.size())

#Task3
# Node class
class Node:
    def __init__(self, data):
        self.data = data   # Store element
        self.next = None   # Reference to next node


# LinkedQueue class
class LinkedQueue:
    def __init__(self):
        self.front = None   # First node
        self.rear = None    # Last node
        self._size = 0      # Size counter
        
        print("Created new LinkedQueue")

    def is_empty(self):
        return self._size == 0


# Example usage
q = LinkedQueue()
print("Queue is empty:", q.is_empty())

#Task4
# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# LinkedQueue class
class LinkedQueue:
    def __init__(self):
        self.front = None
        self.rear = None
        self._size = 0
        print("Created new LinkedQueue")

    # 1. Enqueue
    def enqueue(self, element):
        new_node = Node(element)
        
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        
        self._size += 1
        print(f"Enqueued {element} to the queue")

    # 2. Dequeue
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty!")
            return None
        
        removed = self.front.data
        self.front = self.front.next
        
        if self.front is None:  # Queue becomes empty
            self.rear = None
        
        self._size -= 1
        print(f"Dequeued element: {removed}")
        return removed

    # 3. Peek
    def peek(self):
        if self.is_empty():
            print("Queue is empty!")
            return None
        return self.front.data

    # 4. is_empty
    def is_empty(self):
        return self._size == 0

    # 5. Size
    def size(self):
        return self._size

    # 6. Display
    def display(self):
        current = self.front
        elements = []
        
        while current:
            elements.append(str(current.data))
            current = current.next
        
        print("Display queue:[" + ",".join(elements) + "]")

    # Optional: Display in arrow format
    def display_linked(self):
        current = self.front
        result = ""
        
        while current:
            result += str(current.data) + " -> "
            current = current.next
        
        result += "null"
        print("Current queue:", result)


# Example usage
q = LinkedQueue()

q.enqueue(10)
q.display()

q.enqueue(20)
q.display()

q.enqueue(30)
q.display()
 
print("Front element:", q.peek())

q.dequeue()

q.display_linked()

print("Queue size:", q.size())