"""Vyhodnocení výrazu v postfixové notaci (Reverse Polish Notation - RPN)

Zadání:
Napište funkci, která vyhodnotí aritmetický výraz zadaný v postfixové notaci.

Například:
"1 2 +" -> 3
"8 2 /" -> 4
"5 1 2 + 4 * + 3 -" ->
"5 3 4 * + 3 -" ->
"5 12 + 3 -" ->
"17 3 -" ->
"14" -> 14.
"
"""
""" pro reseni teto ulohy pouziji stack ( zasobnik )"""
from collections import deque

def rpn(string: str) -> int:
    stack = deque()
    tokens = string.split()  # prevede string na seznam a oddeli cisla mezerami

    for token in tokens:
        if token.isdigit():  # Pokud je token cislo -> True a prida znak do Stack
            # tim rozebere zadani na cisla a znaminka (operator)
            stack.append(int(token)) # uklada tokeny ktere jsou int = cisla
        else:  # Pokud je token operátor
            b = stack.pop()  # Druhý operand  # poradi ve kterem nacitam cisla ze zasobniku
            a = stack.pop()  # První operand  # proto musi mit toto poradi aby se mezi sebou operovali spravne

            if token == '+':
                result = a + b
            elif token == '-':
                result = a - b
            elif token == '*':
                result = a * b
            elif token == '/':
                result = a // b  # celociselne deleni

            stack.append(result)

    return stack.pop()  # Konečný výsledek


if __name__ == '__main__':
    strings = ["1 2 +", "8 2 /", "5 1 2 + 4 * + 3 -", "20 30 +"]
    for string in strings:
        print(f"'{string}' -> {rpn(string)}")

# TODO osetrit pred spatne zadanymi cisli