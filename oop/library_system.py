class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        pass

class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count
        
class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self, book):
        return self.books.append(book)
 
    def list_books(self):
        for i, book in enumerate(self.books, 1):
            print(f"{i}. {book}")


# Create a Library instance
my_library = Library()

    # Create instances of each type of book
classic_book = Book("Pride and Prejudice", "Jane Austen")
digital_novel = EBook("Snow Crash", "Neal Stephenson", 500)
paper_novel = PrintBook("The Catcher in the Rye", "J.D. Salinger", 234)

    # Add books to the library
my_library.add_book(classic_book)
my_library.add_book(digital_novel)
my_library.add_book(paper_novel)

    # List all books in the library
my_library.list_books()