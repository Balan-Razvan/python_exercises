import csv


def delete_record(user_id, book_id):
    rows = []

    with open("db_users.csv", "r") as file:
        reader = csv.reader(file)
        rows = [row for row in reader if row[0] == str(user_id) and row[1] == str(book_id)]
    
    with open("db_users.csv", "w") as file:
        writer = csv.writer(file)
        writer.writerows(rows)
    print("record deleted")
