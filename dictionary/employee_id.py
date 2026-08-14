employees = {
    101: "Amit",
    102: "Riya",
    103: "Neha",
    104: "Rahul"
}
employee_id = int(input("Enter employee ID: "))
if employee_id in employees:
    print("Employee exists")
else:
    print("Employee not found")
