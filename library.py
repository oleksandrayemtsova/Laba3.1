import datetime


class Library:
    def __init__(self):
        self.array = []

    @property
    def size(self):
        return len(self.array)

    def add_book(self, book, quantity):
        book.book_number = quantity
        self.array.append(book)

    def __str__(self):
        for book in self.array:
            print(f"ID: {book.id}, Name: {book.name}, Author: {book.author}, Publishing: {book.publishing}, Year: {book.year}, Pages: {book.pages}, Binding: {book.binding}, Language: {book.language}, Size: {book.size}")
        return f"There are {self.size} books in the library"

    def find_by_author(self, author):
        found_books = []
        for book in self.array:
            if author in book.author:
                found_books.append(book)
                print(f"ID: {book.id}, Name: {book.name}, Author: {book.author}")
        return f"Number of books by '{author}': {len(found_books)}"

    def find_by_publishing(self, publishing):
        found_books = []
        for book in self.array:
            if publishing in book.publishing:
                found_books.append(book)
                print(f"ID: {book.id}, Name: {book.name}, Publishing: {book.publishing}")
        return f"Number of books by the publisher {publishing}: {len(found_books)}"

    def published_after_this_year(self, year):
        found_books = []
        for book in self.array:
            if year <= book.year:
                found_books.append(book)
                print(f"ID: {book.id}, Name: {book.name}, Publishing: {book.year}")
        return f"Number of books published after {year}: {len(found_books)}"

    def books_in_the_page_range(self, range1, range2):
        found_books = []
        if range1 and range2 > 0:
            if range1 > range2:
                range1, range2 = range2, range1
            for book in self.array:
                if range1 <= book.pages <= range2:
                    found_books.append(book)
                    print(f"ID: {book.id}, Name: {book.name}, Pages: {book.pages}")
            return f"Number of books with the number of pages from {range1} to {range2} : {len(found_books)}"
        else:
            print("The ranges must be greater than zero!")

    def request_to_receive_a_book(self, id_book, reader):
        for book in self.array:
            if id_book == book.id:
                if book.book_number >= 1:
                    if reader.library_card.size < 3:
                        book.book_number -= 1
                        today = datetime.date.today()
                        return_date = today + datetime.timedelta(days=30)
                        reader.library_card.add_book(book, return_date)
                        return f"Thank you for choosing our library!!!"
                    else:
                        return f"You have already reserved the maximum number of books!"
                else:
                    return f"Unfortunately, this book is reserved!"
        else:
            return f"Book with ID {id_book} does not exist in the library!"


