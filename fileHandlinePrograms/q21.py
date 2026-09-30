def add():
    f=open("books.txt","a")
    i=input("Book ID: ")
    t=input("Title: ")
    a=input("Author: ")
    f.write(i+","+t+","+a+",Available\n")
    f.close()
def search():
    x=input("Book ID: ")
    f=open("books.txt","r")
    for line in f:
        if line.split(",")[0]==x:
            print(line,end="")
    f.close()
def issue():
    x=input("Book ID: ")
    f=open("books.txt","r")
    lines=f.readlines()
    f.close()
    f=open("books.txt","w")
    for line in lines:
        p=line.strip().split(",")
        if p[0]==x:
            p[3]="Issued"
            line=",".join(p)+"\n"
        f.write(line)
    f.close()
def ret():
    x=input("Book ID: ")
    f=open("books.txt","r")
    lines=f.readlines()
    f.close()
    f=open("books.txt","w")
    for line in lines:
        p=line.strip().split(",")
        if p[0]==x:
            p[3]="Available"
            line=",".join(p)+"\n"
        f.write(line)
    f.close()
def show():
    f=open("books.txt","r")
    for line in f:
        if "Available" in line:
            print(line,end="")
    f.close()
add()
show()