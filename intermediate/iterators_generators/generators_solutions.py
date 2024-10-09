import random


# Task 1
# Napis generator `even_numbers()`, ktory bude generovat donekonecna parne (sude) cisla
def even_numbers():
    num = 0
    while True:
        yield num
        num += 2


# Task 2
# Napis generator `my_range(start, stop=None, step=1), ktory sa sprava rovnako ako funkcia range

def my_range(start, stop, step=1):
    if step == 0:
        raise ValueError('Step cannot be 0')

    current = start
    if step >= 1:
        while current < stop:
            yield current
            current += step

    else:
        while current > stop:
            yield current
            current += step


# Task 3
# Napis generator `fib()`, ktory bude donekonecna generovat cisla fibonnaciho postupnosti
# 0 1 1 2 3 5 8 13...
def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


# Task 4
# Napis generator `read_file(file_name)`, ktory otvori subor `file_name` a bude
# postupne vracat jeho riadky
def read_file(file_name):
    with open(file_name) as file:
        for line in file:
            yield line.strip()


# Task 5
# Napis generator `randgen(start, end)`, ktory bude donekonecna generovat nahodne cisla
# v intervale <start, end>.
def randgen(start, end):
    while True:
        yield random.randint(start, end)


# Task 6
# Napis generatory `map` a `filter`, ktore sa spravaju ako builtin funkcie `map` a `filter`
def my_map(func, iterable):
    for obj in iterable:
        yield func(obj)


def my_filter(func, iterable):
    for obj in iterable:
        if func(obj):
            yield obj


if __name__ == "__main__":
    print("Task1")
    even_gen = even_numbers()
    for _ in range(5):
        print(next(even_gen))
    print()
    print("task2")
    for number in my_range(5, 1, -1):
        print(number)
    print()
    print("task3")
    fib_gen = fib()
    for _ in range(10):
        print(next(fib_gen))
    print()
    print("task4")
    for line in read_file('text.txt'):
        print(line)
    print()
    print("task5")
    rand_gen = randgen(1, 10)
    for _ in range(5):
        print(next(rand_gen), end=' ')
    print('\n')
    print("task6")
    print(
        list(map(lambda x: -x, range(-10, 11)))
        == list(my_map(lambda x: -x, range(-10, 11)))
    )

    print(
        list(filter(lambda x: x % 2 == 0, range(-10, 11)))
        == list(my_filter(lambda x: x % 2 == 0, range(-10, 11)))
    )
