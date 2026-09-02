def gettotal(marks):
    return sum(marks)

def getper(marks):
    return sum(marks)/5

def getgrade(per):
    if per>=90:
        return "A"
    elif per>=80:
        return "B"
    elif per>=70:
        return "C"
    elif per>=60:
        return "D"
    else:
        return "F"

def process(s):
    s["total"]=gettotal(s["marks"])
    s["per"]=getper(s["marks"])
    s["grade"]=getgrade(s["per"])

data=[]
n=int(input("Enter number of students: "))

for i in range(n):
    name=input("Enter name: ")
    roll=input("Enter roll number: ")
    marks=list(map(float,input("Enter five marks: ").split()))
    s={"name":name,"roll":roll,"marks":marks}
    process(s)
    data.append(s)

classavg=sum(s["per"] for s in data)/len(data)
high=max(data,key=lambda s:s["total"])
low=min(data,key=lambda s:s["total"])

for s in data:
    print(s["name"],s["roll"],s["total"],s["per"],s["grade"])

print("Class average:",classavg)
print("Highest scorer:",high["name"])
print("Lowest scorer:",low["name"])
