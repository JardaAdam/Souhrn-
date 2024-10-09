"""Třídění kladných celých čísel podle počtu celočíselných dělitelů:
[5, 8, 12, 16, 1, 17, 30, 3, 9, 30, 101, 101] -> [1, 3, 5, 17, 101, 101, 9, 8, 16, 12, 30, 30]

BONUS: Optimalizujte hledání pomocí dynamického programování tak,
abyste pro zadané číslo hledali počet dělitelů jenom jednou.
"""
from J23_quicksort import quicksort


def number_of_dividers_quicksort():
    # TODO: implementovat funkci number_of_dividers_sort
    return quicksort(numbers)


if __name__ == '__main__':
    numbers = [5, 8, 12, 16, 1, 17, 30, 3, 9, 30, 101, 101]
    print(number_of_dividers_quicksort())
