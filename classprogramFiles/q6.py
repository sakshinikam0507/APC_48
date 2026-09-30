class ElectricityBill:
    def __init__(self,n,name,u):
        self.n=n
        self.name=name
        self.u=u
    def bill(self):
        if self.u<=100:
            return self.u*5
        elif self.u<=200:
            return 100*5+(self.u-100)*7
        else:
            return 100*5+100*7+(self.u-200)*10
e=ElectricityBill(101,"Amit",250)
print("Consumer:",e.n,e.name)
print("Bill:",e.bill())