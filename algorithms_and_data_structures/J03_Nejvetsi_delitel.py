# algoritmus vypočtu největšího společného dělitele

a = int(input('Enter number a: '))
b = int(input('Enter number b: '))
while a != b:
    if a > b:
        a = a - b
    else:
        b = b - a
#
print(f"nejvetsi spolecny delitel je: {a}")

# pomoci fce

def gcd(a, b):
    while a != b:   # != porovnani dvou hodnot pokud jsou rovne vraci False
        if a > b:
            a = a - b   # da se zapsat jako a -= b
        else:
            b = b - a   # b -= a
    return a

print(f'nejvetsi spolecny delitel {a} a {b} je {gcd(a, b)}')

# dalsi moznost
def gcd2(a, b):
    n = min(a, b)
    for i in range(n, 0, -1):
        if a % i == 0 and b % i == 0: # % = dělitelné bezezbytku
            return i


print(f'nejvetsi spolecny delitel2 {a} a {b} je {gcd2(a, b)}')

# TODO dodelat testy