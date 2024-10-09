# tento priklad ma uz jasne definovane pocty jeho casti takze se zzabrani chybam v zapisu
class House:
    def __init__(self, windows=None, doors=None, garage=None, swimming_pool=None):
        self.windows = windows
        self.doors = doors
        self.garage = garage
        self.swimming_pool = swimming_pool

    def __str__(self):
        return (f"House with {self.windows} windows, {self.doors} doors, "
                f"{'a garage, ' if self.garage else 'no garage, '}"
                f"{'a swimming pool' if self.swimming_pool else 'no swimming pool'}.")


class DumEliska:
    def __init__(self):
        self._windows = 12
        self._doors = 9
        self._garage = False
        self._swimming_pool = False

    def set_windows(self, count):
        self._windows = count
        return self

    def set_doors(self, count):
        self._doors = count
        return self

    def set_garage(self, count):
        self._garage = count
        return self

    def set_swimming_pool(self, count):
        self._swimming_pool = count
        return self

    def build(self):
        # Vrátíme sestavený objekt House
        return House(self._windows, self._doors, self._garage, self._swimming_pool)


Novakovy_dum = DumEliska()
print(Novakovy_dum.build())