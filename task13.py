class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_read = False

    def mark_as_read(self):
        self.is_read = True

    def status(self):
        if self.is_read:
            print(f"{self.title} — Oqilgan")
        else:
            print(f"{self.title} — Oqilmagan")
            
            
book1 = Book("Alkimyogar", "Paulo Coelho")
book2 = Book("1984", "George Orwell")
book3 = Book("Otamdan qolgan dalalar", "Togay Murod")
book4 = Book("Sariq devni minib", "Xudoyberdi Toxtaboyev")

book1.mark_as_read()
book3.mark_as_read()

books = [book1, book2, book3, book4]
for book in books:
    book.status()
