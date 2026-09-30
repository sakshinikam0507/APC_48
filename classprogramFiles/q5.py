class Book:
    def __init__(self,i,t,a,p):
        self.i=i
        self.t=t
        self.a=a
        self.p=p
    def show(self):
        print(self.i,self.t,self.a,self.p)
b1=Book(1,"Python","Amit",400)
b2=Book(2,"Java","Rahul",500)
b3=Book(3,"C","Priya",300)
b1.show()
b2.show()
b3.show()