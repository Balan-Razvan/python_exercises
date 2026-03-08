import csv

def view_records():
    with open("db_books.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)