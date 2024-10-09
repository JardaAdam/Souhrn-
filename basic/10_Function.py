



def vypis_programu():
    print("Zprava z progranu meteor")   #
    print("aktualni datum: 29.5.2024")
    print("Dnesni teploty: 20°C")
    print("." * 20 )
vypis_programu()



# def secti(cislo1, cislo2):
#     print(cislo1 + cislo2)

# secti(7, 5)

#
def predstaveni_cloveka(jmeno, prijmeni, titul):
    print(f"{titul}. {jmeno} {prijmeni}")

predstaveni_cloveka("Zdenek", "Volny", "Mgr")  # pozicni umisteni
predstaveni_cloveka(prijmeni="Omacka", titul="Ing", jmeno="Jan")
predstaveni_cloveka("Dana", titul="Bc", prijmeni="Nestihl")

# Tipovani promenych
#

def predstaveni_cloveka(jmeno: str, prijmeni: str, titul: str):
    print(f"{titul}. {jmeno} {prijmeni}")

# Default parameters: preddefinovana hodnota


def vypocet_mocniny(mocnenec: int, mocnitel: int=2):
    print(mocnenec ** mocnitel)

vypocet_mocniny(7)
vypocet_mocniny(4,3)

def registrace_lajnera(jmeno: str, prijmeni: str, vek: int, pohlavi: str = "muz"):
    print(f"lajner: {jmeno} {prijmeni}. Vek: {vek}. Pohlavi: {pohlavi}")

registrace_lajnera("Jarda", "Adam", 31)





def spocti_rok_narozeni(vek: int):
    global aktualni_rok         # nedoporucuje se delat! vytvori se az po spusteni funkce
    aktualni_rok = 2024
    return aktualni_rok - vek

rok_narozeni = spocti_rok_narozeni(50)
print(rok_narozeni)
print(aktualni_rok)

# vice navratovich hodnot

def kalkulacka(cislo1: int, cislo2: int) -> tuple:  # Tuple -> neprepsatelny list
    return cislo1 + cislo2, cislo1 - cislo2, cislo1 / cislo2, cislo1 * cislo2

print(kalkulacka(10, 5))
print(kalkulacka(10,5)[1])

# promenliva kalkulacka

def secti(list_cisel: list) -> int :
    vysledek = 0
    for cislo in list_cisel:
        vysledek += cislo

    return vysledek

print(secti([1, 5, 6]))
# Add
# ARGS  *args  pridavame vlastni hodnoty
print("priklad_*arg")
def secti(*cisla) -> int:
    vysledek = 0
    for cislo in cisla:
        vysledek += cislo

    return vysledek

print(secti(4, 5, 8, 9, 3))

print("priklad_**kwargs")
def soucet_ingredienci(**ingredience):
    soucet = 0
    for polozka, pocet in ingredience.items(): #items()
        soucet += pocet

    return soucet

print(soucet_ingredienci(banan=2, jablko=3, pomeranc=4, maslo=2))

#

def popis_rodiny(jmeno_rodiny, **cleni):
    print(f"predstaveni rodiny: {jmeno_rodiny}")
    for role, jmeno in cleni.items():
        print(f"{role.capitalize()}: {jmeno}")

popis_rodiny("novakovi", otec="Petr", matka="lucie", syn="Tomas", dcera="Libuse")



#
#
def spocti_rok_narozeni(age: int):
    """
    Spocitani roku narozeni podle veku uzivatle. od 2024 se odecte vek na vstupu
    :param age: Aktualni vek uzivatele
    :return: vypocitany rok narozeni. (presnost +- rok)
    """
    return 2024 - age

print(spocti_rok_narozeni(25))

#stinove nazvy promennych\funkci -> pozor na prepisovani jiz zadanych veci!!!
# print = 1
# print("Ahoj")

#prejmenovani funkci

vypocti_rok_narozeni = spocti_rok_narozeni

print(vypocti_rok_narozeni(19))















