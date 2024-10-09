"""Abstraktní metody
určují, že každá podtřída musí implementovat
určité funkce, jako je drive() pro pozemní dopravu a sail() pro námořní dopravu.

Abstract Factory
poskytuje flexibilní způsob, jak vytvářet různé druhy objektů,
které sdílejí společné rozhraní.
Díky tomuto návrhu můžeš snadno přidávat nové typy dopravních prostředků,
aniž bys musel měnit kód ve všech továrnách nebo dopravních třídách."""

# Importujeme knihovnu abc, která umožňuje vytváření abstraktních tříd
from abc import ABC, abstractmethod


# 1. Abstraktní třída pro pozemní dopravu
class LandTransport(ABC):
    @abstractmethod
    def drive(self):
        # Abstraktní metoda, kterou musí každá podtřída implementovat
        pass


# 2. Abstraktní třída pro námořní dopravu
class SeaTransport(ABC):
    @abstractmethod
    def sail(self):
        # Abstraktní metoda, kterou musí každá podtřída implementovat
        pass


# 3. Konkrétní třída Car, která implementuje pozemní dopravu
class Car(LandTransport):
    def drive(self):
        # Implementace abstraktní metody drive pro auto
        return "Car is driving on the road."


# 4. Konkrétní třída Bike, která implementuje pozemní dopravu
class Bike(LandTransport):
    def drive(self):
        # Implementace abstraktní metody drive pro kolo
        return "Bike is pedaling on the road."


# 5. Konkrétní třída Ship, která implementuje námořní dopravu
class Ship(SeaTransport):
    def sail(self):
        # Implementace abstraktní metody sail pro loď
        return "Ship is sailing on the sea."


# 6. Konkrétní třída Submarine, která implementuje námořní dopravu
class Submarine(SeaTransport):
    def sail(self):
        # Implementace abstraktní metody sail pro ponorku
        return "Submarine is navigating underwater."


# 7. Abstraktní továrna, která definuje metody pro vytvoření pozemní a námořní dopravy
class TransportFactory(ABC):
    @abstractmethod
    def create_land_transport(self) -> LandTransport:
        # Abstraktní metoda pro vytvoření pozemní dopravy
        pass

    @abstractmethod
    def create_sea_transport(self) -> SeaTransport:
        # Abstraktní metoda pro vytvoření námořní dopravy
        pass


# 8. Konkrétní továrna pro pozemní dopravu
class LandTransportFactory(TransportFactory):
    def create_land_transport(self) -> LandTransport:
        # Vytváříme konkrétní typ pozemní dopravy (auto)
        return Car()

    def create_sea_transport(self) -> SeaTransport:
        # Výchozí námořní doprava (loď) v pozemní továrně
        return Ship()


# 9. Konkrétní továrna pro námořní dopravu
class SeaTransportFactory(TransportFactory):
    def create_land_transport(self) -> LandTransport:
        # Vytváříme konkrétní typ pozemní dopravy (kolo) v námořní továrně
        return Bike()

    def create_sea_transport(self) -> SeaTransport:
        # Vytváříme konkrétní typ námořní dopravy (ponorka)
        return Submarine()


# 10. Hlavní část programu
if __name__ == "__main__":
    # Používáme továrnu pro pozemní dopravu
    land_factory = LandTransportFactory()
    car = land_factory.create_land_transport()  # Vytvoříme auto
    ship = land_factory.create_sea_transport()  # Vytvoříme loď

    print(car.drive())  # Výstup: "Car is driving on the road."
    print(ship.sail())  # Výstup: "Ship is sailing on the sea."

    # Používáme továrnu pro námořní dopravu
    sea_factory = SeaTransportFactory()
    bike = sea_factory.create_land_transport()  # Vytvoříme kolo
    submarine = sea_factory.create_sea_transport()  # Vytvoříme ponorku

    print(bike.drive())  # Výstup: "Bike is pedaling on the road."
    print(submarine.sail())  # Výstup: "Submarine is navigating underwater."
