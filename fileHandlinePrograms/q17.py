f=open("students.txt","w")
f.write("RollNo,Name,Marks\n101,Amit,85\n102,Priya,92\n103,Rahul,78")
f.close()
f=open("students.txt","r")
lines=f.readlines()[1:]
total=0
high=""
maxmark=0
for line in lines:
    r,n,m=line.strip().split(",")
    m=int(m)
    print(r,n,m)
    total+=m
    if m>maxmark:
        maxmark=m
        high=n
    if m>80:
        print("Above 80:",n)
print("Highest:",high,maxmark)
print("Average:",total/len(lines))
f.close()