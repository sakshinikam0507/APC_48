patients = (
    (101, "Amit", 25, "A+"),
    (102, "Riya", 31, "B+"),
    (103, "Neha", 42, "O+"),
    (104, "Rahul", 29, "A+")
)

for patient in patients:
    print(patient)

patient_id = int(input("Enter patient ID: "))
found = False

for patient in patients:
    if patient[0] == patient_id:
        print("Patient:", patient)
        found = True
        break

if not found:
    print("Patient not found")

print("Total patients:", len(patients))

blood_group = input("Enter blood group: ")

for patient in patients:
    if patient[3] == blood_group:
        print(patient)
