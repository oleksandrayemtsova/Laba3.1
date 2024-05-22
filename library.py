import datetime


class Library:
    id_counter = 0

    def __init__(self):
        self.library = {}
        self.keys = self.library.keys()

    @property
    def size(self):
        return len(self.library)

    def add_book(self, book, quantity):
        Library.id_counter += 1
        book.book_number = quantity
        self.library[Library.id_counter] = book

    def __str__(self):
        for book in self.library.keys():
            print('Id:', book, self.library[book])
        return f"There are {self.size} books in the library"

    def find_by_author(self, author):
        found_books = []
        for book in self.library.keys():
            if author in self.library[book].author:
                found_books.append(self.library[book])
                print(f"id: {book}, name: {self.library[book].name}, author: {self.library[book].author}")
        return f"Number of books by '{author}': {len(found_books)}"

    def find_by_publishing(self, publishing):
        found_books = []
        for book in self.library.keys():
            if publishing in self.library[book].publishing:
                found_books.append(self.library[book])
                print(f"id: {book}, name: {self.library[book].name}, publishing: {self.library[book].publishing}")
        return f"Number of books by the publisher {publishing}: {len(found_books)}"

    def published_after_this_year(self, year):
        found_books = []
        for book in self.library.keys():
            if year <= self.library[book].year:
                found_books.append(self.library[book])
                print(f"id: {book}, name: {self.library[book].name}, year: {self.library[book].year}")
        return f"Number of books published after {year}: {len(found_books)}"

    def books_in_the_page_range(self, range1, range2):
        found_books = []
        if range1 and range2 > 0:
            if range1 > range2:
                range1, range2 = range2, range1
            for book in self.library.keys():
                if range1 <= self.library[book].pages <= range2:
                    found_books.append(self.library[book])
                    print(f"id: {book}, name: {self.library[book].name}, pages: {self.library[book].pages}")
            return f"Number of books with the number of pages from {range1} to {range2} : {len(found_books)}"
        else:
            print("The ranges must be greater than zero!")

    def request_to_receive_a_book(self, id_book, reader):
        for book in self.library.keys():
            if id_book == book:
                if self.library[book].book_number >= 1:
                    if reader.library_card.size < 5:
                        self.library[book].book_number -= 1
                        today = datetime.date.today()
                        return_date = today + datetime.timedelta(days=30)
                        reader.library_card.add_book(self.library[book], return_date)
                        return f"Thank you for choosing our library!!!"
                    else:
                        return f"You have already reserved the maximum number of books!"
                else:
                    return f"Unfortunately, this book is reserved!"
        else:
            return f"Book with ID {id_book} does not exist in the library!"


