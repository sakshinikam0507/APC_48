word=input("Enter word: ")
f=open("student.txt","r")
count=0
for no,line in enumerate(f,1):
    n=line.lower().split().count(word.lower())
    if n>0:
        print("Line",no)
        count+=n
print("Occurrences:",count)
f.close()