from library_items import LibraryItems
from books import Books
from nonfiction import NonFiction
from fiction import Fiction

# first fiction book
book1 = Fiction("The Hobbit", "J.R.R. Tolkien", 1937, genre="Fantasy")
print(book1.information())
print(book1.borrow())
print(book1.borrow())
print(book1.return_item())
print(book1.return_item())

# first non-fiction book
book2 = NonFiction("A Brief History of Time", "Stephen Hawking", 1988, subject="Cosmology")
print(book2.information())
print(book2.borrow())