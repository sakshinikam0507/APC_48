class StudentResult:
    def __init__(self,n,m):
        self.n=n
        self.m=m
    def total(self):
        return sum(self.m)
    def per(self):
        return self.total()/5
    def grade(self):
        p=self.per()
        if p>=75:
            return "A"
        elif p>=60:
            return "B"
        elif p>=50:
            return "C"
        else:
            return "D"
    def __del__(self):
        print("Result completed")
s=StudentResult("Amit",[80,75,90,85,88])
print("Name:",s.n)
print("Total:",s.total())
print("Percentage:",s.per())
print("Grade:",s.grade())
del s