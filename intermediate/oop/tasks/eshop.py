# Napis triedu Basket (z angl. košík), ktora bude v sebe uchovavat list poloziek (Item).
# bude obsahovat nasledovne metody:
# - add_item()
# - print_basket()
# - calculate_price() (treba zaokruhlit na 2 desatinne miesta (funkcia round))

class Basket:

    def __init__(self):
        """Inicializace prázdného košíku (seznamu)"""
        self.items = []

    def add_item(self, item):
        """Přidá položku do košíku"""
        self.items.append(item)
        print(f"item '{item.name_item}' was add to basket")

    def print_basket(self):
        """print contents of the basket"""
        if not self.items:
            print("basket is empty.")
        else:
            print("items in basket:")
        for item in self.items:
            print(f" - {item}")
    def calculate_price(self):
        """Vypocita celkovou cenu polozek v kosiku"""
        total_price = sum(item.get_price() for item in self.items)
        return round(total_price, 2)



# Dalej napis triedu Item, ktory bude reprezentovat polozku. Kazda polozka bude mat atributy
# - Name
# - unit_price (jednotkova cena)
# - quantity (mnozstvo)
# a metodu get_price(), ktora vypocita cenu polozky

class Item:


    def __init__(self, name_item, unit_price, quantity_item):
        self.name_item = name_item
        self.unit_price = unit_price
        self.quantity_item = quantity_item

    def get_price(self):
        """return total price based on unit price and quantity"""
        return self.unit_price * self.quantity_item

    def __str__(self):
        return f"{self.name_item}: {self.quantity_item} x {self.unit_price} Kč = {self.get_price()} kč"

# Na zaver napis triedu WeightedItem (vazena polozka), ktora bude dedit z Item a bude mat navyse atribut `weight` (vaha)
# Atribut quantity bude mat vzdy hodnotu 1 a unit_price bude reprezentovat cenu za kilo.
# metoda get_price() teda bude musiet byt pre WeightedItem prepisana.

class WeightedItem(Item):

    def __init__(self, name_init, unit_price, weight):
        super().__init__(name_init, unit_price, 1)
        self.weight = weight

    def get_price(self):
        """return total price based on unit price and weight"""
        return round(self.unit_price * self.weight, 2)

    def __str__(self):
        return f"{self.name_item}: {self.weight} kg x {self.unit_price} kč/kg = {self.get_price()} kč"

# Priklad pouzitia:
if __name__ == "__main__":
    # Banan 27.90kc/kg, 2.61 kilo
    bananas = WeightedItem('banan', 27.90, 2.61)
    # 5 avokad za cenu 32Kc
    avocado = Item('avokado', 32, 5)
    # Jeden balik 4xAA bateriek za 89.90
    batteries = Item('baterky', 89.90, 1)

    # Vsetko hodime do kosiku
    basket = Basket()
    for item in [bananas, avocado, batteries]:
        basket.add_item(item)

    print(basket.print_basket())  # Vypise v rozumnom tvare zoznam poloziek v kosiku
    print(basket.calculate_price())  # Vypise 322.72
