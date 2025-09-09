class LibraryItems

    def __init__(self, title, author):
        self.canborrow = True
        self.title = title
        self.author = author

    def information(self):
        return f"{self.title}{self.author}"

    print(information())

