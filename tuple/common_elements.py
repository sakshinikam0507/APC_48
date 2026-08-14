tuple1 = (1, 2, 3, 4, 5)
tuple2 = (4, 5, 6, 7, 8)
common = tuple(number for number in tuple1 if number in tuple2)
print("Common elements:", common)
