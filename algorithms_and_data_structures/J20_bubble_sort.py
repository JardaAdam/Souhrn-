from typing import List
"""V tomto serazovani jde o to ze se porovnavaji vzdy dve cisla mezi 
sebou a kdyz je leve cislo vetsi nez prave cislo tak se cisla prohodi
a ciklus pokracuje s novim pravim cislem dokud nenarazi na mensi cislo
nebo na konec seznamu"""

def bubble_sort(arr: List[int]) -> List[int]:
    for i in range(len(arr) - 1):
        print(arr)
        changed = False  # radek 7, 11, 12 a 13 je tu proto aby se ciklus zastavil pokud se nic v danem ciklu nezmenilo
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                changed = True
        if not changed:
            return arr
    return arr


if __name__ == '__main__':
    my_numbers = [8, 4, 2, 5, 3, 1, 7, 2, 9, 14, 4, 2]
    # my_numbers = [1, 2, 2, 2, 3, 4, 4, 5, 7, 8, 9, 14]
    print(bubble_sort(my_numbers))
