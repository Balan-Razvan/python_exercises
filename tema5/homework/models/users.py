from db_user_functions.add_records import add_record
from db_user_functions.search_record import search_record
from db_user_functions.view_records import view_records
from db_user_functions.delete_record import delete_record

class Users:
    id = 2
    def __init__(self):
        pass
    def add(self, name: str = "nan", email:str = "nan") -> None:
        add_record(self.id, name, email)
        self.id += 1
    def list_users(self):
        view_records()
    def get(self, id):
        search_record(id)
    def delete_user(self, id):
        delete_record(id)

