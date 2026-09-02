def large(list):
    largest_num = list[0]

    for i in list:
        if i > largest_num:
            largest_num = i

    return largest_num
print(large([15, 21, 3, 14, 55]))