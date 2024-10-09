#
def quicksort(arr):
    if len(arr) <= 1:  # pokud je pole rovno nebo mensi nez 1
        return arr
    # pokud seznam obsahuje alespoň dva prvky
    # vyberu pivot -> do seznamu middle
    pivot = arr[0]  # pivot je cislo na pozici 0 v seznamu =
    # tato varianta neni vhodna pokud mame jiz castecne usporadany seznam
    middle = [x for x in arr if x == pivot]
    # všechny hodnoty menší, než pivot -> left
    left = [x for x in arr if x < pivot]
    # všechny hodnoty větší, než pivot -> right
    right = [x for x in arr if x > pivot]
    # spojíme quicksort(left) + middle + quicksort(right)
    return quicksort(left) + middle + quicksort(right)


if __name__ == '__main__':
    numbers = [8, 4, 2, 5, 3, 1, 7, 2, 9]
    print(quicksort(numbers))
