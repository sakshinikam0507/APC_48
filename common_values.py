dict1 = {"a": 10, "b": 20, "c": 30}
dict2 = {"x": 20, "y": 40, "z": 30}

common = []

for value in dict1.values():
    if value in dict2.values() and value not in common:
        common.append(value)

print("Common values:", common)
