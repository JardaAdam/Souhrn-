# v zakladni tride nic nedela jenom specifikuje co musi ta class umet.

# Dobra varianta pro data Archytecty

"""Použití Factory Method:

Vytvoříme instanci třídy AnimalFactory.
Poté zavoláme metodu create_animal(), do které předáme typ zvířete jako řetězec
 (např. "dog" nebo "cat").
Factory metoda podle typu zvířete vrátí objekt buď Dog, nebo Cat.
Můžeme pak na vrácených objektech zavolat metodu speak() a
dostaneme správný zvuk pro dané zvíře."""

"""Abstraktní třída Animal:
Tato třída definuje obecnou strukturu zvířete. Má metodu speak(),
kterou musí implementovat všechny podtřídy, které dědí z Animal.
Tato metoda je označena jako NotImplementedError, což znamená,
že musí být konkrétně definována v podtřídách."""
class Animal:
    def speak(self):
        raise NotImplementedError("Tato metoda musí být implementována v podtřídě!")


"""Konkrétní třídy Dog a Cat:

Tyto dvě třídy (Dog a Cat) dědí z Animal a implementují metodu speak().
Každé zvíře má svou vlastní verzi této metody: pes vrací "Haf haf!" a 
kočka vrací "Mňau!"."""
class Dog(Animal):
    def speak(self):
        return "Haf haf!"  # Pes štěká

class Cat(Animal):
    def speak(self):
        return "Mňau!"  # Kočka mňouká

# Factory metoda, která podle vstupu vytvoří konkrétní objekt
"""Třída AnimalFactory:

Tato třída představuje Factory Method. Má metodu create_animal(), 
která přijímá parametr animal_type, podle kterého rozhodne, 
zda vytvořit objekt Dog nebo Cat.
Factory metoda vrací objekt odpovídající třídě podle toho, 
jaký vstupní parametr byl předán."""
class AnimalFactory:
    def create_animal(self, animal_type: str) -> Animal:
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()
        else:
            raise ValueError("Neznámý typ zvířete")

# Použití Factory Method
factory = AnimalFactory()

dog = factory.create_animal("dog")  # Factory vrací objekt typu Dog
print(dog.speak())  # => Haf haf!

cat = factory.create_animal("cat")  # Factory vrací objekt typu Cat
print(cat.speak())  # => Mňau!






