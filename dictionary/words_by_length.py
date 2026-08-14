words = ["cat", "dog", "apple", "banana", "book", "pen", "school"]
groups = {}
for word in words:
    length = len(word)
    if length not in groups:
        groups[length] = []
    groups[length].append(word)
print(groups)
