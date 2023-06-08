class Book:
    def __init__(self, name, author, year, page_number, isbn, totalNumber):
        self.name = name
        self.author = author
        self.year = year
        self.page_number = page_number
        self.isbn = isbn
        self.totalNumber = totalNumber

    def __str__(self):
        return self.name + " & " + self.author + " & " + str(self.year) + " & " + str(self.page_number) + " & " + self.isbn + " & " + str(self.totalNumber)
