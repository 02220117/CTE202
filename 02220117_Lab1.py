#Task 1

class CustomList:

    def __init__(self, capacity=10):
       
        self.__elements = [None] * capacity
        
        self.__capacity = capacity
       
        self.__size = 0

        print(f"Created new CustomList with capacity: {self.__capacity}")
        print(f"Current size: {self.__size}")

    # Method to get current size
    def size(self):
        return self.__size

    # Method to get current capacity
    def capacity(self):
        return self.__capacity

    # Method to add an element
    def add(self, item):
        if self.__size >= self.__capacity:
            self.__resize()
        self.__elements[self.__size] = item
        self.__size += 1

    # Private method to resize array when full
    def __resize(self):
        self.__capacity *= 2
        new_array = [None] * self.__capacity
        for i in range(self.__size):
            new_array[i] = self.__elements[i]
        self.__elements = new_array
        print(f"Resized array to new capacity: {self.__capacity}")

    # Method to print all elements
    def display(self):
        print([self.__elements[i] for i in range(self.__size)])


# Example usage
my_list = CustomList()  # Should print initial capacity and size
my_list.add(5)
my_list.add(10)
my_list.display()  # Output: [5, 10]
print(f"Current size: {my_list.size()}")  # Output: 2

    

     #Task 2: Implement Basic Operations
class CustomList:
    def __init__(self, capacity=10):
        # Private array to store elements
        self.__elements = [None] * capacity
        self.__capacity = capacity
        self.__size = 0
        print(f"Created new CustomList with capacity: {self.__capacity}")
        print(f"Current size: {self.__size}")

    # 1. Append element to the end
    def append(self, element):
        if self.__size >= self.__capacity:
            self.__resize()
        self.__elements[self.__size] = element
        print(f"Appended {element} to the list")
        self.__size += 1

    # 2. Get element at a specific index
    def get(self, index):
        if 0 <= index < self.__size:
            element = self.__elements[index]
            print(f"Element at index {index}: {element}")
            return element
        else:
            raise IndexError("Index out of bounds")

    # 3. Set element at a specific index
    def set(self, index, element):
        if 0 <= index < self.__size:
            self.__elements[index] = element
            print(f"Set element at index {index} to {element}")
        else:
            raise IndexError("Index out of bounds")

    # 4. Return current size
    def size(self):
        print(f"Current size: {self.__size}")
        return self.__size

    # Private method to resize the array if needed
    def __resize(self):
        self.__capacity *= 2
        new_array = [None] * self.__capacity
        for i in range(self.__size):
            new_array[i] = self.__elements[i]
        self.__elements = new_array
        print(f"Resized array to new capacity: {self.__capacity}")



my_list = CustomList()
my_list.append(5)           
my_list.get(0)              
my_list.set(0, 10)          
my_list.get(0)              
my_list.size()             