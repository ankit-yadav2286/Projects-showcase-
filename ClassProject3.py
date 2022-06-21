# campus library management system.


# creation of library class
class Library:
    def __init__(self, listOfBooks):
        self.books = listOfBooks

    # Method to display all the books available.
    def displayAvailableBooks(self):
        print("Books present in this library are: ")
        for book in self.books:
            print(" *" + book)

    # Method to borrow books from the .library
    def borrowBook(self, bookName):
        if bookName in self.books:
            print(f"You have been issued {bookName}. Please keep it safe and return it within 30 days")
            self.books.remove(bookName)

        else:
            print("Sorry, This book is either not available or has already been issued to someone else. Please wait until the book is available")
            

    # Method to return or add book to the library
    def returnBook(self, bookName):
        self.books.append(bookName)
        print("Thanks for returning this book! Hope you enjoyed reading it.")


# creation of student class
class Student:
    # method to ask student name of the book he\she want to borrow
    def requestBook(self):
        self.book = input("Enter the name of the book you want to borrow: ")
        return self.book

    # method to ask the student name of the book he\she want to return
    def returnBook(self):
        self.book = input("Enter the name of the book you want to return: ")
        return self.book


if __name__ == "__main__":
    # creation of library class instance
    campusLibrary = Library(["Kite Runner", "Inferno", "Anne Frank", "The Alchemist", "The Train to Pakistan."])
    # creation of student class instance
    student = Student()
    welcomeMsg = '''\n ====== Welcome to Campus Library ======
            Please choose an option:
            1. List all the books
            2. Request a book
            3. Add/Return a book
            4. Exit the Library
            '''
    print(welcomeMsg)

    while (True):

        a = int(input("Enter a choice: "))
        if a == 1:
            campusLibrary.displayAvailableBooks()
        elif a == 2:
            campusLibrary.borrowBook(student.requestBook())
        elif a == 3:
            campusLibrary.returnBook(student.returnBook())
        elif a == 4:
            print("Thanks for choosing Campus Library!")
            exit()
        else:
            print("Invalid Choice!")

