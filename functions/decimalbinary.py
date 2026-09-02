def convert(n):
    if n==0:
        return "0"
    if n==1:
        return "1"
    return convert(n//2)+str(n%2)

n=int(input("Enter decimal number: "))
print("Binary:",convert(n))
