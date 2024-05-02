from book import Book
from library import Library
from reader import Reader
from exception import InputError


def main():
    book1 = Book("Панк 57", "Пенелопа Дуглас", "КСД", 2019, 448, "firm", "Ukrainian", "A5")
    book2 = Book("Для стосунків потрібні двоє", "Володимир Станчишин", "Vivat", 2021, 280, "firm", "Ukrainian", "A5")
    book3 = Book("Емоційні гойдалки війни", "Володимир Станчишин", "Vivat", 2022, 288, "firm", "Ukrainian", "A5")
    book4 = Book("Дім Землі та Крові", "Сара Маас", "ВСЛ", 2024, 880, "firm", "Ukrainian", "A5")
    book5 = Book("Двір срібного полум’я", "Сара Маас", "Vivat", 2023, 896, "firm", "Ukrainian", "A5")
    book6 = Book("Двір холоду і зоряного сяйва", "Сара Маас", "ВСЛ", 2023, 256, "firm", "Ukrainian", "A5")
    book7 = Book("Трон зі скла", "Сара Маас", "Vivat", 2022, 544, "firm", "Ukrainian", "A5")
    book8 = Book("Неприродні випадки", "Річард Шеперд", "РМ", 2020, 448, "firm", "Ukrainian", "A5")
    book9 = Book("Сім етапів смерті", "Річард Шеперд", "РМ", 2023, 320, "firm", "Ukrainian", "A5")
    book10 = Book("Діана", "Ендрю Мортон", "Абабагаламага", 2024, 400, "firm", "Ukrainian", "A5")
    array = [book1, book2, book3, book4, book5, book6, book7, book8, book9, book10]
    library = Library()
    print(f"Welcome to the library!")
    reader = Reader("Sasha", "Yemtsova", "18", "380687562929")
    print(f"Here is your library card:")
    print(reader)
    for book in array:
        library.add_book(book, 2)
    print(library.find_by_author("Сара Маас"), "\n")
    print(library.find_by_publishing("Vivat"), "\n")
    print(library.published_after_this_year(2023), "\n")
    print(library.books_in_the_page_range(250, 350), "\n")
    print(library.books_in_the_page_range(900, 400), "\n")
    print(library.request_to_receive_a_book(5, reader))
    while True:
        print("Please enter the number of the action you want to perform: ")
        print(f"1 - book a book\n2 - return the book\n3 - I don't want to do anything")
        try:
            action = int(input())
        except ValueError as error:
            print(f"Oops {error}! The output is not a number")
        except KeyboardInterrupt:
            print(f"Oops KeyboardInterrupt error!")
        else:
            if action == 1:
                print("Please enter the ID of the selected book: ")
                while True:
                    print(library)
                    try:
                        id_book = int(input())
                    except ValueError as error:
                        print(f"Oops {error}! The output is not a number")
                    except KeyboardInterrupt:
                        print(f"Oops KeyboardInterrupt error!")
                    else:
                        for book in library.array:
                            if id_book <= library.size and id_book > 0:
                                if id_book == book.id:
                                    try:
                                        if book.book_number == 0:
                                            raise InputError(id_book, "Sorry, this book is reserved for another reader, please select another one:")
                                    except InputError as err:
                                        print(err)
                                        break
                                    else:
                                        print(library.request_to_receive_a_book(book.id, reader))
                                        break
                            else:
                                print("Invalid ID\nPlease enter a valid ID:")
                                break
                        print("Would you like to receive the book?\n1-Yes\n2-No")
                        try:
                            answer = int(input())
                        except ValueError as error:
                            print(f"Oops {error}! The output is not a number")
                            break
                        except KeyboardInterrupt:
                            print(f"Oops KeyboardInterrupt error!")
                            break
                        else:
                            if answer == 1:
                                pass
                            if answer == 2:
                                break
                            if reader.library_card.size == 3:
                                print("You have reserved the maximum number of books")
                                break
            elif action == 2:
                while True:
                    print("Please enter the ID of the book you want to return:")
                    try:
                        return_book = int(input())
                    except ValueError as error:
                        print(f"Oops {error}! The output is not a number")
                    except KeyboardInterrupt:
                        print(f"Oops KeyboardInterrupt error!")
                    else:
                        for book in reader.library_card.books:
                            if return_book == book.id:
                                print(reader.library_card.request_to_return_a_book(return_book))
                                break
                            else:
                                print("Please enter a different book ID for the book you want to return")
                                break
                        print("Would you like to return the book?\n1-Yes\n2-No")
                        try:
                            answer = int(input())
                        except ValueError as error:
                            print(f"Oops {error}! The output is not a number")
                            break
                        except KeyboardInterrupt:
                            print(f"Oops KeyboardInterrupt error!")
                            break
                        else:
                            if answer == 1:
                                pass
                            if answer == 2:
                                break
                            if reader.library_card.size == 0:
                                print("You have returned all the books")
                                break
            elif action == 3:
                print("Thank you for visiting us!!!")
                break
            else:
                print("You have entered an incorrect action number, please enter 1 to 3")


if __name__ == "__main__":
    main()
