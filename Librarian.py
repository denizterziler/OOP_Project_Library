import shutil

from Book import Book
from User import User


class Librarian(User):
    def __init__(self, username, password):
        super().__init__(username, password, "Librarian")

    @staticmethod
    def add_book():
        bookName = input("Name of the book:")
        authorBook = input("Author of the book:")
        publicYear = int(input("Publication year of the book:"))
        totalPages = int(input("Total pages of the book:"))
        isbnNumber = input("ISBN number of the book:")
        totalNumber = int(input("How many of this book will be added:"))
        book = Book(bookName, authorBook, publicYear, totalPages, isbnNumber, totalNumber)
        try:
            file = open("txtFiles/booksData.txt", "a")
            file.write(book.__str__() + "\n")
            file.close()
            print("Added!")
        except:
            print("Oops! something error")

    @staticmethod
    def remove_book():
        removeIsbn = input("Enter the ISBN number of the book to remove:")
        f = open("txtFiles/booksData.txt", "r")
        for line in f.readlines():
            if line.split("&")[4].strip().__eq__(removeIsbn.strip()):
                removedName = line.split("&")[0].strip()
                print(removedName + " Removed")
                pass
            else:
                with open("txtFiles/temp.txt", "a") as file:
                    file.write(line)
        shutil.copy('txtFiles/temp.txt', 'txtFiles/booksData.txt')
        with open("txtFiles/temp.txt", 'w') as file:
            pass
        f = open("txtFiles/myBooks.txt", "r")
        for line in f.readlines():
            if line.split("&")[4].strip().__eq__(removeIsbn.strip()):
                removedName = line.split("&")[0].strip()
                pass
            else:
                with open("txtFiles/temp.txt", "a") as file:
                    file.write(line)
        shutil.copy('txtFiles/temp.txt', 'txtFiles/myBooks.txt')
        with open("txtFiles/temp.txt", 'w') as file:
            pass