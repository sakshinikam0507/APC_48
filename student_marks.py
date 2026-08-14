marks = [78, 85, 92, 67, 74, 88, 95, 81, 69, 90,
        76, 84, 73, 89, 91, 65, 79, 87, 93, 71]

highest = marks[0]
lowest = marks[0]

for mark in marks:
    if mark > highest:
        highest = mark
    if mark < lowest:
        lowest = mark

average = sum(marks) / len(marks)

above_average = 0
below_average = 0

for mark in marks:
    if mark > average:
        above_average += 1
    elif mark < average:
        below_average += 1

print("Highest marks:", highest)
print("Lowest marks:", lowest)
print("Average marks:", average)
print("Above average:", above_average)
print("Below average:", below_average)
