employee = {
    "name": "Rahul",
    "department": "IT",
    "salary": 45000
}
key = input("Enter key: ")
if key in employee:
    print(employee[key])
else:
    print("Key not found")
