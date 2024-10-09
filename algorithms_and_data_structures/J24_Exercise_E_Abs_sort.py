"""
Zadání: Chceme neuspořádaný seznam čísel uspořádat podle
absolutní hodnoty:
[2, -5, 3, -2, 2, 1, -1, -9, -7, 8] -> [-1, 1, -2, 2, 2, 3, -5, -7, 8, -9]
"""


def abs_quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = abs(arr[0])
    middle = [x for x in arr if abs(x) == pivot and x < 0] + [x for x in arr if abs(x) == pivot and x > 0]
    left = [x for x in arr if abs(x) < pivot]
    right = [x for x in arr if abs(x) > pivot]
    return abs_quicksort(left) + middle + abs_quicksort(right)


if __name__ == '__main__':
    numbers = [2, -5, 3, -2, 2, 1, -1, -9, -7, 8, 5, -8, 9, 5, -5]
    print(abs_quicksort(numbers))
