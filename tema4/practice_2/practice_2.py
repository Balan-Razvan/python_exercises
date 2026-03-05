import re

with open("story.txt", "r") as file:
    text = file.read().strip()

print(len(re.split(r"[ \s,./;]", text)))
print(re.split(r"[ \s,./;]", text))