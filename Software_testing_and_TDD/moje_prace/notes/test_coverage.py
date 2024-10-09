# instalace -> pip install coverage = instalace knihovny
# prikaz: coverage report *test*.py = vypise v terminalu kolik procent % codu je otestovano
# coverage report (*test*.py) = v zavorce je cast ktera urcuje ktere soubory bude testovat ->
# nazev souboru musi obsahovat toto slovo. * = ohraniceni slova
# Z příkazové řádky pustíme analýzu: coverage run --source="." --omit="*/venv/*" -m pytest
#                                                | zdroje = vsechny | vynechat =
# zapis prikazu pro jeden soubor: coverage run -m pytest .\nazev souboru
#                                            | -m -> zkratka pro modul
# pro vice podrobnosti o testu pouzijeme prikaz: python -m unittest -v
# potom vytvoříme report: coverage report product.py company.py
# výsledek bude vypadat nějak takto:
# (venv) $ coverage report example.py
#
# Name Stmts Miss Cover
# --------------------------------
# example.py 9 1 89%

