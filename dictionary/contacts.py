contacts = {
    "Amit": "9876543210",
    "Riya": "9876501234"
}
name = input("Enter contact name to add: ")
phone = input("Enter phone number: ")
contacts[name] = phone
name = input("Enter contact to search: ")
if name in contacts:
    print("Phone:", contacts[name])
else:
    print("Contact not found")
name = input("Enter contact to update: ")
if name in contacts:
    contacts[name] = input("Enter new phone number: ")
name = input("Enter contact to delete: ")
if name in contacts:
    del contacts[name]
print("Contacts:")
for name, phone in contacts.items():
    print(name, "-", phone)
