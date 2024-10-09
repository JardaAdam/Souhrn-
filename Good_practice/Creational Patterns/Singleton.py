# hash = TODO co to je
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        pass

    class NotSingleton:
        def __init__(self):
            pass

    s = NotSingleton()
    print("Neni jedinacek 1:", hash(s))
    s2 = NotSingleton()
    print("Neni jedinacek 2:", hash(s2))

    class Singleton:
        _instance = None

        def __new__(cls, *args, **kwargs):
            if cls._instance is None:  # Pokud jsme jeste zadnou instanci nevytvorili
                cls._instance = object.__new__(cls, *args, **kwargs)  # vytvor pokud jeste neni vytvorena
            return cls._instance  # pokud jsme nejakou uz vytvorili tak ji vrat

        """pouzivat aby se nevitvarel novi objekt pokud uz je jeden vytvoreny """

        def __init__(self):
            pass


# TODO nechat si to vysvetlit od chat Gpt

s_t = Singleton()
print("Tohle uz je singleton 1:", hash(s_t))
s_t2 = Singleton()
print("Tohle uz je singleton 2:", hash(s_t2))

"""tento singleton se jednou vytvori a potom se vola s dalsich souborech 
"""
# Modulový Singleton
# V Pythonu jsou moduly přirozeně singletony, protože jsou načteny pouze jednou.
# Můžete tedy použít modul k implementaci singletonu.
# singleton.py
shared_variable = "Shared Variable"

# module1.py
import singleton

print(singleton.shared_variable)
singleton.shared_variable()  # " (modified by module1)"

# module2.py
import singleton

print(singleton.shared_variable)


# Borg Singleton
# Borg vzor umožňuje sdílení stavu mezi různými instancemi třídy.

class Borg:
    _shared_state = {}

    def __init__(self):
        self.__dict__ = self._shared_state


borg1 = Borg()
borg2 = Borg()

borg1.state = "State"
print(borg2.state)  # State
