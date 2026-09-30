f=open("attendance.txt","w")
f.write("Amit,70,100\nPriya,80,100\nRahul,60,100")
f.close()
f=open("attendance.txt","r")
for line in f:
    n,p,t=line.strip().split(",")
    per=int(p)/int(t)*100
    print(n,per)
    if per<75:
        print("Below 75:",n)
f.close()