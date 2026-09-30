f=open("student.txt","r")
lines=f.readlines()
for line in lines[::-1]:
    print(line,end="")
f.close()