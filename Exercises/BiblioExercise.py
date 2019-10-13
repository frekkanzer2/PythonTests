from ClassesModules.Singleton import Singleton
from FunctionsModules.CheckTypes import *


# ensure declaration
def ensure(attrName, conditionFunct, doc=""):
    def decorator(Class):
        privateName = "_" + attrName
        setattr(Class, privateName, None)

        def getter(self):
            return getattr(self, privateName)

        def setter(self, value):
            conditionFunct(value)
            setattr(self, privateName, value)

        setattr(Class, attrName, property(getter, setter, doc))
        return Class

    return decorator


# Book class
@ensure("title", checkIfString, "That's the title of the book")
@ensure("author", checkIfString, "That's the author of the book")
@ensure("price", checkIfInt, "That's the price of the book")
class Book:

    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        print("Title:", self.title, "; Author:", self.author, "; Price:", self.price, "$")


# Library class -> it will be used in the Singleton class
@ensure("booksArray", checkIfList, "That's the list of books")
class Library:

    def __init__(self):
        self.booksArray = list()

    def getBookByName(self, value):
        find = bool(False)
        index = 0
        listOfBooks = self.booksArray
        takenBook = None
        while not find and index < len(listOfBooks):
            tempBook = listOfBooks[index]
            if tempBook.title == value:
                find = True
                takenBook = tempBook
            else:
                index += 1
        if find:
            return takenBook
        else:
            return None

    def addBook(self, title, author, price):
        tempBook = Book(title, author, price)
        self.booksArray.append(tempBook)

    def removeBookByTitle(self, title):
        find = bool(False)
        index = 0
        listOfBooks = self.booksArray
        takenBook = None
        while not find and index < len(listOfBooks):
            tempBook = listOfBooks[index]
            if tempBook.title == title:
                find = True
            else:
                index += 1
        if find:
            del listOfBooks[index]
            return True
        else:
            return False


# TEST EVERYTHING
myLibrary = Singleton(Library)
myLibrary.addBook("Ciao Pippo", "Abby", 10)
myLibrary.addBook("Cucina da Daduccio", "Daduccio", 15)
myLibrary.addBook("Mi violentò lui", "Danielo", 500)
myLibrary.addBook("Non ho stuprato nessuno", "Lamberti", 20)
myBook = myLibrary.getBookByName("Mi violentò lui")
myBook.display()
