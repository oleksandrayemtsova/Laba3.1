class Library:
    def __init__(self):
        self.array = []
        self.size = len(self.array)

    def add_book(self, book):
        self.array.append(book)

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
            if range1 < range2:
                for book in self.array:
                    if range1 <= book.pages <= range2:
                        found_books.append(book)
                        print(f"ID: {book.id}, Name: {book.name}, Pages: {book.pages}")
                return f"Number of books with the number of pages from {range1} to {range2} : {len(found_books)}"
            if range2 < range1:
                for book in self.array:
                    if range2 <= book.pages <= range1:
                        found_books.append(book)
                        print(f"ID: {book.id}, Name: {book.name}, Pages: {book.pages}")
                return f"Number of books with the number of pages from {range2} to {range1}: {len(found_books)}"
        else:
            print("The ranges must be greater than zero!")
