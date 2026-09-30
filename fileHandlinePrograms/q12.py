f=open("student.txt","r")
words=f.read().lower().split()
d={}
for word in words:
    d[word]=d.get(word,0)+1
print(d)
f.close()