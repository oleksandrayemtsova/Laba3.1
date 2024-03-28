from library_card import LibraryCard


class Reader:

    def __init__(self, name, surname, age, phone_number):
        self.__name = name
        self.__surname = surname
        self.__age = age
        self.__phone_number = phone_number
        self.__library_card = LibraryCard(name)

    @property
    def name(self):
        return self.__name

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, surname):
        if type(surname) == str:
            self.__surname = surname
        else:
            print("Surname must be a string!")

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if type(age) == int:
            if 0 < age < 150:
                self.__age = age
            else:
                print("Invalid age")
        else:
            print("Age must be an integer!")

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        if type(phone_number) == int:
            if 380000000000 < phone_number < 381000000000:
                self.__phone_number = phone_number
            else:
                print("Invalid phone number")
        else:
            print("Age must be an integer!")

    @property
    def library_card(self):
        return self.__library_card

    def __str__(self):
        return f"Name: {self.name}, Surname: {self.surname}, Age: {self.age}, Phone number: +{self.phone_number}, \n{self.library_card}"





