"""Návrhový vzor Prototype umožňuje klonovat objekty, aniž by bylo nutné
vytvářet jejich novou instanci od začátku. Místo toho jednoduše vytvoříme
kopii (klon) existujícího objektu. Je užitečný, když máš objekt, jehož
vytvoření je nákladné nebo komplikované, a potřebuješ jeho duplikát."""

"""Představme si, že máme třídu Animal, která reprezentuje zvíře. 
Pomocí Prototype budeme schopni klonovat různé zvířata (např. psa a kočku), 
aniž bychom museli znovu volat konstruktor."""

import copy


# 1. Třída Animal, která bude naším prototypem
"""Třída Animal:
Definujeme základní třídu Animal, která má atributy name (jméno) a species (druh).
Metoda make_sound() vrací obecný zvuk zvířete.
Metoda clone() umožňuje klonování objektu pomocí funkce copy.deepcopy(), 
která vytvoří hlubokou kopii objektu."""
class Animal:
    def __init__(self, name, species):
        # Inicializace zvířete s jeho jménem a druhem
        self.name = name
        self.species = species

    def make_sound(self):
        # Výchozí metoda pro vydávání zvuku, která může být přepsána v podtřídách
        return "Some generic animal sound"

    def __str__(self):
        # Tento řetězcový výstup nám zobrazí informace o zvířeti
        return f"{self.name} is a {self.species}"

    def clone(self):
        # Klonování pomocí modulu copy
        return copy.deepcopy(self)


# 2. Třída Dog, která dědí z Animal a přidává specifické vlastnosti
"""Třídy Dog a Cat:
Tyto třídy dědí z Animal a přepisují metodu make_sound(), aby 
vracely specifické zvuky pro psa (Woof!) a kočku (Meow!)."""
class Dog(Animal):
    def make_sound(self):
        # Přepíšeme metodu pro vydávání zvuku specifického pro psa
        return "Woof!"


# 3. Třída Cat, která dědí z Animal a přidává specifické vlastnosti
class Cat(Animal):
    def make_sound(self):
        # Přepíšeme metodu pro vydávání zvuku specifického pro kočku
        return "Meow!"


# Hlavní program
if __name__ == "__main__":
    # 4. Vytvoříme původní objekt psa
    original_dog = Dog(name="Buddy", species="Dog")
    print(original_dog)  # Výstup: "Buddy is a Dog"
    print(f"Sound: {original_dog.make_sound()}")  # Výstup: "Sound: Woof!"

    # 5. Klonujeme původního psa
    cloned_dog = original_dog.clone()
    print(cloned_dog)  # Výstup: "Buddy is a Dog" (je to klon původního psa)
    print(f"Sound: {cloned_dog.make_sound()}")  # Výstup: "Sound: Woof!" (klon má stejné chování)

    # 6. Vytvoříme původní objekt kočky
    original_cat = Cat(name="Whiskers", species="Cat")
    print(original_cat)  # Výstup: "Whiskers is a Cat"
    print(f"Sound: {original_cat.make_sound()}")  # Výstup: "Sound: Meow!"

    # 7. Klonujeme původní kočku
    cloned_cat = original_cat.clone()
    print(cloned_cat)  # Výstup: "Whiskers is a Cat"
    print(f"Sound: {cloned_cat.make_sound()}")  # Výstup: "Sound: Meow!"

"""Prototype umožňuje vytvářet nové objekty pomocí klonování existujících objektů, 
aniž by bylo nutné znovu vytvářet jejich instanci.
V tomto příkladu jsme klonovali objekty Dog a Cat a vytvořili jejich přesné kopie.
Tento vzor je užitečný, když chceme rychle vytvářet duplikáty objektů, 
aniž bychom je museli znovu inicializovat."""


"""Vytváření a klonování:

Vytvoříme objekt psa (original_dog) a zavoláme jeho metody, aby zobrazil 
informace o psu a zvuku, který dělá.
Poté klonujeme psa pomocí metody clone() a zobrazíme informace o klonovaném 
objektu. Klon má stejná data a chování jako původní objekt.
Stejný postup použijeme pro kočku (original_cat) a její klon."""