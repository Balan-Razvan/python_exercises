import csv

def search_record(user_id, book_id):
    with open("db_user_books.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == str(user_id) and row[1] == str(book_id):
                print("found ", row)
                return True
    print("record not found")