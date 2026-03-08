import csv

def add_record(record_id: int = 0, title:str = "nan"):
    with open("db_books.csv", "a") as file:
        writer = csv.writer(file)
        writer.writerow([record_id, title])
    print("record added")