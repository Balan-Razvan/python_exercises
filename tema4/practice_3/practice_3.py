from init_db import init_db
from add_records import add_record
from view_records import view_records
from search_record import search_record
from delete_record import delete_record

init_db()

add_record(2, "razvan", "test@gmail.com")
view_records()
# search_record(1)
delete_record(1)

view_records()