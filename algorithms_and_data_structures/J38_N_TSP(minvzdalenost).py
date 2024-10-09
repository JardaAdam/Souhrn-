""" Problém obchodního cestujícího (TSP)
Dostali jste úkol naplánovat trasu obchodního cestujícího,
který musí navštívit všechna města v seznamu přesně jednou a poté se vrátit zpět do výchozího města.
Napište program, který najde nejkratší možnou trasu (minimální vzdálenost),
kterou může obchodní cestující absolvovat.
"""

from itertools import permutations


def count_distance(Cities, path):
    distance = 0  # pocatecni vzdalenost
    # nasledne prochazim vsechna mesta a pricitam vzdalenost
    for i in range(len(path) - 1):
        distance += Cities[path[i]][path[i + 1]]

    # pridani vzdalenosti zpet do vychoziho mesta
    distance += Cities[path[-1]][path[0]]
    # vratim vyslednou vzdalenost
    return distance


def tsp():
    n = len(cities)
    all_paths = permutations(range(n))
    minimal_distance = float('inf')  # inicializace s nekonecnem
    best_path = None

    for path in all_paths:
        # spočítat vzdálenost aktuální trasy -> vytvořím si pomocnou funkci
        actual_distance = count_distance(cities, path)
        print(f"path={path}, distance={actual_distance}")
        # pokud je aktuální trasa kratší, než dříve nalezená minimal_distance, tak si ji uložím
        if actual_distance < minimal_distance:
            minimal_distance = actual_distance
            best_path = path
    # vrátím výslednou nejkratší trasu
    return best_path, minimal_distance


if __name__ == '__main__':
    cities = [
        # A   B   C   D
        [0, 10, 15, 20],  # A
        [10, 0, 35, 25],  # B
        [15, 35, 0, 30],  # C
        [20, 25, 30, 0]  # D
    ]

    best_path, minimal_distance = tsp()
    print(f"Nejkratší trasa je: {best_path} s minimální vzdáleností: {minimal_distance}")
