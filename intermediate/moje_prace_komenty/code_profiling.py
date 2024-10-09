# TODO Modul timeit
# Modul timeit měří dobu provádění fragmentů kódu v jazyce Python. Jedná se o přesnou metodu, která nebere v úvahu
# procesy na pozadí. Navíc spouští kód vícekrát (ve výchozím nastavení milionkrát), takže výsledek je
# statisticky významný.

# Pro použití modulu použijte následující příkaz:
import timeit


# timeit.timeit(stmt, setup, number)

# stmt = blok kódu, jehož dobu provádění chceme měřit,
# setup = kód, který bude proveden před provedením stmtu, například importem potřebných modulů,
# number = počet opakování kódu, který se má provést.

# setup = "from math import sqrt"
#
# code = '''
# def func():
#         return [sqrt(x) for x in range(100)]
#     '''

# print(timeit.timeit(stmt=code, setup=setup, number=100))

# TODO priklad trojitych uvozovek bez navaznosti na kod

# def foo(x):
#     """
#     tento radek je pro poznamku o tom co ma funkce delat
#     :param x: number
#     :return: value of number x + 1
#     """
#     return x + 1

# print(foo(5))

import timeit

# TODO Definice funkcí linear_search a binary_search
# tento priklad ukazuje casovy rozdil mezi zpusoby linear a binary


def linear_search(lst, to_find):
    """

    :param lst: list cisel ve kterem hledam
    :param to_find: vupisuje index hledaneho cisla
    :return: vypise index hledaneho cisla pokud ho nenajde vypise [don't find it]
    """
    for i, element in enumerate(lst):
        if element == to_find:
            return i
    return "don't find it"


def binary_search(lst, to_find):
    """
    
    :param lst:
    :param to_find:
    :return:
    """
    left, right = 0, len(lst) - 1
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == to_find:
            return mid
        elif lst[mid] < to_find:
            left = mid + 1
        else:
            right = mid - 1
    return -1



if __name__ == "__main__":
    # '''v tomto pripade pouzivame trojite uvozovky pro vicezadkovy zapis neceho co ma byt jeden radek'''
    setup = '''
from __main__ import linear_search, binary_search
import random
    '''

    linear_search_code = '''
lst = sorted([random.randint(0, 1000000) for _ in range(1000)])
to_find = random.randint(0, 1000000)
result = linear_search(lst, to_find)
    '''

    binary_search_code = '''
lst = sorted([random.randint(0, 1000000) for _ in range(1000)])
to_find = random.randint(0, 1000000)
result = binary_search(lst, to_find)
    '''

    print(timeit.timeit(stmt=linear_search_code,
                        setup=setup,
                        number=1000))
    print(timeit.timeit(stmt=binary_search_code,
                        setup=setup,
                        number=1000))

result = linear_search([1, 2, 3, 4, 5], 7)
print(result)  # To by zobrazilo výsledek vyhledávání, například 4 (index cisla 5)

