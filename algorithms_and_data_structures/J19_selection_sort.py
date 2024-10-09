from typing import List
"""na zacatku je nesedrizeny seznam a ciklem hledam nejnizsi cislo
v seznamu na konci ciklu toto cislo vlazim na zacatek seznamu a dalsi 
kolo ciklu zacina na prvnim nesetrizenem cisle a zase hledam nejnizsi
hodnotu. takze v prubehu trizeni se prodluzuje setrizena cast a zkracuje
nesedrizena cast ve ktere bezi ciklus"""

def selection_sort(numbers: List[int]) -> List[int]:
    # pro každý prvek v seznamu:
    for i in range(len(numbers)):  # i definuje začátek nesetřízeného seznamu
        print(f"{numbers}")
        # naleznu nejmenší prvek v nesetřízené části seznamu
        minimal_value = numbers[i]
        minimal_index = i
        for j in range(i+1, len(numbers)):
            if numbers[j] < minimal_value:
                minimal_value = numbers[j]
                minimal_index = j
        # nalezený prvek prohodím s prvním nesetřízeným prvkem
        numbers[i], numbers[minimal_index] = numbers[minimal_index], numbers[i]

    return numbers


if __name__ == '__main__':
    my_numbers = [8, 4, 2, 5, 3, 1, 7, 2, 9, 14, 4, 2]
    print(selection_sort(my_numbers))
