from dataclasses import dataclass

"""pro praxy vyhoda ze drzime data. Uloziste dat"""


@dataclass
class Rectangle:
    a: int
    b: int = 0
    """muzu si tu definovat hodnotu za =  """

    def circuit(self):
        return 2 * (self.a + self.b)

    def area(self):
        return self.a * self.b


if __name__ == "__main__":
    p1 = Rectangle(3, 4)
    p2 = Rectangle(3, 4)
    print(p1)
    print(p1 == p2)

"""aby jsme stejneho zapisu docilili obycejnou cestou zapis vypada takto"""

# class Rectangle:
#     def __init__(self, a: int, b: int):
#         self.a = a
#         self.b = b
#
#     def __repr__(self) -> str:
#         return f"Rectangle(a={self.a}, b={self.b})"
#
#     def __eq__(self, other) -> bool:
#         return isinstance(other, Rectangle) and (self.a, self.b) == (other.a, other.b)
#
#     def circuit(self) -> float:
#         return 2 * (self.a + self.b)
#
#     def area(self) -> float:
#         return self.a * self.b