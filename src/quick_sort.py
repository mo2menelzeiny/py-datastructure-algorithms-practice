def quick_sort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)


def partition_qsort(arr, p, r):
    x = arr[r]  # last item as pivot
    i = p - 1  # partition start index
    for j in range(p, r):
        if arr[j] <= x:  # partition condition
            i = i + 1
            arr[j], arr[i] = arr[i], arr[j]
    arr[r], arr[i + 1] = arr[i + 1], arr[r]
    return i + 1


def sort_qsort(arr, p, r):
    if p < r:
        q = partition_qsort(arr, p, r)
        sort_qsort(arr, p, q - 1)
        sort_qsort(arr, q + 1, r)
    return arr


# random_unsorted = [6, 20, 13, 14, 31, 34, 7, 10, 1, 24, 27, 2, 5, 17, 18, 12]
# random_sorted = selection_sort(random_unsorted)
# print("Selection Sorted: ", random_sorted)
# print("Index: ", binary_search(random_sorted, 31))
# print("Factorial: ", factorial_recursion(5))
# print("Max: ", max_element_recursion(random_sorted))
# print("Quick Sorted: ", quick_sort([6, 20, 13, 14, 31, 34, 7, 10, 1, 24, 27, 2, 5, 17, 18, 12]))
# test_arr = [6, 20, 13, 14, 31, 34, 7, 10, 1, 24, 27, 2, 5, 17, 18, 12]
print("SORTED: ", sort_qsort([3, 18, 1, 2, 102], 0, 4))
