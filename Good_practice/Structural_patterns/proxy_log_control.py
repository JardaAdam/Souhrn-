class RealObject:
    def request(self):
        return "Reálný objekt: Požadavek zpracován"

class Proxy:
    def __init__(self, real_object):
        self._real_object = real_object

    def request(self):
        print("Proxy: Nějaké dodatečné operace před voláním skutečného objektu.")
        return self._real_object.request()

# Vytvoříme skutečný objekt
real_object = RealObject()

# Vytvoříme proxy, které obalí skutečný objekt
proxy = Proxy(real_object)

# Použijeme proxy k volání metody request
response = proxy.request()
print(response)