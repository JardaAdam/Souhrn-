"""Výhody tohoto způsobu (Bridge návrhový vzor):
Oddělení abstrakce od implementace:

Tento vzor umožňuje oddělit nápoje (abstrakci) od způsobu,
jakým jsou nakupovány (implementace). To znamená, že můžeme
měnit nápoje (např. přidávat nové jako džus nebo limonádu)
bez nutnosti měnit způsob nákupu. Stejně tak můžeme měnit
nebo přidávat nové způsoby nákupu (např. nákup online nebo v obchodě)
bez nutnosti měnit nápoje.
Zkrátka: když něco změníš nebo přidáš, nemusíš zasahovat do celého systému,
což snižuje chyby a usnadňuje údržbu.

Flexibilita a rozšiřitelnost:

Tento vzor je velmi flexibilní. Můžeme snadno přidat nový typ
nápoje nebo nový způsob nákupu bez toho, aby to ovlivnilo
ostatní části programu. Pokud bys například chtěl přidat
nový nápoj, jako je čokoláda, stačí vytvořit novou třídu a
nemusíš měnit stávající třídy.
To znamená, že tvůj program je připravený na růst a snadno se
přizpůsobí budoucím změnám.

Jednoduchost údržby:

Díky jasnému oddělení zodpovědností (nápoje a jejich nákup jsou oddělené),
je jednodušší najít chyby a upravovat kód, protože každá část má svůj
jasný úkol. Například pokud se něco pokazí v procesu nákupu, víš, že
chyba je v nákupní části, a nemusíš kontrolovat logiku nápojů.

Výpočetní náročnost:
Paměť a výpočetní výkon:

Paměť:
Kód s Bridge vzorem nevytváří zbytečné kopie dat a
využívá pouze ty objekty, které potřebuje. Použitím objektů
jako Coffee nebo Tea program spotřebuje paměť pouze na
potřebné vlastnosti a nákupní logiku.

Výpočetní náročnost:
Metody jako get_volume() nebo get_taste() jsou velmi jednoduché
(vrací předdefinovanou hodnotu), takže nemají významný vliv na výkon.
Tedy pokud bys měl tisíce různých nápojů, nebude to zpomalovat tvůj
program, protože každý nápoj je lehký a rychlý na vyvolání.

OOP (Objektově orientované programování):

Tento vzor využívá objektově orientované programování,
což může vyžadovat trochu více paměti (vytváříme více objektů),
ale přináší velkou výhodu v organizaci kódu a jeho čitelnosti.
Výměnou za mírně vyšší spotřebu paměti získáš flexibilitu a snadnou údržbu.

Shrnutí pro začátečníky:
Výhody: Tento přístup ti umožní snadno přidávat nové nápoje nebo
způsoby nákupu, aniž bys musel upravovat velkou část kódu.
Je to flexibilní a dobře se udržuje.

Výpočetní náročnost:
Kód nezpůsobuje žádnou zásadní zátěž na paměť nebo výkon,
protože používá jednoduché metody a objekty. Sice vytvoříme několik objektů navíc,
ale díky tomu je náš kód přehlednější a snadno rozšiřitelný."""

# Můžeme použít následující přístup k vytvoření Bridge:

"""Abstrakce: Drink jako obecný nápoj.
Implementace: Způsob nákupu nápoje (např. DrinkPurchase).
Bridge: Spojení mezi těmito dvěma dimenzemi (nápoj a nákup) pomocí kompozice,
kde Drink používá DrinkPurchase k provádění svých metod, jako je buy().
Například takto:
"""


# Definuj abstrakci
class Drink:    # rodicovska trida ktera jenom definuje jake funkce
    # naji jeji potomci mit a az pri vitvoreni potomka se musi funkce
    # implementovat
    def __init__(self, purchase):
        self._purchase = purchase

    def buy(self, cost):
        return self._purchase.buy(cost)

    def get_volume(self):
        raise NotImplementedError   # v pripade ze neni tato funkce
        # implementovana v potomkovi vypis...


    def get_taste(self):
        raise NotImplementedError

    # metoda pro vypsání informací o nápoji
    def vypis_info(self):
        print(f"Volume: {self.get_volume()}")
        print(f"Taste: {self.get_taste()}")


# Implementační rozhraní pro nákup
class DrinkPurchase:
    def buy(self, cost):
        raise NotImplementedError


# Konkrétní implementace nákupu
class CoffeePurchase(DrinkPurchase):
    def buy(self, cost):
        print(f"Buying a coffee for {cost}")
        return Coffee


class TeaPurchase(DrinkPurchase):
    def buy(self, cost):
        print(f"Buying a tea for {cost}")
        return Tea


# Konkrétní nápoje
class Coffee(Drink):
    def get_volume(self):
        return "150ml"

    def get_taste(self):
        return "bitter"


class Tea(Drink):
    def get_volume(self):
        return "250ml"

    def get_taste(self):
        return "sweet"


# Příklad Bridge použití:Tento přístup nyní umožňuje snadné vypsání
# informací o libovolném nápoji použitím stejného mechanismu,
# zatímco proces nákupu a specifikace nápojů jsou oddělené
# pomocí Bridge vzoru.

# Spojení nápoje a způsobu nákupu
coffee = Coffee(CoffeePurchase())
tea = Tea(TeaPurchase())

# Nákup nápoje a vypsání informací
coffee.buy(50)
tea.buy(30)

# Vypsání informací o nápojích
print("\nInformation about Coffee:")
coffee.vypis_info()

print("\nInformation about Tea:")
tea.vypis_info()