# 1 Seznam úkolů na víkend: Vytvořte seznam úkolů na víkend, který obsahuje
# nejméně 5 úkolů. Každý úkol by měl být reprezentován jako řetězec v seznamu.

ukoly_na_vikend = ["ukol 1"]
ukoly_na_vikend.extend(["ukol 2", "ukol 3", "ukol 4", "ukol 5"])
print(ukoly_na_vikend)  # ['ukol 1', 'ukol 2', 'ukol 3', 'ukol 4', 'ukol 5']

# 2 Slovník slovníku: Vytvořte slovník, který obsahuje informace o několika lidech
# (jméno, věk, povolání). Každá osoba by měla být reprezentována jako slovník.

Jarda = {31, "Osvc"}
Honza = {35, "Vcelar"}
Milos = {33, "Viskar"}

udaje_o_skupine = ([Jarda, Milos, Honza])
print(udaje_o_skupine)

# 3 Unikátní čísla: Vytvořte množinu obsahující několik čísel. Zjistěte,
# kolik čísel je v množině, a poté přidejte další číslo a znovu zjistěte počet.
mnozina = {1, 5, 14, 94, 101}
print(mnozina)
print(len(mnozina))
mnozina.add(8)
print(mnozina)
print(len(mnozina))

# 4 Dvojice karet: Vytvořte seznam s dvojicemi karet (např.:
# ['srdce', 'kára', 'piky', 'krečky']). Použijte tuple pro reprezentaci každé dvojice.
dvojice_karet = [("srdce", "kary"), ("piky", "listy")]
print(dvojice_karet)

# 5 Změna hodnoty: Vytvořte seznam čísel a změňte hodnotu prvního prvku na novou hodnotu.
numbers = [20, 30, 50, 80]
numbers[0] = 12
print(numbers)

# 6 Vyhledejte hodnotu: Vytvořte seznam slov a zjistěte, zda konkrétní slovo je v seznamu obsaženo.
ovoce = ["apple", "banana", "orange", "strawbery"]
# print("apple" in ovoce, "je v seznamu")
"""rozdil mezi mnou a pozadovanym vysledkkem"""
search_word = "banana"
print(search_word in ovoce)

# 7 Odstranění duplicity: Vytvořte seznam, který obsahuje duplicitní
# hodnoty, a odstraňte duplicity tak, aby zůstaly pouze jedinečné hodnoty.
seznam_cisel = [1, 2, 5, 7, 1, 5, 3]
vycisteny_seznam = list(set(seznam_cisel))
print(vycisteny_seznam)
print(seznam_cisel.reverse())

# 8 Spojte dva seznamy: Vytvořte dva seznamy a spojte je do jednoho nového seznamu
print("\nTask8")
seznam_holek = ["Alice", "Bara", "Eliska"]
seznam_kluku = ["Jan", "Petr", "Tomas"]

spolecny_seznam = seznam_kluku + seznam_holek
print(spolecny_seznam)

# 9 Seřaďte seznam čísel: Vytvořte seznam čísel a seřaďte ho od nejnižšího po nejvyšší.
print("\nTask9")
cisla = [1, 8, 4, 9, 6, 2, 7]
cisla.sort()
print(cisla)

# 10 Přidání a odebrání prvků z množiny:Vytvořte množinu obsahující
# několik prvků. Přidejte nový prvek do množiny a poté odeberte jeden existující prvek.
# print("\nTask10")
# mnozina = {"houba", 10, "tuzka", True, 49}
# print(mnozina)
# mnozina.add("baterie")
# print(mnozina)
# mnozina.remove("tuzka")
# print(mnozina)

# TODO List

print("\nTask L1")
"""Reverse a list in Python (2 solutions)"""

list1 = [100, 200, 300, 400, 500]
list1.reverse()
print(list1)
"""[500, 400, 300, 200, 100]"""
print("\nTask L2")
"""Write a program to add item 7000 after 6000 in the following Python List"""

list_1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list_1[2][2].append(7000)
print(list_1)

"""[10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]"""

print("\nTask L3")

"""You have given a nested list. Write a program to extend it by adding the sublist ["h", "i", "j"] 
in such a way that it will look like the following list."""

list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]

"""sub list to add"""

sub_list = ["h", "i", "j"]
list1[2][1][2].extend(sub_list)
print(list1)

"""['a', 'b', ['c', ['d', 'e', ['f', 'g', 'h', 'i', 'j'], 'k'], 'l'], 'm', 'n']"""

print("\nTask L4")
"""You have given a Python list. Write a program to find value 20 in the list, and if it is present, 
replace it with 200. Only update the first occurrence of an item."""

list1 = [5, 10, 15, 20, 25, 50, 20]
cislo = list1.index(20)
list1[cislo] = 200
print(list1)

"""[5, 10, 15, 200, 25, 50, 20]"""

print("\nTask L5")
"""Given a Python list, write a program to remove all duplicates."""

list_duplicitni = [5, 20, 15, 20, 25, 50, 20]
list_cisty = sorted(list(set(list_duplicitni)))
print(list_cisty)

"""[5, 15, 20, 25, 50]"""

# TODO Slovnik
print("\nTask S1")
# Merge two Python dictionaries into one
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
Dict = {}
Dict.update(dict1)
Dict.update(dict2)
print(Dict)

"""{'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Fourty': 40, 'Fifty': 50}"""

print("\nTask S2")

"""Print the value of key history’ from the below dict"""

sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}
print(sampleDict["class"]["student"]["marks"]["physics"])

print("\nTask S3")
"""Delete a list of keys from a dictionary"""

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

# Keys to remove
keys = ["name", "salary"]
sample_dict.pop(keys[0])
sample_dict.pop(keys[1])
print(sample_dict)

"""Expected output:"""
"""{'city': 'New york', 'age': 25}"""

# TODO Tuple
print("\nTask T1")
"""Reverse the tuple
Given:"""
tuple1 = (10, 20, 30, 40, 50)

print(tuple1[::-1])
"""Expected output:
(50, 40, 30, 20, 10)"""


"""The given tuple is a nested tuple. write a Python program to print the value 20."""
print("\nTask T2")
tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))
print(tuple1[1][1])
"""Expected output: 20"""

print("\nTask T3")
"""Create a tuple with a single item 50"""
Tuple = (50,)
print(Tuple)
print(len(Tuple))

print("\nTask T4")
"""Write a program to unpack the following tuple into four variables and display the total sum."""

tuple1 = (10, 20, 30, 40)
# v = tuple1[0]
# x = tuple1[1]
# y = tuple1[2]
# z = tuple1[3]
v, x, y, z = tuple1
print(v + x + y + z)

"""100"""

# TODO Set
print("\nTask t1")
"""Given a Python list, Write a program to add all its elements into a given set."""
sample_set = {"Yellow", "Orange", "Black"}
sample_list = ["Blue", "Green", "Red"]
sample_set.update(sample_list)
print(sample_set)

"""Expected output:
Note: Set is unordered.
{'Green', 'Yellow', 'Black', 'Orange', 'Red', 'Blue'}"""
