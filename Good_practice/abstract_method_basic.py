"""Abstraktní metoda je metoda, která není implementována v nadřazené
třídě (abstraktní třídě), ale musí být implementována ve všech podtřídách
(konkrétních třídách), které z této nadřazené třídy dědí. To je užitečné,
když chceš definovat společné rozhraní pro více tříd, ale nechceš v nadřazené
třídě určit konkrétní implementaci."""

"""Tento příklad ukazuje, jak bychom mohli použít abstraktní metodu ve třídě, 
která reprezentuje různé typy zvířat. Každé zvíře má vlastní způsob, jak 
vydávat zvuky, a proto metodu speak() definujeme jako abstraktní."""

from abc import ABC, abstractmethod

# 1. Definujeme abstraktní třídu Animal, která určuje společné
# rozhraní pro všechny zvířata
"""Abstraktní třída Animal:
Tato třída dědí z ABC (což znamená Abstract Base Class – základní abstraktní třída).
Pomocí dekorátoru @abstractmethod definujeme metodu speak(), která musí 
být implementována ve všech třídách, které dědí z Animal.
Abstraktní třídy nemohou být instancovány přímo. Pokus o vytvoření 
instance třídy Animal by vyvolal chybu."""
class Animal(ABC):
    @abstractmethod
    def speak(self):
        # Abstraktní metoda, kterou MUSÍ každá podtřída implementovat
        pass


# 2. Vytvoříme konkrétní třídu Dog, která dědí z Animal a implementuje metodu speak
"""Konkrétní třídy Dog a Cat:
Obě tyto třídy dědí z abstraktní třídy Animal a musí implementovat metodu speak(), 
jinak by Python vyhodil chybu.
Třída Dog implementuje speak() tak, že vrátí řetězec "Haf haf!", 
a třída Cat vrací "Mňau!"."""
class Dog(Animal):
    def speak(self):
        # Implementace metody speak pro psa
        return "Haf haf!"


# 3. Vytvoříme konkrétní třídu Cat, která dědí z Animal a implementuje metodu speak
class Cat(Animal):
    def speak(self):
        # Implementace metody speak pro kočku
        return "Mňau!"

"""Vytváření objektů:
Vytvoříme objekty dog a cat z tříd Dog a Cat.
Pak voláme jejich metody speak(), které vrací odpovídající zvuky pro každé zvíře."""
# 4. Nyní můžeme vytvořit instance psů a koček a zavolat jejich metody speak
dog = Dog()  # Vytváříme objekt třídy Dog
cat = Cat()  # Vytváříme objekt třídy Cat

# Voláme metody speak, které vrátí zvuky zvířat
print(dog.speak())  # => "Haf haf!"
print(cat.speak())  # => "Mňau!"

"""Abstraktní třída poskytuje šablonu, která určuje, že určité metody musí 
být implementovány ve všech podtřídách.
Abstraktní metody jsou deklarovány, ale neimplementovány v abstraktní třídě.
Tento vzor je užitečný, když chceš zajistit, aby všechny podtřídy měly určité 
společné metody, ale každá třída je bude implementovat jinak."""