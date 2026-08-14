numbers = [10, 20, 10, 30, 20, 10, 40, 30]
frequency = {}
for number in numbers:
    frequency[number] = frequency.get(number, 0) + 1
print(frequency)
