"""Sieve of Eratosthenes
https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
Napište program, který vygeneruje všechna prvočísla menší než N
pomocí algoritmu Eratosthenovo síto.

Eratosthenovo síto funguje tak, že postupně "odškrtáváte" násobky každého čísla počínaje 2,
které jsou tím pádem složená čísla. Čísla, která zůstanou neodškrtnutá, jsou prvočísla.
"""


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

i = 8
primes = []
for n in range(2, 200):
    if is_prime(n):
        primes.append(n)


def print_n_prime_numbers(n: int):
    for i in range(n+1):
        if is_prime(i):
            print(i, end=" ")
    print()


if __name__ == '__main__':
    print(f"Number {i} is {is_prime(i)} prime")
    print(primes) # vypise prvocisla
    n = 100
    print_n_prime_numbers(n)

# TODO napsat si timeit a zmerit rychlost pocitani