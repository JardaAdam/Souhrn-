# PEP 8 odstraneni chyb = ctrl + alt + l

# Komentáře - je důležité aby kod byl okomentovaný a bylo pochopitelné
#   co proč jsem v něm udělal.

# = jednořadkoví komentář

"""véceřádkoví komentář"""

"""automaticke formatovace = black, yapf, autopep8"""

"""PEP 8 - lintry
linter - program, který analyzuje kód a identifikuje chyby a stylistické problémy; 
často se používá jako plugin editoru:

pycodestyle
flake8 - navíc obsahuje funkce debuggeru
pylint - hledá chyby v programování, problematický kód, navrhuje opravy

Python IDE (tj. PyCharm) mají tyto vestavěné nástroje."""


def get_default_data():
    """

    :return:
    """
    return {"Hello": "Word"}  # return default dict


#

is_human = True
empty_string = ''
number = 20

if is_human:  # není potřeba psát: is True (if má defaultně nastaveno True or False
    print('This is a human')

if empty_string:
    print('This string is not empty')

if number:
    print('this is not zero')
