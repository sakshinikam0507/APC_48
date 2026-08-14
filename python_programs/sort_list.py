numbers = []

for i in range(10):
    numbers.append(int(input("Enter a number: ")))
print("Ascending order:", sorted(numbers))
print("Descending order:", sorted(numbers, reverse=True))
