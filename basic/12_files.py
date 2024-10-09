#otevreni datovych souboru open(), close()

# open()
# "r" - režim čtení (výchozí hodnota).
# "w" - režim zápisu.
# "x" - režim vytváření. Pokud soubor již existuje, operace se nezdaří.
# "a" - režim vkládání na konec.
# "b" - binární režim.
# "t" - textový režim (výchozí hodnota).
# "+" - režim úprav (čtení / zápis).

# basen = open("basen_org_1250_ANSI_Stredna_europa.txt")

# print(basen.read())
# basen.close()

# WITH open
# with open("basen_org_1250_ANSI_Stredna_europa.txt") as basen:
    # print(basen.read(5))

    # print(basen.readline())

    # print(basen.readline())                # -> pri pouziti vicekrat si pamatuje kde skoncil
    #
    # print(basen.readlines())

    # radek = basen.readline()
    # while radek:
    #     print(radek, end="")
    #     radek = basen.readline()

# zapis

with open("01_novy.xtx", "w") as novy_soubor:
    for index in range(10):

        novy_soubor.write(f"radek s indexem {index}\n")

    novy_soubor.writelines(["Ahoj ", "dnes ", "je ", "pekny ", "den.\n"])



# prekopirovani souboru

with open("basen_org_1250_ANSI_Stredna_europa.txt") as basen:
    with open("01_novy.xtx", "a") as novy_soubor:

        novy_soubor.writelines(basen.read())
        # novy_soubor.writelines(basen.readline())
        print(basen.tell())
# create
with open("01_novy.xtx", "a") as novy_soubor:
    novy_soubor.write("\nPracujeme s creation modem.\n")
    print(novy_soubor.tell())
# append
with open("01_novy.xtx", "a") as soubor:
    soubor.write("radek pridany appendem.\n")
#
# binari modes

# with open("novy.xtx". "rb") as basen:
#     print(basen.readline())

# with open("novy.xtx", "wb") as novy_soubor:
#     novy_soubor.write(b"ucime se Python")


# with open("basen.txt") as basen:
#
# with open("basen.txt") as basen:
#
#  rw +
#     print(basen.tell())
#     print(basen.readline())
#     print(basen.tell())
#     print(basen.readline())
#     print(basen.tell())
#
#     basen.seek(0)
#     print(basen.readline())
#