class House:
    def __init__(self, windows=None, doors=None, garage=None, swimming_pool=None):
        self.windows = windows
        self.doors = doors
        self.garage = garage
        self.swimming_pool = swimming_pool

    def __str__(self):
        return (f"House with {self.windows} windows, {self.doors} doors, "
                f"{'and garage, ' if self.garage else 'no garage, '}"
                f"{'and swimming pool' if self.swimming_pool else 'no swimming pool'}.")


class HouseBuilder:  # typ kde
    def __init__(self, windows=0, doors=0, garage=False, swimming_pool=False):
        # Inicializujeme dům s výchozími hodnotami
        self.house = House(windows, doors, garage, swimming_pool)

    def set_windows(self, windows):
        self.house.windows = windows
        return self

    def set_doors(self, doors):
        self.house.doors = doors
        return self

    def set_garage(self, garage):
        self.house.garage = garage
        return self

    def set_swimming_pool(self, swimming_pool):
        self.house.swimming_pool = swimming_pool
        return self

    def build(self):
        # Vrátíme sestavený objekt House
        return self.house


if __name__ == "__main__":
    # Vytvoříme dům pomocí výchozích hodnot z konstruktoru
    default_house = HouseBuilder().build()
    print(f'defailt {default_house}')  # House with 0 windows, 0 doors, no garage, no swimming pool.

    # Vytvoříme dům s 4 okny, 2 dveřmi, garáží a bazénem
    custom_house = (HouseBuilder(windows=4, doors=2, garage=True, swimming_pool=True).build())
    print(f'custom {custom_house}')  # House with 4 windows, 2 doors, a garage, a swimming pool.

    # Další přizpůsobení domu
    another_house = (HouseBuilder()
                     .set_windows(3)
                     .set_doors(1)
                     .set_garage(False)
                     .set_swimming_pool(True)
                     .build())
    print(f'another {another_house}')  # House with 3 windows, 1 doors, no garage, a swimming pool.

    Jarda_house = (HouseBuilder(10, 5, True, True).build())
    print(f'Jarda {Jarda_house}')
