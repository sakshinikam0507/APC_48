def check(value):
    value=str(value)
    return value==value[::-1]

value=input("Enter a string or number: ")
print(check(value))
