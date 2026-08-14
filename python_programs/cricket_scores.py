scores = [45, 102, 67, 12, 89, 134, 56, 78, 110, 39]
highest = scores[0]
lowest = scores[0]
for score in scores:
    if score > highest:
        highest = score
    if score < lowest:
        lowest = score
total = sum(scores)
average = total / len(scores)
centuries = 0
half_centuries = 0
for score in scores:
    if score >= 100:
        centuries += 1
    elif 50 <= score <= 99:
        half_centuries += 1

print("Highest score:", highest)
print("Lowest score:", lowest)
print("Total runs:", total)
print("Average runs:", average)
print("Centuries:", centuries)
print("Half-centuries:", half_centuries)
