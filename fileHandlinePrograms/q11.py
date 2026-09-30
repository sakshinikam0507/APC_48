f=open("student.txt","r")
words=f.read().split()
long=""
for word in words:
    if len(word)>len(long):
        long=word
print("Longest word:",long)
f.close()