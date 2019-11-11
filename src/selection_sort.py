def selection_sort(arr):
    new_arr = []
    for i in range(len(arr)):
        smallest = arr[0]
        smallest_index = 0
        for j in range(len(arr)):
            if arr[j] < smallest:
                smallest = arr[j]
                smallest_index = j
        new_arr.append(arr.pop(smallest_index))
    return new_arr


def selection_sort_inplace(arr):
    for i in range(len(arr)):
        smallest_index = i
        for j in range(i, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
    return arr


print(selection_sort_inplace([8, 4, 1, 5, 77, 123, 0, 2]))
