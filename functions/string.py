def string(s):
    count=0
    for i in s:
        if i.lower() in 'aeiou':
            count += 1
    return count
print(string("sakshiiiiiiiiiiiiii"))