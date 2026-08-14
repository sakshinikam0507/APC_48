students = {
    "Amit": 85,
    "Riya": 92,
    "Neha": 78
}

name = input("Enter student name to add: ")
marks = int(input("Enter marks: "))
students[name] = marks

name = input("Enter student name to update: ")
if name in students:
    students[name] = int(input("Enter new marks: "))

name = input("Enter student name to delete: ")
if name in students:
    del students[name]

name = input("Enter student name to search: ")
if name in students:
    print("Marks:", students[name])
else:
    print("Student not found")

print("Students:", students)

if students:
    highest = max(students, key=students.get)
    average = sum(students.values()) / len(students)
    print("Highest marks:", highest, students[highest])
    print("Average:", average)
