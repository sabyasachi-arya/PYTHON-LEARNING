# A familiar programme with Type hinting
# inside parameters to show which type of arguments are supported for the selected parameter should be defined
# with a semicolon ":"
# like name: str, book_weight: float
# to show what a function or method is going to return, it is recommended to use an arrow -> and then the type
# outside the parameter section after the first line of the  function before the :
# like this def __repr__(another_self) -> str:
class BooKClass:
    TYPES = ("hardcover", "paperback")

    def __init__(self, name: str, book_type: str, weight: float):  # name, book_type, weight are objects
        #                   ^^^^^ ---------- ^^^^ ------- ^^^^^^  --------> Type Hinting
        self.name_of_book = name
        self.book_type = book_type
        self.weight_of_book = weight

    def __repr__(another_self) -> str:
        #                         ^^^^ -------> Type Hinting
        return (f"Book Name: {another_self.name_of_book}, Type of the book: {another_self.book_type},"
                f" Weight of the book: {another_self.weight_of_book.__float__()}.")  # __float__() is used inside
    # __repr__ or inside function to convert an integer into float

    @classmethod
    def hardcover_or_paperback(cls, name: str, book_weight: float) -> "BooKClass":
        #                                 ^^^^--------------^^^^^------^^^^^^^^^^--------Type Hinting
        # -> "BookClaas" is defining that this function will return BookClass , and classes name has to be written
        # inside "_______" , also because otherwise we will get an error because we are inside the same class
        # if it was returning any other class then we do not need to write the class name inside "_____"
        if book_weight >= 500.0:
            return BooKClass(name, BooKClass.TYPES[0], book_weight)
        else:
            return BooKClass(name, BooKClass.TYPES[1], book_weight)


book = BooKClass.hardcover_or_paperback("DEEP WORK", 250.0)
book_2 = BooKClass.hardcover_or_paperback("The Universe", 560.0)
print(book.name_of_book)
print(book.weight_of_book)
print(book)
print(book_2.name_of_book)
print(book_2.weight_of_book)
print(book_2)