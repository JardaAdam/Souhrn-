"""
Eratosthenovo síto funguje tak, že postupně "odškrtáváte" násobky každého čísla počínaje 2,
které jsou tím pádem složená čísla. Čísla, která zůstanou neodškrtnutá, jsou prvočísla.
"""

"""
0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20
F  F  T  T  F  T  F  T  F  F   F   T   F   T   F   F   F   T   F   T   F
"""
n = 100



# i = index cisla
def sieve_of_eratosthenes(n):
    # vygenerujeme seznam sieve velikosti n+1 (True)
    sieve = [True] * (n + 1)

    # sieve[0] a sieve[1] = False
    sieve[0] = sieve[1] = False  # oznacil jsem si cisla 0, 1 jako False protoze nejsou prvocisli

    # posouvám se v seznamu, každé číslo, které je True, je prvočíslo -> vypíšu
    for i in range(2, (n + 1) // 2):  # //2 -> staci projit prvni pulku seznamu proto delim celkove cislo na pul
        if sieve[i]:
            for j in range(i * 2, n + 1, i):
                # první číslo v seznamu, které je True, je prvočíslo, smažu všechny jeho násobky ze seznamu (False)
                sieve[j] = False

    # vypíšu indexy, na kterých je True
    for i in range(n + 1):
        if sieve[i]:
            print(i, end=" ")
    print()


if __name__ == '__main__':
    sieve_of_eratosthenes(n)

# TODO napsat si timeit a zmerit rychlost pocitani u n = 1 000 000
