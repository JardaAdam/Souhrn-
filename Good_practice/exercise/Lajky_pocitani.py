"""Implementujte program k zobrazování počtu "lajků" známého z Facebooku.

Vysvětlení
Implementujte funkci likes, která by měla jako vstup přijmout seznam jmen (řetězců)
 lidí, kterým se "líbí" daný příspěvek / fotografie, a vypsat správně zformátovaný a
 vyskloňovaný text.

Struktura funkce by měla vypadat takto:
"""

from typing import List


def likes(names: List[str]) -> str:
    num_of_names = len(names)  # Získáme počet jmen v seznamu
    if num_of_names == 0:
        format_output = "nobody likes it :("
    elif num_of_names == 1:
        format_output = f"{names[0]} like it"
    elif num_of_names == 2:
        format_output = f"{names[0]} i {names[1]} like it"
    elif num_of_names == 3:
        format_output = f"{names[0]}, {names[1]} i {names[2]} like it"
    else:
        format_output = f"{names[0]}, {names[1]} i {len(names) - 2} other people like it"

    return format_output


output = likes(["Petr", "Ana", "Lukas", "Pepa", "Honza"])

print(output)
# print(likes([]))  # => "nikdo to nelajkoval"
# print(likes(["Petr"]))  # => "Petr to lajkoval"
# print(likes(["Petr", "Ana"]))  # => "Petr a Ana to lajkovali"
# print(likes(["Petr", "Ana", "Marek"]))  # => "Petr, Ana a Marek to lajkovali"
# print(likes(["Petr", "Ana", "Marek", "Ola"]))  # => "Petr, Ana a další 2 lidé to lajkovali"
