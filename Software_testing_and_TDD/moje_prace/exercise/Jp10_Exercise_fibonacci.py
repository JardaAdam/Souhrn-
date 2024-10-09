def fibonacci(n: int) -> int:
    if n <= 0:
        return 0
    elif n == 1:
        return 1
# rekurzivni fce 'fibonacci'
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)
# fibonaci 10 je soucet fibonacci pro 8 a 9 takze soucet 21 a 34
# Iterativni pristup
    a, b = 0, 1
    for _ in range(2, n + 1): # _ je zde promenna na jedno pouziti
        a, b = b, a + b
    return b


if __name__ == "__main__":
    for i in range(20):
        print(f"Number {i} = {fibonacci(i)}")
