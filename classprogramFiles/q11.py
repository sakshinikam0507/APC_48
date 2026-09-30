class ShoppingCart:
    def __init__(self,n,i):
        self.n=n
        self.i=i
        self.items=[]
    def add(self,n,p):
        self.items.append([n,p])
    def remove(self,n):
        for x in self.items:
            if x[0]==n:
                self.items.remove(x)
                break
    def total(self):
        s=0
        for x in self.items:
            s+=x[1]
        return s
    def __del__(self):
        print("Shopping cart destroyed")
c=ShoppingCart("Amit",101)
c.add("Pen",20)
c.add("Book",100)
c.remove("Pen")
print("Total:",c.total())
del c