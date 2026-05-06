# Counting Sort Implementation 
print("Task 1: Counting Sort")


def counting_sort(arr):
    if not arr:
        return []

    # Find the maximum and minimum element
    max_val = max(arr)
    min_val = min(arr)
    range_of_elements = max_val - min_val + 1

    # Initialize count array
    count = [0] * range_of_elements

    # Store count of each element
    for num in arr:
        count[num - min_val] += 1

    # Update count to contain actual positions
    for i in range(1, range_of_elements):
        count[i] += count[i - 1]

    # Build output array
    output = [0] * len(arr)
    for num in reversed(arr):
        count[num - min_val] -= 1
        output[count[num - min_val]] = num

    return output


# Example Usage
if __name__ == "__main__":
    arr = [4, 2, 2, 8, 3, 3, 1]

    print("Unsorted Array:", arr)           # print original
    sorted_arr = counting_sort(arr)
    print("Sorted Array:", sorted_arr)     # print sorted


##################task2
    print("\nTask 2: Radix Sort")
    

def counting_sort_for_radix(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10  # base 10 for digits 0–9

    # Count occurrences of each digit
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1

    # Update count[i] so it contains actual positions
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array
    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1

    # Copy output to arr
    for i in range(n):
        arr[i] = output[i]


def radix_sort(arr):
    if not arr:
        return []

    max_val = max(arr)
    exp = 1

    # Sort each digit's place
    while max_val // exp > 0:
        counting_sort_for_radix(arr, exp)
        exp *= 10

    return arr


# Example Usage
if __name__ == "__main__":
    arr = [170, 45, 75, 90, 802, 24, 2, 66]

    print("Unsorted Array:", arr)          # original array
    sorted_arr = radix_sort(arr.copy())   # use copy to keep original unchanged
    print("Sorted Array:", sorted_arr)