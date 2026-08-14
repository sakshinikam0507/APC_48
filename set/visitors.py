day1 = {101, 102, 103, 104, 105}
day2 = {103, 104, 106, 107}
print("Unique visitors:", day1 | day2)
print("Returning visitors:", day1 & day2)
print("First day only:", day1 - day2)
print("Second day only:", day2 - day1)
