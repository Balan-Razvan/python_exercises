import csv

def view_records():
    with open("db_users.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)