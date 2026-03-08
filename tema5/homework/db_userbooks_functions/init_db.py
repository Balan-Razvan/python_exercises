import csv
import os

def init_db():
    if os.path.exists("db_user_books.csv"):
        return
     
    with open("db_user_books.csv", 'w') as file:
        writer = csv.writer(file)
        writer.writerow(["user_id", "book_id"])

    print("initialized db")
init_db()