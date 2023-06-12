import csv
from crush.models import User

with open("students.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        user = User(
            class_no=row["class_no"],
            student_no=row["student_no"],
            unique_id=row["unique_id"]
        )
        user.save()
