students = {
    "Amit": "Computer Science",
    "Riya": "Information Technology",
    "Neha": "Computer Science",
    "Rahul": "Mechanical",
    "Priya": "Information Technology"
}

groups = {}

for student, department in students.items():
    if department not in groups:
        groups[department] = []
    groups[department].append(student)

print(groups)
