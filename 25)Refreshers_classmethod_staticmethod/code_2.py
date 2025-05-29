class BooKClass:
    TYPES = ("hardcover", "paperback")

    def __init__(self, name, book_type, weight):  # name, book_type, weight are objects
        self.name_of_book = name
        self.book_type = book_type
        self.weight_of_book = weight

    def __repr__(another_self):
        return (f"Book Name: {another_self.name_of_book}, Type of the book: {another_self.book_type},"
                f" Weight of the book: {another_self.weight_of_book}.")


book = BooKClass("DEEP WORK", "paperback", 250)
print(book.name_of_book)
print(book.weight_of_book)
print(book)
print(BooKClass.TYPES)