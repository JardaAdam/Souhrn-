def prv(n):
    p = []
    delitel = 2
    while n >1:
        if n % delitel == 0:
            p.append(delitel)
            n //= delitel
        else:
            delitel += 1
    return p

n = int(input("Enter number: "))
print(prv(n))

#TODO dodelat testy