from models.users import Users
from models.books import Books
from models.userBooks import UserBooks

users = Users()
books = Books()
userBooks = UserBooks()

# users.add("razvan", "razvan@gmail.com")
# users.add("adi", "adi@gmail.com")
# users.add("alex", "alex@gmail.com")
# users.get(2)
# users.list_users()

# books.add("crima si pedeapsa")
# books.add("1984")
# books.add("ferma animalelor")
# books.list_books()
# books.get(2)

# userBooks.add_book(2, 1)
# userBooks.add_book(2, 2)
# userBooks.add_book(4, 3)
# userBooks.get_books(2)
print(userBooks.has_read_book(4, 3))