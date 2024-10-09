# 1 Vytvořte třídu Osoba: Vytvořte třídu Osoba, která bude mít atributy jmeno a vek.
# Poté vytvořte několik instancí této třídy a vypište je.
class Osoba:

    def __init__(self, jmeno: str, vek: int, pohlavi: str):
        self.jmeno = jmeno
        self.vek = vek
        self.pohlavi = pohlavi
    def predstav_se (self):
        print(f"Ahoj ja jsem {self.jmeno},je mi {self.vek}let, a jsem {self.pohlavi}")

# TODO vytvarim osoby

Honza = Osoba("Honza", 35, "muz")
Katka = Osoba("Katka", 40, "zena")
Petr = Osoba("Petr", 50, "muz")
Honza.predstav_se()
Katka.predstav_se()
Petr.predstav_se()
print(Katka.pohlavi)
# 2 Výpočet Obvodu a Plochy obdélníka: Vytvořte třídu Obdelnik, která bude mít atributy delka a sirka.
# Přidejte metody pro výpočet obvodu a plochy obdélníka.



# 3 Kalkulačka: Vytvořte třídu Kalkulacka, která bude mít metody pro základní matematické operace
# (sčítání, odčítání, násobení, dělení).


# 4 Správce Knižního Regálu: Vytvořte třídu Kniha, která bude mít atributy nazev a autor. Poté vytvořte třídu Regal,
# která bude spravovat knihy (přidání, odebrání, výpis).


# 5 Vytvoření Kruhu: Vytvořte třídu Kruh, která bude mít atribut polomer. Přidejte metodu pro výpočet obvodu kruhu.


# 6 Jednoduchá To-Do List: Vytvořte třídu TodoList, která bude umožňovat přidávání, odebírání a výpis úkolů.


# 7 Bankovní Účet: Vytvořte třídu BankovyUcet, která bude mít atributy sazba (úroková sazba) a zustatek
# (aktuální zůstatek). Přidejte metodu pro výpočet úroku.


# 8 Kalendář: Vytvořte třídu Datum, která bude mít atributy den, mesic a rok.
# Přidejte metodu pro výpis data ve formátu "DD.MM.YYYY".


# 9 Zákazník a Objednávka: Vytvořte třídu Zakaznik s atributy jmeno a email. Vytvořte třídu Objednavka s atributem
# polozky a metodou pro výpočet celkové ceny objednávky.


# 10 Geometrické tvary: Vytvořte třídu Tvar, která bude mít metody pro výpočet obvodu a plochy. Poté vytvořte třídy
# Ctverec a Trojuhelnik, které budou dědit od třídy Tvar a implementovat tyto metody pro své specifické tvary.