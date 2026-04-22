###################task1&2
def selection_sort(arr):
    n = len(arr)
    comparisons = 0
    swaps = 0

    print("Original list:", arr)

    for i in range(n - 1):
        min_index = i

        # Find the minimum element in unsorted part
        for j in range(i + 1, n):
            comparisons += 1
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap if needed
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            swaps += 1

        print(f"Pass {i + 1}: {arr}")

    print("Sorted list:", arr)
    print("Total comparisons:", comparisons)
    print("Total swaps:", swaps)

arr = [29, 10, 14, 37, 13]
selection_sort(arr)

##################task3
print("----- Task 2 Output -----")
def create_index_table(arr, block_size):
    index_table = []

    for i in range(0, len(arr), block_size):
        index_table.append((arr[i], i))

    print("\nIndex table created:")
    for value, index in index_table:
        print(f"{value} -> {index}")

    return index_table

# Test
arr_sorted = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65]
block_size = 3

index_table = create_index_table(arr_sorted, block_size) 

####################task4
print("\n----- Task 4 Output -----")
def indexed_search(arr, index_table, key, block_size):
    print("\nSearch key:", key)

    imin = 0
    imax = len(arr) - 1

    # Step 1: Find range using index table
    for i in range(len(index_table)):
        if i == len(index_table) - 1 or key < index_table[i + 1][0]:
            imin = index_table[i][1]
            if i == len(index_table) - 1:
                imax = len(arr) - 1
            else:
                imax = index_table[i + 1][1] - 1
            print("Index range found:")
            print(f"{index_table[i][0]} <= {key} < {index_table[i + 1][0] if i < len(index_table)-1 else 'end'}")
            break

    # Step 2: Sequential search in range
    print(f"Searching from index {imin} to index {imax}:")

    for i in range(imin, imax + 1):
        print(f"Checking index {i}: {arr[i]}")
        if arr[i] == key:
            print(f"{key} found at index {i}")
            return i

    print(f"{key} not found")
    return -1

# Test (Found case)
indexed_search(arr_sorted, index_table, 45, block_size)

##################task5
print("\n----- Task 5 Output -----")
def indexed_search(arr, index_table, key):
    print("Search key:", key)
    for i in range(len(index_table)):
        if i == len(index_table) - 1 or key < index_table[i + 1][0]:
            imin = index_table[i][1]
            if i == len(index_table) - 1:
                imax = len(arr) - 1
            else:
                imax = index_table[i + 1][1] - 1
            print("Index range found:")
            if i < len(index_table) - 1:
                print(f"{index_table[i][0]} <= {key} < {index_table[i + 1][0]}")
            else:
                print(f"{index_table[i][0]} <= {key} < end")
            break
    print(f"Searching from index {imin} to index {imax}:")
    for i in range(imin, imax + 1):
        print(f"Checking index {i}: {arr[i]}")
        if arr[i] == key:
            print(f"{key} found at index {i}")
            return i
    print(f"{key} not found")
    return -1
arr = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65]
index_table = [(10, 0), (25, 3), (40, 6), (55, 9)]
key = 43
indexed_search(arr, index_table, key)