class CustomList:
    def __init__(self, capacity=10):
        # Private array to store elements
        self.__elements = [None] * capacity
        # Track the total capacity
        self.__capacity = capacity
        # Track current size (number of elements added)
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

    