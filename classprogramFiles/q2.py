class Employee:
    def __init__(self,i,n,s):
        self.i=i
        self.n=n
        self.s=s
    def hra(self):
        return self.s*0.2
    def da(self):
        return self.s*0.1
    def gross(self):
        return self.s+self.hra()+self.da()
e=Employee(101,"Amit",30000)
print("HRA:",e.hra())
print("DA:",e.da())
print("Gross:",e.gross())