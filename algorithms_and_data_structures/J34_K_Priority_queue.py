"""Prioritní fronta
Zadání:
Implementujte frontu, která dokáže zpracovávat prioritní prvky.
Prioritní prvky by měly být vždy zpracovány před ne-prioritními prvky,
přičemž pořadí v rámci prioritní nebo ne-prioritní fronty by mělo být FIFO.

prioritní1 neprioritní1 neprioritní2 prioritní2
-> prioritní1 prioritní2 neprioritní1 neprioritní2
"""
from collections import deque


# varianta s jendou frontou
# class PriorityQueue:
#     def __init__(self):
#         # Použijeme jednu frontu pro všechny prvky
#         self.queue = deque()
#
#     def enqueue(self, item, priority=False):
#         if priority:
#             # Prioritní prvky přidáme na začátek fronty
#             self.queue.appendleft(item)
#         else:
#             # Ne-prioritní prvky přidáme na konec fronty
#             self.queue.append(item)
#
#     def dequeue(self):
#         if self.queue:
#             # Odebíráme prvek z konce (FIFO)
#             return self.queue.popleft()
#         else:
#             raise IndexError("Dequeue from an empty queue")


# varianta s dvema frontami

class PriorityQueue:
    def __init__(self):
        # Dvě oddělené fronty: jedna pro prioritní a druhá pro ne-prioritní prvky
        self.priority_queue = deque()
        self.normal_queue = deque()

    def enqueue(self, item, priority=False):
        if priority:
            self.priority_queue.append(item)
        else:
            self.normal_queue.append(item)

    def dequeue(self):
        if self.priority_queue:
            return self.priority_queue.popleft()
        if self.normal_queue:
            return self.normal_queue.popleft()
        else:
            return IndexError("Dequeue from an empty queue")


if __name__ == '__main__':
    queue = PriorityQueue()
    queue.enqueue("normal task 1")
    queue.enqueue("normal task 2")
    queue.enqueue("priority task 1", True)
    queue.enqueue("priority task 2", True)
    queue.enqueue("normal task 3")
    queue.enqueue("normal task 4")

    print(queue.dequeue())  # "priority task 1"
    print(queue.dequeue())  # "priority task 2"
    print(queue.dequeue())  # "normal task 1"
    print(queue.dequeue())  # "normal task 2"
    print(queue.dequeue())  # "normal task 3"
    print(queue.dequeue())  # "normal task 4"
    print(queue.dequeue())  # "Dequeue from an empty queue"