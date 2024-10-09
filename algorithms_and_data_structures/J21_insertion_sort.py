from typing import List


def insertion_sort(unsorted: List[int]) -> List[int]:
    sorted_list = []  # vytvorim si prazdny list do ktereho postupne ukladam
    for i in range(len(unsorted)):  # range -> prochazi celi seznam (unsorted) pomoci jeho indexu do len(unsorted) -1
        # len vraci delku objektu -> tady je to delka seznamu
        # i = pozice cisla
        j = 0  # pozice v sorted listu na zacatku programu
        while j < len(sorted_list) and sorted_list[j] < unsorted[i]:
            # j < len(sorted_list) = pokud je pozice j mensi nez posledni pozice v seznamu and cislo na pozici
            # j v sorted_list je mensi nez cislo na pozici i v unsorted
            j += 1  # na dalsi pozici
        sorted_list.insert(j, unsorted[i]) # za cislo na pozici j pridej cislo ze seznamu unsorted na pozici i
        # na pozici
    return sorted_list


if __name__ == '__main__':
    my_numbers = [8, 4, 2, 5, 3, 1, 7, 2, 9, 14, 4, 2]
    print(insertion_sort(my_numbers))


