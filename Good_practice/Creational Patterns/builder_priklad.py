...  # tri tecky = Pass
class Dum:
    def __init__(self):
        self.pocet_pokoju = None
        self.pocet_podlazi = None
        self.pocet_oken = None # None je sikovnejsi nez 0 protoze nula nas muze mast. zda se neco stalo
        # a je tam nula nebo se nic nedelo a je tam porad nula. takze kdyz se neco delo a je tam 0 tak se
        # zmeni None na 0


    def popsat(self):
        print(f"Dum ma {self.pocet_pokoju} pokoju, {self.pocet_podlazi} podlazi a {self.pocet_oken} oken.")


class DumBuilder:
    def __init__(self, dum):
        self.dum = dum

    def s_pokoji(self, pocet_pokoju):
        if pocet_pokoju < 1:
            raise ValueError("Dum musi mim nejaky pokoj")
        self.dum.pocet_pokoju = pocet_pokoju
        return self

    def s_podlazi(self, pocet_podlazi):
        if pocet_podlazi in None:
            self.pocet_podlazi = 1
        else:
            self.dum.pocet_podlazi = pocet_podlazi
        return self

    def s_oken(self, pocet_oken):
        self.dum.pocet_oken = pocet_oken
        return self

    def build(self):
        return self.dum.popsat()

# TODO rozjet ji tady nejaky printy a tvorbu domu
dum = Dum



