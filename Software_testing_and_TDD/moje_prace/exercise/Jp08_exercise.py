def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def factorial(n: int) -> int:
    if n < 0:
        raise ValueError

    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


if __name__ == "__main__":
    for i in range(21):
        print(f"Number {i}: is_prime({i}) = {is_prime(i)}"),
#        (f"Number {i}: factorial({i}) = {factorial(i)}")
