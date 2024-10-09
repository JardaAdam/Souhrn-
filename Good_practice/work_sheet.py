class Major:
    majors = []

    def __new__(cls, name, year):
        for major in cls.majors:
            if major.name == name and major.year == year:
                return major
        new_major = object.__new__(cls)
        cls.majors.append(new_major)
        return new_major

    def __init__(self, name, year):
        self.name = name
        self.year = year

    def a(self):
        pass

    def b(self):
        pass


class Student:
    def __init__(self, name, id, year, name_of_major):
        self.name = name
        self.year = year
        self.id = id
        self.major = Major(name=name_of_major, year=year)
