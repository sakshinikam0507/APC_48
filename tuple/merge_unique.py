tuple1 = (1, 2, 3, 4)
tuple2 = (3, 4, 5, 6)
result = tuple(dict.fromkeys(tuple1 + tuple2))
print(result)
