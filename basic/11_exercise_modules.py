# Taks 1
# Mate 2 hraci kostky (1-6). Vytvor funkci hod_kostkou(), ktera vrati nahodne cislo,
# ktere “padlo”. V cyklu while hazej dvema kostkami dokud nepadne stejne cislo.
# Oba hody vzdy vypis do jednoho radku.
# priklad:
# 1 hod: 5, 1
# 2 hod: 4, 6
# 3 hod: 3, 3

import random

def hod_kostkou():
    number1 = random.randint(1, 6)
    number2 = random.randint(1, 6)
    return number1, number2

print(hod_kostkou())



