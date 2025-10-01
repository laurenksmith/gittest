from books import Books


class NonFiction(Books):
    def __init__(self, title, author, datewritten, subject):
        super().__init__(title, author, datewritten)
        self.subject = subject

    def information(self):
        return f"'{self.title}' (Non-Fiction, about {self.subject}) by {self.author}, written in {self.datewritten}."