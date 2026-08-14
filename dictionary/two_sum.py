numbers = [2, 7, 11, 15, 3, 6]
target = int(input("Enter target: "))
seen = {}
for number in numbers:
    difference = target - number
    if difference in seen:
        print("Numbers:", difference, number)
        break
    seen[number] = True
else:
    print("No pair found")
