class MobilePhone:
    def __init__(self,b,m,s,p):
        self.b=b
        self.m=m
        self.s=s
        self.p=p
    def show(self):
        print(self.b,self.m,self.s,self.p)
    def discount(self,d):
        return self.p-self.p*d/100
p=MobilePhone("Samsung","A15","128GB",20000)
p.show()
print("Price after discount:",p.discount(10))