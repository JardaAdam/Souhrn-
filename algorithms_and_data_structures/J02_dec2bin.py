# prevod cisla z desitkove soustavi do binarni

d = int(input("Enter positive decimal number: "))
binary = ''
while True:
    r = d % 2
    if r == 1:
        binary = '1' + binary
    else:
        binary = '0' + binary
    d = d // 2
    if d == 0:
        print(binary)
        break

# optimalizace kodu

d = int(input("Enter positive decimal number: "))
binary = ''
while d > 0:        # odstranim True a nemusim psat break!!
    r = d % 2
    if r == 1:
        binary = '1' + binary
    else:
        binary = '0' + binary
    d = d // 2
    if d == 0:
        print(binary)

print("prepis do funkce")
# d = int(input("Enter positive decimal number: "))

def dec2bin(d):  # d = cislo ktere musim vlozit
    binary = ''

    while True:
        r = d % 2

        if r == 1:
            binary = '1' + binary
        else:
            binary = '0' + binary

        d = d // 2

        if d == 0:
            return (binary)

if __name__ == "__main__":
    print(dec2bin(d))

    for i in range(1, 200):
        print(f"{i}: {dec2bin(i)}")

#TODO dodelat testy