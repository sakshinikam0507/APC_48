marks = {
    "Amit": 85,
    "Riya": 92,
    "Neha": 78,
    "Rahul": 88
}

student = max(marks, key=marks.get)

print("Highest marks:", student, marks[student])
