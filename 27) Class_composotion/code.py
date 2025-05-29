class Bookshelf:  # class Bookshelf created
    def __init__(self, *books):   # class Bookshelf has 1 parameter for __init__(initiation)
        # *books can take multiple amount books as arguments
        self.books = books  # a book variable inside self is assigned for books parameter's arguments

    def __str__(self):  # __str__ method to print out a nice string for the books
        return f"Bookshelf with {len(self.books)} books."  # string
        # with len of self.books means the number of books received as argument


class Book:   # a new class is created for every individual book
    def __init__(self, name_of_book):   # class Book is having one parameter called name
        self.book_name = name_of_book   # a book_name variable is created inside self and the value of
        # name_of_book(the argument which Book class will receive) is assigned to the book_name

    def __str__(self):  # __str__ to print a nice string
        return f"Book: {self.book_name}"  # string


book_1 = Book("The Universe")   # in book_1 variable the Book class is called and an argument has given
book_2 = Book("DEEP WORK")  # similarly in book_2 variable the Book class is called and an argument has given
total_books = Bookshelf(book_1, book_2)  # a total_books variable is created to call the Bookshelf class
# and as we know Bookshelf class can take multiple books as argument because of *books,
# so two arguments are passed like book_1 and book_2
print(total_books)  # printing the total_books will call Bookshelf class and insert the two books inside of it
# and number of books will be shown as per the number of arguments are provided in Bookshelf class
# in this case which is two and a string was coded to be printed , therefore the string with the len(self.books)
# will be printed out.
print(book_1)  # printing the book_1 will call Book class and insert the name of the book which was provided
# as arguments and will print the string (As coded in Book class) with the book name.
print(book_2)  # same as book_1
