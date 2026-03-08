import csv

def add_record(record_id: int = 0, name: str = "nan", email:str = "nan"):
    with open("db_users.csv", "a") as file:
        writer = csv.writer(file)
        writer.writerow([record_id, name, email])
    print("record added")