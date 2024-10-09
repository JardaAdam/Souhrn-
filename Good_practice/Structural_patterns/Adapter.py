"""slouzi jako meziclanek mezi programi ( stara appy mela nazvanou jednotku nejak a v nove casti
kodu se zmenil nazev a adapter slouzi k tomu aby spolu stara a nova cast fungovala"""


class SkladPotravin:
    def __init__(self):
        self.regal = []

    def pridej(self, potravina):
        self.regal += [potravina]
        """ v pridej se zmenila polozka na potravina
        v class Projedna ale nemuzu prejmenovat polozku na potravinu -> takze si vytvorim 
        class SkladNas a t veto classe udelam upravu tak aby mezi sebou mohli fungovat 
        class SkladPotravin a Prodejna"""


# sklad = SkladPotravin()   # vytvoreni skladu
# sklad.pridej("jablko")    # pridavam polozku
# print(f'Ve skladu mame: {sklad.regal}')        # necham si vypsat polozky ve skladu


class Prodejna:
    def __init__(self):  # vytvoreni init delat automapicky i kdyz ho nepotrebuju
        pass

    def pridej_do_skladu(self, sklad2, polozka):
        sklad2.pridej(polozka=polozka)


# prodejna = Prodejna()
# prodejna.pridej_do_skladu(sklad, "hruska")
# print(f'Ve skladu mame: {sklad.regal}')


class SkladNas:
    def __init__(self, warehouse: SkladPotravin):  # SkladNas
        self.sklad = warehouse

    def pridej(self, polozka):
        self.sklad.pridej(potravina=polozka)


sklad = SkladPotravin()
prodejna = Prodejna()
sklad_nas = SkladNas(warehouse=sklad)

print(sklad.regal)
prodejna.pridej_do_skladu(sklad2=sklad_nas, polozka="jablko")
print(sklad.regal)
prodejna.pridej_do_skladu(sklad_nas, "hruška")
print(sklad.regal)
