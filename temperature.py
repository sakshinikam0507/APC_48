temperatures = [
    28, 30, 31, 29, 32, 34, 33, 27, 26, 29,
    31, 35, 36, 34, 30, 28, 27, 29, 32, 33,
    31, 30, 28, 26, 25, 27, 29, 31, 34, 35
]

hottest = temperatures[0]
coldest = temperatures[0]

for temperature in temperatures:
    if temperature > hottest:
        hottest = temperature
    if temperature < coldest:
        coldest = temperature

average = sum(temperatures) / len(temperatures)

above_average = 0
below_average = 0

for temperature in temperatures:
    if temperature > average:
        above_average += 1
    elif temperature < average:
        below_average += 1

print("Hottest temperature:", hottest)
print("Coldest temperature:", coldest)
print("Average temperature:", average)
print("Days above average:", above_average)
print("Days below average:", below_average)
