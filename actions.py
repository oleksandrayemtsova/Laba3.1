from exception import InputError
import threading


def try_except():
    try:
        action = int(input())
    except ValueError as error:
        print(f"Oops {error}! The output is not a number")
    except KeyboardInterrupt:
        print(f"Oops KeyboardInterrupt error!")
    else:
        return action


def receive_the_book(reader, action):
    while True:
        print(f"Would you like to {action} the book?\n"
              "1-Yes\n"
              "2-No")
        answer = try_except()
        if action == "return":
            if answer == 1:
                return "pass"
            if answer == 2:
                return "break"
            if reader.library_card.size == 3:
                print("You have returned all the books")
                return "break"
            else:
                print("You entered an incorrect action number. Please enter 1 or 2: ")
                pass
        if action == "reserve":
            if answer == 1:
                return "pass"
            if answer == 2:
                return "break"
            if reader.library_card.size == 3:
                print("You have reserved the maximum number of books")
                return "break"
            else:
                print("You entered an incorrect action number. Please enter 1 or 2: ")
                pass


def worker(lock, option, library, reader, id_book):
    lock.acquire()
    print('We started booking the book', option.name)
    for book in library.keys:
        if 0 < int(id_book) <= library.size and int(id_book) == book:
            try:
                if library.library[book].book_number == 0:
                    raise InputError(id_book,
                                     "Sorry, this book is reserved for another reader, please select another one:")
            except InputError as err:
                print(err)
                break
            else:
                print(library.request_to_receive_a_book(int(id_book), reader))
                break
    else:
        print("Invalid ID\nPlease enter a valid ID:")
    print('Finished reserving the book', option.name)
    lock.release()


def book_a_book(library, reader):
    print("Please enter the ID of the selected book: ")
    while True:
        print(library)
        id_book = input("Please enter the numbers of the books you want to book separated by a space: ").split()
        print('You have selected the following books:')
        for item in id_book:
            print('-', library.library[int(item)].name)
        print('Expect...')
        tasks = []
        lock = threading.Lock()
        for item in id_book:
            tasks.append(threading.Thread(target=worker, args=(lock, library.library[int(item)], library, reader, item)))
        for task in tasks:
            task.start()
        for task in tasks:
            task.join()
        print('Thank you for waiting!')
        answer = receive_the_book(reader, "reserve")
        if answer == "pass":
            pass
        if answer == "break":
            break


def return_the_book(reader, library):
    while True:
        print("Please enter the ID of the book you want to return:")
        return_book = try_except()
        for book in reader.library_card.books:
            for key in library.keys:
                if book.name == library.library[key].name:
                    print(reader.library_card.request_to_return_a_book(return_book))
                    break
            else:
                print("Please enter a different book ID for the book you want to return")
                break
        answer = receive_the_book(reader,"return")
        if answer == "break":
            break
        if answer == "pass":
            pass


def actions(library, reader):
    while True:
        print("Please enter the number of the action you want to perform: ")
        print(f"1 - book a book\n"
              f"2 - return the book\n"
              f"3 - I don't want to do anything")
        action = try_except()
        print(f"You chose {action}")
        if action == 1:
            book_a_book(library, reader)
        if action == 2:
            return_the_book(reader, library)
        if action == 3:
            print("Thank you for visiting us!!!")
            break
        else:
            print("You have reached the main menu. Select the following action or enter it correctly from 1 to 3")

