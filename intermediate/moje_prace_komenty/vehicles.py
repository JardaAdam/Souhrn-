# Vytvor triedu Vehicle, z ktorej budeme vytvarat pomocou dedicnosti nasledovne triedy:
# - Motorcycle
# - Car
# - Bus
#
# Vehicle ma napriklad atributy
# - brand
# - model
# - color
# - number_of_wheels
# - max_speed - bude definovane natvrdo pre autobusy
# - seat_capacity
#
# metody definovane v triede Vehicle:
# - start (nieco vypise)
# - get_color (vypise farbu)
# - is_possible_to_reach(speed) (vrati True alebo False podla toho, ci moze vehicle dosiahnut zadanu rychlost)

# Na zaver vytvor kratku ukazku, kde si vytvoris objekty a zavolas na ne metody.

"""muj postup"""

class Vehicles:

    def __init__(self, brand, model, color, n_of_wheels, max_speed, seat_capacity):
        self.brand = brand
        self.model = model
        self.color = color
        self.n_of_wheels = n_of_wheels
        self.max_speed = max_speed
        self.seat_capacity = seat_capacity


    def __str__(self):
        return f'{self.color} {self.brand} {self.model}'
    """zde vypisuji co se vypise ve startu"""
    def start(self):
        print(f'Starting {self}')

    def get_color(self):
        print(self.color)

    def is_possidle_to_reach(self, speed):
        return 0 <= speed <= self.max_speed
    """diky teto definici se mi potom vypise True, False"""


class Motorcycles(Vehicles):
    def __init__(self, brand, model, color, max_speed, seat_capacity):
        """init ktery se opakuje z tridy Vehicles"""
        super().__init__(brand, model, color, 2, max_speed, seat_capacity)
        """tady vypisuju veci ktere jsou pro tuto tridu jasne dane a nemeni se
        (motorka ma vzdy dve kola)"""


class Car(Vehicles):

    def __init__(self, brand, model, color, max_speed, seat_capacity):

        super().__init__(brand, model, color, 4, max_speed, seat_capacity)


class Bus(Vehicles):
    MAX_SPEED = 80

    def __init__(self, brand, model, color, n_of_wheels, seat_capacity):

        super().__init__(brand, model, color, n_of_wheels, self.MAX_SPEED, seat_capacity)


class CarCompany:
    def __init__(self):
        self.vehicle_list: list[Vehicles] = []

    def add_vehicle(self, vehicle: Vehicles):
        self.vehicle_list.append(vehicle)

    def show_vehicles(self):
        for vehicle in self.vehicle_list:
            print(vehicle)
        print(f"Total vehicles:", len(self.vehicle_list))

    def calculate_wheels(self):
        wheel_counter = 0
        for vehicle in self.vehicle_list:
            wheel_counter += vehicle.n_of_wheels

        return wheel_counter

    def calculate_seats(self):
        seat_counter = 0
        for vehicle in self.vehicle_list:
            seat_counter += vehicle.seat_capacity

        return seat_counter


if __name__ == "__main__":

    subaru = Car('Subaru', 'Legacy', 'Silver', 260, 5)
    subaru.start()
    subaru.get_color()
    print(subaru.is_possidle_to_reach(150))
    print(subaru.is_possidle_to_reach(270))

    school_bus = Bus('school', 'bus', 'yellow', 6, 46)
    school_bus.start()
    school_bus.get_color()
    print(school_bus.is_possidle_to_reach(10))
    print(school_bus.is_possidle_to_reach(150))

    motorbike = Motorcycles('Suzuky', '500', 'blue', 300, 2)
    motorbike.start()
    motorbike.get_color()
    print(motorbike.is_possidle_to_reach(350))

    print("count car", end="\n\n\n\n")

    the_best_car_company = CarCompany()
    the_best_car_company.add_vehicle(subaru)
    the_best_car_company.add_vehicle(school_bus)
    the_best_car_company.add_vehicle(motorbike)
    the_best_car_company.show_vehicles()
    print(the_best_car_company.calculate_seats())
    print(the_best_car_company.calculate_wheels())
