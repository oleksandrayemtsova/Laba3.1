from library_card import LibraryCard
from person import Person


class Reader(Person):
    def __init__(self, name, surname, age, phone_number):
        super().__init__(name, surname, age, phone_number)
        self.__library_card = LibraryCard(name)

    @property
    def library_card(self):
        return self.__library_card

    def __str__(self):
        return (f"Name: {self.name}, Surname: {self.surname}, Age: {self.age}, Phone number: +{self.phone_number},"
                f""f"\n{self.library_card}")
