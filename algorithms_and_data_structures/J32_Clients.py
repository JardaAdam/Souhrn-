"""Exercise 2.1: Clients

Imagine we have a store.
Implement the store's customer abstract class and 3 classes inheriting from it.
There are three groups of customers:
- Women
- Men
- Children

Each of these groups should be addressed in a different way:
women as Madam, men as Mr, and no prefixes for children.

Each inherited class should have its own string representation.
"""

import abc
from collections import deque # oboustrana fronta pouziva appendleft, popleft
import time


class Client(abc.ABC):
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    @abc.abstractmethod
    def __str__(self) -> str:
        pass
# TODO k cemu je tady abstaktni trida

class Woman(Client):
    def __str__(self) -> str:
        return f"Madam {self.first_name} {self.last_name}"


class Man(Client):
    def __str__(self) -> str:
        return f"Mr {self.first_name} {self.last_name}"


class Child(Client):
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


"""Exercise 2.2: FIFO queue
This exercise creates a queue class using a list. 
In this case, adding an element should consist of using the append method 
(adding an object to the Horsesc queue). 
The removal of an element should be accomplished by removing the first element 
from the list by using pop (the object leaves the queue at the beginning).
"""


class FifoList:
    def __init__(self):
        self.lst = []

    def append(self, data):
        self.lst.append(data)

    def pop(self):
        if len(self.lst):
            return self.lst.pop(0) # nevihoda je ze po odebrani prvniho prvku
            # se musi zbytek seznamu preindexovat protoze index 0 je odebran!!
        return None


"""Exercise 2.3: Cash register
Implement an instance of a class that simulates store operations. 
The cash register should have a queue and be able to join and service new customers. 
Use the implemented FIFO queue class.
"""


class CashRegister:
    def __init__(self):
        self.queue = FifoList()

    def add_client(self, client: Client):
        self.queue.append(client)

    def process(self) -> Client:
        client = self.queue.pop() # po kazdem klientovy ktery se odstranuje
        # z pozice
        # print(f"Process client: {client}")
        return client


"""Exercise 2.4: A quick cash register in the store

To implement the queue, the list usage is not optimal. 
We have to remove the item from the beginning which is a costly operation that requires
copying all items on the list. This lasts proportionally to the length of the list. 
To optimize the queue operation, create a new class using the deque type available 
in the collections module.

deque has methods known from the list, i.e.append and pop. 
It also has popleft and appendleft methods. 
To get the queue behavior, use the append and popleft or appendleft and pop methods.
"""


class FasterCashRegister(CashRegister): # dedi z CashRegister

    def __init__(self):
        super().__init__()  # dedeni
        self.queue = deque()  # optimalizovana fronta pro odebirani z obou stran
        # ale je o dost rychlejsi pri odebirani z indexu 0 nez normalni definice
        # fronty. pri dlouhe fronte urcite pouzivat deque!!
        # deque = oboustana fronta
    def process(self):
        client = self.queue.popleft()  #
        # print(f"Process client: {client}")
        return client


if __name__ == '__main__':
    client1 = Woman("Anna", "Johnson")
    client2 = Man("John", "Smith")
    client3 = Child("Chris", "Novak")

    print(client1)
    print(client2)
    print(client3)

    cr = CashRegister()
    cr.add_client(client1)
    cr.add_client(client2)
    cr.add_client(client3)

    cr.process()
    cr.process()
    cr.process()

    """Exercise 2.5 Compare the duration of action
    Compare the speed of both applications."""
    start = time.time()  # ulozim si aktualni cas

    cr = CashRegister()
    for i in range(400000):
        cr.add_client(client1)
    for i in range(400000):
        cr.process()
    print(f"CashRegister: {time.time() - start}")
                        # {akrualni cas - cas zacatku}
    start = time.time()

    cr = FasterCashRegister()
    for i in range(400000):
        cr.add_client(client1)
    for i in range(400000):
        cr.process()
    print(f"FasterCashRegister: {time.time() - start}")
