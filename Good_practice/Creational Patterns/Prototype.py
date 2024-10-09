# vytváření objektů se skládá ze dvou kroků.

# vytvoření základního objektu (např. částečně dokončeného), prototypu, který se
# naklonuje za účelem výroby nových objektů

# nastavení zbývajících atributů objektů

# pouzivame na slozitejsi projekty

# je vhodny pro objekty ktere maji vetsinu vlastnosti shodnou a potrebujeme je v nove instanci

# deep.copy = chci si uchovat original ale pouzit ho pro dalsi praci.
#   = zkopiruju si a ulozim vysledek narocne operace (ktera muze trvat treba 30min)
# a s kopii pracuji dal ale nezmenim original.


import copy


class Shape:
    def __init__(self, color):
        self.color = color

    def clone(self):
        return copy.deepcopy(self)

class Circle(Shape):
    def __init__(self, radius, color):
        super().__init__(color)
        self.radius = radius

    def __str__(self):
        return f"Circle with radius {self.radius} and color {self.color}"

class Rectangle(Shape):
    def __init__(self, width, height, color):
        super().__init__(color)
        self.width = width
        self.height = height

    def __str__(self):
        return f"Rectangle with width {self.width}, height: {self.height}"

