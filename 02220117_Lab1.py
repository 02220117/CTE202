#task1
class CustomList:
    def __init__(self, capacity=10):
        # Private array to store elements
        self.__elements = [None] * capacity
        self.__capacity = capacity
        self.__size = 0

        print("Created new CustomList with capacity:", self.__capacity)
        print("Current size:", self.__size)

    # Append element to the end
    def append(self, element):
        if self.__size == self.__capacity:
            print("List is full. Cannot append.")
            return
        
        self.__elements[self.__size] = element
        self.__size += 1
        print(f"Appended {element} to the list")

    # Get element at index
    def get(self, index):
        if index < 0 or index >= self.__size:
            print("Index out of range")
            return None
        
        print(f"Element at index {index}: {self.__elements[index]}")
        return self.__elements[index]

    # Set element at index
    def set(self, index, element):
        if index < 0 or index >= self.__size:
            print("Index out of range")
            return
        
        self.__elements[index] = element
        print(f"Set element at index {index} to {element}")

    # Return current size
    def size(self):
        return self.__size


# Example usage
my_list = CustomList()

my_list.append(5)
my_list.get(0)

my_list.set(0, 10)
my_list.get(0)

print("Current size:", my_list.size())


#task2
class CustomList:
    def __init__(self, capacity=10):
        # Private array to store elements
        self.__elements = [None] * capacity
        
        # Variable to track capacity
        self.__capacity = capacity
        
        # Variable to track current size
        self.__size = 0
        
        print("Created new CustomList with capacity:", self.__capacity)
        print("Current size:", self.__size)


# Example usage
my_list = CustomList()