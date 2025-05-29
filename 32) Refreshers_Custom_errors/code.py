class Book:
    def __init__(self, name: str, pages: int):
        self.book_name = name
        self.pages_read = 0
        self.book_pages = pages

    def __repr__(self):
        return (
            f"<Book: {self.book_name}, read {self.pages_read} pages out of {self.book_pages}>"
        )

    def read(self, read_pages: int):
        self.pages_read += read_pages
        if self.pages_read >= self.book_pages:
            print(f"You have completed reading the {self.book_name} book.")
        else:
            print(f"You have read {self.pages_read} pages out of {self.book_pages} of {self.book_name}")


book_1 = Book("Deep Work", 250)
book_1.read(56)
book_1.read(200)