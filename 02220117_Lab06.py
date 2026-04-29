##################task1  Merge SortImplementation
def merge_sort(arr):
    # Edge case: empty or single element list
    if len(arr) <= 1:
        return arr, 0, 0

    def merge(left, right):
        merged = []
        i = j = 0
        comparisons = 0
        accesses = 0

        while i < len(left) and j < len(right):
            comparisons += 1
            accesses += 2  # accessing left[i] and right[j]

            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
                accesses += 1
            else:
                merged.append(right[j])
                j += 1
                accesses += 1

        # Add remaining elements
        while i < len(left):
            merged.append(left[i])
            i += 1
            accesses += 1

        while j < len(right):
            merged.append(right[j])
            j += 1
            accesses += 1

        return merged, comparisons, accesses

    # Divide step
    mid = len(arr) // 2
    left, comp_left, acc_left = merge_sort(arr[:mid])
    right, comp_right, acc_right = merge_sort(arr[mid:])

    # Merge step
    merged, comp_merge, acc_merge = merge(left, right)

    # Total counts
    total_comparisons = comp_left + comp_right + comp_merge
    total_accesses = acc_left + acc_right + acc_merge

    return merged, total_comparisons, total_accesses


# Example usage
arr = [38, 27, 43, 3, 9, 82, 10]

sorted_arr, comparisons, accesses = merge_sort(arr)

print("Original List:", arr)
print("Sorted using Merge Sort:", sorted_arr)
print("Number of comparisons:", comparisons)
print("Number of array accesses:", accesses)

##################task2  Quick SortImplementation

print("\n----- Task 2 Output -----")

def quick_sort(arr):
    comparisons = 0
    swaps = 0

    # Median-of-three pivot selection (optimization)
    def median_of_three(a, low, high):
        mid = (low + high) // 2

        if a[low] > a[mid]:
            a[low], a[mid] = a[mid], a[low]
        if a[low] > a[high]:
            a[low], a[high] = a[high], a[low]
        if a[mid] > a[high]:
            a[mid], a[high] = a[high], a[mid]

        return mid

    # Partition function
    def partition(a, low, high):
        nonlocal comparisons, swaps

        pivot_index = median_of_three(a, low, high)
        a[pivot_index], a[high] = a[high], a[pivot_index]
        swaps += 1

        pivot = a[high]
        i = low - 1

        for j in range(low, high):
            comparisons += 1
            if a[j] <= pivot:
                i += 1
                a[i], a[j] = a[j], a[i]
                swaps += 1

        a[i + 1], a[high] = a[high], a[i + 1]
        swaps += 1

        return i + 1

    # Recursive Quick Sort
    def quicksort_recursive(a, low, high):
        if low < high:
            pi = partition(a, low, high)
            quicksort_recursive(a, low, pi - 1)
            quicksort_recursive(a, pi + 1, high)

    # Edge case handling
    if len(arr) <= 1:
        return arr, comparisons, swaps

    quicksort_recursive(arr, 0, len(arr) - 1)
    return arr, comparisons, swaps


if __name__ == "__main__":
    arr = [38, 27, 43, 3, 9, 82, 10]

    print("Original List:", arr)

    sorted_arr, comparisons, swaps = quick_sort(arr.copy())

    print("Sorted using Quick Sort:", sorted_arr)
    print("Number of comparisons:", comparisons)
    print("Number of swaps:", swaps)