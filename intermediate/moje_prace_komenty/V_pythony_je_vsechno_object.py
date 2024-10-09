def foo(x):
    return x**2
# vytvoreni promenne

print(dir(foo))
# dir = vypise vsechny atributy ktere obsahuje nase funkce

print(callable(foo))
print(callable(21))

def calleble(obj):
    return hasattr(obj, '__call__')

print(dir(foo))
print(callable(foo))
print(callable(21))


class Foo:
    def __call__(self, x):
        return x ** 2


instance = Foo()
print(instance(3))
print(callable(instance))



def bar(x, y):
    return x(y)


bar(abs, -3)
print(bar(abs, -3))


# Funkce map, filter

def is_even(x):
    return x % 2 == 0

print(map(abs, [-1, -2 , 3]))
# je potreba prevest na list aby byl vypis srozumitelny
print(list(map(abs, [-1, -2, 0])))
# cista funkce
print(list(filter(abs, [-1, -2, 0])))
# filter vypisuje pouze prvky ktere jsou True
print(list(filter(is_even, [-1, -2, 0])))
# vypisuje suda cisla

print(bool(0))

def mu_map(f, iterable):
    pass
