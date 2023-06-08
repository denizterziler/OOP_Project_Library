from tabulate import tabulate


class User:
    def __init__(self, username, password, user_type):
        self.username = username
        self.password = password
        self.user_type = user_type

    def sign_up(self):
        print("Sign up")
        user = self.username + "," + str(self.password) + "," + self.user_type + "\n"
        if self.user_type == "Student":
            with open("txtFiles/studentData.txt", "a") as file:
                file.write(user)
        if self.user_type == "Librarian":
            with open("txtFiles/librarianData.txt", "a") as file:
                file.write(user)
        print(self.getName() + " has been signed up as a " + self.getType())
        print("Please Log-In to continue")

    @staticmethod
    def see_all_books():
        books = open("txtFiles/booksData.txt", "r")
        lines = books.readlines()
        books.close()
        print("-*-*-*-*-*-*-*-*-*-*-BOOKS-*-*-*-*-*-*-*-*-*-*-")
        print("\t\tNAME \t\t\t|\t\t\t NUMBER OF BOOKS")
        for line in lines:
            print(line.split("&")[0].strip() + " | " + line.split("&")[-1].strip())
        print("-*-*-*-*-*-*-*-*-*-*-BOOKS-*-*-*-*-*-*-*-*-*-*-")

    def getName(self):
        return self.username

    def getType(self):
        return self.user_type

    @staticmethod
    def search_book():
        f1 = open("txtFiles/booksData.txt", "r")
        allContents = f1.readlines()
        searchOperation = int(input("Search by: \n"
                                    "1.Title\n"
                                    "2.Author\n"
                                    "3.Exit\n"
                                    "-->"))
        if searchOperation == 1:
            bookName = input("Enter the title of the book: ")

            db = False
            for book in allContents:
                if bookName.strip() in book.split("&")[0].strip():
                    db = True
                    print("<!!!>We have the book " + book.split("&")[0].strip() + "<!!!>")
                    decision = input("If you want to see the details of the book? (Y/N): ")
                    if decision == "Y" or decision == "y":
                        print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
                        print("Title:", book.split("&")[0])
                        print("Author:", book.split("&")[1])
                        print("Publication Year:", book.split("&")[2])
                        print("Pages:", book.split("&")[3])
                        print("ISBN:", book.split("&")[4])
                    elif decision == "N" or decision == "n":
                        break
                    else:
                        print("Try again!")
            if not db:
                print("We don't have this book in our system")
        elif searchOperation == 2:
            authorName = input("Enter the name of the author: ")
            for author1 in allContents:
                if authorName.strip() in author1.split("&")[1].strip():
                    print(author1.strip())
