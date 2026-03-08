import csv

def search_record(id):
    with open("db_users.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == str(id):
                print("found ", row)
                return
    print("record not found")