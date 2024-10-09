from dataclasses import dataclass
from copy import deepcopy


"""V jazyce Python existují dvě možnosti kopírování: mělké a hluboké. Mělká kopie kopíruje objekt, ale ne jeho prvky:
to znamená, že oba objekty sdílí jednotlivé prvky (nově vytvořený objekt bude mít jednotlivé prvky uloženy na stejném
míste v paměti jako původní). Hluboká kopie naproti tomu rekurzivně kopíruje objekt a všechny jeho prvky,
které ukládá na jiné místo v paměti, takže v paměti máme oba objekty včetně všech prvků uloženy na dvou
různých místech."""





@dataclass
class Rectangle:
    a: int
    b: int = 0

    """muzu si tu definovat hodnotu za =  """

    def circuit(self):
        return 2 * (self.a + self.b)

    def area(self):
        return self.a * self.b


p1 = Rectangle(3, 4)
lst = [1, p1, 3]
shallow_copy_lst = list(lst)
# shallow_copy_lst = lst[:]
deep_copy_lst = deepcopy(lst)
lst[1].a = 5  # we change the value of the side of the rectangle
print(lst, shallow_copy_lst, deep_copy_lst)

"""shallow_copy_lst = melka kopie
deepcopy = hluboka kopie"""