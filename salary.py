salaries = [28000, 45000, 52000, 65000, 30000, 75000, 48000, 55000]

highest = salaries[0]
lowest = salaries[0]

for salary in salaries:
    if salary > highest:
        highest = salary
    if salary < lowest:
        lowest = salary

average = sum(salaries) / len(salaries)

above_50000 = []
below_30000 = []

for salary in salaries:
    if salary > 50000:
        above_50000.append(salary)
    if salary < 30000:
        below_30000.append(salary)

print("Highest salary:", highest)
print("Lowest salary:", lowest)
print("Average salary:", average)
print("Above 50000:", above_50000)
print("Below 30000:", below_30000)
