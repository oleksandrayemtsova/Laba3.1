from book import Book
from library import Library

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
for book in array:
    library.add_book(book)

print(library.find_by_author("Сара Маас"), "\n")
print(library.find_by_publishing("Vivat"), "\n")
print(library.published_after_this_year(2023), "\n")
print(library.books_in_the_page_range(250, 350), "\n")
print(library.books_in_the_page_range(900, 400), "\n")
print(library.books_in_the_page_range(-10, 0), "\n")

