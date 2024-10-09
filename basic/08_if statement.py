# Control instruction


# prsi = False
#
# if prsi:
#     print("Vezmu si destnik")
#     print("Budu mokry")
# print("Jdu nakupovat")
#
# if prsi:
#     print("Vem si destnik")
#     print("nejezdi na kole")
# else:
#     print("pojedu na kole")
#


cena = 150
vek = 100
pocet = 1
if vek <= 25:
    typ = "student"
    sleva = 0.2

elif vek >= 65:
    if vek >= 100:
        typ = "duchodce vyherce"
        sleva = 2
    else:
        typ = ("senior")
        sleva = 0.5
elif vek == 50:
    typ = "padesatnik"
    sleva = 1
else:
    print("plnolety")
    sleva = 0
print(f"Zakaznik je {typ} Cena listku je: {cena - cena * sleva} kc")


pocet_dni_dovolene = 12
volne_penize = 50000
jsem_nemocny = False

if pocet_dni_dovolene >= 10 and volne_penize >= 50000 and not jsem_nemocny:
    print("jedu na dovolenou")
else:
    print("jdi makat!!")

# if

mam_hlad = False
mam_chut = False

if mam_hlad or mam_chut:
    print("jdu se najist")
else:
    print("nejdu se najist")

# Zkracene

