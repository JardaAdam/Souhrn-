"""Třídění bodů v rovině (2D bodů)
Napište program, který seřadí seznam bodů v rovině podle jejich vzdálenosti od počátku (0,0).
Body budou reprezentovány souřadnicemi v tuple:
[(1, 0), (1, 1), (2, 5), (3, 2), (4, 5), (0, 1), (5, 1)]

BONUS: Pokud mají dva body stejnou vzdálenost, seřaďte je podle jejich úhlu vzhledem k ose X.
"""
from J23_quicksort import quicksort

def abs_2d_points_quicksort(arr):
    # TODO: implementovat funkci abs_2d_points_sort
    return quicksort(points)


if __name__ == '__main__':
    points = [(1, 0), (1, 1), (2, 5), (3, 2), (4, 5), (0, 1), (5, 1)]
    print(abs_2d_points_quicksort(points))