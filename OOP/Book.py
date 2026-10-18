from abc import ABC, abstractmethod
from datetime import datetime

class Printable(ABC):
    """Абстрактный класс для объектов, которые можно вывести."""

    @abstractmethod
    def print_info(self):
        """Выводит информацию об объекте."""
        pass

class Book(Printable):
    """Класс для представления книги."""

    def __init__(self, title, author, year):
        """Создаёт книгу с названием, автором и годом издания."""
        self.title = title
        self.author = author
        self.year = year

    def info(self):
        """Возвращает информацию о книге."""
        return f"Книга - {self.title}, автор - {self.author}, год - {self.year}"

    def print_info(self):
        """Выводит информацию о книге."""
        print(self.info())

    def __str__(self):
        """Возвращает строковое представление книги."""
        return self.info()

    def __eq__(self, other):
        """Сравнивает книги по названию."""
        return isinstance(other, Book) and self.title == other.title

    @property
    def age(self):
        """Возвращает возраст книги в годах."""
        return datetime.now().year - self.year

    @classmethod
    def from_string(cls, data):
        """Создаёт книгу из строки с данными через точку с запятой."""
        title, author, year = data.split(";")
        return cls(title, author, int(year))

class Ebook(Book):
    """Класс для представления электронной книги."""

    def __init__(self, title, author, year, format):
        """Создаёт электронную книгу с указанием формата."""
        super().__init__(title, author, year)
        self.format = format

    def info(self):
        """Возвращает информацию об электронной книге."""
        return f"Книга - {self.title}, автор - {self.author}, год - {self.year}, формат - {self.format}"

    def __str__(self):
        """Возвращает строковое представление электронной книги."""
        return self.info()

book_cats = Book("Путешествия котов", "Лорд де Кот", 2000)
ebook_flower = Ebook("Топ 5 самых красивых цветов", "Роза Цветова", 2022, "Печатный")

print(book_cats.info())
print(ebook_flower)
book_cats.print_info()
