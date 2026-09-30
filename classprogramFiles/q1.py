class Student:
    def __init__(self,r,n,m):
        self.r=r
        self.n=n
        self.m=m
    def show(self):
        print(self.r,self.n,self.m,sum(self.m)/len(self.m))
s1=Student(1,"Amit",[80,75,90,85,88])
s2=Student(2,"Priya",[90,85,92,88,95])
s1.show()
s2.show()