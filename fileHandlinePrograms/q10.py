f=open("student.txt","r")
text=f.read()
a=0
d=0
s=0
sp=0
for ch in text:
    if ch.isalpha():
        a+=1
    elif ch.isdigit():
        d+=1
    elif ch==" ":
        s+=1
    else:
        sp+=1
print("Alphabets:",a)
print("Digits:",d)
print("Spaces:",s)
print("Special characters:",sp)
f.close()