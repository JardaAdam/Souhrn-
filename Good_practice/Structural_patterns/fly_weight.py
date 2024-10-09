"""Flyweight (česky „lehká váha“) je návrhový vzor, který se
používá ke snížení paměťové náročnosti při vytváření velkého
množství objektů. Funguje tak, že sdílí co nejvíce dat mezi
podobnými objekty, aby se zabránilo vytváření více kopií téhož."""

"""Příklad:
Představ si, že máme aplikaci, která vykresluje stromy v lese. 
Každý strom může mít svou polohu, ale všechny stromy stejného 
druhu mají stejné vlastnosti (barvu, typ listí, výšku). 
Místo toho, aby pro každý strom v lese vytvářela aplikace 
zvláštní objekt, můžeme sdílet společné vlastnosti mezi stromy 
stejného typu."""

# Flyweight třída (sdílené vlastnosti stromu)
"""TreeType (Flyweight): 
Toto je třída, která uchovává sdílené vlastnosti 
stromů (jako barva, název a textura). Každý strom stejného typu bude 
mít stejné vlastnosti, takže tuto třídu můžeme sdílet mezi objekty."""
class TreeType:
    def __init__(self, name, color, texture):
        self.name = name      # Název druhu stromu
        self.color = color    # Barva stromu
        self.texture = texture  # Textura listí/stromu

    def draw(self, x, y):
        print(f"Drawing a {self.name} tree of color {self.color} at ({x}, {y})")


# Flyweight Factory (vytváří nebo vrací existující typy stromů)
"""TreeFactory: 
Toto je továrna (factory), která nám vrací již vytvořené objekty typu 
TreeType. Pokud jsme daný typ stromu už vytvořili, továrna vrátí 
existující objekt, místo toho, aby vytvářela nový."""
class TreeFactory:
    _tree_types = {}  # Slovník pro uchování již vytvořených typů stromů

    @staticmethod
    def get_tree_type(name, color, texture):
        # Pokud již daný typ stromu existuje, vrátíme ho
        if (name, color, texture) not in TreeFactory._tree_types:
            TreeFactory._tree_types[(name, color, texture)] = TreeType(name, color, texture)
        return TreeFactory._tree_types[(name, color, texture)]


# Konkrétní strom (má unikátní polohu, ale sdílí typ stromu)
"""Tree:
Tato třída uchovává individuální pozici stromu (např. souřadnice x a y) 
a odkazuje na sdílený TreeType."""
class Tree:
    def __init__(self, x, y, tree_type):
        self.x = x  # Pozice X stromu
        self.y = y  # Pozice Y stromu
        self.tree_type = tree_type  # Typ stromu (sdílené vlastnosti)

    def draw(self):
        # Deleguje kreslení na Flyweight (TreeType)
        self.tree_type.draw(self.x, self.y)


# Třída pro les (uchovává a kreslí stromy)
"""Forest: 
Třída, která reprezentuje celý les. Obsahuje všechny stromy a dokáže 
je vykreslit."""
class Forest:
    def __init__(self):
        self.trees = []  # Seznam všech stromů v lese

    def plant_tree(self, x, y, name, color, texture):
        # Získej typ stromu z Flyweight Factory
        tree_type = TreeFactory.get_tree_type(name, color, texture)
        # Vytvoř strom s unikátní polohou a sdíleným typem
        tree = Tree(x, y, tree_type)
        self.trees.append(tree)

    def draw_forest(self):
        for tree in self.trees:
            tree.draw()


# Použití Flyweight vzoru
forest = Forest()

# Zasazení několika stromů
forest.plant_tree(10, 20, "Oak", "green", "rough")
forest.plant_tree(15, 25, "Pine", "dark green", "smooth")
forest.plant_tree(10, 30, "Oak", "green", "rough")  # Sdílený typ stromu Oak

# Kreslení celého lesa
forest.draw_forest()

"""
Popis pro začátečníka:
Proč Flyweight?
Pokud máš velké množství objektů (například tisíce stromů v lese), 
každý objekt může zabírat hodně paměti, hlavně pokud všechny stromy 
stejného druhu mají podobné vlastnosti (barvu, typ stromu, texturu). 
Flyweight umožňuje sdílení společných vlastností (jako barva, textura) 
mezi objekty, aby se ušetřila paměť.

Jak to funguje?

Úspora paměti:
V našem příkladu dva různé stromy typu "Oak" (Oak tree of color green) 
mají stejné vlastnosti, jako je barva a textura. Namísto vytváření dvou 
samostatných objektů pro každý z nich (což by zbytečně zabíralo paměť), 
sdílíme jeden objekt TreeType mezi oba stromy.

Výpočetní náročnost:

Paměťová úspora: 
Tento vzor šetří paměť tím, že pro stejný druh stromu nevytváříme 
více kopií jejich vlastností. Namísto toho sdílíme jeden objekt 
TreeType mezi více stromy.

Časová náročnost:
Vytvoření objektu stromu je mírně pomalejší, protože musíme zkontrolovat, 
zda daný typ stromu už existuje, nebo jej musíme vytvořit. 
Ale tento čas je velmi malý ve srovnání s paměťovou úsporou při práci 
s velkým množstvím objektů."""