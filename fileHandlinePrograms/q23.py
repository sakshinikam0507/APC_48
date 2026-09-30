f1=open("one.txt","r")
f2=open("two.txt","r")
same=True
for no,(a,b) in enumerate(zip(f1,f2),1):
    if a!=b:
        print("Different at line:",no)
        same=False
        break
if same:
    a=f1.readline()
    b=f2.readline()
    if a or b:
        same=False
        print("Different at line:",no+1)
if same:
    print("Files are identical")
f1.close()
f2.close()