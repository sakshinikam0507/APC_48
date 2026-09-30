f=open("transactions.txt","w")
f.write("D,1000\nW,300\nD,500\nW,200")
f.close()
f=open("transactions.txt","r")
d=0
w=0
large=0
for line in f:
    t,x=line.strip().split(",")
    x=int(x)
    if t=="D":
        d+=x
    else:
        w+=x
    if x>large:
        large=x
print("Total deposits:",d)
print("Total withdrawals:",w)
print("Final balance:",d-w)
print("Largest transaction:",large)
f.close()