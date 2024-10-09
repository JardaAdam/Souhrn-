# 1 Faktoriál: Napište funkci factorial(n), která vrátí faktoriál čísla n.


# 2 První písmeno: Napište funkci first_letter(word), která vrátí první písmeno zadaného slova.


# 3 Reverzní seznam: Napište funkci reverse_list(lst), která vrátí seznam v obráceném pořadí.


# 4 Součet prvků seznamu: Napište funkci sum_list(lst), která spočítá součet všech prvků v seznamu.


# 5 Počet samohlásek: Napište funkci count_vowels(word), která spočítá počet samohlásek v zadaném slově.


# 6 Mocniny čísla: Napište funkci power(x, n), která vrátí x umocněné na n.


# 7 Změna velikosti písmen: Napište funkci change_case(text), která převede všechna písmena ve zadaném textu na
# velká písmena.


# 8 Délka slova: Napište funkci word_length(word), která vrátí délku zadaného slova.


# 9 Seznam čísel: Napište funkci even_numbers(n), která vrátí seznam všech sudých čísel od 1 do n.


# 10 Palindrom: Napište funkci is_palindrome(word), která zjistí, zda je zadané slovo palindromem
# (čte se stejně zleva doprava i zprava doleva).

print("complex tasks")

#TODO 1 Create a function with variable length of arguments
# Write a program to create function func1() to accept a variable length of arguments and print their value.

"""Note: Create a function in such a way that we can pass any number of arguments to this function and the function 
should process them and display each argument’s value."""

Function call:
# call function with 3 arguments
func1(20, 40, 60)

# call function with 2 arguments
func1(80, 100)
"""Expected Output:
Printing values
20
40
60

Printing values
80
100"""

#TODO 2 Return multiple values from a function
# Write a program to create function calculation() such that it can accept two variables and calculate addition and
# subtraction. Also, it must return both addition and subtraction in a single return call.

"""given"""
def calculation(a, b):
    # your code

res = calculation(40, 10)
print(res)

"""output : 50, 30"""

#TODO 3 Create a function with a default argument
# Write a program to create a function show_employee() using the following conditions.
# It should accept the employee’s name and salary and display both.
# If the salary is missing in the function call then assign default value 9000 to salary

"""given""""
showEmployee("Ben", 12000)
showEmployee("Jessa")

"""output: name: Ben salary: 12000
           name: Jessa salary: 9000"""


#TODO 4 Napiste funkci na nalezeni nejvetsiho cisla ze vsech zadanych

maximum(4, 6, 8, 24, 12, 2)

"""output: 24"""

#TODO 5 Vyvtor funkci, ktera si vezme cislo a vypise, jestli je sude nebo liche


#TODO 6 Vytvor funkci, ktera ze zadaneho stringu spocita souhlasky a samohlasky

#TODO 7 Vytvor funkci, ktera ze vsech zadanych cislic spocita faktorial a vrati jejich soucet

#TODO 8
# First, def a function called cube that takes an argument called number.
# Make that function return the cube of that number (i.e. that number multiplied by itself and multiplied by
# itself once again).
# Define a second function called by_three that takes an argument called number. if that number is divisible by 3,
# by_three should call cube(number) and return its result. Otherwise, by_three should return False. -Check if it works.

#TODO 9
# Pokud hotovo:
# Codewars - zkouska a registrace
# zkouset dalsi veci z dnesni hodiny ktere nebyly v prikladech
# popripade nacist data z inputu nebo parametru
# zkusit si priklad kreativne rozsirit
# osetrit chybne vstupy
# dodelat zbytek na https://www.w3schools.com/python/exercise.asp

