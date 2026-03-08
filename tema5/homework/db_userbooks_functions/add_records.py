import csv

def add_record(user_id: int = 0, book_id:int = 0):
    with open("db_user_books.csv", "a") as file:
        writer = csv.writer(file)
        writer.writerow([user_id, book_id])
    print("record added")