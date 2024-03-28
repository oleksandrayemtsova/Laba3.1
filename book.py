class Book:
    id_counter = 0
    name_publishing = {"КСД", "Vivat", "ВСЛ", "Абабагаламага", "РМ"}
    name_binding = {"firm", "mild", "supercover"}
    name_language = {"Ukrainian", "English", "German", "French", "Spanish"}
    name_size = {"A3", "A4", "A5", "A6"}
    name_reservation = {"There is a reservation", "Does not have a reservation"}

    def __init__(self, name, author, publishing, year=2024, pages=200, binding="firm", language="Ukrainian", size="A4", reservation="Does not have a reservation", return_date=0):
        Book.id_counter += 1
        self.__id = Book.id_counter
        self.__name = name
        self.__author = author
        self.__publishing = publishing
        self.__year = year
        self.__pages = pages
        self.__binding = binding
        self.__language = language
        self.__size = size
        self.__reservation = reservation
        self.__return_date = return_date

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if type(name) == str:
            self.__name = name
        else:
            print("Name must be a string!")

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, author):
        if type(author) == str:
            self.__author = author
        else:
            print("Author must be a string!")

    @property
    def publishing(self):
        return self.__publishing

    @publishing.setter
    def publishing(self, publishing):
        if type(publishing) == str:
            for i in Book.name_publishing:
                if publishing == i:
                    self.__publishing = publishing
                    break
            else:
                print("Invalid publishing")
        else:
            print("Publishing must be a string!")

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year):
        if type(year) == int:
            if year > 0:
                self.__year = year
            else:
                print("Invalid year")
        else:
            print("Year must be an integer!")

    @property
    def pages(self):
        return self.__pages

    @pages.setter
    def pages(self, pages):
        if type(pages) == int:
            if pages > 1:
                self.__pages = pages
            else:
                print("Incorrect number of pages")
        else:
            print("Pages must be an integer!")

    @property
    def binding(self):
        return self.__binding

    @binding.setter
    def binding(self, binding):
        if type(binding) == str:
            for i in Book.name_binding:
                if binding == i:
                    self.__binding = binding
                    break
            else:
                print("Invalid binding")
        else:
            print("Binding must be a string!")

    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, language):
        if type(language) == str:
            for i in Book.name_language:
                if language == i:
                    self.__language = language
                    break
            else:
                print("Invalid language!")
            if language == "Russian":
                print("We have no books in this language!!!")
        else:
            print("Language must be a string!")

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if type(size) == str:
            for i in Book.name_size:
                if size == i:
                    self.__size = size
                    break
            else:
                print("Invalid size!")
        else:
            print("Size must be a string!")

    @property
    def id(self):
        return self.__id

    @property
    def reservation(self):
        return self.__reservation

    @reservation.setter
    def reservation(self, reservation):
        for i in Book.name_reservation:
            if reservation == i:
                self.__reservation = reservation
                break
        else:
            print("Invalid reservation!")

    @property
    def return_date(self):
        return self.__return_date

    @return_date.setter
    def return_date(self, return_date):
        self.__return_date = return_date

    def __str__(self):
        return f"ID: {self.id}, Reservation:{self.reservation} Name: {self.name}, Author: {self.author}, Publishing: {self.publishing}, Year: {self.year}, Pages: {self.pages}, Binding: {self.binding}, Language: {self.language}, Size: {self.size}"
