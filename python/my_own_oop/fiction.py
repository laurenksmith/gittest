from books import Books


class Fiction(Books):
    def __init__(self, title, author, datewritten, genre):
        super().__init__(title, author, datewritten)
        self.genre = genre

    def information(self):
        return f"'{self.title}' (Fiction, {self.genre}) by {self.author}, written in {self.datewritten}."
