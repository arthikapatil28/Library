class Book:
    def __init__(self,title,author,isbn):
        self.title=title
        self.author=author
        self.isbn=isbn
    def display(self):
        print(f"Title: {self.title} ,Author{self.author} , ISBN:{self.isbn}")
class Library:
    def __init__(self):
        self.books=[]
    def add_book(self,book):
        self.books.append(book)
        print(f"Book {book.title} is added")
    def remove_book(self,isbn):
        book_to_remove=None
        for book in self.books:
            if book.isbn==isbn:
                book_to_remove=book
        if book_to_remove:
            self.books.remove(book_to_remove)
            print(f"Book {book_to_remove.title} is remove from Library")
    def display_books(self):
        if not self.books:
            print("NO Book found in Library")
        else:
            for book in self.books:
                book.display()
class special_Library(Library):  # inheritence inherted from Library.
    def add_book(self,book):  # overriding the add_book method 
        self.books.append(book)
        print(f"specialLibrary Book  {book.title} is added")
        
Book1 = Book(title="Game of Thrones", author="George R. R. Martin", isbn="1996")
Book2 = Book(title="Good Dad Bad Dad", author="Robert T. Kiyosaki", isbn="1997")
Book3 = Book(title="The Book of Secrets", author="Osho", isbn="1974")
Book4 = Book(title="The Secret", author="Rhonda Byrne", isbn="2006")

My_library=Library()
My_library.add_book(Book1)
My_library.add_book(Book2)
My_library.add_book(Book3)
My_library.add_book(Book4)
My_library.display_books()
My_library.remove_book("1974")
My_library.display_books()
Special_Library=special_Library()
Special_Library.add_book(Book3)
Special_Library.display_books()

    
            
        
        