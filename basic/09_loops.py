# # iterations infinite iteration While nekonecne opakujici se

# TODO while

#
# cislo = 10
#
# while cislo > 0:
#     # print(cislo)
#     cislo -= 1
#
# # nekonecny cyklus
# n = 0
# while 1:
#     # print(f"nekonecny cyklus - {n}")
#     n += 1

# break zastaveni cyklu
# cislo = 10
#
# while cislo > 0:
#
#     cislo -= 1
#
#     if cislo in [8,7,2]:
#         continue
#     if cislo == 4:
#         break

    # print(cislo)
#  TODO  For
# definovana iteration je jasne dany pocet opakovani (for)
# for loop pouzivame k nemu kolekce napr. list
list_jmen = ["Petr","Honza","Kuba","Jaromir"]

# for jmeno in list_jmen:
#     print(jmeno)
#
#     list_cisel = [1,2,3,4,5]
#     vysledek = 0
#
#     for cislo in list_cisel:
#         vysledek += cislo
#
#     print(vysledek)

# items

phonebook = {"Honza" : 12345,
             "Marek" : 67890,
             "deda" : 98765}


print(phonebook.items())

# for kontakt in phonebook:
#     print(kontakt)
#     print(kontakt[kontakt])
#
# for kontakt in phonebook.items():
#     print(kontakt)
#
# for kontakt in phonebook.items():
#     jmeno, cislo = kontakt
#     print(f"kontakt {jmeno} ma cislo {cislo}")


# brake, continue
list_jmen = ["Petr","Honza","Kuba","Jaromir"]
for jmeno in list_jmen:

    if jmeno == "Jaromir":
        break

    if jmeno == "Petr":
            continue



    print(jmeno)

# range
#
# for cislo in range(100):
#     print(cislo)

# enumerate
list_jmen = ["Petr","Honza","Kuba","Jaromir"]

for poradi, jmeno in enumerate(list_jmen, start=1):
    print(f"Bezec {jmeno} se umistil na {poradi}.")




list_mocnin = []
for cislo in range(1, 101):
    list_mocnin.append(cislo ** 2)
# Folded list
list_cisel = [cislo ** 2 for cislo in range(1, 101)]

print(list_mocnin)

# zrychlene

# list_cisel = [cislo for cislo in range(1000)]
# print(list_cisel)

#list_asci

# slovnik




slovnik_mocnin = {cislo: cislo ** 2 for cislo in range(1,101)}
print(slovnik_mocnin)

# vnoreny cyklus
matice_2d = [[1,2,3],[4,5,6],[7,8,9]]

for radek in matice_2d:
    # print(matice_2d)
    # [1, 2, 3]
    # [4, 5, 6]
    # [7, 8, 9]
    for cislo in radek:
        print(cislo)

