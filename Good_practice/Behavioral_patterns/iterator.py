class NasIterator:

    def __init__(self, start=0, end=10):
        self.current = start
        self.end = end

    # def __iter__(self):       #1
    #     return self
    #
    # def __next__(self):
    #     self.current += 1
    #     if self.current <= self.end:
    #         return self.current
    #     else:
    #         raise StopIteration

    def iteruj(self):       #2
        current = self.current
        while current <= self.end:
            yield current
            current += 1


# for i in NasIterator(5, 10):        #1
for i in NasIterator(0, 10).iteruj():   #2
    print(i)
