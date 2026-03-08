from db_books_functions.add_records import add_record
from db_books_functions.search_record import search_record
from db_books_functions.view_records import view_records
from db_books_functions.delete_record import delete_record

class Books:
    id = 1
    def __init__(self):
        pass
    def add(self, title: str = "nan") -> None:
        add_record(self.id, title)
        self.id += 1
    def list_books(self):
        view_records()
    def get(self, id):
        search_record(id)
    def delete_book(self, id):
        delete_record(id)

