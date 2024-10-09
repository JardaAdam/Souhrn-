"""
Co se zde děje:
DrawingAPI je rozhraní, které definuje metodu pro vykreslení kruhu.
DrawingAPI1 a DrawingAPI2 jsou dvě různé implementace vykreslovacího API.
Shape je abstraktní třída, která obsahuje odkaz na vykreslovací API.
CircleShape je konkrétní tvar, který používá specifické API pro vykreslení kruhu.
Použitím tohoto vzoru lze snadno přidávat nové tvary (např. čtverec) nebo nové způsoby vykreslování
(např. jiná knihovna pro 3D vykreslování) bez nutnosti měnit existující kód.
"""


# Krok 1: Rozhraní pro vykreslovací API
class DrawingAPI:
    def draw_circle(self, x, y, radius):
        pass

# Krok 2: Konkrétní implementace vykreslovacího API
class DrawingAPI1(DrawingAPI):
    def draw_circle(self, x, y, radius):
        print(f"API1: Kreslení kruhu o středu ({x}, {y}) a poloměru {radius}")

class DrawingAPI2(DrawingAPI):
    def draw_circle(self, x, y, radius):
        print(f"API2: Kreslení kruhu o středu ({x}, {y}) a poloměru {radius}")

# Krok 3: Abstraktní třída Shape
class Shape:
    def __init__(self, drawing_api: DrawingAPI):
        self._drawing_api = drawing_api

    def draw(self):
        pass

    def resize(self, factor):
        pass

# Krok 4: Konkrétní třída pro kruh
class CircleShape(Shape):
    def __init__(self, x, y, radius, drawing_api: DrawingAPI):
        super().__init__(drawing_api)
        self._x = x
        self._y = y
        self._radius = radius

    def draw(self):
        # Využití DrawingAPI pro vykreslení kruhu
        self._drawing_api.draw_circle(self._x, self._y, self._radius)

    def resize(self, factor):
        # Zvětšení poloměru kruhu
        self._radius *= factor

# Testování Bridge vzoru
circle1 = CircleShape(1, 2, 3, DrawingAPI1())
circle2 = CircleShape(5, 7, 11, DrawingAPI2())

# Kreslení kruhů pomocí různých API
circle1.draw()  # Použije DrawingAPI1
circle2.draw()  # Použije DrawingAPI2

# Změna velikosti kruhu a jeho opětovné vykreslení
circle1.resize(2)
circle1.draw()  # Větší kruh, použití DrawingAPI1