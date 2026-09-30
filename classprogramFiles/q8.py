class Patient:
    def __init__(self,i,n,a,d,f):
        self.i=i
        self.n=n
        self.a=a
        self.d=d
        self.f=f
    def show(self):
        print(self.i,self.n,self.a,self.d,self.f)
    def bill(self,days):
        return self.f*days
p=Patient(1,"Amit",20,"Fever",500)
p.show()
print("Total bill:",p.bill(3))