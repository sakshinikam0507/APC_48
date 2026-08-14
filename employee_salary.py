employees = {
    "Amit": 45000,
    "Riya": 62000,
    "Neha": 38000,
    "Rahul": 75000
}

salaries = employees.values()

print("Highest salary:", max(salaries))
print("Lowest salary:", min(salaries))
print("Average salary:", sum(salaries) / len(employees))

print("Employees earning more than 50000:")

for name, salary in employees.items():
    if salary > 50000:
        print(name, "-", salary)
