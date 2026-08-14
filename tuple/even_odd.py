numbers = (12, 7, 24, 15, 8, 31, 42, 19, 6, 27, 10, 33, 18, 21, 4)
even = 0
odd = 0
for number in numbers:
    if number % 2 == 0:
        even += 1
    else:
        odd += 1
print("Even numbers:", even)
print("Odd numbers:", odd)
