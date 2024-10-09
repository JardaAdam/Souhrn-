"""Dekorátory v Pythonu jsou užitečný nástroj, který umožňuje
modifikovat chování funkcí nebo metod bez nutnosti měnit jejich kód.
V praxi to znamená, že můžeme obalit funkci jinou funkcí, která před
nebo po vykonání původní funkce provede nějakou akci."""

"""Představ si, že chceme logovat (vypisovat) informace o tom, 
kdy se funkce zavolá. Toho můžeme dosáhnout pomocí dekorátoru."""

"""Dekorátor je speciální funkce, která přijímá jako parametr jinou 
funkci, modifikuje její chování, a pak ji vrací zpět."""


# 1. Definuj dekorator
# Dekorátor loguje, kdy byla funkce zavolána

def logovani(funkce):
    def obalena_funkce(*args, **kwargs):
        print(f"Funkce {funkce.__name__} byla zavolána.")
        # Volání původní funkce s jejími parametry
        return funkce(*args, **kwargs)

    return obalena_funkce


# 2. Použití dekorátoru
# Teď použijeme náš dekorátor k obalení nějaké funkce.
# Dekorátor se aplikuje na funkci pomocí symbolu @.
@logovani
def pozdrav(jmeno):
    print(f"Ahoj, {jmeno}!")


# 3. Volání dekorované funkce
# Když teď zavoláme funkci pozdrav(), nejdřív se vykoná kód v dekorátoru
# (který vypíše, že byla zavolána funkce), a pak se zavolá samotná funkce
# pozdrav().

pozdrav("Karle")

"""Shrnutí:
Dekorátor je skvělý nástroj, když chceš upravit chování funkcí, 
aniž bys je musel přímo měnit. V našem příkladu dekorátor logovani 
vypíše zprávu pokaždé, když je funkce zavolána. Stačí jen použít 
@logovani před definicí funkce, kterou chceme dekorovat."""
