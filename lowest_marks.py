marks = {
    "Amit": 85,
    "Riya": 92,
    "Neha": 78,
    "Rahul": 68
}

student = min(marks, key=marks.get)

print("Lowest marks:", student, marks[student])
