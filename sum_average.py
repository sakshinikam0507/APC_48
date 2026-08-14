numbers = []

for i in range(10):
    number = int(input("Enter a number: "))
    numbers.append(number)

total = sum(numbers)
average = total / len(numbers)

print("Sum:", total)
print("Average:", average)
