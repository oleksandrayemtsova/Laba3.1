class LibraryCard:
    counter_number = 0

    def __init__(self, owner):
        LibraryCard.counter_number += 1
        self.__number = LibraryCard.counter_number
        self.__owner = owner
        self.__books = []

    def __str__(self):
        print(f"\n{'*'*100}\nLibrary card:\nNumber: №{self.number}, Owner: {self.owner}\nBooks: {self.books}")
        for book in self.__books:
            print(f"ID: {book.id}, Name: {book.name}, Return date: {book.return_date}")
        return f"{'*'*100}\n"

    @property
    def number(self):
        return self.__number

    @property
    def owner(self):
        return self.__owner

    @property
    def books(self):
        return f"You have {len(self.__books)} books reserved for you"

    @books.setter
    def books(self, book):
        self.__books = book

    @property
    def size(self):
        return len(self.__books)

    def add_book(self, book, return_date):
        self.__books.append(book)
        book.return_date = return_date
        print(f"You have borrowed the book '{book.name}' and must return it by {return_date}")

