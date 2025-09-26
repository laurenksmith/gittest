from library_items import LibraryItems

class Books(LibraryItems):
    def __init__(self, title, author, datewritten):
        super().__init__(title, author)
        self.datewritten = datewritten
