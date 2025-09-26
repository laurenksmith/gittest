class LibraryItems:

    def __init__(self, title, author):
        self.canborrow = True
        self.title = title
        self.author = author

    def information(self):
        return f"'{self.title}'{self.author}"

    def borrow(self):
        if self.canborrow:
            self.canborrow = False
            return f"You have borrowed '{self.title}."
        else:
            return f"Sorry, '{self.title} is already out."

    def return_item(self):
        if not self.canborrow:
            self.canborrow = True
            return f"'{self.title}' has been returned."
        else:
            return f"'{self.title}' was not borrowed."

