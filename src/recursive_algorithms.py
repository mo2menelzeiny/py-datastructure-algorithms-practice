def sum_recursive(arr):
    if not arr:
        return 0
    else:
        return arr[0] + sum(arr[1:])


def count_recursive(arr):
    if not arr:
        return 0
    else:
        return 1 + count_recursive(arr[1:])


def find_max_recursive(arr):
    if len(arr) == 1:
        return arr[0]
    elif arr[0] > arr[1]:
        return arr[0]
    else:
        return find_max_recursive(arr[1:])


def factorial_recursion(n):
    if n == 1:
        return 1
    else:
        return n * factorial_recursion(n - 1)


def max_element_recursion(arr):
    if len(arr) == 1:
        return arr[0]
    elif arr[0] > arr[1]:
        return arr[0]
    else:
        return max_element_recursion(arr[1:])
