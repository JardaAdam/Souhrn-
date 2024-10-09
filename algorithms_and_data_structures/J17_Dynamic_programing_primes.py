"""
Výpis všech prvočísel do zadaného n (10000)
s využitím dynamického programování.
"""
from typing import List


# pomoci mezipameti si pamatuji predchozi vysledky a nepocitam kazde cislo zvlast znovu
def is_prime(n: int, memory: List[int]) -> bool:
    if n < 2:
        return False
    for i in memory:
        if i > (n ** 0.5) + 1:
            return True
        #print(f"Testuji delitelnost {i}")
        if n % i == 0:  # pokud je cislo delitelne bezezbytku
            return False
    return True


# vypsat všechna prvočísla menší než n (10000)
def print_n_prime_numbers(n: int):
    memory = []
    for i in range(n + 1):
        if is_prime(i, memory):
            memory.append(i)
    print(memory)


if __name__ == '__main__':
    print_n_prime_numbers(100)
    #print(is_prime(997))
