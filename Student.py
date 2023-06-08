import shutil
from User import User


class Student(User):
    def __init__(self, username, password):
        super().__init__(username, password, "Student")

    def take_book(self):
        bookName = input("Enter the name of the book to take or q to exit: ")
        bookNotAdded = True
        if bookName.strip().__eq__("q"):
            bookNotAdded = False
        f = open("txtFiles/myBooks.txt", "r")
        for myBook in f.readlines():
            if myBook.split("&")[0].strip().__eq__(bookName.strip()) and myBook.split("&")[-1].strip().__eq__(
                    self.getName()):
                print("<!!!>You cannot take the same book more than once<!!!>")
                bookNotAdded = False
                break
        while bookNotAdded:
            with open("txtFiles/booksData.txt", "r+") as file:
                linesBooks = file.readlines()
                a = 0

            for line in linesBooks:
                if line.split("&")[0].strip() == bookName:
                    if int(line.split("&")[-1].strip()) > 0:
                        integerValue = int(line.split("&")[-1].strip())
                        newLine = line.split("&")[0] + "&" + line.split("&")[1] + "&" + line.split("&")[
                            2] + "&" + \
                                  line.split("&")[3] + "&" + line.split("&")[4] + "& " + str(
                            integerValue - 1) + "\n"
                        linesBooks[a] = newLine
                        with open("txtFiles/booksData.txt", "w") as updatedFile:
                            updatedFile.writelines(linesBooks)
                        f1 = open("txtFiles/booksData.txt", "r")
                        books = f1.readlines()
                        for book in books:
                            if book.split("&")[0].strip().__eq__(bookName.strip()):
                                try:
                                    file = open("txtFiles/myBooks.txt", "a")
                                    book = book.strip() + " & " + self.getName() + "\n"
                                    file.write(book)
                                    file.close()
                                    print("<!>" + bookName + " added to your list<!>")
                                    bookNotAdded = False
                                except:
                                    print("Oops! something error")
                        break
                    else:
                        print("Currently there is not enough amount of the book: " + bookName.strip())
                        print("Wait for someone to return the book")
                        bookNotAdded = False
                a += 1

    def myBooks(self):
        userBooks = []
        print("-*-MY BOOKS-*-")
        print("Student: " + self.getName())
        f = open("txtFiles/myBooks.txt", "r")
        anyBooks = False
        for line in f.readlines():
            if line.split("&")[-1].strip() == self.getName():
                anyBooks = True
                print(line.split("&")[0], "|", line.split("&")[-3].strip())
                userBooks.append(line)
        if anyBooks is False:
            print("<!>You do not have any books yet<!>")
            pass
        else:
            bookOperation = input(
                "-->Enter the ISBN number of the book to see the details or q to exit:  ")
            if bookOperation.__eq__("q"):
                pass
            else:
                for book in userBooks:
                    if book.split("&")[-3].strip().__eq__(bookOperation.strip()):
                        print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
                        print("Title:", book.split("&")[0])
                        print("Author:", book.split("&")[1])
                        print("Publication Year:", book.split("&")[2])
                        print("Pages:", book.split("&")[3])
                        print("ISBN:", book.split("&")[4])

    def return_book(self):
        f = open("txtFiles/myBooks.txt", "r")
        anyBooks = False
        for line in f.readlines():
            if line.split("&")[-1].strip() == self.getName():
                anyBooks = True
        if anyBooks is False:
            print("<!>You do not have any books to return<!>")
            pass
        else:
            bookName = input("Enter the name of the book to return or q to exit: ")
            bookReturned = True
            if bookName.strip().__eq__("q"):
                bookReturned = False
            for myBook in f.readlines():
                if myBook.split("&")[0].strip().__eq__(bookName.strip()) and myBook.split("&")[-1].strip().__eq__(
                        self.getName()):
                    print("You have the book: " + myBook.split("&")[0].strip())
            while bookReturned:
                with open("txtFiles/booksData.txt", "r+") as file:
                    linesBooks = file.readlines()
                    a = 0

                for line in linesBooks:
                    if line.split("&")[0].strip() == bookName:
                        if int(line.split("&")[-1].strip()) >= 0:
                            integerValue = int(line.split("&")[-1].strip())
                            newLine = line.split("&")[0] + "&" + line.split("&")[1] + "&" + line.split("&")[
                                2] + "&" + \
                                      line.split("&")[3] + "&" + line.split("&")[4] + "& " + str(
                                integerValue + 1) + "\n"
                            linesBooks[a] = newLine
                            with open("txtFiles/booksData.txt", "w") as updatedFile:
                                updatedFile.writelines(linesBooks)
                            print("Book " + bookName + " returned")
                            f1 = open("txtFiles/booksData.txt", "r")
                            books = f1.readlines()
                            for book in books:
                                if book.split("&")[0].strip().__eq__(bookName.strip()):
                                    try:

                                        f = open("txtFiles/myBooks.txt", "r")
                                        for line in f.readlines():
                                            if line.split("&")[0].strip().__eq__(bookName.strip()) and line.split("&")[
                                                -1].strip().__eq__(self.getName()):
                                                pass
                                            else:
                                                with open("txtFiles/temp.txt", "a") as file:
                                                    file.write(line)
                                        shutil.copy('txtFiles/temp.txt', 'txtFiles/myBooks.txt')
                                        with open("txtFiles/temp.txt", 'w') as file:
                                            pass
                                        print("Returned to library")
                                        bookReturned = False
                                    except:
                                        print("Oops! Try Again!")
                            break
                        else:
                            print("You cannot return the book")
                    a += 1

    def getName(self):
        return self.username

