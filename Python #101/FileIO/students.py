import csv

# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         print(f"{name} is in {house}")



students = []

with open("students.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append(row) # or {"name": row["name"], "home": row["home"]}


for student in sorted(students, key=lambda student: student["name"], reverse=True):
    print(f"{student['name']} is in {student['home']}")