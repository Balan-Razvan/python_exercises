import csv

def view_records():
    with open("db.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)