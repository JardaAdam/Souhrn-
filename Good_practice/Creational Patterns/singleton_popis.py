class Jedinacek:
    _instance = None

    def __init__(self):
        pass

    def __new__(cls):  # kopiruje celou definici class Jedinacek na dalsi misto v RAM a
        # diky def __init__ do teto kopie vlozi parametry
        # raise Exception("Nelze vytvorit instanci tridy Jedinacek")  # zakazame vytvoreni kopije
        if cls._instance is None:
            cls._instance = object.__new__(cls)  # cls = chci kopiji toho kde jsem.
            # cls = class                 (vkladam sem ceho chci vytvorit kopii)
            #napr. mohl bych vytvorit kopii jine classy
        return cls._instance

    def test(self):
        pass


# print(Jedinacek.__dict__)   # vypise z jakych funkci je classa vytvorena


jedinacek = Jedinacek()
druhy_jedinacek = Jedinacek()
print(jedinacek is druhy_jedinacek)  # True -> vytvori pokazde jen sam sebe
