text = input("Enter a string: ")

frequency = {}

for character in text:
    frequency[character] = frequency.get(character, 0) + 1

for character in text:
    if frequency[character] > 1:
        print("First repeated character:", character)
        break
else:
    print("No repeated character")
