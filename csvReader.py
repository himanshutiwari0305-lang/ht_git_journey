import csv

with open("FileHandling/data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)  # row is a standard list: ['Alice', 'Engineer', 'IT']


from pathlib import Path
file = Path("data.csv")
print(file.exists())

from pathlib import Path
file = Path("FileHandling/data.csv")
print(file.exists())