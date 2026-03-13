class CustomList:

    def __init__(self, capacity=10):
        self.capacity = capacity
        self.array = [None] * capacity
        self.current_size = 0

    def append(self, element):
        self.array[self.current_size] = element
        self.current_size += 1
        print(f"Appended {element} to the list")

    def get(self, index):
        print(f"Element at index {index}: {self.array[index]}")

    def set(self, index, element):
        self.array[index] = element
        print(f"Set element at index {index} to {element}")

    def size(self):
        print(f"Current size: {self.current_size}")


# ---- Run program ----
my_list = CustomList()

my_list.append(5)
my_list.get(0)
my_list.set(0, 10)
my_list.get(0)
my_list.size()

