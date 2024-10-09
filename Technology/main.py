# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions,
# and settings.


# def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    # print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
"""Složka Technology je kořen projektu kde musí být hlavní část projektu (main.py)"""
"""print(__file__) -> kde se nachazi aktualni soubor ve kterem se nachazim
   print(Fighter.__file__) vypise umisteni souboru ktery volame"""

"""__init__.py -> slozka definujici package """

"""!!když vztvářím svoje knihovny tak musí být v kořenu (stejne složce jako main.py) 
nebo se můžu zanořit do složky pomoci -> from složka import knihovna """

"""import muzu pouzit i jako import package a z nej pouze nejake moduli 
import SCHOOL
from SCHOOL import teacher
from SCHOOL import student
from SCHOOL import classroom
SCHOOL = package
teacher, student, classroom = .py (modul)"""


import sys
import matematika
from hra import Dragon
from hra import Fighter
import hra
# print(sys.path)
# print(matematika.pi)
# print(matematika.count(4, 6))
# print(matematika.__file__)

"""z package hra kde v __init__.py mam vytvorene postavi (Bajaja,Fnuk) volam uz jen 
odkud.kdo.co()"""
hra.Bajaja.predstav_se()
hra.Fnuk.predstav_se()

print(__file__)