from db_userbooks_functions.add_records import add_record
from db_userbooks_functions.search_record import search_record
from db_userbooks_functions.view_records import view_records
from db_userbooks_functions.delete_record import delete_record

class UserBooks:
    def __init__(self):
        pass
    def add_book(self, user_id, book_id):
        if not search_record(user_id=user_id, book_id=book_id):
            add_record(user_id=user_id, book_id=book_id)
    def get_books(self, id_user):
        view_records(user_id=id_user)
    def has_read_book(self, id_user, id_book):
        if not search_record(user_id=id_user,book_id=id_book):
            return False
        return True
    def remove_book(self, user_id, book_id):
        delete_record(user_id=user_id, book_id=book_id)


