marks = {
    "Amit": 85,
    "Riya": 92,
    "Neha": 78
}

student = input("Enter student name: ")
new_marks = int(input("Enter new marks: "))

if student in marks:
    marks[student] = new_marks

print(marks)
