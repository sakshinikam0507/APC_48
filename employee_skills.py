employee1 = {"Python", "Java", "SQL", "Git"}
employee2 = {"Python", "C++", "SQL", "Docker"}

print("Common skills:", employee1 & employee2)
print("Employee 1 only:", employee1 - employee2)
print("Employee 2 only:", employee2 - employee1)
print("All skills:", employee1 | employee2)
