class Library:

    def __init__(self):
        self.noOfBooks = 0
        self.booksList = []

    def addNewBook(self, newBook):
        self.booksList.append(newBook)
        self.noOfBooks = len(self.booksList)

    def showBooksName(self):
        print(f'Books Name are : {self.booksList}')

    def showInfo(self):
        print(f'The library has {self.noOfBooks} books')

        
library1 = Library()
library1.addNewBook("Harry Potter")
library1.addNewBook("Marvel Universe")
library1.showInfo()
library1.showBooksName()