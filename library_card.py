
class LibraryCard:
    counter_number = 0

    def __init__(self, owner):
        LibraryCard.counter_number += 1
        self.__number = LibraryCard.counter_number
        self.__owner = owner
        self.books = []

    def __str__(self):
        print(f"{'*'*170}\nLibrary card:\nNumber: №{self.number}, Owner: {self.owner}")
        print(f"Books: {len(self.books)}")
        for book in self.books:
            print(f"Name: {book.name}")
        return f"{'*'*170}"

    @property
    def number(self):
        return self.__number

    @property
    def owner(self):
        return self.__owner

    @property
    def size(self):
        return len(self.books)

    def add_book(self, book, return_date):
        self.books.append(book)
        print(f"You have borrowed the book '{book.name}' and must return it by {return_date}")

    def return_book(self, book):
        book.book_number += 1
        self.books.remove(book)
        print(f"Thank you, you have returned the book '{book.name}'")

    def request_to_return_a_book(self, id_book):
        for book in self.books:
            from main import bookshelves
            for key in bookshelves.keys:
                if id_book == key - 10:
                    if book.name == bookshelves.library[key].name:
                        self.return_book(book)
                        return f"Thank you for choosing our library!!!"
        else:
            return f"We're sorry, you haven't yet reserved the book with the ID {id_book}"


