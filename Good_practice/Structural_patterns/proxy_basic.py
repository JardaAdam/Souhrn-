"""Proxy je návrhový vzor, který se používá k tomu, aby mezi klientem a
skutečným objektem stál zprostředkující objekt (proxy). Tento zprostředkovatel
může přidávat další funkce, jako je kontrola přístupu, ukládání do mezipaměti,
logování nebo řízení životního cyklu objektu.
Jednoduše řečeno, Proxy je jako "zástupce", který stojí mezi tebou (klientem) a
reálným objektem, ke kterému chceš přistupovat."""

"""Představ si, že máme třídu, která simuluje pomalý přístup k serveru, 
protože stahování dat trvá dlouho. Místo toho, abychom pokaždé přistupovali k 
serveru přímo, můžeme použít Proxy, která načte data pouze jednou a příště je 
použije z mezipaměti, čímž ušetříme čas."""

# 1. Skutečný objekt (Real Subject)
# Tento objekt představuje skutečný přístup k serveru.

# Skutečný objekt, který simuluje pomalý přístup k serveru
class Server:
    def get_data(self):
        print("Načítání dat ze serveru... (může to chvíli trvat)")
        return "Data ze serveru"


"""2. Proxy objekt
Proxy objekt zprostředkovává přístup ke skutečnému objektu. 
V tomto případě proxy zajistí, že data ze serveru budou stažena pouze jednou. 
Při opakovaném volání proxy použije uložená data z mezipaměti."""

# Proxy, která zprostředkovává přístup k serveru
class ServerProxy:
    def __init__(self):
        self.server = Server()  # Proxy obsahuje skutečný server
        self.cached_data = None  # Proměnná pro uložení dat z mezipaměti

    def get_data(self):
        if self.cached_data is None:
            # Data ještě nejsou uložena v mezipaměti, načti je ze serveru
            self.cached_data = self.server.get_data()
        else:
            print("Používání dat z mezipaměti...")
        return self.cached_data

# 3. Použití proxy
# Teď použijeme proxy ke stažení dat. První volání načte data ze serveru,
# další volání už budou data používat z mezipaměti.

# Použití proxy k přístupu na server
proxy = ServerProxy()

# První volání načte data ze serveru
print(proxy.get_data())  # Načítání dat ze serveru... Data ze serveru

# Druhé volání použije uložená data
print(proxy.get_data())  # Používání dat z mezipaměti... Data ze serveru


"""Shrnuti:
Proxy vzor je o tom, že vytvoříme "zástupce" (proxy), který stojí mezi klientem (tebou) 
a skutečným objektem (např. serverem).

Proxy může řídit, jak a kdy se k tomuto objektu přistupuje. V našem případě jsme 
použili proxy k tomu, aby se data ze serveru stáhla jen jednou a při dalších 
voláních se použila data z mezipaměti.

Proxy vzor může být použit například pro kontrolu přístupu, ukládání do mezipaměti 
(jako v našem případě) nebo logování.

Proxy je užitečné tam, kde chceme mít kontrolu nad tím, jakým způsobem a kdy se 
k reálnému objektu přistupuje, což může optimalizovat výkon a zjednodušit práci 
s objekty, které mají náročné operace (jako například přístup k serveru).
"""

