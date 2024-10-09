"""Sort MINIMAX
Vyhledáme v nesetřízené posloupnosti nejmenší/největší prvek
a vložím ho na konec setřízené posloupnosti.
"""
from typing import List


def minimax(unsorted: List[int]) -> List[int]:
    """
        Computational complexity:
        - time: O(n^2) - kvadraticka
        - memory: O(n) - linearni 
        :param unsorted:
        :return: sorted
        """
    number_of_iterations = 0
    sorted_list = []
    # print(f"Unsorted list: {unsorted}")
    # dokud původní seznam není prázdný
    while len(unsorted) > 0:
        # najdeme nejmenší prvek v původním seznamu
        minimal_value = unsorted[0]
        minimal_index = 0
        # projdeme celý seznam
        for i in range(1, len(unsorted)):
            number_of_iterations += 1
            # pokud najdeme číslo menší, než jaké je uložené v minimal_value
            if unsorted[i] < minimal_value:
                # do minimal_value uložíme tuto hodnotu
                minimal_value = unsorted[i]
                # do minimal_index vložím index této hodonoty
                minimal_index = i
                # tento forciklus projede celi seznam a na konci ciklu preda nejnizsi cislo do serted_list
        # print(f"Minimal value: {minimal_value} at index {minimal_index}.")
        # nalezený prvek vložím na konec nového seznamu
        sorted_list.append(minimal_value)
        # nalezený prvek odstraním z původního seznamu
        unsorted.pop(minimal_index)
        # print(f"Unsorted list: {unsorted}")
        # print(f"Sorted list:   {sorted_list}")
        # print('-'*80)
    print(f"Number of iterations: {number_of_iterations}")
    return sorted_list


if __name__ == '__main__':
    unsorted_list = [8, 4, 2, 5, 3, 1, 7, 2, 9, 14, 4, 102, -52]
    print(minimax(unsorted_list))