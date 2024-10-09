# users input
# vsechny data od uzivatele prevadi Python na string -> cisla je treba pretipovat do int!!
# input() pri zadani program ceka na vlozeni dat od uzivatele
# lepsi pro mensi programy
# print("spustil se prog na vypocet roku narozeni")
# jmeno_uzivatele = input("zadej sve jmeno: ")
# print(f"Ahoj {jmeno_uzivatele}, vitej v tomto programu!")
#
# vek_uzivatele = int(input("zadej svuj vek: "))
# print(f"Tvuj rok narozeni je {2024 - vek_uzivatele}")

#


 # 07_user_input.py Jarda 31

import sys             #['07_user_input.py', 'Jarda', '31']
print(sys.argv)

print("spustil se prog na vypocet roku narozeni")
jmeno_uzivatele = sys.argv[0]
print(f"Ahoj {jmeno_uzivatele}, vitej v tomto programu!")
#
# vek_uzivatele = int(sys.argv[2])
# print(f"Tvuj rok narozeni je {2024 - vek_uzivatele}")
#
# print(type(vek_uzivatele))

