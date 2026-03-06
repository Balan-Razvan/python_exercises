import csv
import os

def init_db():
    if os.path.exists("db.csv"):
        return
     
    with open("db.csv", 'w') as file:
        writer = csv.writer(file)
        writer.writerow(["id", "name", "email"])

    print("initialized db")