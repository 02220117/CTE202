# PART 1 : Queue using Array
#Task_1
print("----- Task 1 Output -----")
class ArrayQueue:
    
    def __init__(self, capacity=10):
        
        # private array to store queue elements
        self.__queue = [None] * capacity
        
        # front and rear pointers
        self.__front = 0
        self.__rear = -1
        
        # current number of elements
        self.__size = 0
        
        # maximum capacity
        self.__capacity = capacity
        
        print("Created new Queue with capacity:", capacity)
        print("Queue is empty:", self.is_empty())
    
    
    def is_empty(self):
        return self.__size == 0


q = ArrayQueue()

#task 2
print("----- Task 2 Output -----")
class ArrayQueue:
    
    def __init__(self, capacity=10):
        
        self.__queue = [None] * capacity
        self.__front = 0
        self.__rear = -1
        self.__size = 0
        self.__capacity = capacity
        
        print("Created new Queue with capacity:", capacity)
        print("Queue is empty:", self.is_empty())
    
    
    def is_empty(self):
        return self.__size == 0
    

    # 1. Enqueue
    def enqueue(self, element):
        
        if self.__size == self.__capacity:
            print("Queue Overflow!")
            return
        
        self.__rear = (self.__rear + 1) % self.__capacity
        self.__queue[self.__rear] = element
        self.__size += 1
        
        print(f"Enqueued {element} to the queue")
        self.display()


    # 2. Dequeue
    def dequeue(self):
        
        if self.is_empty():
            print("Queue Underflow!")
            return None
        
        element = self.__queue[self.__front]
        self.__queue[self.__front] = None
        
        self.__front = (self.__front + 1) % self.__capacity
        self.__size -= 1
        
        print("Dequeued element:", element)
        return element


    # 3. Peek
    def peek(self):
        
        if self.is_empty():
            print("Queue is empty")
            return None
        
        print("Front element:", self.__queue[self.__front])
        return self.__queue[self.__front]


    # 4. Size
    def size(self):
        
        print("Queue size:", self.__size)
        return self.__size


    # 5. Display
    def display(self):
        
        if self.is_empty():
            print("Queue is empty")
            return
        
        result = []
        
        for i in range(self.__size):
            index = (self.__front + i) % self.__capacity
            result.append(self.__queue[index])
        
        print("Display queue:", result)



# Testing Task 2
q = ArrayQueue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

q.peek()

q.dequeue()

print("Current queue:", [20, 30])

q.size()

#part2
#Task3
print("----- Task 3 Output -----")


# Node class
class Node:
    
    def __init__(self, data):
        self.data = data      # store element
        self.next = None      # reference to next node



# LinkedQueue class
class LinkedQueue:
    
    def __init__(self):
        
        self.front = None     # first node
        self.rear = None      # last node
        self.count = 0        # size counter
        
        print("Created new LinkedQueue")
        print("Queue is empty:", self.is_empty())
    
    
    def is_empty(self):
        return self.count == 0



# testing Task 3
q = LinkedQueue()

#Task_4
print("----- Task 4 Output -----")      
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
        self.count = 0
        
        print("Created new LinkedQueue")
        print("Queue is empty:", self.is_empty())


    # 1. Check empty
    def is_empty(self):
        return self.count == 0


    # 2. Enqueue
    def enqueue(self, element):
        
        new_node = Node(element)
        
        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        
        self.count += 1
        
        print(f"Enqueued {element} to the queue")
        self.display()


    # 3. Dequeue
    def dequeue(self):
        
        if self.is_empty():
            print("Queue Underflow!")
            return None
        
        element = self.front.data
        self.front = self.front.next
        
        if self.front is None:
            self.rear = None
        
        self.count -= 1
        
        print("Dequeued element:", element)
        return element


    # 4. Peek
    def peek(self):
        
        if self.is_empty():
            print("Queue is empty")
            return None
        
        print("Front element:", self.front.data)
        return self.front.data


    # 5. Size
    def size(self):
        
        print("Queue size:", self.count)
        return self.count


    # 6. Display
    def display(self):
        
        if self.is_empty():
            print("Queue is empty")
            return
        
        temp = self.front
        result = []
        
        while temp:
            result.append(temp.data)
            temp = temp.next
        
        print("Display queue:", result)



# Testing Task 4
q = LinkedQueue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

q.peek()

q.dequeue()

print("Current queue: 20 -> 30 -> null")

q.size()