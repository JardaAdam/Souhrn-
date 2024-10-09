class dragon:

    """idealne jeste udelat predka pro Dragon a Fighter"""

    def __init__(self, jmeno, zivoty):
        self.jmeno = jmeno
        self.zivoty = zivoty


    def predstav_se(self):
        print(f"Ja jsem dragon {self.jmeno} a mam {self.zivoty} zivotu.")