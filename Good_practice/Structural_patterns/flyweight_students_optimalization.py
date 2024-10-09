"""Zadání:
Cílem je optimalizovat paměťovou náročnost aplikace pro správu studentů tím, že využiješ návrhový vzor Flyweight.
Místo toho, aby se duplikovala data u každého studenta, vytvoříme Flyweight objekt, který sdílí společné atributy
mezi studenty.

StudentFlyweight (Major):
Flyweight třída bude obsahovat atributy, které jsou společné pro více studentů, například:
major (hlavní obor),
year (ročník).

Student:
Třída, která bude reprezentovat jednotlivého studenta. Tato třída bude obsahovat unikátní atributy, například:
name (jméno),
id (identifikátor studenta).

FlyweightFactory (MajorFactory):
Třída, která bude spravovat a vracet Flyweight objekty na základě sdílených atributů (obor, ročník).
Pokud již existuje Flyweight pro danou kombinaci, použije se existující instance, jinak se vytvoří nová.

Postup:
Vytvoř Flyweight třídu a implementuj factory pro správu sdílených dat.
Zajisti, aby se neustále nevytvářely nové instance Flyweight, ale místo toho se používaly sdílené objekty.
Flyweight objekt bude použit studenty, aby se snížilo množství redundance v paměti.

Nápověda:
Použij například slovník (dict) ve FlyweightFactory pro ukládání Flyweight objektů. Klíčem může být kombinace
oboru a ročníku. (edited) """


class Major:
    # majors = []      #
    #
    # def __new__(cls, name, year):
    #     for major in cls.majors:
    #         if major.name == name and major.year == year:
    #             return major
    #
    #     new_major = object.__new__(cls)
    #     cls.majors.append(new_major)
    #     return new_major

    def __init__(self, name, year):
        self.name = name
        self.year = year

    def a(self):
        ...

    def b(self):
        ...



class Student:
    def __init__(self, name, id, year, name_of_major):
        self.name = name
        self.id = id
        self.year = year
        # self.major = Major(name=name_of_major, year=year)  # volani pro Major.__new__
        self.major = MajorFactory.get_major(name=name_of_major, year=year)


class MajorFactory:
    majors = []

    @classmethod
    def get_major(cls, name, year):
        for major in cls.majors:
            if major.name == name and major.year == year:
                return major
        new_major = Major(name, year)
        cls.majors.append(new_major)
        return new_major


student_1 = Student("Honza", 10, 2022, "Biology")
student_2 = Student("Pepa", 15, 2022, "Biology")
print(student_1.major.name)
print(student_2.major)
print(student_1.major is student_2.major)
