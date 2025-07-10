class Book:
    def __init__(self, title, auther, is_read):
        self.title = title
        self.auther = auther
        self.is_read = is_read
        
    def mark_as_read(self):
        self.is_read = True
        print("kitob uqilgan deb belgilandi ")
        
    def status(self):
        if self.is_read:
            print("uqilgan")
            
        else:
            print("uqilmagan")

books = Book("Utgan kunlar", "utkir hoshimov", True)

books.status()
books.mark_as_read()
books.status()        
        