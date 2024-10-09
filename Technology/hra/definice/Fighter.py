class fighter:


    def __init__(self, jmeno, zivoty):
        self.jmeno = jmeno
        self.zivoty = zivoty


    def predstav_se(self):
        print(f"Ja jsem fighter {self.jmeno} a mam {self.zivoty} zivotu.")