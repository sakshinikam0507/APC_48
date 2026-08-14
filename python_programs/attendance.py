students = ["Amit", "Riya", "Neha", "Rahul", "Priya"]
print("Total students:", len(students))
name = input("Enter student name to search: ")
if name in students:
    print("Student is present")
else:
    print("Student is absent")
new_student = input("Enter a new student name: ")
students.append(new_student)
absent_student = input("Enter absent student name to remove: ")
if absent_student in students:
    students.remove(absent_student)
print("Students present:", students)
