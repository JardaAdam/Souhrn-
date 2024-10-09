# TODO Class definuje urcitou sablonu ktera je zaklad pro tvorbu vice podobnych (auta)
# ve tride vytvorim zakladni rysi a s pomoci teto (sablony) nadafinuju presne jednotlivce
# __init__ -> magicka metoda- vola se sama pri urcitem ukonu.
#          -> vola se pri
import random
# TODO - proc OOP


# TODO - Class definice - metody a atributy
class Clovek:

    VYSKYT = "Evropa"

# TODO - konstruktor init

    def __init__(self,jmeno_clovek, vek_clovek):  # self -> propojuje metody (je to nulty parametr)
       # pupecni snura, propojuje zakladni parametry s funkcemi
       # prvni poviny parametr
        self.jmeno = jmeno_clovek
        self.vek = vek_clovek

    def predstav_se(self):
        print(f"Moje jmeno je {self.jmeno} a je mi {self.vek} let. Rok narozeni: {self.VYSKYT}")

    def nakrm_se(self, jidlo:str = "rohlik"):
        print("krmim se",jidlo)

# TODO - vytvorit objekty
kamarad = Clovek("Honza", 25)
kamarad.predstav_se()
kamarad.vek = 30
kamarad.jmeno = "Honza"
kamarad.predstav_se()
print(kamarad.jmeno)
kamarad.nakrm_se("chleba")

# # TODO - nezavislost objektu
# stepan = Clovek("Stepan", 50)
# # stepan.jmeno = "Stepan"
# stepan.DATUM_NAROZENI = "12.12.2000"
#
# radovan.predstav_se()
# stepan.predstav_se()


# TODO - vnitrni promenne - _p
# class Clovek:
#
#     # TODO - konstruktor init
#     def __init__(self, jmeno_cloveka, vek_cloveka):
#         self.jmeno = jmeno_cloveka
#         self._vek = vek_cloveka  # _ ochrana proti prepsani
#
#     def predstav_se(self):
#         print(f"Moje jmeno je {self.jmeno} a je mi {self._vek} let.")
#

# honza = Clovek("Honza", 34)
# print(honza._vek)
# honza._vek = -5
# honza.predstav_se()

# TODO - soukrome promenne - __p #
# class Clovek:
#
#     # TODO - konstruktor init
#     def __init__(self, jmeno_cloveka, vek_cloveka):
#         self.jmeno = jmeno_cloveka
#
#         if vek_cloveka >= 0:
#             self.__vek = vek_cloveka
#         else:
#             raise ValueError("Zadany vek cloveka je mensi nez 0!")
#
#     def ziskej_vek(self):
#         return self.__vek
#
#     def nastav_vek(self, novy_vek: int):
#         if novy_vek >= self.__vek:
#             self.__vek = novy_vek
#         else:
#             raise ValueError("Zadany vek cloveka je mensi nez aktualni!")
#
#     def predstav_se(self):
#         print(f"Moje jmeno je {self.jmeno} a je mi {self.__vek} let.")
#
#
# honza = Clovek("Honza", 34)
# # print(honza.__vek)
# # honza.__vek = -5
# honza.predstav_se()
# print(honza.ziskej_vek())
# honza.nastav_vek(40)
# honza.predstav_se()

# TODO - properties # geter = bere #setter = nastavuje # deleter = maze
class Clovek:

    # TODO - konstruktor init
    def __init__(self, jmeno_cloveka, vek_cloveka):
        self.__jmeno = jmeno_cloveka

        if vek_cloveka >= 0:
            self.__vek = vek_cloveka
        else:
            raise ValueError("Zadany vek cloveka je mensi nez 0!")

    @property
    def vek(self):
        return self.__vek

    @vek.setter
    def vek(self, novy_vek: int):
        if novy_vek >= self.__vek:
            self.__vek = novy_vek
        else:
            raise ValueError("Zadany vek cloveka je mensi nez aktualni!") #raise vyhozuje Error

    @vek.deleter
    def vek(self):
        del self.__vek

    def predstav_se(self):
        print(f"Moje jmeno je {self.__jmeno} a je mi {self.__vek} let.")


honza = Clovek("Honza", 34)
print(honza.vek)
honza.__vek = -5
honza.predstav_se()
# print(honza.vek)
# honza.vek = 40
honza.predstav_se()

# del honza.jmeno


# TODO - garbage collector
# TODO - odkazovani, kopie

# TODO - __dict__
class Trojuhelnik:

    def __init__(self):
        self.a = 3
        self.b = 4
        self.c = 5


trojuhelnik = Trojuhelnik()
# print(trojuhelnik.__dict__)


# TODO - magic methods
class Clovek:

    def __init__(self, jmeno_cloveka, vek_cloveka):
        self.jmeno = jmeno_cloveka
        self.vek = vek_cloveka

    def __str__(self):
        return self.jmeno

    def __int__(self):
        return self.vek

    def __eq__(self, other):
        return self.vek == other.vek

    def __len__(self):
        return len(self.jmeno)

    def __add__(self, other):
        return Clovek(random.choice([self.jmeno, other.jmeno]), 0)

    def predstav_se(self):
        print(f"Moje jmeno je {self.jmeno} a je mi {self.vek} let.")


zdenek = Clovek("Zdenek", 30)
eva = Clovek("Eva", 30)
# print(str(zdenek))
# print(int(zdenek))
# print(zdenek == eva)
# # print(zdenek > eva)
# print(len(eva))
# dite = eva + zdenek
# dite.predstav_se()


# TODO - dedeni
class Savec:

    def __init__(self, jmeno, vek):
        self.jmeno = jmeno
        self.vek = vek

    def dychej(self):
        print("Nadech")
        print("Vydech")

    def napij_se(self):
        print("Piju")


class Slon(Savec):

    def __init__(self, jmeno, vek, delka_klu):
        super().__init__(jmeno, vek)
        self.delka_klu = delka_klu


class Zirafa(Savec):

    def __init__(self, jmeno, vek, delka_krku):
        super().__init__(jmeno, vek)
        self.delka_krku = delka_krku


class Opice(Savec):

    def skoc_na_strom(self):
        print("Skacu na strom.")


slon = Slon("Bonifac", 30, 100)
zirafa = Zirafa("Zofie", 5, 200)
opice = Opice("Karel", 2)

# slon.dychej()
# zirafa.napij_se()
# opice.skoc_na_strom()

# TODO - dedeni ze dvou trid
class Netopyr:

    def let(self):
        print("Letim")


class Clovek:

    # TODO - zapouzdreni metod
    def __behej(self):
        print("Bezim")


class Batman(Netopyr, Clovek):

    def chyt_zlocince(self):
        self.let()
        self.__behej()
        print("Zneskudnuji zlocince")


bruce_wayne = Batman()
# bruce_wayne.chyt_zlocince()

# TODO - polymorfismus


# TODO - isinstance, type
# print(type(5))
# print(type(bruce_wayne))

# print(isinstance(bruce_wayne, Batman))
# print(isinstance(bruce_wayne, Netopyr))
# print(isinstance(bruce_wayne, Opice))