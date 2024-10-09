"""pouzivaji se pro ignorovani urcitych erroru v urcitych pripadech
chranime se tim spadnuti programu ve vyhimecnych situacich """

"""try, except = v pripade provedeni prikazu [try] program pokracuje dale a neprovede se 
[except] v pripade ze se neprovede [try] provede se [except] """

# a = 3
# b = [1, 0, 2]
# for elem in b:
#     try:
#         result = a / elem
#         """prvni se snazi program provest [try] v okamziku kdy b = 0 -> nelze deleni provest
#         program pokracuje na except"""
#     except ZeroDivisionError:
#         continue
#     """protoze v mnozine "b" je obsazena nula tak pouzijeme except aby program pokracoval
#         misto toho aby vypsal error a zastavil se. pod except mame napsano continue takze
#         program v pripade ZeroDivisionError pokracuje dale."""
#     print(f"Result is: {result}")
#
# def foo():
#     print(0)
#     div_ab(1,0)
#     print(1)
#
#
# def bar()
#     return 0/0
#
#
# def div_ab(1,0)
#
# def foo():
#     try:
#         print(0)
#         bar(0)
#         print(1)
#     except ZeroDivisionError as e:
#         """ ZeroDivisionError prejmenuji na e pomoci [as]"""
#         print('exception occured:'e)
#
#
# """finally = na zaver proved. v pripade prace se souborem na konci procesu i v pripade ze
# z nejakeho duvodu nastane error tak na konci diky finally napr zavreme soubor [file.close()]"""
#
#     try:
#         file = open("temp.txt")
#         file.write("Alice has a cat")
#     except IOError:
#         print("An error occurred while processing the file.!")
#     finally:
#         file.close()


"""raise V kódu máme také možnost vyhazovat výjimky, když chceme signalizovat, že určité chování je chybou. 
K tomu slouží klíčové slovo"""

# a = 3
# b = [1, 0, 2]
# for elem in b:
#     if elem == 0:
#         raise ValueError("The divisor cannot be zero")
#     result = a / elem
#     print(f"Result is: {result}")
#
# try:
#     arr = []
#     'asdf' + 1
# except ZeroDivisionError:
#     print('zerodivisionerror')
# except IndexError:
#     print('indexerror')
# except Exception:
#     print('other exeption')

"""retezeni except pod sebe stane se vzdicky jen ta prvni z nich"""


"""vytvoreni vlastnich vyjimek = Můžeme také vytvořit vlastní třídy výjimek. K tomu potřebujeme vytvořit třídu, 
která dědí z rodičovské třídy všech výjimek: Exception."""

"""metoda1 """


# class CustomException(Exception):
#     pass
#
#
# a = 3
# b = [1, 0, 2]
# for elem in b:
#     if elem == 0:
#         raise CustomException("The divisor cannot be zero")
#     """v () napiseme hlasku kterou chceme vypsat do terminalu"""
#     result = a / elem
#     print(f"Result is: {result}")


"""Metoda 2"""


# class CustomException(Exception):
#     def __init__(self):
#         message = "The divisor cannot be zero"
#         super().__init__(message)
"""sprava ktera se ma vypsat pri namy vytvorene podmince je napsana zde nahore na az dale v raise
tato metoda je dobra kdyz by jsme opakovali vicekrat CustomException"""


# a = 3
# b = [1, 0, 2]
# for elem in b:
#     if elem == 0:
#         raise CustomException()
#     result = a / elem
#     print(f"Result is: {result}")


"""Task"""
print("task")
# Napis funkciu handle_math(x) a vrati 3 vysledky (v tuple)
# - cislo 42 / x
# sqrt(x)
# log(x)

# Vytvor custom exception MathException a raisni ju s rozumnou hlaskou vtedy,
# ak nevieme vykonat jednu z danych operacii. V opacnom pripade vrat 3 vysledky.

import math
x = float(input("write positive number x: "))


def handle_math(x):
    """control when is x positive number"""
    if x <= 0:
        raise ValueError("x must be positive number")

    division_result = 42 / x
    sqrt_result = math.sqrt(x)
    log_result = math.log(x)
    return (division_result, sqrt_result, log_result)


results = handle_math(x)

print(results)



