f=open("student.txt","r")
text=f.read().lower()
v=0
c=0
for ch in text:
    if ch.isalpha():
        if ch in "aeiou":
            v+=1
        else:
            c+=1
print("Vowels:",v)
print("Consonants:",c)
f.close()