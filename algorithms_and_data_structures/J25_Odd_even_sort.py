"""Uspořádáme seznam celých čísel tak,
že nejprve budou všechna lichá čísla (uspořádaná podle velikosti)
a následně všechna sudá čísla (uspořádaná podle velikosti).
[5, 3, 4, 2, -6, 7, -7, 8, 1, 2] -> [-7, 1, 3, 5, 7, -6, 2, 2, 4, 8]
"""
from J23_quicksort import quicksort
from J24_Exercise_E_Abs_sort import abs_quicksort


def odd_even_quicksort(arr):
    return quicksort([x for x in arr if x % 2]) + quicksort([x for x in arr if x % 2 == 0])
    """ protoze quicksort jiz mame napsany tak vytvorime pouze funkci ktera ho pouzije
    a zmenime touto funkci jenom vysledek"""


def odd_even_abs_quicksort(arr):
    return abs_quicksort([x for x in arr if x % 2]) + abs_quicksort([x for x in arr if x % 2 == 0])
""" zase pouze funkce ktera pouzije uz funkcni kod jen upravim kriteria a spustim"""

if __name__ == '__main__':
    unsorted = [5, 3, 4, 2, -6, 7, -7, 8, 1, 2]
    print(odd_even_quicksort(unsorted))
    print(odd_even_abs_quicksort(unsorted))