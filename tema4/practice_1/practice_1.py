with open("source.txt", "r") as file:
    text = file.read()

with open("copy.txt", "w") as file:
    file.write(text)