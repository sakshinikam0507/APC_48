data=[]
n=int(input("Enter num of data: "))

for i in range(n):
    name=input("Enter name: ")
    marks=float(input("Enter marks: "))
    data.append((name,marks))

data.sort(key=lambda s:s[1])
print(data)
