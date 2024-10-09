# 1. Definuj Abstrakci (Shape)
# Shape je abstraktní třída, která představuje základní abstrakci pro různé tvary.
# Obsahuje odkaz na DrawingAPI, který bude použit k vykreslování tvaru.
class Shape:
    def __init__(self, drawing_api):
        # Drawing API je uloženo do proměnné, což umožňuje volání jeho metod.
        self._drawing_api = drawing_api

    # Abstraktní metoda, kterou musí každá třída, která rozšiřuje Shape, implementovat.
    def draw(self):
        raise NotImplementedError

    # Abstraktní metoda pro změnu velikosti tvaru, kterou je třeba implementovat.
    def resize(self, factor):
        raise NotImplementedError


# 2. Definuj Implementační Rozhraní (DrawingAPI)
# DrawingAPI je rozhraní, které definuje metodu pro vykreslení kruhu.
# Různé implementace DrawingAPI budou poskytovat různé způsoby vykreslení tvarů.
class DrawingAPI:
    def draw_circle(self, x, y, radius):
        # Tato metoda bude implementována v konkrétních implementacích.
        raise NotImplementedError


# 3. Definuj Konkrétní Implementace (DrawingAPI1 a DrawingAPI2)
# Třída DrawingAPI1 je konkrétní implementace DrawingAPI, která vykresluje kruh určitým způsobem.
class DrawingAPI1(DrawingAPI):
    def draw_circle(self, x, y, radius):
        # Zde se definuje specifický způsob vykreslení kruhu pro API1.
        print(f"Drawing API 1: Circle at ({x}, {y}) with radius {radius}")


# Třída DrawingAPI2 je jiná konkrétní implementace DrawingAPI, která vykresluje kruh jiným způsobem.
class DrawingAPI2(DrawingAPI):
    def draw_circle(self, x, y, radius):
        # API2 používá jiný způsob vykreslení kruhu než API1.
        print(f"Drawing API 2: Circle at ({x}, {y}) with radius {radius}")


# 4. Rozšiř Abstrakci (Circle)
# Třída Circle je konkrétní tvar (kruh), který dědí od Shape.
# Může používat libovolnou implementaci DrawingAPI pro vykreslení kruhu.
class Circle(Shape):
    def __init__(self, x, y, radius, drawing_api):
        # Inicilizuje Shape s konkrétním DrawingAPI a nastaví souřadnice a poloměr kruhu.
        super().__init__(drawing_api)
        self._x = x  # X-ová souřadnice středu kruhu
        self._y = y  # Y-ová souřadnice středu kruhu
        self._radius = radius  # Poloměr kruhu

    def draw(self):
        # Tato metoda využívá aktuální DrawingAPI k vykreslení kruhu.
        self._drawing_api.draw_circle(self._x, self._y, self._radius)

    def resize(self, factor):
        # Zvýšení (nebo snížení) velikosti kruhu násobením poloměru zadaným faktorem.
        self._radius *= factor


# Použití Bridge vzoru:

# Vytvoření instance Circle s implementací DrawingAPI1
circle1 = Circle(5, 10, 7, DrawingAPI1())

# Kreslí kruh s využitím API1
circle1.draw()  # Výstup: Drawing API 1: Circle at (5, 10) with radius 7

# Zvětšení kruhu o faktor 2
circle1.resize(2)

# Opětovné vykreslení zvětšeného kruhu s využitím API1
circle1.draw()  # Výstup: Drawing API 1: Circle at (5, 10) with radius 14

# Vytvoření druhé instance kruhu s implementací DrawingAPI2
circle2 = Circle(15, 20, 10, DrawingAPI2())

# Kreslí kruh s využitím API2
circle2.draw()  # Výstup: Drawing API 2: Circle at (15, 20) with radius 10

# TODO video pokracovani 1:56:00 2024-09-04
