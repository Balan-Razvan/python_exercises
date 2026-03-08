import csv
from db_books_functions.search_record import search_record

def view_records(user_id):
    with open("db_user_books.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == str(user_id):
                search_record(row[1])