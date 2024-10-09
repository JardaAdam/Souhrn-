"""
Write code simulating a Stack of books. The class should allow you to add and remove books from the Stack,
browse titles in Stack and show the last position on the Stack. Use magic methods to allow for:

    adding Stacks together
    comparing Stack sizes
    Stack string representation
    stating Stack length
"""

from typing import List


class BooksStack:
    def __init__(self, stack_name, category):
        self.stack_name = stack_name
        self.category = category
        self.books_stack = []

    def add_new_book(self, title: str):
        self.books_stack.append(title)

    def get_book(self):
        return self.books_stack.pop()

    def all_books(self) -> List[str]:
        return self.books_stack

    def __add__(self, second_stack):
        new_stack = BooksStack(self.stack_name, self.category)
        new_stack.books_stack = self.books_stack + second_stack.books_stack
        return new_stack

    # comparison Fce pro porovnavani stacku
    def __gt__(self, second_stack):  # __gt__ = greater than
        return len(self) > second_stack
    """porovnavaci fce = vraci true pokud je moje knihovna vetsi nez 
    second_stack"""
    def __lt__(self, second_stack):  # less than
        return len(self) < second_stack
    """porovnavaci fce = vraci true pokud je moje knihovna nemsi nez 
    second_stack"""
    def __ge__(self, second_stack):   # greater or equal
        return len(self) >= second_stack

    def __le__(self, second_stack):   # less or equal
        return len(self) <= second_stack

    def __str__(self):    # spousti se v printu
        return f"stack: {self.stack_name} with category of books: {self.category}"

    def __repr__(self):  # representace zasobniku
        result = f"stack_name: {self.stack_name}\n"
        result += f"category: {self.category}\n"
        result += f"books: {self.books_stack}"
        return result

    def __len__(self):
        return len(self.books_stack)
    """pocita celkovi pocet knih ve stack"""


if __name__ == "__main__":
    my_books = BooksStack("My Stack of Books", "Natural")

    my_books.add_new_book("Cheetahs")
    my_books.add_new_book("Elephants")
    my_books.add_new_book("Cats")

    print(f'my books: {my_books.all_books()}')
    print(f"beru si knihu: ['{my_books.get_book()}']")
    print(my_books.all_books())

    her_books = BooksStack("Her Stack of Books", "Natural")
    her_books.add_new_book("Horses")
    print(f'her books: {her_books.all_books()}')
    our_books = BooksStack("Our stack of books", "Natural")
    our_books.books_stack = my_books.books_stack + her_books.books_stack
    print(f'nase knihy: {our_books.all_books()}')

    print(my_books > her_books)
    print(my_books <= her_books)

    print('stack')
    print(my_books)
    print('repr')
    print(repr(my_books))

    print(len(my_books))

    print(repr(our_books))
    print(len(our_books))
