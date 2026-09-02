emps=[]
n=int(input("Enter number of employees: "))

for i in range(n):
    name=input("Enter name: ")
    dept=input("Enter department: ")
    salary=float(input("Enter salary: "))
    emps.append({"name":name,"department":dept,"salary":salary})

above=list(filter(lambda e:e["salary"]>50000,emps))
emps=list(map(lambda e:{**e,"salary":e["salary"]*1.10},emps))
emps=sorted(emps,key=lambda e:e["salary"])

print("Above 50000:",above)
print("Increased salaries:",emps)
print("Sorted employees:",emps)
