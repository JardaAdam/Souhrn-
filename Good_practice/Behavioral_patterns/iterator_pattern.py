"""Iterator pattern umožňuje postupně procházet kolekci (např. seznam, slovník)
bez toho, abychom museli znát její vnitřní strukturu.
Pomáhá zpřístupnit prvky jedné po druhé a poskytuje uniformní způsob,
jak kolekci projít."""
"""
Iterator je objekt, který poskytuje metody pro iteraci přes kolekci.
V Pythonu používáme k tomu speciální metody: __iter__() a __next__().
"""

# Definice vlastní kolekce s vlastním iterátorem
class MyNumbers:
    def __init__(self):
        self.numbers = [1, 2, 3, 4, 5]
        self.index = 0

    # Tato metoda vrací iterátor (vrátí objekt samotný)
    def __iter__(self):
        return self

    # Tato metoda vrací další prvek
    def __next__(self):
        if self.index < len(self.numbers):
            current = self.numbers[self.index]
            self.index += 1
            return current
        else:
            raise StopIteration  # Zastaví iteraci

# Použití iterátoru
my_numbers = MyNumbers()
for number in my_numbers:
    print(number)  # Výstup: 1, 2, 3, 4, 5 (každý na nové řádce)



# class NasIterator:
#
#     def __init__(self, start=0, end=10):
#         self.current = start
#         self.end = end
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.current += 1
#         if self.current <= self.end:
#             return self.current
#         else:
#             raise StopIteration
#
#
# for i in NasIterator(5,10):
#     print(i)
