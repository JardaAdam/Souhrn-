def fibonacci(n):
    if n == 0 or n == 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


if __name__ == "__main__":
    for i in range(21):
        print(f"fib({i}) = {fibonacci(i)}")
