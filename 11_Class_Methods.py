class Book:
    total_books : int = 0

    @classmethod
    def add_book(cls) -> None:
        cls.total_books += 1

    @classmethod
    def increment_book_count(cls) -> str:
        return f"Total Book: {cls.total_books}"
    

if __name__ in "__main__" :
    book1 : Book = Book()
    book1.add_book()
    book1.add_book()
    book1.add_book()
    book1.add_book()
    book1.add_book()
    print(book1.increment_book_count())