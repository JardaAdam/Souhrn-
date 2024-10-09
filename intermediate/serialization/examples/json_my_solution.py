import json
from dataclasses import dataclass


# Task 1
# Napis funkciu load_book_from_json(file_name), ktora nacita knihy do dataclassy
# Book (ktoru treba tiez vytvorit)


@dataclass(frozen=True)
class Book:
    title: str
    author: str
    year: int
    isbn: str

    def __str__(self):
        return f'{self.title} by {self.author} from {self.year}. ISBN: {self.isbn}'


def load_books_from_json(file_name):
    loaded_books = []
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            data = json.load(file)
            books_data = data.get('books', [])
            """musim provest inport json"""
            for book in books_data:
                loaded_books.append(Book(**book))
    except FileNotFoundError:
        print(f"File {file_name} not found.")
    return loaded_books


# with open("books.json") as in_file:
#     data = json.load(in_file)
# print(data['books'])


# Task 2
# Napis funkciu print_books(books), ktora v peknom formate vypise vsetky knihy
# a na zaver vypise aj ich pocet


def print_books(books):
    for book in books:
        print(book)
    print(f'book count: {len(books)}')


# Task 3
# Napis funkciu add_book(book), ktora upravi json file `books.json` tak, ze sa don
# prida nova kniha predana cez parameter `book` (typu `Book`)


def add_book(book):
    """spatne provedeny zapis!"""

    # with open("books.json", 'a', encoding='utf-8') as out_file:
        #json.dump(new_book, out_file, indent=2)
    try:
        with open('books.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            books = data.get('books', [])
    except FileNotFoundError:
        data = {'books': []}
        books = data['books']
        """pri druhem zpusteni se zapise znovu pridavana kniha.
        chce to osetrit podminkou aby se nezapsala kniha podruhe"""
    books.append(book.__dict__)

    with open("books.json", 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


# Task 4
# Napis funkciu remove_book(isbn), ktora vymaze knihu z .json suboru podla isbn cisla.

def remove_book(isbn_value):
    with open('books.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Hledání slovníku s daným ISBN
    for book in data.get("books", []):
        if book.get("isbn") == isbn_value:
            data["books"].remove(book)
            print(f"Odstraněn slovník s ISBN '{isbn_value}': {book}")
            break
    else:
        print(f"Slovník s ISBN '{isbn_value}' nebyl nalezen.")

    with open('books.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=2)

    # Použití funkce

print('vystup')

if __name__ == '__main__':
    file_name = 'books.json'

    print("task 2")
    """Load and print existing books"""
    books = load_books_from_json(file_name)
    print_books(books)

    print("task 3")
    # new_book = {
    #         "title": "Babička",
    #         "author": "Božena Němcová",
    #         "year": 1855,
    #         "isbn": "978-8000063370"}
    # add_book(new_book)

    """Add a new book"""
    new_book = Book(
        title="Babička",
        author="Božena Němcová",
        year=1855,
        isbn="978-8000063370"
    )
    add_book(new_book)

    """print books after adding the new one"""
    print("Books after adding new book:")
    """Count_book -> tento radek musim napsat znovu aby se zapocitala i posledni zmena"""
    books = load_books_from_json(file_name)
    print_books(books)
    """remove_book -> funkce se musi radit pod sepe v poradi ve kterem se maji provadet!!
>nevim proc ale kdyz je tento zapis tady tak mi nejak rusi zapis ceskych pismen v kooks.json
>pokud ho zakomentuji tak se v souboru books.json zapise vsechno vporadku, pokud dam tento
zapis nad zapis Add tak to se zapisem do books.json taky nic neudela!!"""
    isbn_value = 'isbn'
    remove_book("978-0061120084")

    books = load_books_from_json(file_name)
    print_books(books)

#, encoding='utf-8'
# isbn = "978-0061120084"
#     remove_book(isbn)