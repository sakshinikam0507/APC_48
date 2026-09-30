f=open("employees.txt","w")
f.write("1,Amit,CSE,30000\n2,Priya,IT,45000\n3,Rahul,HR,35000")
f.close()
f=open("employees.txt","r")
total=0
high=""
maxsal=0
for line in f:
    i,n,d,s=line.strip().split(",")
    s=int(s)
    print(i,n,d,s)
    total+=s
    if s>maxsal:
        maxsal=s
        high=n
print("Highest paid:",high,maxsal)
print("Average salary:",total/3)
x=int(input("Enter salary: "))
f.seek(0)
for line in f:
    i,n,d,s=line.strip().split(",")
    if int(s)>x:
        print("Above salary:",n)
f.close()