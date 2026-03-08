import csv
import os

def init_db():
    if os.path.exists("db_books.csv"):
        return
     
    with open("db_books.csv", 'w') as file:
        writer = csv.writer(file)
        writer.writerow(["id", "title"])

    print("initialized db")
init_db()