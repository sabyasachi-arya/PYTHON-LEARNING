class BooKClass:
    TYPES = ("hardcover", "paperback")

    def __init__(self, name, book_type, weight):  # name, book_type, weight are objects
        self.name_of_book = name
        self.book_type = book_type
        self.weight_of_book = weight

    def __repr__(another_self):
        return (f"Book Name: {another_self.name_of_book}, Type of the book: {another_self.book_type},"
                f" Weight of the book: {another_self.weight_of_book}.")

    @classmethod
    def hardcover_or_paperback(cls, name, book_weight):
        if book_weight >= 500:
            return BooKClass(name, BooKClass.TYPES[0], book_weight)
        else:
            return BooKClass(name, BooKClass.TYPES[1], book_weight)


book = BooKClass.hardcover_or_paperback("DEEP WORK", 250)
book_2 = BooKClass.hardcover_or_paperback("The Universe", 560)
print(book.name_of_book)
print(book.weight_of_book)
print(book)
print(book_2.name_of_book)
print(book_2.weight_of_book)
print(book_2)