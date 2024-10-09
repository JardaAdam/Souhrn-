"""Abstraktní třída je zobecněním jiných tříd, ale sama o sobě neexistuje (nelze vytvářet objekty tohoto typu).
Například třídy jako Kruh, Čtverec a Trojúhelník odpovídají skutečným geometrickým útvarům a každá z nich
má specifické vlastnosti. Můžeme je však všechny zobecnit na třídu Utvar, která ale přímo neexistuje a
nemá ani žádné objekty - bude to tedy abstraktní třída s metodami, které jsou společné všem těmto útvárům."""

"""K vytvoření abstraktních tříd použijeme balíček abc. Abstraktní metody nemají tělo a musí být 
implementovány dědičnými metodami."""

from abc import ABC, abstractmethod
from math import pi


class Figure(ABC):
    @abstractmethod
    def circuit(self):
        pass

    @abstractmethod
    def area(self):
        pass


"""Třídy rozšiřující třídu Utvar."""


class Rectangle(Figure):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def circuit(self):
        return 2 * (self.a + self.b)

    def area(self):
        return self.a * self.b


class Circle(Figure):
    def __init__(self, r):
        self.r = r

    def circuit(self):
        return 2 * self.r * pi

    def area(self):
        return pi * self.r ** 2


"""volani"""

rectangle = Rectangle(3, 5)
circle = Circle(12)
print(rectangle.circuit())
print(circle.circuit())
