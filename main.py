from Book import Book
from Menu import Menu
from Student import Student
from Librarian import Librarian


def verifyLogin(username, userPass):
    sLog = False
    lLog = False
    try:
        with open("txtFiles/studentData.txt", 'r') as fileData:
            lines = fileData.readlines()
            for line in lines:
                fields = line.split(",")
                if fields[0] == username and fields[1] == userPass:
                    sLog = True
                    return fields[2]
        with open("txtFiles/librarianData.txt", 'r') as fileData:
            lines = fileData.readlines()
            for line in lines:
                fields = line.split(",")
                if fields[0] == username and fields[1] == userPass:
                    lLog = True
                    return fields[2]
        if sLog is False and lLog is False:
            return "Not Found"
    except OSError:
        return "File operation failed"
    except Exception:
        return "Error"


program = True
while program:
    print("!Welcome to the Library Application!")
    loginPage = True
    while loginPage:
        firstOp = int(input(Menu.firstMenu()))
        if firstOp == 1:
            studentLogin = True
            librarianLogin = True
            userName = input("Enter the name: ")
            password = input("Enter the password: ")
            user_type = verifyLogin(userName, password)
            if user_type.strip() == "Student":
                while studentLogin:
                    user_student = Student(userName, password)
                    print("-*-*-*-*-*-*-*-*-*-*-*-*")
                    operation = int(input(Menu.operationMenu()))
                    if operation == 1:
                        user_student.see_all_books()
                    elif operation == 2:
                        user_student.take_book()
                    elif operation == 3:
                        user_student.myBooks()
                    elif operation == 4:
                        user_student.return_book()
                    elif operation == 5:
                        user_student.search_book()
                    elif operation == 6:
                        studentLogin = False
                    else:
                        print("Error")
            elif user_type.strip() == "Librarian":
                while librarianLogin:
                    user_librarian = Librarian(userName, password)
                    print("-*-*-*-*-*-*-*-*-*-*-*-*")
                    operation = int(input(Menu.librarianMenu()))
                    if operation == 1:
                        user_librarian.see_all_books()
                    elif operation == 2:
                        user_librarian.add_book()
                    elif operation == 3:
                        user_librarian.remove_book()
                    elif operation == 4:
                        print("search not active")
                    elif operation == 5:
                        librarianLogin = False
                    else:
                        print("Error")
            else:
                print("UserName or Password is wrong!")

        elif firstOp == 2:
            userName = input("Enter the name: ")
            password = input("Enter the password: ")
            user_type = input("Student or Librarian?: ")
            if user_type == "Student":
                student = Student(userName, password)
                student.sign_up()
            elif user_type == "Librarian":
                librarian = Librarian(userName, password)
                librarian.sign_up()

        elif firstOp == 3:
            loginPage = False
            program = False
        else:
            print("<!>Wrong Input<!>")

