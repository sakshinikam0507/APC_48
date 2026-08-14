names = ["Amit", "Riya", "Neha"]
ages = [25, 31, 42]

name = input("Enter patient name: ")
age = int(input("Enter patient age: "))

names.append(name)
ages.append(age)

search_name = input("Enter patient name to search: ")

if search_name in names:
    index = names.index(search_name)
    print("Patient found")
    print("Age:", ages[index])
else:
    print("Patient not found")

delete_name = input("Enter patient name to delete: ")

if delete_name in names:
    index = names.index(delete_name)
    names.pop(index)
    ages.pop(index)

print("Patients:")

for i in range(len(names)):
    print(names[i], "-", ages[i])

print("Total patients:", len(names))
