def avg(data):
    return sum(x[1] for x in data)/len(data)

data=[]
n=int(input("Enter number of students: "))

for i in range(n):
    name=input("Enter name: ")
    marks=float(input("Enter marks: "))
    data.append((name,marks))

above=list(filter(lambda x:x[1]>75,data))
sorteddata=sorted(data,key=lambda x:x[1])

print("Average marks:",avg(data))
print("Above 75:",above)
print("Sorted students:",sorteddata)
