emps=[]
n=int(input("Enter num of emps: "))

for i in range(n):
    name=input("Enter name: ")
    salary=float(input("Enter salary: "))
    emps.append((name,salary))

emps.sort(key=lambda e:e[1])
print(emps)
